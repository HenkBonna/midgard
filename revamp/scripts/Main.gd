extends Node3D

const TEST_START_Z: float = 0.0
const HARE_TEST_START_Z: float = 750.0
const DOG_MOUNT_Z: float = 890.0
const DOG_FINISH_Z: float = 1410.0
const DOG_FORWARD_SPEED: float = 12.0
const STAGE_HAWK: int = 0
const STAGE_HARE: int = 1
const STAGE_DOG: int = 2

@export var start_as_hare_for_testing: bool = false

var collected_count: int = 0
var total_collectibles: int = 0
var player: CharacterBody3D
var goal: Area3D
var final_goal: Area3D
var status_label: Label
var velocity_label: Label
var start_card: CanvasLayer
var vignette_layer: CanvasLayer
var effects_prompt: Label
var effects_prompt_timer: Timer
var screen_effects_enabled: bool = false
var finish_card: CanvasLayer
var level_finished: bool = false
var camera_pivot: Node3D
var camera: Camera3D
var finish_rabbit: Node3D
var rabbit_touch_area: Area3D
var dog_mount: Node3D
var dog_transition_started: bool = false
var transition_end_plane: MeshInstance3D
var finish_approach_started: bool = false
var stage_host: Node3D
var stage_root: Node3D
var stage_nodes: Dictionary = {}
var active_stage_id: int = -1

func _ready() -> void:
	build_environment()
	create_ground()
	stage_host = Node3D.new()
	stage_host.name = "StageHost"
	add_child(stage_host)
	build_player()
	build_hud()
	build_vignette_overlay()
	if start_as_hare_for_testing:
		total_collectibles = 13
		_activate_stage(STAGE_HARE)
		switch_animal(load("res://scenes/animals/Hare.tscn") as PackedScene)
	else:
		_activate_stage(STAGE_HAWK)
	_prepare_test_start()
	_update_hud()
	build_start_card()
	get_tree().paused = true

func _process(_delta: float) -> void:
	if player == null:
		return

	if active_stage_id == STAGE_HAWK and player.global_position.z >= 640.0:
		_load_stage(STAGE_HARE)
	elif active_stage_id == STAGE_HARE and player.global_position.z >= 830.0:
		_load_stage(STAGE_DOG)

	if velocity_label != null:
		var flight_velocity: Vector3 = player.call("get_flight_velocity")
		var camera_state: String = player.call("get_camera_state_name")
		var form_name: String = player.call("get_form_name")
		velocity_label.text = "Camera: %s\nPlayer: %s\nVelocity: %.1f, %.1f, %.1f" % [camera_state, form_name, flight_velocity.x, flight_velocity.y, flight_velocity.z]

func _input(event: InputEvent) -> void:
	if not event is InputEventKey or not event.pressed or event.echo:
		return
	if event.keycode == KEY_ESCAPE:
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
	elif event.keycode == KEY_T:
		_toggle_screen_effects()

func _stage_scene_path(stage_id: int) -> String:
	match stage_id:
		STAGE_HAWK:
			return "res://scenes/stages/HawkStage.tscn"
		STAGE_HARE:
			return "res://scenes/stages/HareStage.tscn"
		_:
			return "res://scenes/stages/DogStage.tscn"

func _load_stage(stage_id: int) -> Node3D:
	if stage_nodes.has(stage_id):
		return stage_nodes[stage_id]

	var stage_scene := load(_stage_scene_path(stage_id)) as PackedScene
	var stage := stage_scene.instantiate() as Node3D
	stage_host.add_child(stage)
	stage_nodes[stage_id] = stage
	match stage_id:
		STAGE_HAWK:
			goal = stage.get("finish_area")
			total_collectibles = int(stage.get("total_collectibles"))
			stage.connect("ring_picked_up", _on_collectible_picked_up)
			stage.connect("finish_line_crossed", _on_goal_body_entered)
		STAGE_HARE:
			transition_end_plane = stage.get("transition_end_plane")
			finish_rabbit = stage.get("finish_rabbit")
			rabbit_touch_area = stage.get("rabbit_touch_area")
			dog_mount = stage.get("dog_mount")
			final_goal = stage.get("dog_mount_line")
			stage.connect("rabbit_touched", _on_rabbit_touched)
			stage.connect("dog_mount_line_crossed", _on_final_goal_body_entered)
		STAGE_DOG:
			final_goal = stage.get("finish_line")
			stage.connect("finish_line_crossed", _on_dog_final_goal_body_entered)
	return stage

