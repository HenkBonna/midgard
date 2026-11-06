extends Node3D

var collected_count: int = 0
var total_collectibles: int = 0
var player: CharacterBody3D
var goal: Area3D
var status_label: Label
var velocity_label: Label
var start_card: CanvasLayer

func _ready() -> void:
	build_environment()
	build_level()
	build_player()
	build_collectibles()
	build_goal()
	build_hud()
	_update_hud()
	build_start_card()
	get_tree().paused = true

func _process(_delta: float) -> void:
	if player == null:
		return

	if velocity_label != null:
		var flight_velocity: Vector3 = player.call("get_flight_velocity")
		velocity_label.text = "Velocity: %.1f, %.1f, %.1f" % [flight_velocity.x, flight_velocity.y, flight_velocity.z]

	if goal == null or status_label == null or player.position.z < goal.position.z:
		return
	status_label.text = "Victory! You flew through every ring." if collected_count >= total_collectibles else "The gate is still closed. Fly through all the rings."

func _input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and event.keycode == KEY_ESCAPE:
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)

func build_environment() -> void:
	var environment_node := WorldEnvironment.new()
	var environment := Environment.new()
	environment.background_mode = Environment.BG_COLOR
	environment.background_color = Color(0.92, 0.93, 0.95)
	environment.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	environment.ambient_light_color = Color(0.98, 0.98, 1.0)
	environment.ambient_light_energy = 1.2
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
	material.albedo_color = color
	material.roughness = roughness
	mesh.material_override = material
	body.add_child(mesh)

	add_child(body)

func build_level() -> void:
	create_box_body("Ground", Vector3(0, -0.5, 360), Vector3(112, 1, 780), Color(0.08, 0.22, 0.12))

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

func build_player() -> void:
	player = CharacterBody3D.new()
	player.name = "Player"
	player.position = Vector3(0, 1.2, 0)
	player.add_to_group("player")

	var collision := CollisionShape3D.new()
	var capsule_shape := CapsuleShape3D.new()
	capsule_shape.radius = 0.55
	capsule_shape.height = 1.2
	collision.shape = capsule_shape
	player.add_child(collision)

	var body_mesh := MeshInstance3D.new()
	var arrow_mesh := ArrayMesh.new()
	var arrow_arrays: Array = []
	arrow_arrays.resize(Mesh.ARRAY_MAX)
	arrow_arrays[Mesh.ARRAY_VERTEX] = PackedVector3Array([
		Vector3(-0.9, -0.35, -0.8), Vector3(0.9, -0.35, -0.8), Vector3(0.0, -0.35, 1.4),
		Vector3(-0.9, 0.35, -0.8), Vector3(0.9, 0.35, -0.8), Vector3(0.0, 0.35, 1.4)
	])
	arrow_arrays[Mesh.ARRAY_INDEX] = PackedInt32Array([
		0, 1, 2, 3, 5, 4,
		0, 3, 5, 0, 5, 2,
		1, 2, 5, 1, 5, 4,
		0, 1, 4, 0, 4, 3
	])
	arrow_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrow_arrays)
	body_mesh.mesh = arrow_mesh
	var material := StandardMaterial3D.new()
	material.albedo_color = Color(0.96, 0.58, 0.24)
	material.cull_mode = BaseMaterial3D.CULL_DISABLED
	material.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	material.roughness = 0.35
	body_mesh.material_override = material
	player.add_child(body_mesh)

	var camera_pivot := Node3D.new()
	camera_pivot.name = "CameraPivot"
	camera_pivot.position = Vector3(0, 1.8, 0)
	player.add_child(camera_pivot)

	var camera := Camera3D.new()
	camera.name = "Camera3D"
	camera.position = Vector3(0.0, 4.0, -9.0)
	camera.rotation_degrees = Vector3(0.0, 180.0, 0.0)
	camera.current = true
	camera.near = 0.05
	camera.far = 250.0
	camera.h_offset = 0.0
	camera.v_offset = 0.0
	camera.fov = 82.0
	camera_pivot.add_child(camera)

	player.set_script(load("res://scripts/Player.gd"))
	add_child(player)

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

func build_goal() -> void:
	goal = Area3D.new()
	goal.name = "Goal"
	goal.position = Vector3(0, 12.0, 725)
	goal.monitoring = true
	goal.monitorable = true
	goal.body_entered.connect(_on_goal_body_entered)

	var collision := CollisionShape3D.new()
	var box_shape := BoxShape3D.new()
	box_shape.size = Vector3(3.2, 4.0, 3.2)
	collision.shape = box_shape
	goal.add_child(collision)

	var mesh := MeshInstance3D.new()
	var prism := CylinderMesh.new()
	prism.top_radius = 1.2
	prism.bottom_radius = 1.2
	prism.height = 4.0
	mesh.mesh = prism
	var material := StandardMaterial3D.new()
	material.albedo_color = Color(0.9, 0.91, 0.93)
	material.emission_enabled = true
	material.emission = Color(0.94, 0.95, 0.97)
	material.emission_energy_multiplier = 1.1
	mesh.material_override = material
	goal.add_child(mesh)

	add_child(goal)

func build_hud() -> void:
	var hud := CanvasLayer.new()
	hud.name = "HUD"

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
	velocity_label.offset_top = -52
	velocity_label.offset_right = 380
	velocity_label.offset_bottom = -20
	velocity_label.add_theme_font_size_override("font_size", 18)
	velocity_label.add_theme_color_override("font_color", Color(1, 1, 1))
	velocity_label.add_theme_color_override("font_outline_color", Color(0, 0, 0))
	velocity_label.add_theme_constant_override("outline_size", 4)
	hud.add_child(velocity_label)

	add_child(hud)

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

func _on_collectible_picked_up() -> void:
	collected_count += 1
	if player != null:
		player.call("activate_speed_boost")
	_update_hud()

func _update_hud() -> void:
	if status_label == null:
		return

	status_label.text = "Rings: %d / %d" % [collected_count, total_collectibles] if collected_count < total_collectibles else "Gate unlocked! Fly through the glowing portal."

func _on_goal_body_entered(body: Node) -> void:
	if body == player and collected_count >= total_collectibles:
		status_label.text = "Victory! You flew through every ring."
	elif body == player:
		status_label.text = "The gate is still closed. Fly through all the rings."
