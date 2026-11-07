extends "res://scripts/AnimalForm.gd"

@export var fly_speed: float = 16.0
@export var lateral_acceleration: float = 65.0
@export var vertical_acceleration: float = 50.0
@export var max_lateral_velocity: float = 18.0
@export var max_vertical_velocity: float = 14.0
@export var ring_boost_multiplier: float = 1.52
@export var ring_boost_duration: float = 1.0
@export var camera_follow_speed: float = 1.9
@export var boost_roll_duration: float = 0.9
@export var turn_bank_angle: float = 0.85
@export var turn_bank_response: float = 10.0
@export var soar_speed_bonus: float = 0.4
@export var wing_fold_angle: float = 1.3
@export var soar_release_lift: float = 4.0
@export var gravity: float = 0.0
@export var soar_gravity: float = 28.0
@export var gravity_ramp_up: float = 40.0
@export var gravity_release_rate: float = 100.0
@export var release_upward_gravity: float = 4.0
@export var release_gravity_duration: float = 0.5
@export var release_speed_reduction: float = 0.08
@export var release_brake_duration: float = 0.5
@export var soar_camera_push: float = 1.0
@export var soar_camera_response: float = 7.5
@export var finish_approach_speed: float = 9.0
@export var finish_camera_follow_speed: float = 4.0
@export var finish_camera_response: float = 10.0

const SIDE_LIMIT: float = 18.0
const MIN_HEIGHT: float = 2.5
const MAX_HEIGHT: float = 24.0

var lateral_velocity: float = 0.0
var vertical_velocity: float = 0.0
var target_roll: float = 0.0
var hawk_spin: Node3D
var hawk_impact: Node3D
var camera_jolt: float = 0.0
var impact_cooldown: float = 0.0
var impact_wing_flare: float = 0.0
var ring_boost_remaining: float = 0.0
var release_gravity_remaining: float = 0.0
var release_brake_remaining: float = 0.0
var boost_roll_elapsed: float = -1.0
var soar_amount: float = 0.0
var was_soaring: bool = false
var finish_approach_active: bool = false
var finish_approach_start: Vector3 = Vector3.ZERO
var finish_approach_target: Vector3 = Vector3.ZERO
var finish_approach_control_a: Vector3 = Vector3.ZERO
var finish_approach_control_b: Vector3 = Vector3.ZERO
var finish_approach_elapsed: float = 0.0
var finish_approach_duration: float = 1.0
var wing_parts: Array[Node3D] = []
var wing_rest_rotations: Array[Vector3] = []
var folding_wings: Array[Node3D] = []
var folding_directions: Array[float] = []
var folding_rest_rotations: Array[Vector3] = []
var leg_parts: Array[Node3D] = []
var leg_rest_rotations: Array[Vector3] = []
var wing_trails: Array[MeshInstance3D] = []
var animation_time: float = 0.0

func _ready() -> void:
    hawk_impact = $HawkImpact
    hawk_spin = $HawkImpact/HawkSpin
    _add_animation_part("Cube_002", wing_parts, wing_rest_rotations)
    _add_animation_part("Plane_001", wing_parts, wing_rest_rotations)
    _add_animation_part("Cube_003", wing_parts, wing_rest_rotations)
    _add_animation_part("Plane_002", wing_parts, wing_rest_rotations)
    _add_folding_wing("Cube_002", 1.0)
    _add_folding_wing("Cube_003", -1.0)
    _add_animation_part("Plane", leg_parts, leg_rest_rotations)
    _add_animation_part("Cube_004", leg_parts, leg_rest_rotations)
    position = Vector3(-4.0, 6.5, 0.0)
    camera_pivot.top_level = true
    camera_pivot.global_position = global_position + Vector3(0.0, 2.0, 0.0)
    camera_pivot.global_rotation = Vector3.ZERO
    var obstacle_sensor := $ObstacleSensor as Area3D
    obstacle_sensor.body_entered.connect(_on_obstacle_body_entered)
    _create_wing_trail(-1.15)
    _create_wing_trail(1.15)
    Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _add_animation_part(part_name: String, parts: Array[Node3D], rest_rotations: Array[Vector3]) -> void:
    var part := hawk_spin.find_child(part_name, true, false) as Node3D
    if part != null:
        parts.append(part)
        rest_rotations.append(part.rotation)

