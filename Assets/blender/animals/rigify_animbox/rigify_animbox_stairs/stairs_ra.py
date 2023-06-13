import bpy
import fnmatch


from bpy.props import (PointerProperty)
from bpy.types import (Panel)
 
 


#------------------ Stairs ----------------------------------


class OBJECT_OT_add_walk_stairs_geo_animbox_ra(bpy.types.Operator):
    '''Add Stairs - depending on the chosen option:
Down / Up Stairs / Straight / Spiral'''

    bl_idname = "object.add_walk_stairs_geo_animbox_ra"
    bl_label = "Add Stairs"
    bl_options = {'REGISTER', 'UNDO'}


 

    def execute(self, context):

        scene = context.scene


        current_mode = bpy.context.mode
        if current_mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    

        
        # Ref
        spiral_stairs_opt = scene.animbox_ra_props.spiral_stairs
        up_stairs_opt = scene.animbox_ra_props.up_stairs


        # Delete Stairs Mesh
        for o in bpy.data.objects:
            if o.type == 'MESH' and o.name.startswith('Stairs_up_down'):
                bpy.data.objects.remove(o, do_unlink=True)    

        for block in bpy.data.meshes:
            s = bpy.data.meshes.get('Stairs_up_down') 
            if s and block.users == 0:
                bpy.data.meshes.remove(block)

        # Delete Spiral Empty
        for o in bpy.data.objects:
            if o.type == 'EMPTY' and o.name.startswith('Spiral_Empty'):
                bpy.data.objects.remove(o)    
        
        
        def add_empty():
            bpy.context.object
            bpy.ops.object.empty_add(type='SPHERE', radius=0.1, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

        add_empty()

        
        bpy.context.object.name = 'Spiral_Empty'
        bpy.context.object.rotation_euler[2] = 0.286234
  

        def stair_down_up_stairs():
            bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
            stair_step = bpy.context.selected_objects[0]
            stair_step.name = 'Stairs_up_down'
            stair_step.data.name = 'Stairs_up_down'
            stair_step.dimensions = [1.0, 0.4, 0.2]
            stair_step.location.z = -0.1
            if up_stairs_opt:
                stair_step.location.y = -0.1
            
 
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

            
            mod = stair_step.modifiers.new("Stairs_Array" , 'ARRAY')

            mod.relative_offset_displace[0] = 0
            mod.relative_offset_displace[1] = -1
            mod.relative_offset_displace[2] = -1  
            mod.count = 12
            
            if up_stairs_opt: 
                mod.relative_offset_displace[2] = 1
         
            if spiral_stairs_opt:
                mod.count = 12
                mod.use_object_offset = True
                mod.offset_object = bpy.data.objects["Spiral_Empty"]
                     
              
        stair_down_up_stairs() 
            
                  

        return {'FINISHED'}

 
#------------------ End  Stairs -----------------------------
#============================================================    
#============================================================    
#============================================================    






#------------------ Stairs Walk -----------------------------



class OBJECT_OT_stairs_walk_animbox_ra(bpy.types.Operator):
    '''Stairs Walk - depending on the chosen option:
Down / Up Stairs / Straight / Spiral'''

    bl_idname = "object.stairs_walk_animbox_ra"
    bl_label = "Stairs Walk"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)

    def execute(self, context):

        scene = context.scene

        # Ref
        spiral_stairs_opt = scene.animbox_ra_props.spiral_stairs
        up_stairs_opt = scene.animbox_ra_props.up_stairs

        exclude_arms = scene.animbox_ra_props.exclude_arms_from_anim


        # TOTAL RESET

        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        bpy.ops.anim.keyframe_clear_v3d() 
        bpy.ops.pose.select_all(action = 'DESELECT')
        bpy.ops.screen.frame_jump(end=False)
            
        def reset_props():
            scene = bpy.context.scene
            ra_props = scene.animbox_ra_props 
            
            ra_props.property_unset('stairs_arms_rot_y_bool')
            ra_props.property_unset('stairs_arms_rot_x_bool')
            ra_props.property_unset('stairs_foot_loc_bool')
            ra_props.property_unset('stairs_foot_rot_bool')
            ra_props.property_unset('stairs_adjuster_transform_amount')  
            ra_props.property_unset('stairs_adjuster_transform_amount_arms')
            
        reset_props()   


        pose_bones = bpy.context.object.pose.bones

            
        # FRAME RANGE
        bpy.context.scene.frame_start = 1
        if bpy.context.scene.frame_end < 250:
            bpy.context.scene.frame_end = 250
        
 

        # NAMES

        Head = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "head*")]
        Neck = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "neck*")]
         
        Torso = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "torso*")]

        Arm_Parent_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_parent.R*")]
        Arm_Parent_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_parent.L*")]

        Arm_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_fk.R*")]
        Arm_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_fk.L*")]
         
        Foot_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_ik.R*")]
        Foot_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_ik.L*")]     
         
 
        Heel_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_heel_ik.R*")]
        Heel_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_heel_ik.L*")]     
                 




#------------------- Arm Keys ------------------

        def arm_pos():
            
            def insert_keys_rot(frame):
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                               

            for o in Arm_R:
                if not exclude_arms:

                    o.rotation_quaternion=(0.915, 0.026, -0.085, 0.394)
                    insert_keys_rot(1)
                    o.rotation_quaternion=(0.899, 0.133, -0.019, 0.416)
                    insert_keys_rot(20)
                    o.rotation_quaternion=(0.907, -0.080, -0.160, 0.382)
                    insert_keys_rot(40)
                    o.rotation_quaternion=(0.866, 0.247, 0.062, 0.430)
                    insert_keys_rot(60)
                    o.rotation_quaternion=(0.907, -0.080, -0.160, 0.382)
                    insert_keys_rot(80)
                    o.rotation_quaternion=(0.866, 0.247, 0.062, 0.430)
                    insert_keys_rot(100)
                    o.rotation_quaternion=(0.907, -0.080, -0.160, 0.382)
                    insert_keys_rot(120)
                    o.rotation_quaternion=(0.866, 0.247, 0.062, 0.430)
                    insert_keys_rot(140)
                    o.rotation_quaternion=(0.907, -0.080, -0.160, 0.382)
                    insert_keys_rot(160)
                    o.rotation_quaternion=(0.866, 0.247, 0.062, 0.430)
                    insert_keys_rot(180)
                    o.rotation_quaternion=(0.907, -0.080, -0.160, 0.382)
                    insert_keys_rot(200)
                    o.rotation_quaternion=(0.866, 0.247, 0.062, 0.430)
                    insert_keys_rot(220)


            for o in Arm_L:
                if not exclude_arms:

                    o.rotation_quaternion=(0.915, 0.026, 0.085, -0.394)
                    insert_keys_rot(1)
                    o.rotation_quaternion=(0.911, -0.049, 0.134, -0.386)
                    insert_keys_rot(20)
                    o.rotation_quaternion=(0.866, 0.247, -0.062, -0.430)
                    insert_keys_rot(40)
                    o.rotation_quaternion=(0.907, -0.080, 0.160, -0.382)
                    insert_keys_rot(60)
                    o.rotation_quaternion=(0.866, 0.247, -0.062, -0.430)
                    insert_keys_rot(80)
                    o.rotation_quaternion=(0.907, -0.080, 0.160, -0.382)
                    insert_keys_rot(100)
                    o.rotation_quaternion=(0.866, 0.247, -0.062, -0.430)
                    insert_keys_rot(120)
                    o.rotation_quaternion=(0.907, -0.080, 0.160, -0.382)
                    insert_keys_rot(140)
                    o.rotation_quaternion=(0.866, 0.247, -0.062, -0.430)
                    insert_keys_rot(160)
                    o.rotation_quaternion=(0.907, -0.080, 0.160, -0.382)
                    insert_keys_rot(180)
                    o.rotation_quaternion=(0.866, 0.247, -0.062, -0.430)
                    insert_keys_rot(200)
                    o.rotation_quaternion=(0.907, -0.080, 0.160, -0.382)
                    insert_keys_rot(220)