func _activate_stage(stage_id: int) -> void:
	var previous_stage_id := active_stage_id
	var next_stage := _load_stage(stage_id)
	if previous_stage_id == stage_id:
		stage_root = next_stage
		return

	if previous_stage_id >= 0 and stage_nodes.has(previous_stage_id):
		stage_nodes[previous_stage_id].queue_free()
		stage_nodes.erase(previous_stage_id)
		_clear_stage_references(previous_stage_id)
	active_stage_id = stage_id
	stage_root = next_stage
	_set_stage_references(stage_id, next_stage)

func _set_stage_references(stage_id: int, stage: Node3D) -> void:
	match stage_id:
		STAGE_HAWK:
			goal = stage.get("finish_area")
			total_collectibles = int(stage.get("total_collectibles"))
		STAGE_HARE:
			transition_end_plane = stage.get("transition_end_plane")
			finish_rabbit = stage.get("finish_rabbit")
			rabbit_touch_area = stage.get("rabbit_touch_area")
			dog_mount = stage.get("dog_mount")
			final_goal = stage.get("dog_mount_line")
		STAGE_DOG:
			final_goal = stage.get("finish_line")

func _clear_stage_references(stage_id: int) -> void:
	match stage_id:
		STAGE_HAWK:
			goal = null
		STAGE_HARE:
			transition_end_plane = null
			finish_rabbit = null
			rabbit_touch_area = null
			final_goal = null
			dog_mount = null
		STAGE_DOG:
			final_goal = null

func build_environment() -> void:
	var environment_node := WorldEnvironment.new()
	var environment := Environment.new()
	environment.background_mode = Environment.BG_SKY
	environment.background_color = Color(0.62, 0.79, 0.9)
	var sky := Sky.new()
	var sky_material := ProceduralSkyMaterial.new()
	sky_material.sky_top_color = Color(0.1, 0.36, 0.72)
	sky_material.sky_horizon_color = Color(0.55, 0.78, 0.92)
	sky_material.ground_bottom_color = Color(0.35, 0.6, 0.85)
	sky_material.ground_horizon_color = Color(0.58, 0.79, 0.93)
	sky.sky_material = sky_material
	environment.sky = sky
	environment.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	environment.ambient_light_color = Color(0.98, 0.98, 1.0)
	environment.ambient_light_energy = 1.2
	environment.fog_enabled = true
	environment.fog_light_color = Color(0.62, 0.79, 0.9)
	environment.fog_density = 0.02
	environment.fog_depth_begin = 75.0
	environment.fog_depth_end = 140.0
	environment.fog_depth_curve = 3.2
	environment.fog_sky_affect = 1.0
	environment_node.environment = environment
	add_child(environment_node)

	var sun := DirectionalLight3D.new()
	sun.position = Vector3(8, 20, 10)
	sun.rotation_degrees = Vector3(-35, 35, 0)
	sun.light_energy = 1.3
	sun.shadow_enabled = true
	add_child(sun)

func create_ground() -> void:
	var ground := MeshInstance3D.new()
	ground.name = "Ground"
	var plane := PlaneMesh.new()
	plane.size = Vector2(20000.0, 20000.0)
	ground.mesh = plane
	var material := StandardMaterial3D.new()
	material.albedo_color = Color(0.08, 0.22, 0.12)
	material.roughness = 0.85
	ground.material_override = material
	add_child(ground)

	var ground_body := StaticBody3D.new()
	ground_body.name = "GroundCollision"
	ground_body.position.y = -0.5
	var ground_shape := CollisionShape3D.new()
	var ground_box := BoxShape3D.new()
	ground_box.size = Vector3(20000.0, 1.0, 20000.0)
	ground_shape.shape = ground_box
	ground_body.add_child(ground_shape)
	add_child(ground_body)

