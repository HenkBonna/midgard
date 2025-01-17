extends CharacterBody3D


var SPEED = 2.0
var onRail = false

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")


func _physics_process(delta):
	# Add the gravity.

	
	if not is_on_floor():
		velocity.y -= gravity * delta

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var input_dir = Input.get_vector("left", "right","forward", "backward")
	var direction = (transform.basis * Vector3(input_dir.y, 0, input_dir.x)).normalized()
	if direction:
		velocity.z = direction.z * SPEED
	else:		velocity.z = move_toward(velocity.z, 0, SPEED)

	move_and_slide()
