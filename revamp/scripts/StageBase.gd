extends Node3D

func create_box_body(name: String, position: Vector3, size: Vector3, color: Color, roughness: float = 0.85, rounded_collision: bool = true) -> StaticBody3D:
    var body := StaticBody3D.new()
    body.name = name
    body.position = position
    body.add_to_group("obstacle")

    var collision := CollisionShape3D.new()
    if rounded_collision:
        var capsule := CapsuleShape3D.new()
        capsule.radius = minf(size.x, size.z) * 0.48
        capsule.height = maxf(size.y, capsule.radius * 2.0)
        collision.shape = capsule
    else:
        var shape := BoxShape3D.new()
        shape.size = size
        collision.shape = shape
    body.add_child(collision)

    var mesh := MeshInstance3D.new()
    var box := BoxMesh.new()
    box.size = size
    mesh.mesh = box
    var material := StandardMaterial3D.new()
    material.albedo_color = color
    material.roughness = roughness
    mesh.material_override = material
    body.add_child(mesh)
    add_child(body)
    return body

func add_tree_multimeshes(scene: PackedScene, placements: Array[Transform3D]) -> void:
    var source_root := scene.instantiate()
    var mesh_parts: Array[Dictionary] = []
    _collect_tree_meshes(source_root, Transform3D.IDENTITY, mesh_parts)
    source_root.free()

    for part in mesh_parts:
        var mesh: Mesh = part["mesh"]
        var local_transform: Transform3D = part["transform"]
        var multimesh := MultiMesh.new()
        multimesh.transform_format = MultiMesh.TRANSFORM_3D
        multimesh.mesh = mesh
        multimesh.instance_count = placements.size()
        for index in range(placements.size()):
            multimesh.set_instance_transform(index, placements[index] * local_transform)

        var instance := MultiMeshInstance3D.new()
        instance.multimesh = multimesh
        instance.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
        add_child(instance)

func _collect_tree_meshes(node: Node, parent_transform: Transform3D, result: Array[Dictionary]) -> void:
    var node_transform := parent_transform
    if node is Node3D:
        node_transform *= (node as Node3D).transform
    if node is MeshInstance3D and (node as MeshInstance3D).mesh != null:
        var mesh_instance := node as MeshInstance3D
        result.append({"mesh": mesh_instance.mesh, "transform": node_transform})
    for child in node.get_children():
        _collect_tree_meshes(child, node_transform, result)

func create_finish_area(name: String, position: Vector3, size: Vector2, color: Color = Color(0.35, 0.72, 0.9, 0.22)) -> Area3D:
    var area := Area3D.new()
    area.name = name
    area.position = position
    var collision := CollisionShape3D.new()
    var box_shape := BoxShape3D.new()
    box_shape.size = Vector3(size.x, size.y, 1.0)
    collision.shape = box_shape
    area.add_child(collision)

    var mesh := MeshInstance3D.new()
    var plane := PlaneMesh.new()
    plane.size = size
    mesh.mesh = plane
    mesh.rotation_degrees.x = 90.0
    var material := StandardMaterial3D.new()
    material.albedo_color = color
    material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
    material.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
    material.cull_mode = BaseMaterial3D.CULL_DISABLED
    mesh.material_override = material
    area.add_child(mesh)
    add_child(area)
    return area
