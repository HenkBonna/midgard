extends "res://scripts/AnimalForm.gd"

signal controls_unlocked(world_position: Vector3)
signal dog_mounted(world_position: Vector3)

@export var forward_speed: float = 10.0
@export var forward_acceleration: float = 18.0
@export var lateral_speed: float = 11.0
@export var lateral_acceleration: float = 30.0
@export var gravity: float = 28.0
@export var minimum_hop_speed: float = 7.0
@export var maximum_hop_speed: float = 15.0
@export var hop_charge_duration: float = 0.8
@export var intro_hop_speed: float = 13.0

const SIDE_LIMIT: float = 18.0

var hop_charge: float = 0.0
var action_was_held: bool = false
var intro_hops_remaining: int = 0
var intro_hops_active: bool = false
var dog_mount_active: bool = false
var dog_mount_start: Vector3 = Vector3.ZERO
var dog_mount_control_a: Vector3 = Vector3.ZERO
var dog_mount_control_b: Vector3 = Vector3.ZERO
var dog_mount_target: Vector3 = Vector3.ZERO
var dog_mount_elapsed: float = 0.0
var dog_mount_duration: float = 1.0

func get_form_name() -> String:
    return "Hare"

func restore_transition_state(state: Dictionary) -> void:
    var bird_position: Vector3 = state.get("position", global_position)
    global_position = Vector3(bird_position.x, 0.0, bird_position.z)
    use_hare_camera()
    intro_hops_remaining = 1
    intro_hops_active = true
    hop_charge = 0.0
    action_was_held = false
    velocity = Vector3(
        float(state.get("lateral_velocity", 0.0)),
        0.0,
        float(state.get("forward_speed", forward_speed))
    )

func _physics_process(delta: float) -> void:
    if dog_mount_active:
        _advance_dog_mount(delta)
        update_camera_follow(delta)
        return

    read_keyboard_controls()
    var controls_just_unlocked := false
    velocity.z = move_toward(velocity.z, forward_speed, forward_acceleration * delta)

    if intro_hops_active:
        velocity.x = move_toward(velocity.x, 0.0, lateral_acceleration * delta)
        if is_on_floor():
            if intro_hops_remaining > 0:
                velocity.y = intro_hop_speed
                intro_hops_remaining -= 1
            else:
                intro_hops_active = false
                velocity.y = 0.0
                controls_just_unlocked = true
        else:
            velocity.y -= gravity * delta
    elif is_on_floor():
        velocity.x = move_toward(velocity.x, direction_input.x * lateral_speed, lateral_acceleration * delta)
        velocity.y = 0.0
        if action_held:
            hop_charge = minf(hop_charge + delta / hop_charge_duration, 1.0)
        elif action_was_held:
            velocity.y = lerpf(minimum_hop_speed, maximum_hop_speed, hop_charge)
            hop_charge = 0.0
    else:
        velocity.x = move_toward(velocity.x, direction_input.x * lateral_speed, lateral_acceleration * delta)
        velocity.y -= gravity * delta

    action_was_held = action_held and not intro_hops_active
    move_and_slide()

    position.x = clampf(position.x, -SIDE_LIMIT, SIDE_LIMIT)
    if controls_just_unlocked:
        controls_unlocked.emit(global_position)
    update_camera_follow(delta)

func begin_dog_mount(target: Vector3) -> void:
    dog_mount_start = global_position
    dog_mount_target = target
    dog_mount_control_a = dog_mount_start + Vector3(0.0, 2.8, 4.0)
    dog_mount_control_b = dog_mount_target + Vector3(0.0, 1.2, -3.0)
    dog_mount_elapsed = 0.0
    dog_mount_duration = 1.0
    dog_mount_active = true
    intro_hops_active = false
    focus_camera_on(target)

func _advance_dog_mount(delta: float) -> void:
    dog_mount_elapsed = minf(dog_mount_elapsed + delta, dog_mount_duration)
    var progress: float = dog_mount_elapsed / dog_mount_duration
    var inverse: float = 1.0 - progress
    global_position = (
        dog_mount_start * inverse * inverse * inverse
        + dog_mount_control_a * 3.0 * inverse * inverse * progress
        + dog_mount_control_b * 3.0 * inverse * progress * progress
        + dog_mount_target * progress * progress * progress
    )
    if progress >= 1.0:
        dog_mount_active = false
        dog_mounted.emit(global_position)
