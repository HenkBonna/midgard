extends CharacterBody3D

@export var fly_speed: float = 18.0
@export var lateral_acceleration: float = 30.0
@export var vertical_acceleration: float = 27.0
@export var max_lateral_velocity: float = 22.0
@export var max_vertical_velocity: float = 18.0
@export var ring_boost_multiplier: float = 1.35
@export var ring_boost_duration: float = 1.0

var lane_positions: Array[float] = [-12.0, -4.0, 4.0, 12.0]
var target_lane_index: int = 1
var target_height: float = 6.5
var lateral_velocity: float = 0.0
var vertical_velocity: float = 0.0
var target_roll: float = 0.0
var camera_pivot: Node3D
var ring_boost_remaining: float = 0.0

func _ready() -> void:
    camera_pivot = $CameraPivot
    position = Vector3(lane_positions[target_lane_index], target_height, 0.0)
    Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _unhandled_input(event: InputEvent) -> void:
    if event is InputEventKey and event.pressed:
        match event.keycode:
            KEY_A, KEY_LEFT:
                target_lane_index = min(target_lane_index + 1, lane_positions.size() - 1)
            KEY_D, KEY_RIGHT:
                target_lane_index = max(target_lane_index - 1, 0)
            KEY_W, KEY_UP:
                target_height += 3.0
            KEY_S, KEY_DOWN:
                target_height -= 3.0
            KEY_SPACE:
                target_height += 4.0

    target_height = clamp(target_height, 2.5, 24.0)

func activate_speed_boost() -> void:
    ring_boost_remaining = ring_boost_duration

func _get_current_fly_speed() -> float:
    if ring_boost_remaining <= 0.0:
        return fly_speed

    # Ease the boost in and out over its short duration.
    var boost_progress: float = 1.0 - ring_boost_remaining / ring_boost_duration
    var boost_envelope: float = sin(boost_progress * PI)
    return fly_speed * lerpf(1.0, ring_boost_multiplier, boost_envelope)

func get_flight_velocity() -> Vector3:
    return Vector3(lateral_velocity, vertical_velocity, _get_current_fly_speed())

func _physics_process(delta: float) -> void:
    var lane_target_x: float = lane_positions[target_lane_index]
    var lane_difference: float = lane_target_x - position.x
    var height_difference: float = target_height - position.y

    lateral_velocity += lane_difference * lateral_acceleration * delta
    lateral_velocity = clamp(lateral_velocity, -max_lateral_velocity, max_lateral_velocity)
    lateral_velocity *= 0.72
    position.x += lateral_velocity * delta

    vertical_velocity += height_difference * vertical_acceleration * delta
    vertical_velocity = clamp(vertical_velocity, -max_vertical_velocity, max_vertical_velocity)
    vertical_velocity *= 0.7
    position.y += vertical_velocity * delta

    if ring_boost_remaining > 0.0:
        ring_boost_remaining = maxf(ring_boost_remaining - delta, 0.0)
    position.z += _get_current_fly_speed() * delta

    var roll_strength: float = clamp(lateral_velocity / max_lateral_velocity, -1.0, 1.0)
    target_roll = roll_strength * 0.22
    rotation.z = lerp(rotation.z, target_roll, 0.06)
    rotation.x = lerp(rotation.x, -vertical_velocity * 0.03, 0.09)

    move_and_slide()

    if camera_pivot != null:
        camera_pivot.global_position = global_position + Vector3(0.0, 2.0, 0.0)
