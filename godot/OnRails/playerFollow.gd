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
	Player = $Player
	RabbitPath = get_node("../RabbitPath")
	TurnPoint = get_node("../TurnLooker")
	Player.onRail = true
	Speed = 4

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var input_dir = Input.get_vector("left", "right", "forward", "backward")
	
	# Storing the old positions
	var old_pos = position
	
	# Normalizing old values via lerp
	Player.position.x = lerp(Player.position.x,0.0, 0.05)
	Player.position.x += input_dir.x * 0.1
	Player.position.x = clamp(Player.position.x, -5.0, 5.0)
	
	Speed = lerp(Speed, 4.0, 0.02)
	Speed -= input_dir.y * 0.1
	Speed = clamp(Speed, 2.0, 8.0)

	
	progress += delta * (Speed)
	TurnPoint.progress += delta * (Speed)
	RabbitPath.progress = clamp(RabbitPath.progress + delta * (5), progress, progress + 8)
	
	#Calculating the movementvector
	var movement = (position - old_pos).normalized()
	var turn_direction = position.direction_to(TurnPoint.position)

	# Calculating the magnitude of the turn
	var dot_product = movement.dot(turn_direction)
	var angle = acos(dot_product)
	
	if angle > PI/8:
		print("in a Turn")
		Turning = true
		if Input.is_action_pressed("action"):
			progress -= delta 
			TurnPoint.progress -= delta  
			RabbitPath.progress -= delta
			MovementBurst += 0.1
		elif angle > PI/4:
			Player.position.x += movement.cross(turn_direction).y * 0.1
			Speed -= 0.1
	else :
		print("not in a Turn")
		Turning = false
		Speed += MovementBurst
		MovementBurst = 0
	Player.move_and_slide()
