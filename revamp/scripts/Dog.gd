extends "res://scripts/AnimalForm.gd"

@export var forward_speed: float = 12.0
@export var forward_acceleration: float = 20.0
@export var lateral_speed: float = 14.0
@export var lateral_acceleration: float = 40.0
@export var gravity: float = 28.0
@export var drift_charge_duration: float = 0.75
@export var drift_hop_min_speed: float = 4.5
@export var drift_hop_max_speed: float = 7.0

const SIDE_LIMIT: float = 17.0

var drift_charge: float = 0.0
var was_drifting: bool = false
var skeleton: Skeleton3D
var dog_model: Node3D
var dog_model_rest_y: float = 0.0
var gait_phase: float = 0.0
var leg_bone_indices: Dictionary = {}
var leg_rest_rotations: Dictionary = {}
var body_bone_indices: Dictionary = {}
var body_rest_rotations: Dictionary = {}

const LEG_BONES: Array[String] = [
    "front_thigh.L", "front_thigh.R", "front_shin.L", "front_shin.R",
    "thigh.L", "thigh.R", "shin.L", "shin.R"
]
const BODY_BONES: Array[String] = ["spine.004", "spine.008", "spine.005", "breast.L", "breast.R", "pelvis.L", "pelvis.R"]

func _ready() -> void:
    dog_model = get_node_or_null("DogModel") as Node3D
    if dog_model != null:
        dog_model_rest_y = dog_model.position.y
    skeleton = find_child("Skeleton3D", true, false) as Skeleton3D
    if skeleton == null:
        return
    for bone_name in LEG_BONES:
        var bone_index: int = skeleton.find_bone(bone_name)
        if bone_index >= 0:
            leg_bone_indices[bone_name] = bone_index
            leg_rest_rotations[bone_name] = skeleton.get_bone_pose_rotation(bone_index)
    for bone_name in BODY_BONES:
        var bone_index: int = skeleton.find_bone(bone_name)
        if bone_index >= 0:
            body_bone_indices[bone_name] = bone_index
            body_rest_rotations[bone_name] = skeleton.get_bone_pose_rotation(bone_index)

func get_form_name() -> String:
    return "Dog"

func restore_transition_state(state: Dictionary) -> void:
    var dog_position: Vector3 = state.get("position", global_position)
    global_position = Vector3(dog_position.x, 0.0, dog_position.z)
    velocity = Vector3(0.0, 0.0, forward_speed)
    use_dog_camera()

func _physics_process(delta: float) -> void:
    read_keyboard_controls()
    var drifting: bool = action_held and is_on_floor()
    var drift_steer: float = 1.0 + drift_charge * 0.35
    var drift_acceleration: float = lateral_acceleration * (0.7 if drifting else 1.0)
    velocity.x = move_toward(velocity.x, direction_input.x * lateral_speed * drift_steer, drift_acceleration * delta)
    velocity.z = move_toward(velocity.z, forward_speed, forward_acceleration * delta)

    if is_on_floor():
        velocity.y = 0.0
        if action_held:
            drift_charge = minf(drift_charge + delta / drift_charge_duration, 1.0)
        elif was_drifting:
            velocity.y = lerpf(drift_hop_min_speed, drift_hop_max_speed, drift_charge)
            drift_charge = 0.0
    else:
        velocity.y -= gravity * delta

    was_drifting = drifting
    move_and_slide()
    position.x = clampf(position.x, -SIDE_LIMIT, SIDE_LIMIT)
    var turn_amount: float = clampf(velocity.x / maxf(lateral_speed, 0.01), -1.0, 1.0)
    var drift_yaw: float = signf(velocity.x) * drift_charge * 0.22
    rotation.y = lerp_angle(rotation.y, turn_amount * 0.42 - drift_yaw, 1.0 - exp(-8.0 * delta))
    rotation.z = lerp_angle(rotation.z, -turn_amount * 0.16, 1.0 - exp(-8.0 * delta))
    update_camera_follow(delta)

func _process(delta: float) -> void:
    if skeleton == null:
        return
    var speed_ratio: float = clampf(absf(velocity.z) / maxf(forward_speed, 0.01), 0.0, 1.0)
    var gait_amount: float = speed_ratio if is_on_floor() else speed_ratio * 0.15
    gait_phase += delta * lerpf(3.0, 10.0, speed_ratio)
    var stride: float = sin(gait_phase) * gait_amount
    _set_leg_swing("front_thigh.L", stride * 0.78)
    _set_leg_swing("front_thigh.R", -stride * 0.78)
    _set_leg_swing("thigh.L", -stride * 0.88)
    _set_leg_swing("thigh.R", stride * 0.88)
    _set_leg_swing("front_shin.L", maxf(-stride, 0.0) * 0.75)
    _set_leg_swing("front_shin.R", maxf(stride, 0.0) * 0.75)
    _set_leg_swing("shin.L", maxf(stride, 0.0) * 0.65)
    _set_leg_swing("shin.R", maxf(-stride, 0.0) * 0.65)
    var body_bounce: float = absf(sin(gait_phase * 2.0)) * gait_amount
    if dog_model != null:
        dog_model.position.y = dog_model_rest_y + body_bounce * 0.24 - drift_charge * 0.08
        dog_model.rotation.x = sin(gait_phase * 2.0) * 0.05 * gait_amount
        var turn_lean: float = -clampf(velocity.x / maxf(lateral_speed, 0.01), -1.0, 1.0) * 0.12
        var drift_lean: float = -signf(velocity.x) * drift_charge * 0.18
        dog_model.rotation.z = turn_lean + drift_lean
    _set_body_swing("spine.004", sin(gait_phase * 2.0) * 0.14 * gait_amount)
    _set_body_swing("spine.008", stride * 0.2)
    _set_body_swing("spine.005", -stride * 0.14)
    _set_body_swing("breast.L", stride * 0.08)
    _set_body_swing("breast.R", stride * 0.08)
    _set_body_swing("pelvis.L", -stride * 0.1)
    _set_body_swing("pelvis.R", -stride * 0.1)

func _set_leg_swing(bone_name: String, angle: float) -> void:
    if not leg_bone_indices.has(bone_name):
        return
    var bone_index: int = leg_bone_indices[bone_name]
    var rest_rotation: Quaternion = leg_rest_rotations[bone_name]
    skeleton.set_bone_pose_rotation(bone_index, rest_rotation * Quaternion(Vector3.RIGHT, angle))

func _set_body_swing(bone_name: String, angle: float) -> void:
    if not body_bone_indices.has(bone_name):
        return
    var bone_index: int = body_bone_indices[bone_name]
    var rest_rotation: Quaternion = body_rest_rotations[bone_name]
    skeleton.set_bone_pose_rotation(bone_index, rest_rotation * Quaternion(Vector3.RIGHT, angle))
