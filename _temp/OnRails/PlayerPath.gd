extends PathFollow3D

var player : CharacterBody3D
var point: Node3D


# Called when the node enters the scene tree for the first time.
func _ready():
	point = $Node3D
	player = $Node3D/Player
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var distance = player.global_transform.origin.distance_to(point.global_transform.origin)
	if distance > 5:
		var direction = (point.global_transform.origin - player.global_transform.origin).normalized()
		#player.global_transform.origin += direction * 0.1

		player.velocity.x = direction.x * player.player_acc
		player.velocity.z = direction.z * player.player_acc
		

		player.move_and_slide()

	progress += player.forward_momentum * delta
	pass