#-------------------Straight Down----------------
#------------------------------------------------
#------------------------------------------------
#------------------------------------------------


        def stairs_straight(): 


            def arm_ik_to_fk():            
                for o in Arm_Parent_R:
                    o["IK_FK"] = float(1)
                        
                for o in Arm_Parent_L:
                    o["IK_FK"] = float(1)
                        
            arm_ik_to_fk()


            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)

            def insert_keys_loc(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
     
            def insert_keys_rot(frame):
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                                
            # Arm Keys    
            arm_pos()                     




            for o in Torso:
                o.location=(0.00, 0.00, 0.00)
                insert_keys_loc(1)
                o.location=(-0.02, -0.07, -0.01)
                insert_keys_loc(11)
                o.location=(0.00, -0.23, -0.26)
                insert_keys_loc(24)
                o.location=(0.02, -0.39, -0.22)
                insert_keys_loc(33)
                o.location=(-0.01, -0.63, -0.46)
                insert_keys_loc(46)
                o.location=(-0.02, -0.79, -0.42)
                insert_keys_loc(54)
                o.location=(0.01, -1.03, -0.66)
                insert_keys_loc(66)
                o.location=(0.02, -1.19, -0.62)
                insert_keys_loc(74)
                o.location=(-0.01, -1.43, -0.86)
                insert_keys_loc(86)
                o.location=(-0.02, -1.59, -0.82)
                insert_keys_loc(94)
                o.location=(0.01, -1.83, -1.06)
                insert_keys_loc(106)
                o.location=(0.02, -1.99, -1.02)
                insert_keys_loc(114)
                o.location=(-0.01, -2.23, -1.26)
                insert_keys_loc(126)
                o.location=(-0.02, -2.39, -1.22)
                insert_keys_loc(134)
                o.location=(0.01, -2.63, -1.46)
                insert_keys_loc(146)
                o.location=(0.02, -2.79, -1.42)
                insert_keys_loc(154)
                o.location=(-0.01, -3.03, -1.66)
                insert_keys_loc(166)
                o.location=(-0.02, -3.19, -1.62)
                insert_keys_loc(174)
                o.location=(0.01, -3.43, -1.86)
                insert_keys_loc(186)
                o.location=(0.02, -3.59, -1.82)
                insert_keys_loc(194)
                o.location=(-0.01, -3.83, -2.06)
                insert_keys_loc(206)
                o.location=(-0.02, -3.99, -2.02)
                insert_keys_loc(214)
                o.location=(-0.02, -4.12, -2.27)
                insert_keys_loc(226)


            for o in Foot_R:
                o.location=(0.00, 0.00, 0.00)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.00)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(20)
                o.location=(0.00, -0.35, 0.03)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(28)
                o.location=(0.00, -0.70, -0.20)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(36)
                o.location=(0.00, -0.75, -0.40)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(43)
                o.location=(0.00, -0.75, -0.40)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(61)
                o.location=(0.00, -1.15, -0.37)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(69)
                o.location=(0.00, -1.50, -0.62)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(77)
                o.location=(0.00, -1.55, -0.80)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(84)
                o.location=(0.00, -1.55, -0.80)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(101)
                o.location=(0.00, -1.95, -0.77)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(109)
                o.location=(0.00, -2.30, -1.02)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(117)
                o.location=(0.00, -2.35, -1.20)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(124)
                o.location=(0.00, -2.35, -1.20)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(141)
                o.location=(0.00, -2.75, -1.17)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(149)
                o.location=(0.00, -3.10, -1.42)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(157)
                o.location=(0.00, -3.15, -1.60)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(164)
                o.location=(0.00, -3.15, -1.60)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(181)
                o.location=(0.00, -3.55, -1.57)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(189)
                o.location=(0.00, -3.90, -1.82)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(197)
                o.location=(0.00, -3.95, -2.00)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(204)
                o.location=(0.00, -3.95, -2.00)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(221)


            for o in Foot_L:
                o.location=(-0.00, 0.00, 0.00)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(-0.00, -0.13, 0.04)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(7)
                o.location=(-0.00, -0.30, -0.03)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(14)
                o.location=(-0.00, -0.35, -0.20)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(21)
                o.location=(-0.00, -0.35, -0.20)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(41)
                o.location=(-0.00, -0.75, -0.17)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(49)
                o.location=(-0.00, -1.12, -0.42)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(57)
                o.location=(-0.00, -1.15, -0.60)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(64)
                o.location=(-0.00, -1.15, -0.60)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(81)
                o.location=(-0.00, -1.55, -0.57)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(89)
                o.location=(-0.00, -1.92, -0.82)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(97)
                o.location=(-0.00, -1.95, -1.00)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(104)
                o.location=(-0.00, -1.95, -1.00)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(121)
                o.location=(-0.00, -2.35, -0.97)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(129)
                o.location=(-0.00, -2.72, -1.22)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(137)
                o.location=(-0.00, -2.75, -1.40)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(144)
                o.location=(-0.00, -2.75, -1.40)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(161)
                o.location=(-0.00, -3.15, -1.37)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(169)
                o.location=(-0.00, -3.52, -1.62)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(177)
                o.location=(-0.00, -3.55, -1.80)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(184)
                o.location=(-0.00, -3.55, -1.80)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(201)
                o.location=(-0.00, -3.95, -1.77)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(209)
                o.location=(-0.00, -4.32, -2.02)
                o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
                insert_keys(217)
                o.location=(-0.00, -4.35, -2.20)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(224)
                o.location=(-0.00, -4.35, -2.20)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(241)


            for o in Heel_R:
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(1)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(12)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(23)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(32)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(39)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(45)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(52)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(63)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(72)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(79)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(85)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(92)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(103)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(112)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(119)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(125)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(132)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(143)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(152)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(159)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(165)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(172)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(183)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(192)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(199)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(205)


            for o in Heel_L:
                o.rotation_euler=(-0.000, 0.000, 0.000)
                insert_keys_rot(1)
                o.rotation_euler=(-0.000, 0.000, 0.000)
                insert_keys_rot(12)
                o.rotation_euler=(0.262, 0.000, 0.000)
                insert_keys_rot(18)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(24)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(33)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(44)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(53)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(60)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(66)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(73)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(84)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(93)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(100)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(106)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(113)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(124)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(133)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(140)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(146)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(153)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(164)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(173)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(180)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(186)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(193)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(204)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(213)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(220)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(226)


            # Action Name
            ob = bpy.context.object
            ob.animation_data.action.name = ob.name +'_Down_Stairs' 
                
                 

