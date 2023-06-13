import bpy

from bpy.props import (BoolProperty, IntProperty, FloatProperty, PointerProperty,)

from bpy.types import ( PropertyGroup )




#------------ Update Func. Reset Bool Options -------------------------

def reset_stairs_arms_x(self, context):
    scene = bpy.context.scene
    ra_props = scene.animbox_ra_props  
    ra_props.property_unset('stairs_arms_rot_y_bool')
 

def reset_stairs_arms_y(self, context):
    scene = bpy.context.scene
    ra_props = scene.animbox_ra_props  
    ra_props.property_unset('stairs_arms_rot_x_bool')
 

def reset_stairs_feet_rot(self, context):
    scene = bpy.context.scene
    ra_props = scene.animbox_ra_props  
    ra_props.property_unset('stairs_foot_loc_bool')


def reset_stairs_feet_loc(self, context):
    scene = bpy.context.scene
    ra_props = scene.animbox_ra_props  
    ra_props.property_unset('stairs_foot_rot_bool')




# =====================================================
#            Update Func Walk
# =====================================================


def reset_walk_cycle_18_fun_animbox_ra(self, context):
    scene = bpy.context.scene
    ra_props = scene.animbox_ra_props  

    ra_props.property_unset('walk_cycle_24_frames_animbox_ra')


    ra_props.property_unset('run_cycle_14_frames_animbox_ra')
    ra_props.property_unset('run_cycle_18_frames_animbox_ra')


def reset_walk_cycle_24_fun_animbox_ra(self, context):
    scene = bpy.context.scene
    ra_props = scene.animbox_ra_props  

    ra_props.property_unset('walk_cycle_18_frames_animbox_ra')

    
    ra_props.property_unset('run_cycle_14_frames_animbox_ra')
    ra_props.property_unset('run_cycle_18_frames_animbox_ra')

    
 
# =====================================================
#            Update Func Run
# =====================================================


def reset_run_cycle_14_fun_animbox_ra(self, context):
    scene = bpy.context.scene
    ra_props = scene.animbox_ra_props  

    ra_props.property_unset('run_cycle_18_frames_animbox_ra')

    ra_props.property_unset('walk_cycle_18_frames_animbox_ra')
    ra_props.property_unset('walk_cycle_24_frames_animbox_ra')


def reset_run_cycle_18_fun_animbox_ra(self, context):
    scene = bpy.context.scene
    ra_props = scene.animbox_ra_props  

    ra_props.property_unset('run_cycle_14_frames_animbox_ra')

    ra_props.property_unset('walk_cycle_18_frames_animbox_ra')
    ra_props.property_unset('walk_cycle_24_frames_animbox_ra')
 


# =====================================================
#            Update Fun Run
# =====================================================


#------------ Update Func. Reset Bool Options -------------------------





class Animbox_Ra_Prop_Gr(bpy.types.PropertyGroup):
    



#======= Exclude Arms from Animation =========
    exclude_arms_from_anim : bpy.props.BoolProperty(
        name="",
        description="Exclude Arm Animation - Option",
        default = False
    )

 


#======= Mirror After Frames =================
 
    frame_int : bpy.props.IntProperty(
        name= "Frames",
        min=0, 
        soft_max=24
    )


#======= Walk Stairs Opt =====================

    up_stairs : bpy.props.BoolProperty(
        name="",
        description="Up Stairs - Option",
        default = False
    )

    spiral_stairs : bpy.props.BoolProperty(
        name="",
        description="Spiral Stairs - Option",
        default = False
    )


#--------------- Stairs Down Adjuster -------------------------------


    stairs_foot_loc_bool : bpy.props.BoolProperty(
        name="",
        description="Adjust Z Location - Option",
        default = False,
        update = reset_stairs_feet_loc,
    )


    stairs_foot_rot_bool : bpy.props.BoolProperty(
        name="",
        description="Adjust X Rotation - Option",
        default = False,
        update = reset_stairs_feet_rot,
    )

 
