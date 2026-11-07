shader_type canvas_item;

uniform sampler2D scene_texture : hint_screen_texture, repeat_disable, filter_linear_mipmap;
uniform float max_blur_lod : hint_range(0.0, 2.0) = 0.35;
uniform float vignette_strength : hint_range(0.0, 0.5) = 0.2;
uniform float chromatic_amount : hint_range(0.0, 0.01) = 0.0025;
// Tune from 0.0 (flat) to 0.5 (25% screen-height shift at the horizon edges).
uniform float horizon_curve : hint_range(0.0, 0.5) = 0.5;

void fragment() {
    vec2 centered_uv = (SCREEN_UV - vec2(0.5)) * 2.0;
    float edge_distance = length(centered_uv);
    float edge_amount = smoothstep(0.72, 1.3, edge_distance);
    float blur_level = edge_amount * max_blur_lod;
    float curved_horizon = 0.5 + horizon_curve * 0.5 * centered_uv.x * centered_uv.x;
    float source_y;
    if (SCREEN_UV.y < curved_horizon) {
        source_y = 0.5 * SCREEN_UV.y / curved_horizon;
    } else {
        source_y = 0.5 + 0.5 * (SCREEN_UV.y - curved_horizon) / (1.0 - curved_horizon);
    }
    vec2 source_uv = vec2(SCREEN_UV.x, source_y);
    source_uv = clamp(source_uv, vec2(0.0), vec2(1.0));
    vec2 radial_direction = centered_uv;
    radial_direction /= max(length(radial_direction), 0.0001);
    vec2 chromatic_offset = radial_direction * chromatic_amount * edge_amount;
    vec3 red_sample = textureLod(scene_texture, source_uv + chromatic_offset, blur_level).rgb;
    vec3 blue_sample = textureLod(scene_texture, source_uv - chromatic_offset, blur_level).rgb;
    vec3 scene_color = vec3(red_sample.r, (red_sample.g + blue_sample.g) * 0.5, blue_sample.b);
    float vignette = smoothstep(0.25, 1.1, edge_distance) * vignette_strength;
    COLOR = vec4(scene_color * (1.0 - vignette), 1.0);
}