#-------------------End Straight Down------------
#------------------------------------------------
#------------------------------------------------



#-------------------Straight Up------------------
#------------------------------------------------
#------------------------------------------------


        def stairs_straight_up(): 
                 
            def arm_ik_to_fk():            
                for o in Arm_Parent_R:
                    o["IK_FK"] = float(1)
                        
                for o in Arm_Parent_L:
                    o["IK_FK"] = float(1)
                        
            arm_ik_to_fk()


            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)


            def insert_keys_rot(frame):
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                                
 
            # Arm Keys    
            arm_pos()  


            for o in Torso:
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(0.013, -0.193, -0.020)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(20)
                o.location=(0.020, -0.424, 0.191)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(32)
                o.location=(0.006, -0.587, 0.180)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(40)
                o.location=(-0.020, -0.830, 0.389)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(52)
                o.location=(-0.006, -0.991, 0.377)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(60)
                o.location=(0.020, -1.231, 0.591)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(72)
                o.location=(0.006, -1.391, 0.578)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(80)
                o.location=(-0.020, -1.630, 0.794)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(92)
                o.location=(-0.006, -1.789, 0.777)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(100)
                o.location=(0.020, -2.028, 0.994)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(112)
                o.location=(0.006, -2.187, 0.977)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(120)
                o.location=(-0.020, -2.425, 1.192)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(132)
                o.location=(-0.006, -2.583, 1.177)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(140)
                o.location=(0.020, -2.821, 1.390)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(152)
                o.location=(0.006, -2.979, 1.378)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(160)
                o.location=(-0.020, -3.217, 1.592)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(172)
                o.location=(-0.006, -3.375, 1.581)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(180)
                o.location=(0.020, -3.611, 1.790)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(192)
                o.location=(0.006, -3.769, 1.779)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(200)
                o.location=(-0.020, -4.005, 1.983)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(212)
                o.location=(-0.020, -4.115, 1.974)
                o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
                insert_keys(220)


            for o in Foot_R:
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(20)
                o.location=(0.000, -0.150, 0.226)
                o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
                insert_keys(26)
                o.location=(0.000, -0.519, 0.486)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(34)
                o.location=(0.000, -0.800, 0.400)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(40)
                o.location=(0.000, -0.800, 0.400)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(60)
                o.location=(-0.000, -0.948, 0.641)
                o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
                insert_keys(66)
                o.location=(-0.000, -1.323, 0.885)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(74)
                o.location=(0.000, -1.600, 0.800)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(80)
                o.location=(0.000, -1.600, 0.800)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(100)
                o.location=(0.000, -1.740, 1.023)
                o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
                insert_keys(106)
                o.location=(0.000, -2.131, 1.291)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(114)
                o.location=(0.000, -2.400, 1.200)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(120)
                o.location=(0.000, -2.400, 1.200)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(140)
                o.location=(0.000, -2.545, 1.422)
                o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
                insert_keys(146)
                o.location=(0.000, -2.921, 1.692)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(154)
                o.location=(0.000, -3.200, 1.600)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(160)
                o.location=(0.000, -3.200, 1.600)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(180)
                o.location=(0.000, -3.336, 1.792)
                o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
                insert_keys(186)
                o.location=(0.000, -3.728, 2.094)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(194)
                o.location=(0.000, -4.000, 2.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(200)
                o.location=(0.000, -4.000, 2.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(220)


            for o in Foot_L:
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(-0.000, -0.177, 0.294)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(12)
                o.location=(0.000, -0.400, 0.200)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(19)
                o.location=(0.000, -0.400, 0.200)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(40)
                o.location=(-0.000, -0.544, 0.406)
                o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
                insert_keys(46)
                o.location=(-0.000, -0.922, 0.678)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(54)
                o.location=(0.000, -1.200, 0.600)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(60)
                o.location=(0.000, -1.200, 0.600)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(80)
                o.location=(0.000, -1.358, 0.818)
                o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
                insert_keys(86)
                o.location=(0.000, -1.721, 1.083)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(94)
                o.location=(0.000, -2.000, 1.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(100)
                o.location=(0.000, -2.000, 1.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(120)
                o.location=(0.000, -2.154, 1.211)
                o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
                insert_keys(126)
                o.location=(0.000, -2.525, 1.481)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(134)
                o.location=(0.000, -2.800, 1.400)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(140)
                o.location=(0.000, -2.800, 1.400)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(160)
                o.location=(0.000, -2.960, 1.625)
                o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
                insert_keys(166)
                o.location=(0.000, -3.325, 1.893)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(174)
                o.location=(0.000, -3.600, 1.800)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(180)
                o.location=(0.000, -3.600, 1.800)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(200)
                o.location=(0.000, -3.757, 1.988)
                o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
                insert_keys(206)
                o.location=(0.000, -4.137, 2.287)
                o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
                insert_keys(214)
                o.location=(0.000, -4.400, 2.200)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(220)



            # Action Name
            ob = bpy.context.object
            ob.animation_data.action.name = ob.name +'_Up_Stairs' 
                
                 

#-------------------End Straight Up--------------
#------------------------------------------------
#------------------------------------------------








#-------------------Spiral Down--------------
#--------------------------------------------
#--------------------------------------------
#--------------------------------------------

        def stairs_spiral_down():
                   
            def arm_ik_to_fk():            
                for o in Arm_Parent_R:
                    o["IK_FK"] = float(1)
                        
                for o in Arm_Parent_L:
                    o["IK_FK"] = float(1)
                        
            arm_ik_to_fk()


            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)


            def insert_keys_rot(frame):
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                                
                
                            
            # Arm Keys    
            arm_pos()  







            for o in Torso:
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(0.005, -0.042, -0.040)
                o.rotation_quaternion=(0.999, 0.000, 0.000, 0.048)
                insert_keys(12)
                o.location=(0.044, -0.217, -0.251)
                o.rotation_quaternion=(0.997, 0.000, 0.000, 0.081)
                insert_keys(24)
                o.location=(0.082, -0.381, -0.214)
                o.rotation_quaternion=(0.988, 0.000, 0.000, 0.145)
                insert_keys(33)
                o.location=(0.098, -0.593, -0.459)
                o.rotation_quaternion=(0.979, 0.000, 0.000, 0.208)
                insert_keys(46)
                o.location=(0.136, -0.745, -0.415)
                o.rotation_quaternion=(0.966, 0.000, 0.000, 0.267)
                insert_keys(54)
                o.location=(0.261, -0.905, -0.659)
                o.rotation_quaternion=(0.947, 0.000, 0.000, 0.321)
                insert_keys(66)
                o.location=(0.364, -1.045, -0.615)
                o.rotation_quaternion=(0.925, 0.000, 0.000, 0.381)
                insert_keys(74)
                o.location=(0.480, -1.244, -0.859)
                o.rotation_quaternion=(0.894, 0.000, 0.000, 0.447)
                insert_keys(86)
                o.location=(0.596, -1.345, -0.815)
                o.rotation_quaternion=(0.862, 0.000, 0.000, 0.502)
                insert_keys(94)
                o.location=(0.837, -1.412, -1.060)
                o.rotation_quaternion=(0.813, 0.000, 0.000, 0.581)
                insert_keys(106)
                o.location=(0.974, -1.474, -1.015)
                o.rotation_quaternion=(0.758, 0.000, 0.000, 0.654)
                insert_keys(114)
                o.location=(1.181, -1.593, -1.260)
                o.rotation_quaternion=(0.689, 0.000, 0.000, 0.726)
                insert_keys(126)
                o.location=(1.348, -1.604, -1.215)
                o.rotation_quaternion=(0.658, 0.000, 0.000, 0.754)
                insert_keys(134)
                o.location=(1.558, -1.533, -1.460)
                o.rotation_quaternion=(0.597, 0.000, 0.000, 0.802)
                insert_keys(146)
                o.location=(1.707, -1.503, -1.415)
                o.rotation_quaternion=(0.547, 0.000, 0.000, 0.836)
                insert_keys(154)
                o.location=(1.953, -1.474, -1.660)
                o.rotation_quaternion=(0.485, 0.000, 0.000, 0.873)
                insert_keys(166)
                o.location=(2.101, -1.398, -1.615)
                o.rotation_quaternion=(0.436, 0.000, 0.000, 0.900)
                insert_keys(174)
                o.location=(2.223, -1.233, -1.859)
                o.rotation_quaternion=(0.354, 0.000, 0.000, 0.936)
                insert_keys(186)
                o.location=(2.331, -1.133, -1.815)
                o.rotation_quaternion=(0.301, 0.000, 0.000, 0.955)
                insert_keys(194)
                o.location=(2.518, -1.002, -2.058)
                o.rotation_quaternion=(0.232, 0.000, 0.000, 0.972)
                insert_keys(206)
                o.location=(2.613, -0.857, -2.015)
                o.rotation_quaternion=(0.173, 0.000, 0.000, 0.983)
                insert_keys(214)
                o.location=(2.645, -0.666, -2.255)
                o.rotation_quaternion=(0.105, 0.000, 0.000, 0.993)
                insert_keys(226)


            for o in Foot_R:
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(20)
                o.location=(0.054, -0.364, 0.036)
                o.rotation_quaternion=(0.996, 0.098, 0.019, 0.090)
                insert_keys(28)
                o.location=(0.120, -0.699, -0.214)
                o.rotation_quaternion=(0.981, 0.101, 0.022, 0.180)
                insert_keys(36)
                o.location=(0.136, -0.754, -0.400)
                o.rotation_quaternion=(0.982, 0.000, 0.000, 0.189)
                insert_keys(43)
                o.location=(0.136, -0.754, -0.400)
                o.rotation_quaternion=(0.982, 0.000, 0.000, 0.189)
                insert_keys(62)
                o.location=(0.348, -1.049, -0.359)
                o.rotation_quaternion=(0.941, 0.124, 0.060, 0.310)
                insert_keys(69)
                o.location=(0.594, -1.355, -0.613)
                o.rotation_quaternion=(0.911, 0.141, 0.077, 0.380)
                insert_keys(77)
                o.location=(0.637, -1.415, -0.800)
                o.rotation_quaternion=(0.874, 0.000, 0.000, 0.486)
                insert_keys(84)
                o.location=(0.637, -1.415, -0.800)
                o.rotation_quaternion=(0.874, 0.000, 0.000, 0.486)
                insert_keys(102)
                o.location=(0.988, -1.590, -0.759)
                o.rotation_quaternion=(0.822, 0.062, 0.102, 0.558)
                insert_keys(109)
                o.location=(1.371, -1.674, -1.017)
                o.rotation_quaternion=(0.757, 0.096, 0.099, 0.636)
                insert_keys(117)
                o.location=(1.414, -1.688, -1.200)
                o.rotation_quaternion=(0.707, 0.000, 0.000, 0.707)
                insert_keys(124)
                o.location=(1.414, -1.688, -1.200)
                o.rotation_quaternion=(0.707, 0.000, 0.000, 0.707)
                insert_keys(142)
                o.location=(1.802, -1.631, -1.153)
                o.rotation_quaternion=(0.598, 0.050, 0.172, 0.776)
                insert_keys(149)
                o.location=(2.181, -1.502, -1.413)
                o.rotation_quaternion=(0.533, 0.050, 0.127, 0.825)
                insert_keys(157)
                o.location=(2.237, -1.483, -1.600)
                o.rotation_quaternion=(0.462, 0.000, 0.000, 0.887)
                insert_keys(164)
                o.location=(2.237, -1.483, -1.600)
                o.rotation_quaternion=(0.462, 0.000, 0.000, 0.887)
                insert_keys(182)
                o.location=(2.524, -1.221, -1.552)
                o.rotation_quaternion=(0.370, 0.035, 0.143, 0.898)
                insert_keys(189)
                o.location=(2.769, -0.925, -1.817)
                o.rotation_quaternion=(0.250, 0.001, 0.119, 0.955)
                insert_keys(197)
                o.location=(2.802, -0.896, -2.000)
                o.rotation_quaternion=(0.198, 0.000, 0.000, 0.980)
                insert_keys(204)
                o.location=(2.802, -0.896, -2.000)
                o.rotation_quaternion=(0.198, 0.000, 0.000, 0.980)
                insert_keys(222)


            for o in Foot_L:
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(0.023, -0.109, 0.029)
                o.rotation_quaternion=(0.989, 0.076, 0.011, 0.062)
                insert_keys(7)
                o.location=(0.038, -0.299, -0.041)
                o.rotation_quaternion=(0.975, 0.172, 0.025, 0.152)
                insert_keys(14)
                o.location=(0.036, -0.343, -0.200)
                o.rotation_quaternion=(0.980, 0.000, 0.000, 0.201)
                insert_keys(20)
                o.location=(0.036, -0.343, -0.200)
                o.rotation_quaternion=(0.980, 0.000, 0.000, 0.201)
                insert_keys(42)
                o.location=(0.121, -0.651, -0.170)
                o.rotation_quaternion=(0.943, 0.113, 0.013, 0.313)
                insert_keys(49)
                o.location=(0.298, -0.961, -0.429)
                o.rotation_quaternion=(0.928, 0.138, 0.043, 0.342)
                insert_keys(57)
                o.location=(0.298, -0.967, -0.600)
                o.rotation_quaternion=(0.918, 0.000, 0.000, 0.397)
                insert_keys(64)
                o.location=(0.298, -0.967, -0.600)
                o.rotation_quaternion=(0.918, 0.000, 0.000, 0.397)
                insert_keys(82)
                o.location=(0.515, -1.201, -0.573)
                o.rotation_quaternion=(0.856, 0.079, 0.020, 0.504)
                insert_keys(89)
                o.location=(0.859, -1.386, -0.817)
                o.rotation_quaternion=(0.803, 0.091, 0.054, 0.585)
                insert_keys(97)
                o.location=(0.900, -1.404, -1.000)
                o.rotation_quaternion=(0.745, 0.000, 0.000, 0.667)
                insert_keys(104)
                o.location=(0.900, -1.404, -1.000)
                o.rotation_quaternion=(0.745, 0.000, 0.000, 0.667)
                insert_keys(122)
                o.location=(1.236, -1.463, -0.955)
                o.rotation_quaternion=(0.644, 0.096, 0.093, 0.749)
                insert_keys(129)
                o.location=(1.581, -1.449, -1.222)
                o.rotation_quaternion=(0.540, 0.096, 0.136, 0.817)
                insert_keys(137)
                o.location=(1.572, -1.451, -1.400)
                o.rotation_quaternion=(0.532, 0.000, 0.000, 0.847)
                insert_keys(144)
                o.location=(1.572, -1.451, -1.400)
                o.rotation_quaternion=(0.532, 0.000, 0.000, 0.847)
                insert_keys(162)
                o.location=(1.901, -1.305, -1.355)
                o.rotation_quaternion=(0.431, 0.066, 0.097, 0.887)
                insert_keys(169)
                o.location=(2.189, -1.075, -1.619)
                o.rotation_quaternion=(0.343, 0.073, 0.162, 0.909)
                insert_keys(177)
                o.location=(2.192, -1.077, -1.800)
                o.rotation_quaternion=(0.265, 0.000, 0.000, 0.964)
                insert_keys(184)
                o.location=(2.192, -1.077, -1.800)
                o.rotation_quaternion=(0.265, 0.000, 0.000, 0.964)
                insert_keys(202)
                o.location=(2.382, -0.819, -1.741)
                o.rotation_quaternion=(0.174, 0.062, 0.155, 0.962)
                insert_keys(209)
                o.location=(2.508, -0.489, -2.027)
                o.rotation_quaternion=(0.103, 0.024, 0.119, 0.970)
                insert_keys(217)
                o.location=(2.517, -0.464, -2.200)
                o.rotation_quaternion=(0.029, 0.000, 0.000, 1.000)
                insert_keys(224)
                o.location=(2.517, -0.464, -2.200)
                o.rotation_quaternion=(0.029, 0.000, 0.000, 1.000)
                insert_keys(242)


            for o in Heel_R:
                o.rotation_euler=(-0.000, 0.000, 0.000)
                insert_keys_rot(1)
                o.rotation_euler=(-0.000, 0.000, 0.000)
                insert_keys_rot(12)
                o.rotation_euler=(0.436, 0.000, 0.000)
                insert_keys_rot(23)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(32)
                o.rotation_euler=(0.210, 0.000, 0.000)
                insert_keys_rot(40)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(45)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(52)
                o.rotation_euler=(0.436, 0.000, 0.000)
                insert_keys_rot(63)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(72)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(80)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(84)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(92)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(103)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(112)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(121)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(125)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(132)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(143)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(152)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(162)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(166)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(172)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(183)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(192)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(201)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(205)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(212)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(223)


            for o in Heel_L:
                o.rotation_euler=(-0.000, 0.000, 0.000)
                insert_keys_rot(1)
                o.rotation_euler=(-0.000, 0.000, 0.000)
                insert_keys_rot(12)
                o.rotation_euler=(0.260, 0.000, 0.000)
                insert_keys_rot(18)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(24)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(33)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(44)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(53)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(61)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(65)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(73)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(84)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(93)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(101)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(105)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(113)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(124)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(133)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(141)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(145)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(153)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(164)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(173)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(181)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(185)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(193)
                o.rotation_euler=(0.384, 0.000, 0.000)
                insert_keys_rot(204)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(211)
                o.rotation_euler=(0.209, 0.000, 0.000)
                insert_keys_rot(220)
                o.rotation_euler=(0.000, 0.000, 0.000)
                insert_keys_rot(224)





            # Action Name
            ob = bpy.context.object
            ob.animation_data.action.name = ob.name +'_Down_Stairs_Spiral' 
                
                 

#-------------------End Spiral Down--------------
#------------------------------------------------
#------------------------------------------------





#------------------------------------------------
#-------------------Spiral Up--------------------
#------------------------------------------------
#------------------------------------------------

        def stairs_spiral_up():
            
                
            def arm_ik_to_fk():            
                for o in Arm_Parent_R:
                    o["IK_FK"] = float(1)
                        
                for o in Arm_Parent_L:
                    o["IK_FK"] = float(1)
                        
            arm_ik_to_fk()



            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)

            def insert_keys_rot(frame):
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                                
                
            # Arm Keys    
            arm_pos()  






            for o in Torso:
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(0.010, -0.168, -0.018)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.050)
                insert_keys(20)
                o.location=(0.050, -0.354, 0.166)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.120)
                insert_keys(32)
                o.location=(0.076, -0.525, 0.172)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.180)
                insert_keys(40)
                o.location=(0.111, -0.776, 0.389)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.300)
                insert_keys(53)
                o.location=(0.188, -0.880, 0.386)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.350)
                insert_keys(60)
                o.location=(0.360, -1.059, 0.596)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.450)
                insert_keys(73)
                o.location=(0.473, -1.185, 0.582)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.480)
                insert_keys(80)
                o.location=(0.643, -1.377, 0.796)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.600)
                insert_keys(93)
                o.location=(0.760, -1.432, 0.779)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.650)
                insert_keys(100)
                o.location=(0.980, -1.485, 0.990)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.800)
                insert_keys(113)
                o.location=(1.134, -1.532, 0.968)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 0.900)
                insert_keys(120)
                o.location=(1.387, -1.628, 1.197)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 1.100)
                insert_keys(133)
                o.location=(1.516, -1.605, 1.190)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 1.250)
                insert_keys(140)
                o.location=(1.750, -1.490, 1.385)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 1.520)
                insert_keys(153)
                o.location=(1.901, -1.437, 1.379)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 1.600)
                insert_keys(160)
                o.location=(2.171, -1.402, 1.584)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 2.200)
                insert_keys(173)
                o.location=(2.265, -1.303, 1.574)
                o.rotation_quaternion=(1.056, 0.030, 0.000, 2.500)
                insert_keys(180)
                o.location=(2.362, -1.118, 1.793)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 3.000)
                insert_keys(193)
                o.location=(2.457, -1.014, 1.776)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 3.600)
                insert_keys(200)
                o.location=(2.668, -0.841, 1.996)
                o.rotation_quaternion=(1.129, 0.030, 0.000, 9.986)
                insert_keys(213)
                o.location=(2.669, -0.787, 1.989)
                o.rotation_quaternion=(1.000, 0.030, 0.000, 18.000)
                insert_keys(220)


            for o in Foot_R:
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(20)
                o.location=(-0.013, -0.095, 0.187)
                o.rotation_quaternion=(0.925, 0.377, 0.036, 0.047)
                insert_keys(26)
                o.location=(0.054, -0.469, 0.515)
                o.rotation_quaternion=(0.961, 0.318, 0.048, 0.118)
                insert_keys(34)
                o.location=(0.165, -0.807, 0.400)
                o.rotation_quaternion=(0.987, 0.000, 0.000, 0.160)
                insert_keys(40)
                o.location=(0.165, -0.807, 0.400)
                o.rotation_quaternion=(0.987, 0.000, 0.000, 0.160)
                insert_keys(60)
                o.location=(0.208, -0.949, 0.626)
                o.rotation_quaternion=(0.878, 0.360, 0.175, 0.235)
                insert_keys(66)
                o.location=(0.488, -1.254, 0.905)
                o.rotation_quaternion=(0.859, 0.281, 0.181, 0.336)
                insert_keys(74)
                o.location=(0.705, -1.429, 0.800)
                o.rotation_quaternion=(0.899, 0.000, 0.000, 0.438)
                insert_keys(80)
                o.location=(0.705, -1.429, 0.800)
                o.rotation_quaternion=(0.899, 0.000, 0.000, 0.438)
                insert_keys(100)
                o.location=(0.841, -1.519, 1.053)
                o.rotation_quaternion=(0.749, 0.359, 0.287, 0.466)
                insert_keys(106)
                o.location=(1.177, -1.637, 1.364)
                o.rotation_quaternion=(0.721, 0.195, 0.208, 0.573)
                insert_keys(114)
                o.location=(1.484, -1.684, 1.200)
                o.rotation_quaternion=(0.751, 0.000, 0.000, 0.661)
                insert_keys(120)
                o.location=(1.484, -1.684, 1.200)
                o.rotation_quaternion=(0.751, 0.000, 0.000, 0.661)
                insert_keys(140)
                o.location=(1.637, -1.695, 1.431)
                o.rotation_quaternion=(0.603, 0.223, 0.350, 0.670)
                insert_keys(146)
                o.location=(2.005, -1.561, 1.753)
                o.rotation_quaternion=(0.504, 0.180, 0.320, 0.707)
                insert_keys(154)
                o.location=(2.292, -1.457, 1.600)
                o.rotation_quaternion=(0.530, 0.000, 0.000, 0.848)
                insert_keys(160)
                o.location=(2.292, -1.457, 1.600)
                o.rotation_quaternion=(0.530, 0.000, 0.000, 0.848)
                insert_keys(180)
                o.location=(2.447, -1.338, 1.846)
                o.rotation_quaternion=(0.370, 0.129, 0.399, 0.815)
                insert_keys(186)
                o.location=(2.650, -1.057, 2.141)
                o.rotation_quaternion=(0.309, 0.051, 0.289, 0.852)
                insert_keys(194)
                o.location=(2.812, -0.810, 2.000)
                o.rotation_quaternion=(0.256, 0.000, 0.000, 0.967)
                insert_keys(200)
                o.location=(2.812, -0.810, 2.000)
                o.rotation_quaternion=(0.256, 0.000, 0.000, 0.967)
                insert_keys(220)


            for o in Foot_L:
                o.location=(0.000, 0.000, 0.000)
                o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
                insert_keys(1)
                o.location=(-0.006, -0.143, 0.306)
                o.rotation_quaternion=(0.984, 0.252, -0.014, 0.094)
                insert_keys(12)
                o.location=(-0.024, -0.356, 0.200)
                o.rotation_quaternion=(0.994, 0.000, 0.000, 0.111)
                insert_keys(20)
                o.location=(-0.024, -0.356, 0.200)
                o.rotation_quaternion=(0.994, 0.000, 0.000, 0.111)
                insert_keys(40)
                o.location=(0.028, -0.439, 0.421)
                o.rotation_quaternion=(0.925, 0.318, 0.064, 0.156)
                insert_keys(46)
                o.location=(0.139, -0.799, 0.714)
                o.rotation_quaternion=(0.903, 0.237, 0.052, 0.311)
                insert_keys(54)
                o.location=(0.315, -1.023, 0.600)
                o.rotation_quaternion=(0.898, 0.000, 0.000, 0.439)
                insert_keys(60)
                o.location=(0.315, -1.023, 0.600)
                o.rotation_quaternion=(0.898, 0.000, 0.000, 0.439)
                insert_keys(80)
                o.location=(0.386, -1.111, 0.824)
                o.rotation_quaternion=(0.804, 0.366, 0.189, 0.426)
                insert_keys(86)
                o.location=(0.673, -1.300, 1.109)
                o.rotation_quaternion=(0.799, 0.261, 0.116, 0.491)
                insert_keys(94)
                o.location=(0.905, -1.445, 1.000)
                o.rotation_quaternion=(0.737, 0.000, 0.000, 0.676)
                insert_keys(100)
                o.location=(0.905, -1.445, 1.000)
                o.rotation_quaternion=(0.737, 0.000, 0.000, 0.676)
                insert_keys(120)
                o.location=(1.021, -1.484, 1.220)
                o.rotation_quaternion=(0.576, 0.310, 0.306, 0.671)
                insert_keys(126)
                o.location=(1.371, -1.504, 1.524)
                o.rotation_quaternion=(0.531, 0.210, 0.199, 0.714)
                insert_keys(134)
                o.location=(1.632, -1.438, 1.400)
                o.rotation_quaternion=(0.521, 0.000, 0.000, 0.853)
                insert_keys(140)
                o.location=(1.632, -1.438, 1.400)
                o.rotation_quaternion=(0.521, 0.000, 0.000, 0.853)
                insert_keys(160)
                o.location=(1.774, -1.406, 1.622)
                o.rotation_quaternion=(0.397, 0.212, 0.365, 0.808)
                insert_keys(166)
                o.location=(2.072, -1.254, 1.932)
                o.rotation_quaternion=(0.310, 0.162, 0.267, 0.852)
                insert_keys(174)
                o.location=(2.267, -1.093, 1.800)
                o.rotation_quaternion=(0.248, 0.000, 0.000, 0.969)
                insert_keys(180)
                o.location=(2.267, -1.093, 1.800)
                o.rotation_quaternion=(0.248, 0.000, 0.000, 0.969)
                insert_keys(200)
                o.location=(2.338, -0.998, 2.038)
                o.rotation_quaternion=(0.127, 0.101, 0.380, 0.902)
                insert_keys(206)
                o.location=(2.489, -0.728, 2.295)
                o.rotation_quaternion=(0.006, 0.062, 0.303, 0.918)
                insert_keys(214)
                o.location=(2.497, -0.389, 2.200)
                o.rotation_quaternion=(-0.047, 0.000, 0.000, 0.999)
                insert_keys(220)





            # Action Name
            ob = bpy.context.object
            ob.animation_data.action.name = ob.name +'_Up_Stairs_Spiral' 

                
                 

