extends Node3D

const TEST_START_Z: float = 0.0

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
var transition_end_plane: MeshInstance3D
var finish_approach_started: bool = false

func _ready() -> void:
	build_environment()
	build_level()
	build_trees()
	build_player()
	build_collectibles()
	_prepare_test_start()
	build_goal()
	build_transition_end_marker()
	build_finish_rabbit()
	build_hare_obstacles()
	build_final_goal()
	build_hud()
	build_vignette_overlay()
	_update_hud()
	build_start_card()
	get_tree().paused = true

func build_transition_end_marker() -> void:
	transition_end_plane = MeshInstance3D.new()
	transition_end_plane.name = "TransitionEndPlane"
	var plane := PlaneMesh.new()
	plane.size = Vector2(56.0, 24.0)
	transition_end_plane.mesh = plane
	transition_end_plane.position = Vector3(0.0, 12.0, 0.0)
	transition_end_plane.rotation_degrees.x = 90.0
	var material := StandardMaterial3D.new()
	material.albedo_color = Color(1.0, 0.08, 0.06, 0.3)
	material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	material.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	material.cull_mode = BaseMaterial3D.CULL_DISABLED
	transition_end_plane.material_override = material
	transition_end_plane.visible = false
	add_child(transition_end_plane)

func _process(_delta: float) -> void:
	if player == null:
		return

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
	environment.fog_density = 0.0015
	environment.fog_depth_begin = 55.0
	environment.fog_depth_end = 250.0
	environment.fog_depth_curve = 1.2
	environment.fog_sky_affect = 0.0
	environment_node.environment = environment
	add_child(environment_node)

	var sun := DirectionalLight3D.new()
	sun.position = Vector3(8, 20, 10)
	sun.rotation_degrees = Vector3(-35, 35, 0)
	sun.light_energy = 1.3
	sun.shadow_enabled = true
	add_child(sun)

func create_box_body(name: String, position: Vector3, size: Vector3, color: Color, roughness: float = 0.85) -> void:
	var body := StaticBody3D.new()
	body.name = name
	body.position = position
	body.add_to_group("obstacle")

	var collision := CollisionShape3D.new()
	var rounded_shape := CapsuleShape3D.new()
	rounded_shape.radius = minf(size.x, size.z) * 0.48
	rounded_shape.height = maxf(size.y, rounded_shape.radius * 2.0)
	collision.shape = rounded_shape
	body.add_child(collision)

	var mesh := MeshInstance3D.new()
	var box_mesh := BoxMesh.new()
	box_mesh.size = size
	mesh.mesh = box_mesh
	var material := StandardMaterial3D.new()
	material.albedo_color = color
	material.roughness = roughness
	mesh.material_override = material
	body.add_child(mesh)

	add_child(body)

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

func build_level() -> void:
	create_ground()

	var lane_x: Array[float] = [-18.0, -9.0, 0.0, 9.0, 18.0]
	for index in range(96):
		var tower_z := 8.0 + index * 7.5
		var tower_x: float = lane_x[index % lane_x.size()]
		var tower_height: float = 8.0 + float(index % 9) * 2.2
		var tower_color := Color(0.63 + randf() * 0.18, 0.70 + randf() * 0.18, 0.78 + randf() * 0.18)
		create_box_body("Tower_%02d" % (index + 1), Vector3(tower_x, tower_height * 0.5 - 0.5, tower_z), Vector3(2.8, tower_height, 2.8), tower_color, 0.8)

	var rooftop_details := [
		Vector3(-12.0, 7.5, 16.0),
		Vector3(-6.0, 9.0, 30.0),
		Vector3(0.0, 8.5, 46.0),
		Vector3(6.0, 10.0, 62.0),
		Vector3(12.0, 8.5, 80.0),
		Vector3(-12.0, 9.0, 96.0),
		Vector3(-6.0, 10.5, 116.0),
		Vector3(0.0, 11.0, 136.0),
		Vector3(6.0, 8.8, 158.0),
		Vector3(12.0, 9.2, 180.0),
		Vector3(-12.0, 10.8, 198.0),
		Vector3(-6.0, 9.6, 214.0),
		Vector3(0.0, 10.8, 228.0),
		Vector3(6.0, 9.5, 246.0),
		Vector3(12.0, 11.0, 264.0)
	]
	for index in range(rooftop_details.size()):
		var detail_color := Color(0.68 + randf() * 0.12, 0.73 + randf() * 0.12, 0.82 + randf() * 0.12)
		create_box_body("Rooftop_%02d" % (index + 1), rooftop_details[index], Vector3(2.2, 2.0, 2.2), detail_color, 0.7)

