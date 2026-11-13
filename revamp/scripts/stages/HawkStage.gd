extends "res://scripts/StageBase.gd"

signal ring_picked_up
signal finish_line_crossed(body: Node)

var total_collectibles: int = 0
var finish_area: Area3D

func _ready() -> void:
    _build_city()
    _build_trees()
    _build_rings()
    finish_area = create_finish_area("HawkFinish", Vector3(0.0, 12.0, 725.0), Vector2(56.0, 24.0))
    finish_area.body_entered.connect(_on_finish_body_entered)

func _build_city() -> void:
    var lane_x: Array[float] = [-18.0, -9.0, 0.0, 9.0, 18.0]
    for index in range(96):
        var tower_z: float = 8.0 + index * 7.5
        var tower_x: float = lane_x[index % lane_x.size()]
        var tower_height: float = 8.0 + float(index % 9) * 2.2
        var tower_color := Color(0.63 + randf() * 0.18, 0.70 + randf() * 0.18, 0.78 + randf() * 0.18)
        create_box_body("Tower_%02d" % (index + 1), Vector3(tower_x, tower_height * 0.5 - 0.5, tower_z), Vector3(2.8, tower_height, 2.8), tower_color, 0.8)

    var rooftops := [
        Vector3(-12.0, 7.5, 16.0), Vector3(-6.0, 9.0, 30.0), Vector3(0.0, 8.5, 46.0),
        Vector3(6.0, 10.0, 62.0), Vector3(12.0, 8.5, 80.0), Vector3(-12.0, 9.0, 96.0),
        Vector3(-6.0, 10.5, 116.0), Vector3(0.0, 11.0, 136.0), Vector3(6.0, 8.8, 158.0),
        Vector3(12.0, 9.2, 180.0), Vector3(-12.0, 10.8, 198.0), Vector3(-6.0, 9.6, 214.0),
        Vector3(0.0, 10.8, 228.0), Vector3(6.0, 9.5, 246.0), Vector3(12.0, 11.0, 264.0)
    ]
    for index in range(rooftops.size()):
        var color := Color(0.68 + randf() * 0.12, 0.73 + randf() * 0.12, 0.82 + randf() * 0.12)
        create_box_body("Rooftop_%02d" % (index + 1), rooftops[index], Vector3(2.2, 2.0, 2.2), color, 0.7)

func _build_trees() -> void:
    var tree_scenes: Array[PackedScene] = [
        load("res://assets/models/foliage/tree1.glb") as PackedScene,
        load("res://assets/models/foliage/pine_tree1.glb") as PackedScene
    ]
    var leafy: Array[Transform3D] = []
    var pine: Array[Transform3D] = []
    var tree_count := 840
    for index in range(tree_count):
        var side := -1.0 if index % 2 == 0 else 1.0
        var progress: float = float(index) / float(tree_count - 1)
        var tree_position := Vector3(side * randf_range(31.0, 53.0), 0.0, 20.0 + progress * 700.0)
        var basis := Basis(Vector3.UP, randf_range(0.0, TAU)).scaled(Vector3.ONE * randf_range(0.85, 1.25))
        var transform := Transform3D(basis, tree_position)
        if index % 4 < 2:
            leafy.append(transform)
        else:
            pine.append(transform)
    add_tree_multimeshes(tree_scenes[0], leafy)
    add_tree_multimeshes(tree_scenes[1], pine)

func _build_rings() -> void:
    var positions := [
        Vector3(-4.0, 6.5, 30.0), Vector3(4.0, 8.0, 54.0), Vector3(4.0, 7.5, 82.0),
        Vector3(-4.0, 10.0, 108.0), Vector3(-4.0, 8.0, 176.0), Vector3(4.0, 9.5, 244.0),
        Vector3(4.0, 7.5, 312.0), Vector3(-4.0, 10.0, 380.0), Vector3(4.0, 8.5, 430.0),
        Vector3(-12.0, 12.0, 500.0), Vector3(4.0, 15.0, 560.0), Vector3(12.0, 10.0, 620.0),
        Vector3(-4.0, 18.0, 680.0)
    ]
    total_collectibles = positions.size()
    for index in range(positions.size()):
        var ring := Area3D.new()
        ring.name = "Ring_%02d" % (index + 1)
        ring.position = positions[index]
        ring.add_to_group("collectible")
        ring.set_script(load("res://scripts/Collectible.gd"))
        ring.picked_up.connect(_on_ring_picked_up)
        add_child(ring)

func _on_ring_picked_up() -> void:
    ring_picked_up.emit()

func _on_finish_body_entered(body: Node) -> void:
    finish_line_crossed.emit(body)
