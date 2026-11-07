extends "res://scripts/AnimalForm.gd"

signal controls_unlocked(world_position: Vector3)

@export var forward_speed: float = 10.0
@export var forward_acceleration: float = 18.0
@export var lateral_speed: float = 11.0
@export var lateral_acceleration: float = 30.0
@export var gravity: float = 28.0
@export var minimum_hop_speed: float = 7.0
@export var maximum_hop_speed: float = 15.0
@export var hop_charge_duration: float = 0.8
@export var intro_hop_speed: float = 14.0

const SIDE_LIMIT: float = 18.0

var hop_charge: float = 0.0
var action_was_held: bool = false
var intro_hops_remaining: int = 0
var intro_hops_active: bool = false

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
