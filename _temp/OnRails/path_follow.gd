extends PathFollow3D

@export var speed: float = 5.0


# Called when the node enters the scene tree for the first time.
func _ready():
	loop = true

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float):
	progress += speed * delta
	