#-------------------End Spiral Up----------------
#------------------------------------------------
#------------------------------------------------


        if not spiral_stairs_opt and not up_stairs_opt:
            stairs_straight()    
           
        if not spiral_stairs_opt and up_stairs_opt:
            stairs_straight_up()    
           
  
 
           
        if spiral_stairs_opt and not up_stairs_opt:  
            stairs_spiral_down()

        if spiral_stairs_opt and up_stairs_opt:  
            stairs_spiral_up()



        return {'FINISHED'}



#------------------ End Stairs Walk --------------------------
#=============================================================
#=============================================================
#=============================================================




#--------------------- Feet / Heel Adjuster ------------------


 
class OBJECT_OT_foot_adjust_stairs_animbox_ra(bpy.types.Operator):
    '''Adjust Feet Z Location / X Rotation 
- Adjust Heels X Rotation
- depending on the selected option'''

    bl_idname = "object.foot_adjust_stairs_animbox_ra"
    bl_label = "Adjust Feet/Heels"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' )
                
             

    def execute(self, context):
        
        scene = bpy.context.scene
  
        # Ref
        foot_loc = scene.animbox_ra_props.stairs_foot_loc_bool
        foot_rot = scene.animbox_ra_props.stairs_foot_rot_bool

        amount = scene.animbox_ra_props.stairs_adjuster_transform_amount
  
        ob = bpy.context.object
        pose_bones = bpy.context.object.pose.bones
        anim_data = ob.animation_data
        action = anim_data.action



        def adjust_foot_down_stairs():

            if not foot_loc and not foot_rot:
                self.report({'INFO'}, 'Please Select any "Adjust" option') 

    
           
            foot_r_frames = (36, 77, 117, 157, 197)
            foot_l_frames = (57, 97, 137, 177, 217)
            
            num = amount

            for b in pose_bones:
                if b.name.startswith('foot_ik.R'):
             
                    if foot_loc:
                        for i in (foot_r_frames):
                            scene.frame_set(i)
                            b.location.z += num
                            b.keyframe_insert(data_path="location", index=-1)  

                            scene.frame_set(36)

                    if foot_rot:
                        for i in (foot_r_frames):
                            scene.frame_set(i)                    
                            b.rotation_quaternion.x += num
                            b.keyframe_insert(data_path="rotation_quaternion", index=1)        

                            scene.frame_set(36)


                if b.name.startswith('foot_ik.L'):
             
                    if foot_loc:
                        for i in (foot_l_frames):
                            scene.frame_set(i)
                            b.location.z += num
                            b.keyframe_insert(data_path="location", index=-1)        

                    if foot_rot:
                        for i in (foot_l_frames):
                            scene.frame_set(i)                    
                            b.rotation_quaternion.x += num
                            b.keyframe_insert(data_path="rotation_quaternion", index=1)        

 
 