func _add_folding_wing(part_name: String, direction: float) -> void:
    var wing := hawk_spin.find_child(part_name, true, false) as Node3D
    if wing != null:
        folding_wings.append(wing)
        folding_directions.append(direction)
        folding_rest_rotations.append(wing.rotation)

func _process(delta: float) -> void:
    animation_time += delta
    impact_wing_flare = move_toward(impact_wing_flare, 0.0, delta * 3.0)
    for index in range(wing_parts.size()):
        var phase: float = float(index) * 0.7
        var jitter: float = sin(animation_time * 15.0 + phase) * 0.08 + sin(animation_time * 23.0 + phase) * 0.04
        jitter *= 1.0 + soar_amount * 0.5
        wing_parts[index].rotation = wing_rest_rotations[index] + Vector3(0.0, jitter * 0.4, jitter)

    for index in range(folding_wings.size()):
        var fold: float = folding_directions[index] * wing_fold_angle * soar_amount
        var flare: float = -folding_directions[index] * 0.3 * impact_wing_flare
        folding_wings[index].rotation = folding_rest_rotations[index] + Vector3(0.0, fold + flare, 0.0)
    hawk_spin.rotation.x = soar_amount * 0.7

    for index in range(leg_parts.size()):
        var sway: float = sin(animation_time * 5.0 + float(index) * 0.8) * 0.04
        leg_parts[index].rotation = leg_rest_rotations[index] + Vector3(sway, 0.0, sway * 0.3)

    for trail in wing_trails:
        trail.call("set_soar_amount", soar_amount)

func activate_speed_boost() -> void:
    ring_boost_remaining = ring_boost_duration
    boost_roll_elapsed = 0.0

func begin_finish_approach(target: Vector3) -> void:
    finish_approach_start = global_position
    finish_approach_target = target
    var offset: Vector3 = target - finish_approach_start
    var arc_height: float = clampf(absf(offset.y) * 0.15 + 1.0, 1.0, 4.0)
    var control_height: float = minf(maxf(finish_approach_start.y, target.y) + arc_height, MAX_HEIGHT + 1.0)
    finish_approach_control_a = Vector3(
        finish_approach_start.x + offset.x * 0.2,
        control_height,
        finish_approach_start.z + offset.z * 0.28
    )
    finish_approach_control_b = Vector3(
        target.x - offset.x * 0.12,
        minf(maxf(finish_approach_start.y, target.y) + arc_height * 0.35, MAX_HEIGHT + 0.5),
        target.z - offset.z * 0.22
    )
    finish_approach_elapsed = 0.0
    finish_approach_duration = maxf(1.7, finish_approach_start.distance_to(target) / finish_approach_speed)
    finish_approach_active = true
    focus_camera_on(target)
    was_soaring = false
    soar_amount = 1.0
    gravity = 0.0
    ring_boost_remaining = 0.0
    release_gravity_remaining = 0.0
    release_brake_remaining = 0.0

func _advance_finish_approach(delta: float) -> void:
    finish_approach_elapsed = minf(finish_approach_elapsed + delta, finish_approach_duration)
    var progress: float = finish_approach_elapsed / finish_approach_duration
    var inverse: float = 1.0 - progress
    var next_position: Vector3 = (
        finish_approach_start * inverse * inverse * inverse
        + finish_approach_control_a * 3.0 * inverse * inverse * progress
        + finish_approach_control_b * 3.0 * inverse * progress * progress
        + finish_approach_target * progress * progress * progress
    )
    var previous_position: Vector3 = global_position
    global_position = next_position
    lateral_velocity = (next_position.x - previous_position.x) / delta
    vertical_velocity = (next_position.y - previous_position.y) / delta
    rotation.x = 0.12 + progress * 0.18
    rotation.z = lerp_angle(rotation.z, -clampf(lateral_velocity / max_lateral_velocity, -1.0, 1.0) * turn_bank_angle, 1.0 - exp(-turn_bank_response * delta))

