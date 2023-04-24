extends CharacterBody3D

@onready var wolf = $wolf
@onready var spring_arm_pivot = $SpringArmPivot
@onready var spring_arm = $SpringArmPivot/SpringArm3D
@onready var anim_tree = $AnimationTree

@export var max_SPEED = 10

const LERP_VAL =.15
const LERP_VAL_SPEED = .1
var ACTION_LERP = 1

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")

func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _unhandled_input(event):
	if Input.is_action_just_pressed("quit"):
		get_tree().quit()
	
	if event is InputEventMouseMotion:
		spring_arm_pivot.rotate_y(-event.relative.x * .005)
		#spring_arm.rotate_x(-event.relative.y * .005)
		spring_arm.rotation.x = clamp(spring_arm.rotation.x, -PI/4, PI/4)
	

func Handle_direction(a, d):
	if (a and velocity.length() > 5):
		clamp(d.x, -PI/4, PI/4) 
		clamp(d.z, -PI/4, PI/4) 
	return d

func _physics_process(delta):
	# Add the gravity.
	if not is_on_floor():
		velocity.y -= gravity * delta



	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var input_dir = Input.get_vector("move_right", "move_left", "move_forward", "move_back")
	var action = Input.is_action_pressed("action")
	var direction = (transform.basis * Vector3(input_dir.y, 0, input_dir.x)).normalized()
	direction = Handle_direction(action, direction)

	if action:
		velocity = velocity * 0.8

	direction = direction.rotated(Vector3.UP, spring_arm_pivot.rotation.y)
	if direction:
		velocity.x = lerp(velocity.x, direction.x * max_SPEED, LERP_VAL_SPEED * ACTION_LERP)
		velocity.z = lerp(velocity.z, direction.z * max_SPEED, LERP_VAL_SPEED * ACTION_LERP)
		wolf.rotation.y = lerp_angle(wolf.rotation.y, atan2(velocity.z, -velocity.x), LERP_VAL)
	else:
		velocity.x = lerp(velocity.x, 0.0, LERP_VAL)
		velocity.z = lerp(velocity.z, 0.0, LERP_VAL)

	anim_tree.set("parameters/BlendSpace1D/blend_position", velocity.length()/5)
	
	move_and_slide()