func build_trees() -> void:
	var tree_scenes: Array[PackedScene] = [
		load("res://assets/models/foliage/tree1.glb") as PackedScene,
		load("res://assets/models/foliage/pine_tree1.glb") as PackedScene
	]
	var leafy_positions: Array[Transform3D] = []
	var pine_positions: Array[Transform3D] = []
	var tree_count := 840
	for index in range(tree_count):
		var side := -1.0 if index % 2 == 0 else 1.0
		var progress: float = float(index) / float(tree_count - 1)
		var position := Vector3(side * randf_range(31.0, 53.0), 0.0, 20.0 + progress * 700.0)
		var basis := Basis(Vector3.UP, randf_range(0.0, TAU)).scaled(Vector3.ONE * randf_range(0.85, 1.25))
		var instance_transform := Transform3D(basis, position)
		if index % 4 < 2:
			leafy_positions.append(instance_transform)
		else:
			pine_positions.append(instance_transform)

	_add_tree_multimeshes(tree_scenes[0], leafy_positions)
	_add_tree_multimeshes(tree_scenes[1], pine_positions)

func _add_tree_multimeshes(scene: PackedScene, placements: Array[Transform3D]) -> void:
	var source_root := scene.instantiate()
	var mesh_parts: Array[Dictionary] = []
	_collect_tree_meshes(source_root, Transform3D.IDENTITY, mesh_parts)
	source_root.free()

	for part in mesh_parts:
		var mesh: Mesh = part["mesh"]
		var local_transform: Transform3D = part["transform"]
		var multimesh := MultiMesh.new()
		multimesh.transform_format = MultiMesh.TRANSFORM_3D
		multimesh.mesh = mesh
		multimesh.instance_count = placements.size()
		for index in range(placements.size()):
			multimesh.set_instance_transform(index, placements[index] * local_transform)

		var instance := MultiMeshInstance3D.new()
		instance.multimesh = multimesh
		instance.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
		add_child(instance)

func _collect_tree_meshes(node: Node, parent_transform: Transform3D, result: Array[Dictionary]) -> void:
	var node_transform := parent_transform
	if node is Node3D:
		node_transform *= (node as Node3D).transform

	if node is MeshInstance3D and (node as MeshInstance3D).mesh != null:
		var mesh_instance := node as MeshInstance3D
		result.append({"mesh": mesh_instance.mesh, "transform": node_transform})

	for child in node.get_children():
		_collect_tree_meshes(child, node_transform, result)

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

func switch_animal(animal_scene: PackedScene) -> void:
	if player == null or animal_scene == null or level_finished:
		return

	var transition_state: Dictionary = player.call("capture_transition_state")
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

func build_collectibles() -> void:
	var positions := [
		Vector3(-4.0, 6.5, 30.0),
		Vector3(4.0, 8.0, 54.0),
		Vector3(4.0, 7.5, 82.0),
		Vector3(-4.0, 10.0, 108.0),
		Vector3(-4.0, 8.0, 176.0),
		Vector3(4.0, 9.5, 244.0),
		Vector3(4.0, 7.5, 312.0),
		Vector3(-4.0, 10.0, 380.0),
		Vector3(4.0, 8.5, 430.0),
		Vector3(-12.0, 12.0, 500.0),
		Vector3(4.0, 15.0, 560.0),
		Vector3(12.0, 10.0, 620.0),
		Vector3(-4.0, 18.0, 680.0)
	]

	for index in range(positions.size()):
		var collectible := Area3D.new()
		collectible.name = "Ring_%02d" % (index + 1)
		collectible.position = positions[index]
		collectible.add_to_group("collectible")
		collectible.set_script(load("res://scripts/Collectible.gd"))
		collectible.picked_up.connect(_on_collectible_picked_up)
		add_child(collectible)

	total_collectibles = positions.size()

func _prepare_test_start() -> void:
	if player == null:
		return
	player.global_position.z = TEST_START_Z
	collected_count = maxi(total_collectibles - 1, 0)
	camera_pivot.global_position = player.global_position + Vector3(0.0, 2.0, 0.0)

func build_goal() -> void:
	goal = Area3D.new()
	goal.name = "Goal"
	goal.position = Vector3(0, 12.0, 725)
	goal.monitoring = true
	goal.monitorable = true
	goal.body_entered.connect(_on_goal_body_entered)

	var collision := CollisionShape3D.new()
	var box_shape := BoxShape3D.new()
	box_shape.size = Vector3(56.0, 24.0, 1.0)
	collision.shape = box_shape
	goal.add_child(collision)

	var mesh := MeshInstance3D.new()
	var finish_plane := PlaneMesh.new()
	finish_plane.size = Vector2(56.0, 24.0)
	mesh.mesh = finish_plane
	mesh.rotation_degrees.x = 90.0
	var material := StandardMaterial3D.new()
	material.albedo_color = Color(0.35, 0.72, 0.9, 0.22)
	material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	material.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	material.cull_mode = BaseMaterial3D.CULL_DISABLED
	mesh.material_override = material
	goal.add_child(mesh)

	add_child(goal)

