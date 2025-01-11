extends PathFollow3D

@export var point : Node3D
@export var movementVector: Vector3
var SPEED : float

# Called when the node enters the scene tree for the first time.
func _ready():
	point = $Point
	SPEED = 4

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