#-------------------------- Heels Stairs Up ----------------
        def adjust_heels_up_stairs():
            
            set_frames = (1, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220)
            
            adjust_frame_heel_right = (20, 60, 100, 140, 180, 220)
            
            adjust_frame_heel_left = (40, 80, 120, 160, 200)
            
            
            num = amount
            
            
            for b in pose_bones:
                if b.name.startswith('foot_heel_ik.R'):            

                    for i in (set_frames):
                        scene.frame_set(i)
                        b.keyframe_insert(data_path="rotation_euler", index=0)        
                    
                    for r in (adjust_frame_heel_right):
                        scene.frame_set(r)
                        b.rotation_euler.x += num
                        b.keyframe_insert(data_path="rotation_euler", index=0)        
                        


                if b.name.startswith('foot_heel_ik.L'): 

                    for i in (set_frames):
                        scene.frame_set(i)
                        b.keyframe_insert(data_path="rotation_euler", index=0)        


                    for l in (adjust_frame_heel_left):
                        scene.frame_set(l)
                        b.rotation_euler.x += num
                        b.keyframe_insert(data_path="rotation_euler", index=0)        
                        



#---------------------------- Adjust -----------------------


        if anim_data:
            if anim_data.action:
                if '_Down_Stairs' in action.name and not '_Spiral' in action.name:
                    
                    adjust_foot_down_stairs()




                if '_Up_Stairs' in action.name and not '_Spiral' in action.name:
                    
                    adjust_heels_up_stairs()
                    scene.frame_set(40)


                 

        return {'FINISHED'}