func build_player() -> void:
	camera_pivot = Node3D.new()
	camera_pivot.name = "CameraPivot"
	camera_pivot.position = Vector3(0, 1.8, 0)
	add_child(camera_pivot)

	camera = Camera3D.new()
	camera.name = "Camera3D"
	camera.position = Vector3(0.0, 0.75, -1.5)
	camera.rotation_degrees = Vector3(0.0, 180.0, 0.0)
	camera.current = true
	camera.near = 0.05
	camera.far = 250.0
	camera.h_offset = 0.0
	camera.v_offset = 0.0
	camera.fov = 82.0
	camera_pivot.add_child(camera)

	player = load("res://scenes/animals/Bird.tscn").instantiate() as CharacterBody3D
	player.name = "Player"
	player.add_to_group("player")
	player.call("configure_camera_rig", camera_pivot, camera)
	add_child(player)

func switch_animal(animal_scene: PackedScene, state_override: Dictionary = {}) -> void:
	if player == null or animal_scene == null or level_finished:
		return

	var transition_state: Dictionary = state_override
	if transition_state.is_empty():
		transition_state = player.call("capture_transition_state")
	var next_animal := animal_scene.instantiate() as CharacterBody3D
	if next_animal == null:
		return
	next_animal.name = "Player"
	next_animal.add_to_group("player")
	if next_animal.has_signal("controls_unlocked"):
		next_animal.connect("controls_unlocked", _on_hare_controls_unlocked)
	next_animal.call("configure_camera_rig", camera_pivot, camera)
	add_child(next_animal)
	next_animal.call("restore_transition_state", transition_state)
	var previous_animal: CharacterBody3D = player
	player = next_animal
	previous_animal.queue_free()

func _prepare_test_start() -> void:
	if player == null:
		return
	if player.get_script().resource_path == "res://scripts/Hare.gd":
		player.global_position = Vector3(0.0, 0.0, HARE_TEST_START_Z)
		player.velocity = Vector3(0.0, 0.0, float(player.get("forward_speed")))
		collected_count = total_collectibles
	else:
		player.global_position.z = TEST_START_Z
		collected_count = maxi(total_collectibles - 1, 0)
	camera_pivot.global_position = player.global_position + Vector3(0.0, 2.0, 0.0)

func build_hud() -> void:
	var hud := CanvasLayer.new()
	hud.name = "HUD"
	hud.layer = 3

	var margin := MarginContainer.new()
	margin.offset_left = 20
	margin.offset_top = 20
	margin.offset_right = 250
	margin.offset_bottom = 90
	hud.add_child(margin)

	status_label = Label.new()
	status_label.name = "StatusLabel"
	status_label.text = "Fly through the golden rings and reach the gate."
	status_label.add_theme_font_size_override("font_size", 22)
	status_label.add_theme_color_override("font_color", Color(1, 1, 1))
	status_label.add_theme_color_override("font_outline_color", Color(0, 0, 0))
	status_label.add_theme_constant_override("outline_size", 4)
	margin.add_child(status_label)

	velocity_label = Label.new()
	velocity_label.name = "VelocityLabel"
	velocity_label.set_anchors_and_offsets_preset(Control.PRESET_BOTTOM_LEFT)
	velocity_label.offset_left = 20
	velocity_label.offset_top = -104
	velocity_label.offset_right = 500
	velocity_label.offset_bottom = -20
	velocity_label.add_theme_font_size_override("font_size", 18)
	velocity_label.add_theme_color_override("font_color", Color(1, 1, 1))
	velocity_label.add_theme_color_override("font_outline_color", Color(0, 0, 0))
	velocity_label.add_theme_constant_override("outline_size", 4)
	hud.add_child(velocity_label)

	effects_prompt = Label.new()
	effects_prompt.name = "EffectsPrompt"
	effects_prompt.set_anchors_and_offsets_preset(Control.PRESET_CENTER_BOTTOM)
	effects_prompt.offset_left = -180
	effects_prompt.offset_top = -76
	effects_prompt.offset_right = 180
	effects_prompt.offset_bottom = -42
	effects_prompt.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	effects_prompt.add_theme_font_size_override("font_size", 20)
	effects_prompt.add_theme_color_override("font_color", Color(1, 1, 1))
	effects_prompt.add_theme_color_override("font_outline_color", Color(0, 0, 0))
	effects_prompt.add_theme_constant_override("outline_size", 4)
	effects_prompt.hide()
	hud.add_child(effects_prompt)

	effects_prompt_timer = Timer.new()
	effects_prompt_timer.wait_time = 1.5
	effects_prompt_timer.one_shot = true
	effects_prompt_timer.timeout.connect(effects_prompt.hide)
	hud.add_child(effects_prompt_timer)

	add_child(hud)