func capture_transition_state() -> Dictionary:
    var state := super.capture_transition_state()
    state["lateral_velocity"] = lateral_velocity
    state["vertical_velocity"] = vertical_velocity
    state["gravity"] = gravity
    state["soar_amount"] = soar_amount
    state["forward_speed"] = _get_current_fly_speed()
    return state

func restore_transition_state(state: Dictionary) -> void:
    super.restore_transition_state(state)
    lateral_velocity = float(state.get("lateral_velocity", 0.0))
    vertical_velocity = float(state.get("vertical_velocity", 0.0))
    gravity = float(state.get("gravity", 0.0))
    soar_amount = float(state.get("soar_amount", 0.0))

func reset_run() -> void:
    position = Vector3(-4.0, 6.5, 0.0)
    rotation = Vector3.ZERO
    lateral_velocity = 0.0
    vertical_velocity = 0.0
    gravity = 0.0
    ring_boost_remaining = 0.0
    release_gravity_remaining = 0.0
    release_brake_remaining = 0.0
    soar_amount = 0.0
    was_soaring = false
    finish_approach_active = false
    finish_approach_target = Vector3.ZERO
    finish_approach_elapsed = 0.0
    use_hawk_camera()
    boost_roll_elapsed = -1.0
    impact_cooldown = 0.0
    camera_jolt = 0.0
    impact_wing_flare = 0.0
    hawk_impact.position = Vector3.ZERO
    hawk_impact.rotation = Vector3.ZERO
    hawk_spin.rotation = Vector3.ZERO
    camera_pivot.global_position = global_position + Vector3(0.0, 2.0, 0.0)
    camera.position = camera_rest_position

func _on_obstacle_body_entered(body: Node3D) -> void:
    if not body.is_in_group("obstacle") or impact_cooldown > 0.0:
        return

    impact_cooldown = 0.6
    camera_jolt = 1.4
    impact_wing_flare = 1.0
    var kick_side: float = -1.0 if global_position.x < body.global_position.x else 1.0
    var impact_tween := create_tween()
    impact_tween.set_trans(Tween.TRANS_CUBIC).set_ease(Tween.EASE_OUT)
    impact_tween.tween_property(hawk_impact, "position", Vector3(kick_side * 0.4, -0.25, -0.4), 0.05)
    impact_tween.parallel().tween_property(hawk_impact, "rotation", Vector3(0.5, 0.0, kick_side * 0.75), 0.05)
    impact_tween.set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)
    impact_tween.tween_property(hawk_impact, "position", Vector3.ZERO, 0.35)
    impact_tween.parallel().tween_property(hawk_impact, "rotation", Vector3.ZERO, 0.35)

func _create_wing_trail(side: float) -> void:
    var anchor := Node3D.new()
    anchor.position = Vector3(side, 0.3, -0.23)
    hawk_spin.add_child(anchor)

    var trail := MeshInstance3D.new()
    trail.set_script(load("res://scripts/WingTrail.gd"))
    trail.call("set_anchor", anchor)
    add_child(trail)
    wing_trails.append(trail)

func _get_current_fly_speed() -> float:
    if finish_approach_active:
        return finish_approach_speed

    var ring_multiplier: float = 1.0
    if ring_boost_remaining > 0.0:
        # Ease the boost in and out over its short duration.
        var boost_progress: float = 1.0 - ring_boost_remaining / ring_boost_duration
        ring_multiplier = lerpf(1.0, ring_boost_multiplier, sin(boost_progress * PI))
    var brake_multiplier: float = 1.0
    if release_brake_remaining > 0.0:
        var brake_progress: float = 1.0 - release_brake_remaining / release_brake_duration
        brake_multiplier = 1.0 - release_speed_reduction * sin(brake_progress * PI)
    return fly_speed * (ring_multiplier + soar_amount * soar_speed_bonus) * brake_multiplier

func get_flight_velocity() -> Vector3:
    return Vector3(lateral_velocity, vertical_velocity, _get_current_fly_speed())

