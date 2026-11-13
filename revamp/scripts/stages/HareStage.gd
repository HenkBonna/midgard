extends "res://scripts/StageBase.gd"

signal rabbit_touched(body: Node)
signal dog_mount_line_crossed(body: Node)

var transition_end_plane: MeshInstance3D
var finish_rabbit: Node3D
var rabbit_touch_area: Area3D
var dog_mount: Node3D
var dog_mount_line: Area3D

func _ready() -> void:
    _build_transition_marker()
    _build_rabbit()
    _build_obstacles()
    _build_dog_mount()
    dog_mount_line = create_finish_area("HareFinish", Vector3(0.0, 12.0, 870.0), Vector2(56.0, 24.0))
    dog_mount_line.body_entered.connect(_on_dog_mount_line_entered)

func _build_transition_marker() -> void:
    transition_end_plane = MeshInstance3D.new()
    transition_end_plane.name = "TransitionEndPlane"
    var plane := PlaneMesh.new()
    plane.size = Vector2(56.0, 24.0)
    transition_end_plane.mesh = plane
    transition_end_plane.position = Vector3(0.0, 12.0, 0.0)
    transition_end_plane.rotation_degrees.x = 90.0
    var material := StandardMaterial3D.new()
    material.albedo_color = Color(1.0, 0.08, 0.06, 0.3)
    material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
    material.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
    material.cull_mode = BaseMaterial3D.CULL_DISABLED
    transition_end_plane.material_override = material
    transition_end_plane.visible = false
    add_child(transition_end_plane)

func _build_rabbit() -> void:
    finish_rabbit = (load("res://assets/models/player/rabbit.glb") as PackedScene).instantiate() as Node3D
    finish_rabbit.name = "FinishRabbit"
    finish_rabbit.position = Vector3(0.0, 0.0, 745.0)
    finish_rabbit.scale = Vector3.ONE * 1.5
    add_child(finish_rabbit)

    rabbit_touch_area = Area3D.new()
    rabbit_touch_area.name = "RabbitTouchArea"
    rabbit_touch_area.position = Vector3(0.0, 0.7, 745.0)
    var touch_shape := CollisionShape3D.new()
    var touch_sphere := SphereShape3D.new()
    touch_sphere.radius = 1.4
    touch_shape.shape = touch_sphere
    rabbit_touch_area.add_child(touch_shape)
    rabbit_touch_area.body_entered.connect(_on_rabbit_touched)
    add_child(rabbit_touch_area)

func _build_obstacles() -> void:
    var obstacles := [
        {"position": Vector3(0.0, 0.55, 760.0), "size": Vector3(3.0, 1.1, 2.5)},
        {"position": Vector3(4.0, 0.9, 775.0), "size": Vector3(3.2, 1.8, 3.0)},
        {"position": Vector3(0.0, 1.3, 790.0), "size": Vector3(5.0, 2.6, 4.5)},
        {"position": Vector3(-4.0, 0.7, 808.0), "size": Vector3(3.5, 1.4, 3.0)},
        {"position": Vector3(2.5, 1.1, 825.0), "size": Vector3(4.2, 2.2, 3.5)},
        {"position": Vector3(-2.0, 0.55, 844.0), "size": Vector3(3.0, 1.1, 2.5)}
    ]
    for index in range(obstacles.size()):
        var obstacle: Dictionary = obstacles[index]
        create_box_body("HareBox_%02d" % (index + 1), obstacle["position"], obstacle["size"], Color(0.42, 0.55, 0.64) if index % 2 == 0 else Color(0.57, 0.45, 0.34), 0.85, false)

func _build_dog_mount() -> void:
    dog_mount = Node3D.new()
    dog_mount.name = "DogMount"
    dog_mount.position = Vector3(0.0, 0.0, 890.0)
    var dog_model := (load("res://assets/models/player/dog.glb") as PackedScene).instantiate() as Node3D
    dog_model.scale = Vector3.ONE * 1.8
    dog_mount.add_child(dog_model)
    add_child(dog_mount)

func _on_rabbit_touched(body: Node) -> void:
    rabbit_touched.emit(body)

func _on_dog_mount_line_entered(body: Node) -> void:
    dog_mount_line_crossed.emit(body)
