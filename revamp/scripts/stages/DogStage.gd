extends "res://scripts/StageBase.gd"

signal finish_line_crossed(body: Node)

var finish_line: Area3D

func _ready() -> void:
	_build_slalom()
	finish_line = create_finish_area("DogFinish", Vector3(0.0, 12.0, 1410.0), Vector2(56.0, 24.0))
	finish_line.body_entered.connect(_on_finish_line_entered)

func _build_slalom() -> void:
	var pine_scene := load("res://assets/models/foliage/pine_tree1.glb") as PackedScene
	var placements: Array[Transform3D] = []
	var offsets: Array[float] = [-9.0, 8.0, -4.0, 11.0, -11.0, 5.0, -7.0, 10.0]
	for index in range(24):
		var tree_position := Vector3(offsets[index % offsets.size()], 0.0, 920.0 + index * 18.0)
		var tree_scale: float = randf_range(1.25, 1.65)
		var basis := Basis(Vector3.UP, randf_range(0.0, TAU)).scaled(Vector3.ONE * tree_scale)
		placements.append(Transform3D(basis, tree_position))
		var trunk := StaticBody3D.new()
		trunk.name = "DogSlalomTree_%02d" % (index + 1)
		trunk.position = tree_position
		trunk.add_to_group("obstacle")
		var collision := CollisionShape3D.new()
		var shape := CapsuleShape3D.new()
		shape.radius = 0.45
		shape.height = 1.8
		collision.position.y = 0.9
		collision.shape = shape
		trunk.add_child(collision)
		add_child(trunk)
	add_tree_multimeshes(pine_scene, placements)

func _on_finish_line_entered(body: Node) -> void:
	finish_line_crossed.emit(body)