#------------------ End Feet / Heels Adjuster ----------------
#=============================================================
#=============================================================
#=============================================================




#--------------------- Arm Adjuster --------------------------

 
class OBJECT_OT_arm_adjust_stairs_animbox_ra(bpy.types.Operator):
    '''Adjust Arms X / Y Rotation 
- depending on the selected option'''
    bl_idname = "object.arm_adjust_stairs_animbox_ra"
    bl_label = "Adjust Arms"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' )

    def execute(self, context):
        scene = bpy.context.scene
        
 
        # Ref
        arm_rot_x = scene.animbox_ra_props.stairs_arms_rot_x_bool
        arm_rot_y = scene.animbox_ra_props.stairs_arms_rot_y_bool
        amount_arms = scene.animbox_ra_props.stairs_adjuster_transform_amount_arms
                

        if not arm_rot_x and not arm_rot_y:
            self.report({'INFO'}, 'Please Select "X" or "Y"') 

    
        pose_bones = bpy.context.object.pose.bones
         
        num = amount_arms
         
        # Arm Frames
        arm_frames = (1, 20, 40, 60, 80, 100,
                      120, 140, 160, 180, 200, 220) 
         
         
        # Right Arm Frames
        arm_frames_for_r = (20, 60, 100, 140, 180, 220) 
        arm_frames_back_r = ( 40, 80, 120, 160, 200) 
           
         
        # Left Arm Frames
        arm_frames_for_l = ( 40, 80, 120, 160, 200) 
        arm_frames_back_l = (20, 60, 100, 140, 180, 220) 

     