func get_form_name() -> String:
    return "Hawk"

func _physics_process(delta: float) -> void:
    impact_cooldown = maxf(impact_cooldown - delta, 0.0)
    camera_jolt = move_toward(camera_jolt, 0.0, delta * 2.5)

    if finish_approach_active:
        _advance_finish_approach(delta)
        var approach_shake := Vector3(sin(animation_time * 70.0) * 0.2, sin(animation_time * 53.0) * 0.12, 0.0) * camera_jolt
        var approach_camera_offset := Vector3(0.0, 0.0, soar_camera_push * soar_amount) + approach_shake
        update_camera_follow(delta, approach_camera_offset)
        return

    read_keyboard_controls()
    var lateral_input: float = direction_input.x
    var vertical_input: float = direction_input.y
    var is_soaring: bool = action_held
    if is_soaring:
        release_gravity_remaining = 0.0
        gravity = move_toward(gravity, soar_gravity, gravity_ramp_up * delta)
        soar_amount = move_toward(soar_amount, 1.0, delta * 3.5)
    else:
        if was_soaring:
            release_gravity_remaining = release_gravity_duration
            release_brake_remaining = release_brake_duration
            vertical_velocity = maxf(vertical_velocity, soar_release_lift)
        if release_gravity_remaining > 0.0:
            gravity = -release_upward_gravity
            release_gravity_remaining = maxf(release_gravity_remaining - delta, 0.0)
        else:
            gravity = move_toward(gravity, 0.0, gravity_release_rate * delta)
        soar_amount = move_toward(soar_amount, 0.0, delta * 6.0)
        release_brake_remaining = maxf(release_brake_remaining - delta, 0.0)
    was_soaring = is_soaring

    lateral_velocity = move_toward(lateral_velocity, lateral_input * max_lateral_velocity, lateral_acceleration * delta)
    if vertical_input != 0.0 or gravity == 0.0:
        vertical_velocity = move_toward(vertical_velocity, vertical_input * max_vertical_velocity, vertical_acceleration * delta)
    vertical_velocity = clampf(vertical_velocity - gravity * delta, -max_vertical_velocity, max_vertical_velocity)

    var next_x: float = position.x + lateral_velocity * delta
    var next_y: float = position.y + vertical_velocity * delta
    if absf(next_x) > SIDE_LIMIT:
        lateral_velocity = 0.0
    if next_y < MIN_HEIGHT or next_y > MAX_HEIGHT:
        vertical_velocity = 0.0
    position.x = clampf(next_x, -SIDE_LIMIT, SIDE_LIMIT)
    position.y = clampf(next_y, MIN_HEIGHT, MAX_HEIGHT)

    if ring_boost_remaining > 0.0:
        ring_boost_remaining = maxf(ring_boost_remaining - delta, 0.0)
    position.z += _get_current_fly_speed() * delta

    var roll_strength: float = clamp(lateral_velocity / max_lateral_velocity, -1.0, 1.0)
    target_roll = -roll_strength * turn_bank_angle
    rotation.z = lerp_angle(rotation.z, target_roll, 1.0 - exp(-turn_bank_response * delta))
    rotation.x = lerp(rotation.x, -vertical_velocity * 0.03, 0.09)

    if boost_roll_elapsed >= 0.0:
        boost_roll_elapsed += delta
        var roll_progress: float = minf(boost_roll_elapsed / boost_roll_duration, 1.0)
        var eased_roll: float = roll_progress * roll_progress * (3.0 - 2.0 * roll_progress)
        hawk_spin.rotation.z = TAU * eased_roll
        if roll_progress >= 1.0:
            boost_roll_elapsed = -1.0
            hawk_spin.rotation.z = 0.0

    move_and_slide()

    var shake := Vector3(sin(animation_time * 70.0) * 0.2, sin(animation_time * 53.0) * 0.12, 0.0) * camera_jolt
    var camera_offset := Vector3(0.0, 0.0, soar_camera_push * soar_amount) + shake
    update_camera_follow(delta, camera_offset, camera_follow_speed, soar_camera_response)
