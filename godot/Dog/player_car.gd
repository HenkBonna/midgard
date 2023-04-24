extends CharacterBody3D

@onready var wolf = $wolf
@onready var spring_arm_pivot = $SpringArmPivot
@onready var spring_arm = $SpringArmPivot/SpringArm3D
@onready var anim_tree = $AnimationTree

@export var wheel_base = 0.6  # distance between front/rear axles
@export var steering_limit = 20.0  # front wheel max turning angle (deg)
@export var engine_power = 6.0
@export var braking = -9.0
@export var friction = -2.0
@export var drag = -2.0
@export var max_speed_reverse = 3.0


const SPEED = 5.0
const LERP_VAL =.15
var acceleration = Vector3.ZERO
var steer_angle = 0.0
# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")

func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func apply_friction(delta):
	if velocity.length() < 0.2 and acceleration.length() == 0:
		velocity.x = 0
		velocity.z = 0
	var friction_force = velocity * friction * delta
	var drag_force = velocity * velocity.length() * drag * delta
	acceleration += drag_force + friction_force

func calculate_steering(delta):
	var rear_wheel = transform.origin + transform.basis.z * wheel_base / 2.0
	var front_wheel = transform.origin - transform.basis.z * wheel_base / 2.0
	rear_wheel += velocity * delta
	front_wheel += velocity.rotated(transform.basis.y, steer_angle) * delta
	var new_heading = rear_wheel.direction_to(front_wheel)

	var d = new_heading.dot(velocity.normalized())
	if d > 0:
		velocity = new_heading * velocity.length()
	if d < 0:
		velocity = -new_heading * min(velocity.length(), max_speed_reverse)
	look_at(transform.origin + new_heading, transform.basis.y)

func get_input():
	var turn = Input.get_action_strength("move_left")
	turn -= Input.get_action_strength("move_right")
	steer_angle = turn * deg_to_rad(steering_limit)
	acceleration = Vector3.ZERO
	if Input.is_action_pressed("move_forward"):
		acceleration = -transform.basis.z * engine_power
	if Input.is_action_pressed("move_back"):
		acceleration = -transform.basis.z * braking

func _unhandled_input(event):
	if Input.is_action_just_pressed("quit"):
		get_tree().quit()
	
	if event is InputEventMouseMotion:
		spring_arm_pivot.rotate_y(-event.relative.x * .005)
		#spring_arm.rotate_x(-event.relative.y * .005)
		spring_arm.rotation.x = clamp(spring_arm.rotation.x, -PI/4, PI/4)
	

func _physics_process(delta):
	# Add the gravity.
	if is_on_floor():
		get_input()
		apply_friction(delta)
		calculate_steering(delta)
	acceleration.y -= gravity
	velocity += acceleration * delta


	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var input_dir = Input.get_vector("move_right", "move_left", "move_forward", "move_back")
	var direction = (transform.basis * Vector3(input_dir.y, 0, input_dir.x)).normalized()
	direction = direction.rotated(Vector3.UP, spring_arm_pivot.rotation.y)
	if direction:
		wolf.rotation.y = lerp_angle(wolf.rotation.y, atan2(velocity.z, -velocity.x), LERP_VAL)


	anim_tree.set("parameters/BlendSpace1D/blend_position", velocity.length()/20)
	
	move_and_slide()
