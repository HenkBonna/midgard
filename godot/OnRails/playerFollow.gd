extends PathFollow3D

var Player : CharacterBody3D
var RabbitPath: PathFollow3D
var TurnPoint: PathFollow3D
var MovementBurst : float
var Turning : bool
var Speed : float

var last_direction = Vector3.ZERO
# Called when the node enters the scene tree for the first time.
func _ready():
	Player = get_node("../../Player")
	RabbitPath = get_node("../RabbitPath")
	TurnPoint = get_node("../TurnLooker")
	Player.onRail = true
	Speed = 4

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var input_dir = Input.get_vector("left", "right", "forward", "backward")
	
	# Storing the old positions
	var old_pos = Player.position
	
	
	Speed = lerp(Speed, 4.0, 0.1)
	Speed -= input_dir.y * 0.1


	
	progress += delta * (Speed)

	RabbitPath.progress = clamp(RabbitPath.progress + delta * (6), progress, progress + 8)
	
	#Calculating the movementvector
	var movement = (position - old_pos).normalized()
	var turn_direction = position.direction_to(TurnPoint.position)
	var distance_player = Player.global_position.distance_to(global_position)
	if ( distance_player > 5):
		if (distance_player > 10):
			Player.global_position = TurnPoint.global_position
		else:
			Player.global_position += (distance_player - 5) * Player.global_position.direction_to(global_position)
			Player.move_and_slide()
	Player.look_at(RabbitPath.global_position)
	# Calculating the magnitude of the turn
	var dot_product = movement.dot(turn_direction)
	var angle = acos(dot_product)

	if angle > PI/30:
		print("in a Turn")
		Turning = true
		RabbitPath.progress -= delta
		if Input.is_action_pressed("action"):
			progress -= delta 
			RabbitPath.progress -= delta
			Player.position.x += sign(movement.cross(turn_direction).y) * 0.1
			MovementBurst += 0.3
		elif angle > PI/4:
			Player.position.x += sign(movement.cross(turn_direction).y) * 0.1
			Speed -= 2
	else :
		print("not in a Turn")
		Turning = false
		Speed += MovementBurst
		MovementBurst = 0
