extends MeshInstance3D

@export var trail_width: float = 0.12
@export var trail_lifetime: float = 0.45

var anchor: Node3D
var points: Array[Vector3] = []
var ages: Array[float] = []
var ribbon: ArrayMesh
var trail_material: StandardMaterial3D
var soar_amount: float = 0.0

func set_anchor(source: Node3D) -> void:
    anchor = source

func _ready() -> void:
    top_level = true
    global_transform = Transform3D.IDENTITY
    cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
    ribbon = ArrayMesh.new()
    mesh = ribbon

    trail_material = StandardMaterial3D.new()
    trail_material.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
    trail_material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
    trail_material.cull_mode = BaseMaterial3D.CULL_DISABLED
    trail_material.vertex_color_use_as_albedo = true
    trail_material.emission_enabled = true
    material_override = trail_material
    set_soar_amount(0.0)

func set_soar_amount(amount: float) -> void:
    soar_amount = clampf(amount, 0.0, 1.0)
    var color := Color(1.0, 0.88, 0.68).lerp(Color(0.08, 0.48, 1.0), soar_amount)
    trail_material.albedo_color = color
    trail_material.emission = color
    trail_material.emission_energy_multiplier = lerpf(0.65, 1.8, soar_amount)

func _process(delta: float) -> void:
    if not is_instance_valid(anchor):
        return

    for index in range(ages.size()):
        ages[index] += delta
    while not ages.is_empty() and ages[-1] > trail_lifetime:
        ages.pop_back()
        points.pop_back()

    var current_point := anchor.global_position
    if points.is_empty() or current_point.distance_to(points[0]) >= 0.1:
        points.push_front(current_point)
        ages.push_front(0.0)
    if points.size() > 36:
        points.pop_back()
        ages.pop_back()

    _rebuild_ribbon()

func _rebuild_ribbon() -> void:
    ribbon.clear_surfaces()
    if points.size() < 2:
        return

    var vertices := PackedVector3Array()
    var colors := PackedColorArray()
    var indices := PackedInt32Array()
    var last_index: int = points.size() - 1

    for index in range(points.size()):
        var direction := points[0] - points[min(index + 1, last_index)]
        if direction.length_squared() < 0.0001 and index > 0:
            direction = points[index - 1] - points[index]
        direction = direction.normalized()
        var side := Vector3.UP.cross(direction).normalized()
        if side.length_squared() < 0.0001:
            side = Vector3.RIGHT

        var progress := float(index) / float(last_index)
        var width := trail_width * pow(1.0 - progress, 1.2)
        var fade := (1.0 - progress) * (1.0 - ages[index] / trail_lifetime)
        vertices.append(to_local(points[index] - side * width))
        vertices.append(to_local(points[index] + side * width))
        colors.append(Color(1.0, 1.0, 1.0, fade))
        colors.append(Color(1.0, 1.0, 1.0, fade))

    for index in range(last_index):
        var start := index * 2
        indices.append_array(PackedInt32Array([start, start + 1, start + 2, start + 1, start + 3, start + 2]))

    var arrays: Array = []
    arrays.resize(Mesh.ARRAY_MAX)
    arrays[Mesh.ARRAY_VERTEX] = vertices
    arrays[Mesh.ARRAY_COLOR] = colors
    arrays[Mesh.ARRAY_INDEX] = indices
    ribbon.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