func build_vignette_overlay() -> void:
	vignette_layer = CanvasLayer.new()
	vignette_layer.layer = 2
	vignette_layer.visible = screen_effects_enabled

	var overlay := ColorRect.new()
	overlay.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	overlay.mouse_filter = Control.MOUSE_FILTER_IGNORE
	var overlay_material := ShaderMaterial.new()
	overlay_material.shader = load("res://shaders/vignette_blur.gdshader")
	overlay.material = overlay_material
	vignette_layer.add_child(overlay)
	add_child(vignette_layer)

func _toggle_screen_effects() -> void:
	screen_effects_enabled = not screen_effects_enabled
	vignette_layer.visible = screen_effects_enabled
	effects_prompt.text = "Screen effects: ON" if screen_effects_enabled else "Screen effects: OFF"
	effects_prompt.show()
	effects_prompt_timer.start()

func build_start_card() -> void:
	start_card = CanvasLayer.new()
	start_card.layer = 10
	start_card.process_mode = Node.PROCESS_MODE_ALWAYS

	var backdrop := ColorRect.new()
	backdrop.color = Color(0.02, 0.06, 0.08, 0.72)
	backdrop.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	start_card.add_child(backdrop)

	var center := CenterContainer.new()
	center.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	center.mouse_filter = Control.MOUSE_FILTER_IGNORE
	start_card.add_child(center)

	var start_button := Button.new()
	start_button.text = "Press Space to start"
	start_button.custom_minimum_size = Vector2(420, 72)
	start_button.add_theme_font_size_override("font_size", 30)
	start_button.focus_mode = Control.FOCUS_ALL
	start_button.pressed.connect(_start_game)

	var space_shortcut := Shortcut.new()
	var space_key := InputEventKey.new()
	space_key.keycode = KEY_SPACE
	space_shortcut.events.append(space_key)
	start_button.shortcut = space_shortcut
	center.add_child(start_button)

	add_child(start_card)
	start_button.grab_focus()

func _start_game() -> void:
	get_tree().paused = false
	start_card.queue_free()

func _show_finish_card() -> void:
	if level_finished:
		return
	level_finished = true
	status_label.text = "Victory! You flew through every ring."
	get_tree().paused = true
	Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
	finish_card = CanvasLayer.new()
	finish_card.layer = 11
	finish_card.process_mode = Node.PROCESS_MODE_ALWAYS
	var backdrop := ColorRect.new()
	backdrop.color = Color(0.02, 0.06, 0.08, 0.78)
	backdrop.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	finish_card.add_child(backdrop)
	var center := CenterContainer.new()
	center.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	center.mouse_filter = Control.MOUSE_FILTER_IGNORE
	finish_card.add_child(center)
	var content := VBoxContainer.new()
	content.alignment = BoxContainer.ALIGNMENT_CENTER
	content.add_theme_constant_override("separation", 20)
	center.add_child(content)
	var title := Label.new()
	title.text = "FLIGHT COMPLETE"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 44)
	content.add_child(title)
	var ring_result := Label.new()
	ring_result.text = "Rings: %d / %d" % [collected_count, total_collectibles]
	ring_result.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	ring_result.add_theme_font_size_override("font_size", 22)
	content.add_child(ring_result)
	var replay_button := Button.new()
	replay_button.text = "Play again"
	replay_button.custom_minimum_size = Vector2(280, 64)
	replay_button.add_theme_font_size_override("font_size", 26)
	replay_button.pressed.connect(_restart_run)
	var replay_shortcut := Shortcut.new()
	var replay_key := InputEventKey.new()
	replay_key.keycode = KEY_SPACE
	replay_shortcut.events.append(replay_key)
	replay_button.shortcut = replay_shortcut
	content.add_child(replay_button)
	add_child(finish_card)
	replay_button.grab_focus()