#--------------------- Left Arm ------------------------
                
           
        for b in pose_bones:
            if b.name.startswith('upper_arm_fk.L'):
                

                if arm_rot_y and not arm_rot_x:
                    for i in (arm_frames):
                        scene.frame_set(i)
                    
                        b.rotation_mode = 'XYZ'
                        b.rotation_euler[2] += num
                 
                        b.rotation_mode = 'QUATERNION'
                        b.keyframe_insert(data_path = 'rotation_quaternion')

                        scene.frame_set(40)                        
                
                
                if arm_rot_x and not arm_rot_y:
                    for i in (arm_frames_for_l):
                        scene.frame_set(i)
                        
                        b.rotation_mode = 'XYZ'
                        b.rotation_euler[0] += num
                 
                        b.rotation_mode = 'QUATERNION'
                        b.keyframe_insert(data_path = 'rotation_quaternion')
 
 
                    for i in (arm_frames_back_l):
                        scene.frame_set(i)
                        
                        b.rotation_mode = 'XYZ'
                        b.rotation_euler[0] -= num
                 
                        b.rotation_mode = 'QUATERNION'
                        b.keyframe_insert(data_path = 'rotation_quaternion')

 

#--------------------- Right Arm ------------------------
              
            if b.name.startswith('upper_arm_fk.R'):
                
                
                if arm_rot_y and not arm_rot_x:
                    for i in (arm_frames):
                        scene.frame_set(i)
                    
                        b.rotation_mode = 'XYZ'
                        b.rotation_euler[2] -= num
                 
                        b.rotation_mode = 'QUATERNION'
                        b.keyframe_insert(data_path = 'rotation_quaternion')
                
                        scene.frame_set(40)            
                
                if arm_rot_x and not arm_rot_y:
                    for i in (arm_frames_for_r):
                        scene.frame_set(i)
                    
                        b.rotation_mode = 'XYZ'
                        b.rotation_euler[0] += num
                 
                        b.rotation_mode = 'QUATERNION'
                        b.keyframe_insert(data_path = 'rotation_quaternion')

             
                    for i in (arm_frames_back_r):
                        scene.frame_set(i)
                
                        b.rotation_mode = 'XYZ'
                        b.rotation_euler[0] -= num
                 
                        b.rotation_mode = 'QUATERNION'
                        b.keyframe_insert(data_path = 'rotation_quaternion')

                        scene.frame_set(40)



        return {'FINISHED'}


