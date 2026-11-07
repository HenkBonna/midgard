extends Area3D

signal picked_up

var pulse_phase: float = 0.0
var collected: bool = false
var ring_material: StandardMaterial3D
var marker_material: StandardMaterial3D
var glow: OmniLight3D

func _ready() -> void:
    monitoring = true
    monitorable = true
    body_entered.connect(_on_body_entered)

    # Keep the trigger inside the opening so the player must fly through the ring.
    var collision := CollisionShape3D.new()
    var ring_shape := CylinderShape3D.new()
    ring_shape.radius = 1.8
    ring_shape.height = 3.0
    collision.shape = ring_shape
    collision.rotation_degrees.x = 90.0
    add_child(collision)

    var mesh := MeshInstance3D.new()
    var ring := TorusMesh.new()
    ring.inner_radius = 2.2
    ring.outer_radius = 3.0
    ring.ring_segments = 48
    ring.rings = 16
    mesh.mesh = ring
    mesh.rotation_degrees.x = 90.0

    ring_material = StandardMaterial3D.new()
    ring_material.albedo_color = Color(1.0, 0.82, 0.18)
    ring_material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
    ring_material.emission_enabled = true
    ring_material.emission = Color(1.0, 0.84, 0.28)
    ring_material.emission_energy_multiplier = 1.5
    ring_material.roughness = 0.25
    mesh.material_override = ring_material
    add_child(mesh)

    var marker := MeshInstance3D.new()
    var marker_mesh := SphereMesh.new()
    marker_mesh.radius = 0.18
    marker_mesh.height = 0.36
    marker.mesh = marker_mesh
    marker.position = Vector3(0.0, 2.8, 0.0)
    marker_material = StandardMaterial3D.new()
    marker_material.albedo_color = Color(1.0, 0.96, 0.72)
    marker_material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
    marker_material.emission_enabled = true
    marker_material.emission = Color(1.0, 0.9, 0.55)
    marker_material.emission_energy_multiplier = 2.0
    marker.material_override = marker_material
    add_child(marker)

    glow = OmniLight3D.new()
    glow.light_color = Color(1.0, 0.82, 0.18)
    glow.light_energy = 1.3
    glow.omni_range = 4.0
    add_child(glow)

func _process(delta: float) -> void:
    if collected:
        return
    rotation.z += delta * 0.8
    pulse_phase += delta * 2.0
    scale = Vector3.ONE * (1.0 + sin(pulse_phase) * 0.05)

func _on_body_entered(body: Node) -> void:
    if collected or not body.is_in_group("player"):
        return

    collected = true
    monitoring = false
    for child in get_children():
        if child is CollisionShape3D:
            child.set_deferred("disabled", true)
    picked_up.emit()

    var collect_tween := create_tween()
    collect_tween.set_parallel()
    collect_tween.tween_property(self, "scale", scale * 1.4, 0.35).set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)
    collect_tween.tween_property(ring_material, "albedo_color:a", 0.0, 0.35)
    collect_tween.tween_property(marker_material, "albedo_color:a", 0.0, 0.3)
    collect_tween.tween_property(ring_material, "emission_energy_multiplier", 0.0, 0.3)
    collect_tween.tween_property(glow, "light_energy", 0.0, 0.25)
    collect_tween.chain().tween_callback(queue_free)
