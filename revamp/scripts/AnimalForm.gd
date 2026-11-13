extends CharacterBody3D

const CAMERA_HAWK: int = 0
const CAMERA_TRANSITION: int = 1
const CAMERA_HARE: int = 2
const CAMERA_DOG: int = 3

var camera_pivot: Node3D
var camera: Camera3D
var camera_rest_position: Vector3
var camera_rest_basis: Basis
var camera_state: int = CAMERA_HAWK
var camera_focus_target: Vector3 = Vector3.ZERO
var camera_focus_offset: Vector3 = Vector3.ZERO
var camera_transition_from_position: Vector3 = Vector3.ZERO
var camera_transition_from_basis: Basis = Basis.IDENTITY
var camera_transition_elapsed: float = 0.0
var camera_transition_duration: float = 0.0
var direction_input: Vector2 = Vector2.ZERO
var action_held: bool = false

func configure_camera_rig(pivot: Node3D, camera_node: Camera3D) -> void:
	camera_pivot = pivot
	camera = camera_node
	camera_rest_position = camera_node.position
	camera_rest_basis = camera_node.global_basis
	camera_transition_from_position = camera_node.position
	camera_transition_from_basis = camera_node.global_basis

func set_controls(direction: Vector2, is_action_held: bool) -> void:
	direction_input = direction
	action_held = is_action_held

func get_flight_velocity() -> Vector3:
	return velocity

func read_keyboard_controls() -> void:
	direction_input = Vector2.ZERO
	if Input.is_key_pressed(KEY_A) or Input.is_key_pressed(KEY_LEFT):
		direction_input.x += 1.0
	if Input.is_key_pressed(KEY_D) or Input.is_key_pressed(KEY_RIGHT):
		direction_input.x -= 1.0
	if Input.is_key_pressed(KEY_W) or Input.is_key_pressed(KEY_UP):
		direction_input.y += 1.0
	if Input.is_key_pressed(KEY_S) or Input.is_key_pressed(KEY_DOWN):
		direction_input.y -= 1.0
	action_held = Input.is_key_pressed(KEY_SPACE)

func capture_transition_state() -> Dictionary:
	return {
		"position": global_position,
		"velocity": velocity
	}

func restore_transition_state(state: Dictionary) -> void:
	global_position = state.get("position", global_position)
	velocity = state.get("velocity", Vector3.ZERO)

func use_hawk_camera(duration: float = 0.8) -> void:
	camera_state = CAMERA_HAWK
	camera_focus_offset = Vector3.ZERO
	_begin_camera_transition(duration)

func focus_camera_on(target: Vector3, duration: float = 1.0) -> void:
	camera_focus_target = target
	camera_focus_offset = Vector3.ZERO
	camera_state = CAMERA_TRANSITION
	_begin_camera_transition(duration)

func use_hare_camera(duration: float = 1.2) -> void:
	camera_state = CAMERA_HARE
	camera_focus_offset = Vector3(0.0, 0.9, 6.0)
	_begin_camera_transition(duration)

func use_dog_camera(duration: float = 1.0) -> void:
	camera_state = CAMERA_DOG
	camera_focus_offset = Vector3(0.0, 1.0, 8.0)
	_begin_camera_transition(duration)

func _begin_camera_transition(duration: float) -> void:
	if camera == null:
		return
	camera_transition_from_position = camera.position
	camera_transition_from_basis = camera.global_basis
	camera_transition_elapsed = 0.0
	camera_transition_duration = maxf(duration, 0.001)

func get_camera_state_name() -> String:
	match camera_state:
		CAMERA_TRANSITION:
			return "Transition"
		CAMERA_HARE:
			return "Hare"
		CAMERA_DOG:
			return "Dog"
		_:
			return "Hawk"

func get_form_name() -> String:
	return "Animal"

func update_camera_follow(delta: float, extra_offset: Vector3 = Vector3.ZERO, follow_speed: float = 2.2, camera_response: float = 6.0, focus_target: Vector3 = Vector3.ZERO, focus_enabled: bool = false) -> void:
	if camera_pivot == null or camera == null:
		return

	match camera_state:
		CAMERA_TRANSITION:
			follow_speed = 4.0
			camera_response = 10.0
			extra_offset += Vector3(0.0, 0.2, 0.25)
			focus_target = camera_focus_target
			focus_enabled = true
		CAMERA_HARE:
			follow_speed = 2.8
			camera_response = 5.5
			extra_offset += Vector3(0.0, 0.3, -3.0)
			focus_target = global_position + camera_focus_offset
			focus_enabled = true
		CAMERA_DOG:
			follow_speed = 2.8
			camera_response = 5.5
			extra_offset += Vector3(0.0, 0.45, -3.5)
			focus_target = global_position + camera_focus_offset
			focus_enabled = true

	var camera_target: Vector3 = global_position + Vector3(0.0, 2.0, 0.0)
	var follow_weight: float = 1.0 - exp(-follow_speed * delta)
	camera_pivot.global_position = camera_pivot.global_position.lerp(camera_target, follow_weight)
	var camera_weight: float = 1.0 - exp(-camera_response * delta)
	var target_position: Vector3 = camera_rest_position + extra_offset
	var target_basis: Basis = camera_rest_basis
	if focus_enabled:
		var view_direction: Vector3 = focus_target - camera.global_position
		if view_direction.length_squared() > 0.0001:
			target_basis = Basis.looking_at(view_direction, Vector3.UP)

	if camera_transition_elapsed < camera_transition_duration:
		camera_transition_elapsed = minf(camera_transition_elapsed + delta, camera_transition_duration)
		var transition_progress: float = camera_transition_elapsed / camera_transition_duration
		var eased_progress: float = transition_progress * transition_progress * (3.0 - 2.0 * transition_progress)
		camera.position = camera_transition_from_position.lerp(target_position, eased_progress)
		camera.global_basis = camera_transition_from_basis.slerp(target_basis, eased_progress)
	else:
		camera.position = camera.position.lerp(target_position, camera_weight)
		camera.global_basis = camera.global_basis.slerp(target_basis, camera_weight)