#-------------------------------------------------------------
#--------------------- End Arm Adjuster ----------------------
#-------------------------------------------------------------




#---------------------- Stairs Panel-------------------------


class PANEL_PT_stairs_panel_animbox_ra(bpy.types.Panel):
    bl_label = "Stairs"
    bl_idname = 'PANEL_PT_stairs_panel_animbox_ra'
    bl_parent_id = 'PANEL_ANIM_BOX_PT_rigify_anim_box_00_1'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        ra_props = scene.animbox_ra_props 

   
        box = layout.box()  
        row = box.row(align=True)

        row.label(text="", icon='OPTIONS')
        row.scale_x = 2
        row.prop(ra_props, "up_stairs", icon='SORT_DESC')
        row.prop(ra_props, "spiral_stairs", icon='MOD_SCREW')
        row.prop(ra_props, "exclude_arms_from_anim", icon='CANCEL')


        row = box.row(align=True)
        row.operator("object.add_walk_stairs_geo_animbox_ra")
        row.operator("object.stairs_walk_animbox_ra",text='Walk')
 




#---------------------- End Stairs Panel-------------------------





#---------------------- Arm Adjuster Panel ---------------------


class PANEL_PT_stairs_panel_adjust_arms_ra(bpy.types.Panel):
    bl_label = "Adjust Arms"
    bl_idname = 'PANEL_PT_stairs_panel_adjust_arms_ra'
    bl_parent_id = 'PANEL_PT_stairs_panel_animbox_ra'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Stairs"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):    
        ob = bpy.context.object
        
        if ob is not None:
            if ob.animation_data:
                if ob.animation_data.action:
                    action = ob.animation_data.action
                    if '_Stairs' in action.name:
                          
                        return (action)        
                    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        ra_props = scene.animbox_ra_props 

    
        box = layout.box() 
        row = box.row(align=True)

        row.prop(ra_props, "stairs_arms_rot_x_bool", text='X', icon='CHECKMARK')  
        row.prop(ra_props, "stairs_arms_rot_y_bool", text='Y', icon='CHECKMARK') 
        row.scale_x = 2
        row.prop(ra_props, "stairs_adjuster_transform_amount_arms")  
 
        row = box.row()
        
        row.scale_y = 1.2
        row.operator("object.arm_adjust_stairs_animbox_ra", text='Adjust Arms')

   

#---------------------- End Arm Adjuster Panel ----------------------








#---------------------- Feet Adjuster Panel ---------------------


class PANEL_PT_stairs_panel_adjust_feet_ra(bpy.types.Panel):
    bl_label = "Down Stairs - Adjust Feet"
    bl_idname = 'PANEL_PT_stairs_panel_adjust_feet_ra'
    bl_parent_id = 'PANEL_PT_stairs_panel_animbox_ra'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Stairs"
    bl_options = {'DEFAULT_CLOSED', 'HIDE_HEADER'}

    @classmethod
    def poll(cls, context):    
        ob = bpy.context.object
        
        if ob is not None:
            if ob.animation_data:
                if ob.animation_data.action:
                    action = ob.animation_data.action
                    if '_Down_Stairs' in action.name and not '_Spiral' in action.name:
                          
                        return (action)        
                    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        ra_props = scene.animbox_ra_props 

    
        box = layout.box() 
        row = box.row(align=True)

        row.prop(ra_props, "stairs_foot_loc_bool", icon='CON_LOCLIKE')  
        row.prop(ra_props, "stairs_foot_rot_bool", icon='CON_ROTLIKE') 
        row.scale_x = 2
        row.prop(ra_props, "stairs_adjuster_transform_amount")  
 
        row = box.row()
        
        row.scale_y = 1.2
        row.operator("object.foot_adjust_stairs_animbox_ra", text='Adjust Feet')

  


#---------------------- End Feet Adjuster Panel ----------------------







#---------------------- Heel Adjuster Panel ---------------------


class PANEL_PT_stairs_panel_adjust_heels_ra(bpy.types.Panel):
    bl_label = "Up Stairs - Adjust Heels"
    bl_idname = 'PANEL_PT_stairs_panel_adjust_heels_ra'
    bl_parent_id = 'PANEL_PT_stairs_panel_animbox_ra'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Stairs"
    bl_options = {'DEFAULT_CLOSED', 'HIDE_HEADER'}

    @classmethod
    def poll(cls, context):    
        ob = bpy.context.object
        
        if ob is not None:
            if ob.animation_data:
                if ob.animation_data.action:
                    action = ob.animation_data.action
                    if '_Up_Stairs' in action.name and not '_Spiral' in action.name:

                        return (action)        
                    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        ra_props = scene.animbox_ra_props 

    
        box = layout.box() 
        row = box.row(align=True)
 
        row.scale_y = 1.2
        row.operator("object.foot_adjust_stairs_animbox_ra", text='Adjust Heels')
        row.scale_x = 0.7
        row.prop(ra_props, "stairs_adjuster_transform_amount")  

            

#---------------------- End Heels Adjuster Panel ----------------------










classes = [ 

            OBJECT_OT_add_walk_stairs_geo_animbox_ra,
            OBJECT_OT_stairs_walk_animbox_ra,
            OBJECT_OT_foot_adjust_stairs_animbox_ra,
            OBJECT_OT_arm_adjust_stairs_animbox_ra,

            PANEL_PT_stairs_panel_animbox_ra,
            PANEL_PT_stairs_panel_adjust_arms_ra,
            PANEL_PT_stairs_panel_adjust_feet_ra,
            PANEL_PT_stairs_panel_adjust_heels_ra,            
            
          ]
 
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        

 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

 
 
 
 
 
 
if __name__ == "__main__":
    register()  