func _restart_run() -> void:
	get_tree().paused = false
	finish_card.queue_free()
	for collectible in get_tree().get_nodes_in_group("collectible"):
		collectible.free()
	collected_count = 0
	level_finished = false
	finish_approach_started = false
	dog_transition_started = false
	if transition_end_plane != null:
		transition_end_plane.hide()
	if finish_rabbit != null:
		finish_rabbit.queue_free()
		finish_rabbit = null
	if dog_mount != null:
		dog_mount.queue_free()
		dog_mount = null
	if rabbit_touch_area != null:
		rabbit_touch_area.queue_free()
		rabbit_touch_area = null
	var start_scene_path := "res://scenes/animals/Hare.tscn" if start_as_hare_for_testing else "res://scenes/animals/Bird.tscn"
	switch_animal(load(start_scene_path) as PackedScene)
	for stage in stage_nodes.values():
		stage.queue_free()
	stage_nodes.clear()
	active_stage_id = -1
	stage_root = null
	goal = null
	final_goal = null
	finish_rabbit = null
	rabbit_touch_area = null
	dog_mount = null
	transition_end_plane = null
	if start_as_hare_for_testing:
		total_collectibles = 13
	else:
		total_collectibles = 0
	_activate_stage(STAGE_HARE if start_as_hare_for_testing else STAGE_HAWK)
	if player.has_method("reset_run"):
		player.call("reset_run")
	_prepare_test_start()
	_update_hud()
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _on_collectible_picked_up() -> void:
	collected_count += 1
	if player != null and player.has_method("activate_speed_boost"):
		player.call("activate_speed_boost")
	_update_hud()

func _update_hud() -> void:
	if status_label == null:
		return

	status_label.text = "Rings: %d / %d" % [collected_count, total_collectibles] if collected_count < total_collectibles else "Gate unlocked! Fly through the glowing portal."

func _on_goal_body_entered(body: Node) -> void:
	if body != player or finish_approach_started:
		return
	finish_approach_started = true
	transition_end_plane.global_position = Vector3(0.0, 12.0, finish_rabbit.global_position.z + 10.0)
	transition_end_plane.show()
	status_label.text = "Following the rabbit..."
	player.call("begin_finish_approach", finish_rabbit.global_position + Vector3(0.0, 1.0, 0.0))

func _on_final_goal_body_entered(body: Node) -> void:
	if body != player or dog_transition_started or dog_mount == null or not player.has_method("begin_dog_mount"):
		return
	dog_transition_started = true
	player.connect("dog_mounted", _on_hare_mounted_dog, CONNECT_ONE_SHOT)
	status_label.text = "The rabbit leaps onto the dog..."
	player.call("begin_dog_mount", dog_mount.global_position + Vector3(0.0, 1.55, 0.0))

func _on_hare_mounted_dog(_position: Vector3) -> void:
	if dog_mount == null:
		return
	var dog_position: Vector3 = dog_mount.global_position
	dog_mount.queue_free()
	dog_mount = null
	var dog_state := {
		"position": dog_position,
		"lateral_velocity": 0.0,
		"vertical_velocity": 0.0,
		"dog_forward_speed": DOG_FORWARD_SPEED
	}
	switch_animal(load("res://scenes/animals/Dog.tscn") as PackedScene, dog_state)
	_activate_stage(STAGE_DOG)
	status_label.text = "Dog: weave around the pines. Space to jump."

func _on_dog_final_goal_body_entered(body: Node) -> void:
	if body == player:
		_show_finish_card()

func _on_rabbit_touched(body: Node) -> void:
	if body != player or finish_rabbit == null:
		return
	rabbit_touch_area.set_deferred("monitoring", false)
	transition_end_plane.global_position = Vector3(0.0, 12.0, player.global_position.z + 10.0)
	switch_animal(load("res://scenes/animals/Hare.tscn") as PackedScene)
	_activate_stage(STAGE_HARE)
	finish_rabbit.queue_free()
	finish_rabbit = null
	rabbit_touch_area.queue_free()
	rabbit_touch_area = null
	status_label.text = "Hare: hold Space to charge a longer hop."

func _on_hare_controls_unlocked(_world_position: Vector3) -> void:
	status_label.text = "Hare controls active."