#========================= Transformation Amount ====================



    stairs_adjuster_transform_amount : bpy.props.FloatProperty(
        name="",
        default=0.01,
        description="Transformation Amount",
        min= -0.1,
        max= 0.1,
        step=1,
        precision=2,

    )


#------------------------ Arms --------------------------


    stairs_arms_rot_x_bool : bpy.props.BoolProperty(
        name="",
        description="Adjust X Rotation - Option",
        default = False,
        update = reset_stairs_arms_x,
    )

    stairs_arms_rot_y_bool : bpy.props.BoolProperty(
        name="",
        description="Adjust Y Rotation - Option",
        default = False,
        update = reset_stairs_arms_y,
        
    )


    stairs_adjuster_transform_amount_arms : bpy.props.FloatProperty(
        name="",
        default=0.01,
        description="Transformation Amount - Arms",
        min= -0.5,
        max= 0.5,
        step=1,
        precision=2,

    )


    
#--------------- End Stairs Down Adjuster ---------------------------
#====================================================================





#--------------- Progressive Walk Run -------------------------------


#---------------------------- Setup ---------------------------------

    # Walk / Run Curve - Add Curve Option
    create_setup_walk_run_curve_animbox_ra : bpy.props.BoolProperty(
        name="",
        description="On Curve - Option",
        default = False,
    )



    # Adjust Curve 'Run Speed'
    run_curve_speed_animbox_ra : bpy.props.BoolProperty(
        name="",
        description="Run Speed - Option",
        default = False,
    )



    # Multiply Frame Range Number
    multiply_frame_range_animbox_ra : bpy.props.IntProperty(
        name="",
        default=4,
        description="Extend the frame range - multiply number",
        min=0,
    )



#========================= Feet Cleanup - Walk Cycle =================

    # Frame Range 

    walk_cycle_frame_range_animbox_ra : bpy.props.IntProperty(
        name="",
        default=24,
        description="Walk Cycle - Frame Range",
        min=1,
    )




    # Number of 'Staple' Frames
    staple_frames_animbox_ra : bpy.props.IntProperty(
        name="",
        default=10,
        description="Number of 'Staple' Frames",
        min=1,
    )


    # Repeat process selected number of times
    staple_repeat_times_animbox_ra : bpy.props.IntProperty(
        name="",
        default=1,
        description="Repeat Times",
        min=1,
    )




#--------------- End Progressive Walk Run ---------------------------
#====================================================================





#----------------- Unlimited Rig Size - Walk / Run ------------------
#====================================================================
#====================================================================
#====================================================================



 
#----------------------- Walk --------------------------------------

    # 18 Frames Walk Cycle - Checkbox
    walk_cycle_18_frames_animbox_ra : bpy.props.BoolProperty(
        name="18",
        description="18 Frames Walk Cycle",
        default = False,
        update = reset_walk_cycle_18_fun_animbox_ra,
    )



    # 24 Frames Walk Cycle - Checkbox
    walk_cycle_24_frames_animbox_ra : bpy.props.BoolProperty(
        name="24",
        description="24 Frames Walk Cycle",
        default = False,
        update = reset_walk_cycle_24_fun_animbox_ra,
    )


#----------------------- Walk --------------------------------------


#------------------------- Run ------------------------------------

    # 14 Frames Run Cycle - Checkbox
    run_cycle_14_frames_animbox_ra : bpy.props.BoolProperty(
        name="14",
        description="14 Frames Run Cycle",
        default = False,
        update = reset_run_cycle_14_fun_animbox_ra,
    )



    # 18 Frames run Cycle - Checkbox
    run_cycle_18_frames_animbox_ra : bpy.props.BoolProperty(
        name="18",
        description="18 Frames Run Cycle",
        default = False,
        update = reset_run_cycle_18_fun_animbox_ra,
    )



#-------------------------- Run -----------------------------------


#----------------- End Unlimited Rig Size - Walk / Run --------------
#====================================================================






classes = [ Animbox_Ra_Prop_Gr ]




def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.animbox_ra_props = bpy.props.PointerProperty(type= Animbox_Ra_Prop_Gr)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)



    del bpy.types.Scene.animbox_ra_props



if __name__ == "__main__":
    register()




