func build_final_goal() -> void:
	final_goal = Area3D.new()
	final_goal.name = "FinalGoal"
	final_goal.position = Vector3(0.0, 12.0, 870.0)
	final_goal.body_entered.connect(_on_final_goal_body_entered)
	var collision := CollisionShape3D.new()
	var box_shape := BoxShape3D.new()
	box_shape.size = Vector3(56.0, 24.0, 1.0)
	collision.shape = box_shape
	final_goal.add_child(collision)

	var mesh := MeshInstance3D.new()
	var plane := PlaneMesh.new()
	plane.size = Vector2(56.0, 24.0)
	mesh.mesh = plane
	mesh.rotation_degrees.x = 90.0
	var material := StandardMaterial3D.new()
	material.albedo_color = Color(0.35, 0.72, 0.9, 0.22)
	material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	material.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	material.cull_mode = BaseMaterial3D.CULL_DISABLED
	mesh.material_override = material
	final_goal.add_child(mesh)
	add_child(final_goal)

func build_finish_rabbit() -> void:
	var rabbit_scene := load("res://assets/models/player/rabbit.glb") as PackedScene
	finish_rabbit = rabbit_scene.instantiate() as Node3D
	finish_rabbit.name = "FinishRabbit"
	finish_rabbit.position = Vector3(0.0, 0.0, 745.0)
	finish_rabbit.scale = Vector3.ONE * 1.5
	add_child(finish_rabbit)

	rabbit_touch_area = Area3D.new()
	rabbit_touch_area.name = "RabbitTouchArea"
	rabbit_touch_area.position = Vector3(0.0, 0.7, 745.0)
	var touch_shape := CollisionShape3D.new()
	var touch_sphere := SphereShape3D.new()
	touch_sphere.radius = 1.4
	touch_shape.shape = touch_sphere
	rabbit_touch_area.add_child(touch_shape)
	rabbit_touch_area.body_entered.connect(_on_rabbit_touched)
	add_child(rabbit_touch_area)

func build_hare_obstacles() -> void:
	var obstacles := [
		{"position": Vector3(0.0, 0.55, 760.0), "size": Vector3(3.0, 1.1, 2.5)},
		{"position": Vector3(4.0, 0.9, 775.0), "size": Vector3(3.2, 1.8, 3.0)},
		{"position": Vector3(0.0, 1.3, 790.0), "size": Vector3(5.0, 2.6, 4.5)},
		{"position": Vector3(-4.0, 0.7, 808.0), "size": Vector3(3.5, 1.4, 3.0)},
		{"position": Vector3(2.5, 1.1, 825.0), "size": Vector3(4.2, 2.2, 3.5)},
		{"position": Vector3(-2.0, 0.55, 844.0), "size": Vector3(3.0, 1.1, 2.5)}
	]
	for index in range(obstacles.size()):
		var obstacle: Dictionary = obstacles[index]
		var size: Vector3 = obstacle["size"]
		var body := StaticBody3D.new()
		body.name = "HareBox_%02d" % (index + 1)
		body.position = obstacle["position"]
		body.add_to_group("hare_obstacle")

		var collision := CollisionShape3D.new()
		var box_shape := BoxShape3D.new()
		box_shape.size = size
		collision.shape = box_shape
		body.add_child(collision)

		var mesh := MeshInstance3D.new()
		var box_mesh := BoxMesh.new()
		box_mesh.size = size
		mesh.mesh = box_mesh
		var material := StandardMaterial3D.new()
		material.albedo_color = Color(0.42, 0.55, 0.64) if index % 2 == 0 else Color(0.57, 0.45, 0.34)
		material.roughness = 0.85
		mesh.material_override = material
		body.add_child(mesh)
		add_child(body)

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
	start_button.text = "Press Space to soar"
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
	transition_end_plane.hide()
	if rabbit_touch_area != null:
		rabbit_touch_area.queue_free()
		rabbit_touch_area = null
	if player.get_script().resource_path != "res://scripts/Player.gd":
		switch_animal(load("res://scenes/animals/Bird.tscn") as PackedScene)
	player.call("reset_run")
	build_collectibles()
	build_finish_rabbit()
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
	if body == player:
		_show_finish_card()

func _on_rabbit_touched(body: Node) -> void:
	if body != player or finish_rabbit == null:
		return
	rabbit_touch_area.set_deferred("monitoring", false)
	transition_end_plane.global_position = Vector3(0.0, 12.0, player.global_position.z + 10.0)
	switch_animal(load("res://scenes/animals/Hare.tscn") as PackedScene)
	finish_rabbit.queue_free()
	finish_rabbit = null
	rabbit_touch_area.queue_free()
	rabbit_touch_area = null
	status_label.text = "Hare: hold Space to charge a longer hop."

func _on_hare_controls_unlocked(_world_position: Vector3) -> void:
	status_label.text = "Hare controls active."
