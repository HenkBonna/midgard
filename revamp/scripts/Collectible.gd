extends Area3D

signal picked_up

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

    var material := StandardMaterial3D.new()
    material.albedo_color = Color(1.0, 0.82, 0.18)
    material.emission_enabled = true
    material.emission = Color(1.0, 0.84, 0.28)
    material.emission_energy_multiplier = 1.5
    material.roughness = 0.25
    mesh.material_override = material
    add_child(mesh)

    var glow := OmniLight3D.new()
    glow.light_color = Color(1.0, 0.82, 0.18)
    glow.light_energy = 1.3
    glow.omni_range = 4.0
    add_child(glow)

func _on_body_entered(body: Node) -> void:
    if body.is_in_group("player"):
        picked_up.emit()
        queue_free()
