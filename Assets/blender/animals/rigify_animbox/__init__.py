bl_info = {
	"name": "Rigify Animbox",
	"author": "valangdance",
	"version": (0, 4, 2),
	"blender": (3, 1, 0),
	"location": "3D View > RA",
	"description": "",
	"tracker_url": "",
	"category": "Animation"}



import bpy
from bpy.props import (StringProperty, IntProperty, BoolProperty)
from bpy.types import Operator, AddonPreferences




from. import cycle_creator_ra
from. import fk_ik_switcher_ra
from. import human_rig_ra
from. import jump_tool_ra
from. import mirror_ops_ra
from. import obj2bone_ra
from. import panel_ra
from. import props_ra
from. import reset_ra
from. import selector_ra
from. import var_ops_ra



from.magic_run_walk import rigify_magic_run_ra, rigify_magic_walk_ra, adaptive_rig_size_walk_run_ra
from.pwr import pwr_ra
from.rig_box import eye_control_setup_ra
from.rig_box.rigify_samples import rigify_samples_arms, rigify_samples_human_metarig, rigify_samples_legs
from.rig_box.rigify_samples import rigify_samples_spine, rigify_zoo_metarig_dog, rigify_zoo_metarigs_cat
from.rig_box.rigify_samples import rigify_zoo_metarigs_cheetah, rigify_zoo_metarigs_horse

from.rigify_animbox_stairs import stairs_ra

from.rigify_animbox_zoo import cat_anim_ra, cat_ra, cheetah_anim_ra, cheetah_ra
from.rigify_animbox_zoo import dog_anim_ra, dog_ra, horse_anim_ra, horse_ra




modules = (
           cycle_creator_ra, fk_ik_switcher_ra, human_rig_ra, jump_tool_ra,
           mirror_ops_ra, obj2bone_ra, panel_ra, props_ra, reset_ra, selector_ra, var_ops_ra,

           # Magic Run Walk
           rigify_magic_run_ra, rigify_magic_walk_ra, adaptive_rig_size_walk_run_ra,

           # Progressive Walk Run
           pwr_ra,

           # Rig Box
           eye_control_setup_ra,

           # Rigify Samples
           rigify_samples_arms, rigify_samples_human_metarig, rigify_samples_legs,
           rigify_samples_spine, rigify_zoo_metarig_dog, rigify_zoo_metarigs_cat,
           rigify_zoo_metarigs_cheetah, rigify_zoo_metarigs_horse,

           # Zoo
           cat_anim_ra, cat_ra, cheetah_anim_ra, cheetah_ra,
           dog_anim_ra, dog_ra, horse_anim_ra, horse_ra,

           # Stairs
           stairs_ra,


           )





class RigifyAnimboxAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__


    rigify_zoo_bool: BoolProperty(
        name="Rigify Zoo",
        default=True,
    )

    rigify_human_bool: BoolProperty(
        name="Rigify Human",
        default=True,
    )

    progressive_walk_run_bool: BoolProperty(
        name="Progressive Walk-Run",
        default=True,
    )

    rigify_walk_run_bool: BoolProperty(
        name="Rigify Walk / Run",
        default=True,
    )

    rig_box_bool: BoolProperty(
        name="RigBox",
        default=True,
    )

    mirror_cycle_bool: BoolProperty(
        name="Mirror / Cycle",
        default=True,
    )

    select_key_reset_bool: BoolProperty(
        name="Select / Key / Reset",
        default=True,
    )

    rigify_fk_ik_bool: BoolProperty(
        name="Rigify - FK <> IK",
        default=True,
    )

    rigify_jumps_turns_bool: BoolProperty(
        name="Rigify - Jumps/Turns",
        default=True,
    )

    motion_path_bool: BoolProperty(
        name="Motion Path",
        default=True,
    )

    object_tools_bool: BoolProperty(
        name="Object Tools",
        default=True,
    )




    def draw(self, context):
        layout = self.layout
        layout.label(text="Enable / disable modules",  icon='HIDE_OFF')

        row = layout.row()
        row.prop(self, "rigify_zoo_bool", expand=True)
        row.prop(self, "rigify_human_bool", expand=True)
        row.prop(self, "progressive_walk_run_bool", expand=True)

        row = layout.row()
        row.prop(self, "rigify_walk_run_bool", expand=True)
        row.prop(self, "rig_box_bool", expand=True)
        row.prop(self, "mirror_cycle_bool", expand=True)

        row = layout.row()
        row.prop(self, "select_key_reset_bool", expand=True)
        row.prop(self, "rigify_fk_ik_bool", expand=True)
        row.prop(self, "rigify_jumps_turns_bool", expand=True)


        row = layout.row()
        row.prop(self, "motion_path_bool", expand=True)
        row.prop(self, "object_tools_bool", expand=True)







def register():
    bpy.utils.register_class(RigifyAnimboxAddonPreferences)

    for c in modules:
        c.register()


def unregister():
    bpy.utils.unregister_class(RigifyAnimboxAddonPreferences)

    for c in modules:
        c.unregister()


if __name__ == "__main__":
    register()



