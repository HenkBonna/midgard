import bpy
import fnmatch



# RIGIFY AUTOMATION TOOLS


# =====================================================
#                     RIGIFY MAGIC WALK
# =====================================================

# Navigation:

# 24 FRAMES  WALK CYCLE - Line 1460

# 32 FRAMES  WALK CYCLE - Line 2860

# =====================================================
#          MULTIPLE LIMBS - 18 FRAMES  WALK CYCLE
# =====================================================


# 18 FRAMES WALK CYCLE FOR RIGIFY HUMAN WITH MULTIPLE LIMBS. 
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_magic_walk_multiple_limbs_18_ra(bpy.types.Operator):
    '''18 Frames Walk Cycle For Rigify Human With Multiple Limbs.
Original Bone Names Should Remain Unchanged !!!
'''
    bl_idname = "object.rigify_magic_walk_multiple_limbs_18_ra"
    bl_label = "18"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)
                

    def execute(self, context):

        scene = context.scene
      
        # Ref
        exclude_arms = scene.animbox_ra_props.exclude_arms_from_anim

 

        # TOTAL RESET

        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        #bpy.ops.pose.transforms_clear()
        bpy.ops.anim.keyframe_clear_v3d() 
        bpy.ops.pose.select_all(action = 'DESELECT')
        bpy.ops.screen.frame_jump(end=False)
            


         
        bones = bpy.context.object.data.bones
        pose_bones = bpy.context.object.pose.bones

           
         
        # DEFINING FRAME RANGE

        # START
        bpy.context.scene.frame_start = 1

        # END
        bpy.context.scene.frame_end = 18
         


        # NAMES DEFINITION


        # Find matching Chest Name                
        Chest = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "chest*")]
         

        # Find matching Torso Name
        Torso = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "torso*")]


        # Find matching Arm_Parent Name
        Arm_Parent_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_parent.R*")]
        Arm_Parent_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_parent.L*")]


        # Find matching Arm Name
        Arm_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_fk.R*")]
        Arm_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_fk.L*")]
         


        # Find matching Feets Name
        Foot_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_ik.R*")]
        Foot_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_ik.L*")]     
         

        # Find matching Heels Name
        Heel_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_heel_ik.R*")]
        Heel_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_heel_ik.L*")]     
                 


# =====================================================
#      DEFAULT SIZE   - 18 Frames Cycle
# =====================================================

         
        def walk_cycle_18_size_default():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                         
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                      
 


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.07)
                insert_keys(1)
                o.location=(0.02, 0.00, -0.01)
                insert_keys(5)
                o.location=(-0.00, 0.00, -0.07)
                insert_keys(10)
                o.location=(-0.02, 0.00, -0.01)
                insert_keys(14)
                o.location=(0.00, 0.00, -0.07)
                insert_keys(19)


            for o in Foot_R:
                o.location=(0.00, 0.46, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, 0.04, 0.08)
                o.rotation_quaternion=(1.01, 0.10, -0.00, 0.00)
                insert_keys(5)
                o.location=(0.00, -0.40, 0.00)
                o.rotation_quaternion=(0.98, -0.20, -0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, -0.25, 0.00)
                o.rotation_quaternion=(0.99, 0.00, -0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(14)
                o.location=(0.00, 0.46, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.40, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.25, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(5)
                o.location=(0.00, 0.46, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, 0.04, 0.08)
                o.rotation_quaternion=(1.00, 0.10, 0.00, -0.00)
                insert_keys(14)
                o.location=(0.00, -0.40, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(19)


            for o in Heel_R:
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(12)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(19)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(3)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)

                            
           #walk_cycle_18_size_default() 
                        

# =====================================================
#   END   DEFAULT SIZE   - 18 Frames Cycle
# =====================================================
               





# =====================================================
#      SIZE  << 0.1 - 0.3 >>  18 Frames Cycle
# =====================================================

 
        def walk_cycle_18_size_01_03():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            
            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(19)

            
            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.02, 0.00, -0.02)
                insert_keys(5)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(-0.02, 0.00, -0.02)
                insert_keys(14)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(-0.00, 0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.00, 0.06)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, -0.08, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(14)
                o.location=(-0.00, 0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.08, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, 0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, 0.00, 0.06)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(14)
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.30, 0.00, 0.10)
                    insert_keys(1)
                    o.rotation_quaternion=(0.97, -0.19, -0.00, 0.15)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.30, 0.00, 0.10)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:     
                    o.rotation_quaternion=(1.00, -0.20, 0.00, -0.15)
                    insert_keys(1)
                    o.rotation_quaternion=(0.95, 0.29, -0.00, -0.10)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.20, 0.00, -0.15)
                    insert_keys(19)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(19)
            
                
            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                         
            #walk_cycle_18_size_01_03() 
               
         
# =====================================================
#   END  SIZE  << 0.1 - 0.3 >>  18 Frames Cycle
# =====================================================
 
  
 


# =====================================================
#      SIZE  << 0.3 - 0.5 >>  18 Frames Cycle
# =====================================================

 
        def walk_cycle_18_size_03_05():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(19)


            for o in Torso:
                o.location=(0.000, 0.000, -0.040)
                insert_keys(1)
                o.location=(0.020, 0.000, -0.000)
                insert_keys(5)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(10)
                o.location=(-0.020, 0.000, -0.000)
                insert_keys(14)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(19)


            for o in Foot_R:
                o.location=(-0.00, 0.21, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, 0.01, 0.08)
                o.rotation_quaternion=(0.99, 0.21, -0.00, 0.00)
                insert_keys(5)
                o.location=(-0.00, -0.24, 0.00)
                o.rotation_quaternion=(0.98, -0.20, -0.00, 0.00)
                insert_keys(10)
                o.location=(-0.00, -0.17, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(12)
                o.location=(-0.00, 0.00, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(14)
                o.location=(-0.00, 0.21, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(-0.00, -0.24, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.17, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.00, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, 0.21, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, 0.01, 0.08)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(14)
                o.location=(-0.00, -0.24, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(19)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(12)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(19)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(3)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)



        # walk_cycle_18_size_03_05()

# =====================================================
#   END  SIZE  << 0.3 - 0.5 >>  18 Frames Cycle
# =====================================================




# =====================================================
#      SIZE  << 0.5 - 0.6 >>  18 Frames Cycle
# =====================================================

 
        def walk_cycle_18_size_05_06():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.02, 0.00, 0.00)
                insert_keys(5)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(-0.02, 0.00, 0.00)
                insert_keys(14)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(-0.00, 0.32, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, -0.27, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(14)
                o.location=(-0.00, 0.32, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.27, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, 0.32, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(14)
                o.location=(0.00, -0.27, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(19)


            for o in Heel_R:
                o.rotation_euler=(0.40, 0.00, 0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, 0.00, 0.00)
                insert_keys(5)
                o.rotation_euler=(0.00, 0.00, 0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, 0.00, 0.00)
                insert_keys(12)
                o.rotation_euler=(0.00, 0.00, 0.00)
                insert_keys(14)
                o.rotation_euler=(0.40, 0.00, 0.00)
                insert_keys(19)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(3)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)

        # walk_cycle_18_size_05_06()

# =====================================================
#   END  SIZE  << 0.5 - 0.6 >>  18 Frames Cycle
# =====================================================




# =====================================================
#      SIZE  << 0.6 - 0.7 >>  18 Frames Cycle
# =====================================================

 
        def walk_cycle_18_size_06_07():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.02, 0.00, -0.01)
                insert_keys(5)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(-0.02, 0.00, -0.01)
                insert_keys(14)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(0.00, 0.28, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(5)
                o.location=(0.00, -0.29, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, -0.13, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(12)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(14)
                o.location=(0.00, 0.28, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.29, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(5)
                o.location=(0.00, 0.28, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(14)
                o.location=(0.00, -0.29, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(19)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(12)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(19)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(3)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)


        # walk_cycle_18_size_06_07()

# =====================================================
#   END   SIZE  << 0.6 - 0.7 >>  18 Frames Cycle
# =====================================================


# =====================================================
#      SIZE  << 0.7 - 0.8 >>  18 Frames Cycle
# =====================================================

 
        def walk_cycle_18_size_07_08():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.02, 0.00, 0.00)
                insert_keys(5)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(-0.02, 0.00, 0.00)
                insert_keys(14)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(5)
                o.location=(0.00, -0.28, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, -0.13, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(12)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(14)
                o.location=(0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.28, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(5)
                o.location=(0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(14)
                o.location=(0.00, -0.28, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(19)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(12)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(19)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(3)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)

        # walk_cycle_18_size_07_08()

# =====================================================
#   END   SIZE  << 0.7 - 0.8 >>  18 Frames Cycle
# =====================================================






# =====================================================
#  SIZE  << 0.8 - 0.84 >>  18 Frames Cycle
# =====================================================
 
          
        def walk_cycle_18_size_08_084(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                   

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.07)
                insert_keys(1)
                o.location=(0.02, 0.00, -0.01)
                insert_keys(5)
                o.location=(-0.00, 0.00, -0.07)
                insert_keys(10)
                o.location=(-0.02, 0.00, -0.01)
                insert_keys(14)
                o.location=(0.00, 0.00, -0.07)
                insert_keys(19)


            for o in Foot_R:
                o.location=(0.00, 0.43, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(5)
                o.location=(0.00, -0.35, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, -0.25, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(12)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(14)
                o.location=(0.00, 0.43, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.35, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.25, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(5)
                o.location=(0.00, 0.43, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(14)
                o.location=(0.00, -0.35, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(19)


            for o in Heel_R:
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(12)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(19)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(3)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)

        # walk_cycle_18_size_08_084()

# =====================================================
#  END SIZE  << 0.8 - 0.84 >>  18 Frames Cycle
# =====================================================
 



        

# =====================================================
#  SIZE  << 0.84 - 0.9 >>  18 Frames Cycle
# =====================================================
 
          
        def walk_cycle_18_size_084_09(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.07)
                insert_keys(1)
                o.location=(0.02, 0.00, -0.02)
                insert_keys(5)
                o.location=(-0.00, 0.00, -0.07)
                insert_keys(10)
                o.location=(-0.02, 0.00, -0.02)
                insert_keys(14)
                o.location=(0.00, 0.00, -0.07)
                insert_keys(19)


            for o in Foot_R:
                o.location=(0.00, 0.38, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.05, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(5)
                o.location=(0.00, -0.46, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, -0.25, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(12)
                o.location=(0.00, -0.05, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(14)
                o.location=(0.00, 0.38, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(-0.00, -0.46, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.25, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, -0.05, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, 0.38, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, -0.05, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(14)
                o.location=(-0.00, -0.46, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(19)


            for o in Heel_R:
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(12)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(19)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(3)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(5)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(10)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(14)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)


                        
             #walk_cycle_18_size_084_09()
               

# =====================================================
#    END SIZE  << 0.84 - 0.9 >>  18 Frames Cycle
# =====================================================
 

                           

 

 
# ========================================================================
#  MEASURING LEG LENGTH - a way of specifying the leg movement Amplitude
# ========================================================================
 
                   
        bones = bpy.context.object.data.bones
        pose_bones = bpy.context.object.pose.bones

        # Measuring Leg Length ( Left )
        def get_left_Leg_length(bonename_1, bonename_2, bonename_3, bonename_4):
               
            for  bone in pose_bones:
                if bone.name == bonename_1:
                    bonelength_1 = bone.length
                    
                if bone.name == bonename_2:
                    bonelength_2 = bone.length
             
                if bone.name == bonename_3:
                    bonelength_3 = bone.length    

                if bone.name == bonename_4:
                    bonelength_4 = bone.length    
             

            masterlength = bonelength_1 + bonelength_2 + bonelength_3 + bonelength_4        
                    
            # Size Default
            if masterlength > 0.9 and masterlength < 1:
                walk_cycle_18_size_default()    
                print("Length is","%.2f" % masterlength)


            # Size 0.1 to 0.3
            if masterlength > 0.1 and masterlength < 0.3:
                walk_cycle_18_size_01_03() 
                print("Length is","%.2f" % masterlength)
            


            # Size 0.3 to 0.5
            if masterlength > 0.3 and masterlength < 0.5:
                walk_cycle_18_size_03_05() 
                print("Length is","%.2f" % masterlength)
            


            # Size 0.5 to 0.6
            if masterlength > 0.5 and masterlength < 0.6:
                walk_cycle_18_size_05_06() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.6 to 0.7
            if masterlength > 0.6 and masterlength < 0.7:
                walk_cycle_18_size_06_07() 
                print("Length is","%.2f" % masterlength)
            


            # Size 0.7 to 0.8
            if masterlength > 0.7 and masterlength < 0.8:
                walk_cycle_18_size_07_08() 
                print("Length is","%.2f" % masterlength)
            


            # Size 0.8 to 0.84
            if masterlength > 0.8 and masterlength < 0.84:
                walk_cycle_18_size_08_084()    
                print("Length is","%.2f" % masterlength)



            # Size 0.84 to 0.9
            if masterlength > 0.84 and masterlength < 0.9:
                walk_cycle_18_size_084_09()   
                print("Length is","%.2f" % masterlength)



            # Size Bigger then "Default"
            if masterlength > 1:
                walk_cycle_18_size_default()   
                print("Length is","%.2f" % masterlength)
      

        get_left_Leg_length('DEF-shin.L','DEF-shin.L.001','DEF-thigh.L','DEF-thigh.L.001')
      
 
# ===========================================================================
#  END MEASURING LEG LENGTH - a way of specifying the leg movement Amplitude
# ===========================================================================
 

        # Add Cycles Modifier

        ob = bpy.context.object
        ob_fcurve = ob.animation_data.action.fcurves


        def add_cycle_modifier():
            
               
            for fc in ob_fcurve:
                d_path = ('location', 'rotation_quaternion', 'rotation_euler', 'scale',)
                     
                if fc.data_path.endswith((d_path)):
                    fc.modifiers.new(type='CYCLES')
                
                fc.update()


        add_cycle_modifier()
         

        # Action Name
        ob = bpy.context.object
        ob.animation_data.action.name = ob.name + '_Walk_18' 

    
        # JUMP TO START AND PLAY ANIMATION
        bpy.ops.screen.frame_jump(end=False)
        bpy.ops.screen.animation_play()



        # FRAME SELECTED RANGE IN TIMELINE

        for area in bpy.context.screen.areas:
            if area.type == 'DOPESHEET_EDITOR':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        ctx = bpy.context.copy()
                        ctx['area'] = area
                        ctx['region'] = region
                        bpy.ops.action.view_all(ctx)
                        break
                break
        # Frame selected range in GRAPH_EDITOR 
        for area in bpy.context.screen.areas:
            if area.type == 'GRAPH_EDITOR':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        ctx = bpy.context.copy()
                        ctx['area'] = area
                        ctx['region'] = region
                        bpy.ops.graph.view_all(ctx)
                        break
                break
      

        return {'FINISHED'}


  
# =====================================================
#    END   MULTIPLE LIMBS - 18 FRAMES  WALK CYCLE
# =====================================================
  
  
  


#======================================================
#======================================================
#======================================================




# =====================================================
#          MULTIPLE LIMBS - 24 FRAMES  WALK CYCLE
# =====================================================


# 24 FRAMES WALK CYCLE FOR RIGIFY HUMAN WITH MULTIPLE LIMBS. 
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_magic_walk_multiple_limbs_24_ra(bpy.types.Operator):
    '''24 FRAMES Walk Cycle For Rigify Human With Multiple Limbs.
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_magic_walk_multiple_limbs_24_ra"
    bl_label = "24"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)
                

    def execute(self, context):

        scene = context.scene
      
        # Ref
        exclude_arms = scene.animbox_ra_props.exclude_arms_from_anim



        # TOTAL RESET

        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        #bpy.ops.pose.transforms_clear()
        bpy.ops.anim.keyframe_clear_v3d() 
        bpy.ops.pose.select_all(action = 'DESELECT')
        bpy.ops.screen.frame_jump(end=False)
            


         
        bones = bpy.context.object.data.bones
        pose_bones = bpy.context.object.pose.bones

           
         
        # DEFINING FRAME RANGE

        # START
        bpy.context.scene.frame_start = 1

        # END
        bpy.context.scene.frame_end = 24
         

        # NAMES DEFINITION


        # Find matching Chest Name                
        Chest = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "chest*")]
         

        # Find matching Torso Name
        Torso = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "torso*")]


        # Find matching Arm_Parent Name
        Arm_Parent_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_parent.R*")]
        Arm_Parent_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_parent.L*")]


        # Find matching Arm Name
        Arm_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_fk.R*")]
        Arm_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_fk.L*")]
         


        # Find matching Feets Name
        Foot_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_ik.R*")]
        Foot_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_ik.L*")]     
         

        # Find matching Heels Name
        Heel_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_heel_ik.R*")]
        Heel_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_heel_ik.L*")]     
                 


# =====================================================
#      DEFAULT SIZE   - 24 FRAMES Cycle
# =====================================================
    
        def walk_cycle_24_size_default():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                         
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
 

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(13)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(25)



            for o in Torso:
                o.location=(0.00, 0.00, -0.08)
                insert_keys(1)
                o.location=(0.01, 0.00, -0.01)
                insert_keys(7)
                o.location=(0.00, 0.00, -0.08)
                insert_keys(13)
                o.location=(-0.01, 0.00, -0.01)
                insert_keys(19)
                o.location=(0.00, 0.00, -0.08)
                insert_keys(25)



            for o in Foot_R:
                o.location=(0.00, 0.47, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(7)
                o.location=(0.00, -0.40, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(13)
                o.location=(0.00, -0.33, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(15)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, 0.47, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)


            for o in Foot_L:
                o.location=(-0.00, -0.40, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.33, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(7)
                o.location=(-0.00, 0.47, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, -0.40, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(25)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(25)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(25)


            for o in Heel_R:
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(25)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(13)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)


                            
           #walk_cycle_24_size_default()                    

# =====================================================
#   END   DEFAULT SIZE   - 24 FRAMES Cycle
# =====================================================
               



# =====================================================
#      SIZE  << 0.1 - 0.3 >>  24 FRAMES Cycle
# =====================================================

 
        def walk_cycle_24_size_01_03():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            
            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(13)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(25)

            
            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.02, 0.00, -0.02)
                insert_keys(7)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(13)
                o.location=(-0.02, 0.00, -0.02)
                insert_keys(19)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(25)


            for o in Foot_R:
                o.location=(-0.00, 0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.00, 0.06)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(7)
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, -0.11, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(15)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, 0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)


            for o in Foot_L:
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.11, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(7)
                o.location=(-0.00, 0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, 0.00, 0.06)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(25)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.30, 0.00, 0.10)
                    insert_keys(1)
                    o.rotation_quaternion=(0.97, -0.19, -0.00, 0.15)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, 0.30, 0.00, 0.10)
                    insert_keys(25)


            for o in Arm_L:
                if not exclude_arms:       
                    o.rotation_quaternion=(1.00, -0.20, 0.00, -0.15)
                    insert_keys(1)
                    o.rotation_quaternion=(0.95, 0.29, -0.00, -0.10)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, -0.20, 0.00, -0.15)
                    insert_keys(25)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(25)

                
            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(13)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)

                         
            #walk_cycle_24_size_01_03() 
                     
# =====================================================
#   END  SIZE  << 0.1 - 0.3 >>  24 FRAMES Cycle
# =====================================================
 
  
  

# =====================================================
#      SIZE  << 0.3 - 0.5 >>  24 FRAMES Cycle
# =====================================================

 
        def walk_cycle_24_size_03_05():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(13)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(25)


            for o in Torso:
                o.location=(0.000, 0.000, -0.040)
                insert_keys(1)
                o.location=(0.010, 0.000, -0.005)
                insert_keys(7)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(13)
                o.location=(-0.010, 0.000, -0.005)
                insert_keys(19)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(25)


            for o in Foot_R:
                o.location=(0.00, 0.21, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.02, 0.08)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(7)
                o.location=(0.00, -0.24, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(13)
                o.location=(0.00, -0.18, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(15)
                o.location=(0.00, 0.00, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, 0.21, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)


            for o in Foot_L:
                o.location=(0.00, -0.24, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(0.00, 0.00, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(7)
                o.location=(0.00, 0.21, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(13)
                o.location=(0.00, 0.02, 0.08)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, -0.24, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(25)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(25)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(25)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(25)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(13)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)


        # walk_cycle_24_size_03_05()


# =====================================================
#    END  SIZE  << 0.3 - 0.5 >>  24 FRAMES Cycle
# =====================================================

 


# =====================================================
#      SIZE  << 0.5 - 0.6 >>  24 FRAMES Cycle
# =====================================================

 
        def walk_cycle_24_size_05_06():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(13)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(25)


            for o in Torso:
                o.location=(0.000, 0.000, -0.040)
                insert_keys(1)
                o.location=(0.010, 0.000, -0.005)
                insert_keys(7)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(13)
                o.location=(-0.010, 0.000, -0.005)
                insert_keys(19)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(25)


            for o in Foot_R:
                o.location=(0.00, 0.33, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(7)
                o.location=(0.00, -0.24, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(13)
                o.location=(0.00, -0.18, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(15)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, 0.33, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)


            for o in Foot_L:
                o.location=(-0.00, -0.24, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(7)
                o.location=(-0.00, 0.33, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, -0.24, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(25)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(25)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(25)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(25)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(13)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)

        # walk_cycle_24_size_05_06()

# =====================================================
#   END   SIZE  << 0.5 - 0.6 >>  24 FRAMES Cycle
# =====================================================

 


# =====================================================
#      SIZE  << 0.6 - 0.7 >>  24 FRAMES Cycle
# =====================================================

 
        def walk_cycle_24_size_06_07():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(13)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(25)



            for o in Torso:
                o.location=(0.000, 0.000, -0.040)
                insert_keys(1)
                o.location=(0.010, 0.000, -0.005)
                insert_keys(7)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(13)
                o.location=(-0.010, 0.000, -0.005)
                insert_keys(19)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(25)


            for o in Foot_R:
                o.location=(0.00, 0.28, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(7)
                o.location=(0.00, -0.29, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(13)
                o.location=(0.00, -0.18, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(15)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, 0.28, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)


            for o in Foot_L:
                o.location=(-0.00, -0.29, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(7)
                o.location=(-0.00, 0.28, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, -0.29, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(25)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(25)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(25)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(25)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(13)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)


        # walk_cycle_24_size_06_07()
     

# =====================================================
#    END  SIZE  << 0.6 - 0.7 >>  24 FRAMES Cycle
# =====================================================

 

# =====================================================
#  SIZE  << 0.7 - 0.8 >>  24 FRAMES Cycle
# =====================================================
 
     
        def walk_cycle_24_size_07_08(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                        
    

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(13)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(25)


            for o in Torso:
                o.location=(0.000, 0.000, -0.040)
                insert_keys(1)
                o.location=(0.010, 0.000, -0.005)
                insert_keys(7)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(13)
                o.location=(-0.010, 0.000, -0.005)
                insert_keys(19)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(25)


            for o in Foot_R:
                o.location=(0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(7)
                o.location=(0.00, -0.27, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(13)
                o.location=(0.00, -0.18, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(15)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)


            for o in Foot_L:
                o.location=(-0.00, -0.27, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(7)
                o.location=(-0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, -0.27, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(25)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(25)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(25)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(25)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(13)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)

        # walk_cycle_24_size_07_08()

# =====================================================
#  END SIZE  << 0.7 - 0.8 >>  24 FRAMES Cycle
# =====================================================
 
     
         




# =====================================================
#  SIZE  << 0.8 - 0.84 >>  24 FRAMES Cycle
# =====================================================
 
     
        def walk_cycle_24_size_08_084(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                        


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(13)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(25)


            for o in Torso:
                o.location=(0.000, 0.000, -0.070)
                insert_keys(1)
                o.location=(0.010, 0.000, -0.007)
                insert_keys(7)
                o.location=(0.000, 0.000, -0.070)
                insert_keys(13)
                o.location=(-0.010, 0.000, -0.007)
                insert_keys(19)
                o.location=(0.000, 0.000, -0.070)
                insert_keys(25)


            for o in Foot_R:
                o.location=(0.00, 0.41, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(7)
                o.location=(0.00, -0.35, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(13)
                o.location=(0.00, -0.33, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(15)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, 0.41, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)


            for o in Foot_L:
                o.location=(0.00, -0.35, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.33, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(7)
                o.location=(0.00, 0.41, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(13)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, -0.35, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(25)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(25)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(25)


            for o in Heel_R:
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(25)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(13)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)


        # walk_cycle_24_size_08_084()

# =====================================================
#  END SIZE  << 0.8 - 0.84 >>  24 FRAMES Cycle
# =====================================================
 
     
         



          

# =====================================================
#  SIZE  << 0.84 - 0.9 >>  24 FRAMES Cycle
# =====================================================
 
     
        def walk_cycle_24_size_084_09(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                       


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(13)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(25)



            for o in Torso:
                o.location=(0.000, 0.000, -0.070)
                insert_keys(1)
                o.location=(0.010, 0.000, -0.020)
                insert_keys(7)
                o.location=(0.000, 0.000, -0.070)
                insert_keys(13)
                o.location=(-0.010, 0.000, -0.020)
                insert_keys(19)
                o.location=(0.000, 0.000, -0.070)
                insert_keys(25)


            for o in Foot_R:
                o.location=(0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(7)
                o.location=(0.00, -0.43, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(13)
                o.location=(0.00, -0.33, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(15)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)


            for o in Foot_L:
                o.location=(-0.00, -0.43, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.33, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(7)
                o.location=(-0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, -0.43, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(25)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(25)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(13)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(25)


            for o in Heel_R:
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(25)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(7)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(13)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(19)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)



             #walk_cycle_24_size_084_09() 
               

# =====================================================
#    END SIZE  << 0.84 - 0.9 >>  24 FRAMES Cycle
# =====================================================
 
      


 
# ========================================================================
#  MEASURING LEG LENGTH - a way of specifying the leg movement Amplitude
# ========================================================================
 
                   
        bones = bpy.context.object.data.bones
        pose_bones = bpy.context.object.pose.bones

        # Measuring Leg Length ( Left )
        def get_left_Leg_length(bonename_1, bonename_2, bonename_3, bonename_4):
               
            for  bone in pose_bones:
                if bone.name == bonename_1:
                    bonelength_1 = bone.length
                    
                if bone.name == bonename_2:
                    bonelength_2 = bone.length
             
                if bone.name == bonename_3:
                    bonelength_3 = bone.length    

                if bone.name == bonename_4:
                    bonelength_4 = bone.length    
             

            masterlength = bonelength_1 + bonelength_2 + bonelength_3 + bonelength_4        
                    
            # Size Default
            if masterlength > 0.9 and masterlength < 1:
                walk_cycle_24_size_default()    
                print("Length is","%.2f" % masterlength)


            # Size 0.1 to 0.3
            if masterlength > 0.1 and masterlength < 0.3:
                walk_cycle_24_size_01_03() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.3 to 0.5
            if masterlength > 0.3 and masterlength < 0.5:
                walk_cycle_24_size_03_05() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.5 to 0.6
            if masterlength > 0.5 and masterlength < 0.6:
                walk_cycle_24_size_05_06() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.6 to 0.7
            if masterlength > 0.6 and masterlength < 0.7:
                walk_cycle_24_size_06_07() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.7 to 0.8
            if masterlength > 0.7 and masterlength < 0.8:
                walk_cycle_24_size_07_08() 
                print("Length is","%.2f" % masterlength)
            
            
            # Size 0.8 to 0.84
            if masterlength > 0.8 and masterlength < 0.84:
                walk_cycle_24_size_08_084()    
                print("Length is","%.2f" % masterlength)


            # Size 0.84 to 0.9
            if masterlength > 0.84 and masterlength < 0.9:
                walk_cycle_24_size_084_09()    
                print("Length is","%.2f" % masterlength)


            # Size Bigger then "Default"
            if masterlength > 1:
                walk_cycle_24_size_default()   
                print("Length is","%.2f" % masterlength)
      

        get_left_Leg_length('DEF-shin.L','DEF-shin.L.001','DEF-thigh.L','DEF-thigh.L.001')
      
 
# ===========================================================================
#  END MEASURING LEG LENGTH - a way of specifying the leg movement Amplitude
# ===========================================================================
 


        # Add Cycles Modifier

        ob = bpy.context.object
        ob_fcurve = ob.animation_data.action.fcurves


        def add_cycle_modifier():
            
               
            for fc in ob_fcurve:
                d_path = ('location', 'rotation_quaternion', 'rotation_euler', 'scale',)
                     
                if fc.data_path.endswith((d_path)):
                    fc.modifiers.new(type='CYCLES')
                
                fc.update()


        add_cycle_modifier()
         

        # Action Name
        ob = bpy.context.object
        ob.animation_data.action.name = ob.name + '_Walk_24' 

    
        # JUMP TO START AND PLAY ANIMATION
        bpy.ops.screen.frame_jump(end=False)
        bpy.ops.screen.animation_play()



        # FRAME SELECTED RANGE IN TIMELINE

        for area in bpy.context.screen.areas:
            if area.type == 'DOPESHEET_EDITOR':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        ctx = bpy.context.copy()
                        ctx['area'] = area
                        ctx['region'] = region
                        bpy.ops.action.view_all(ctx)
                        break
                break
        # Frame selected range in GRAPH_EDITOR 
        for area in bpy.context.screen.areas:
            if area.type == 'GRAPH_EDITOR':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        ctx = bpy.context.copy()
                        ctx['area'] = area
                        ctx['region'] = region
                        bpy.ops.graph.view_all(ctx)
                        break
                break
      

        return {'FINISHED'}



# =====================================================
#    END   MULTIPLE LIMBS - 24 FRAMES  WALK CYCLE
# =====================================================





#======================================================
#======================================================
#======================================================





# =====================================================
#          MULTIPLE LIMBS - 32 FRAMES  WALK CYCLE
# =====================================================


# 32 FRAMES WALK CYCLE FOR RIGIFY HUMAN WITH MULTIPLE LIMBS. 
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_magic_walk_multiple_limbs_32_ra(bpy.types.Operator):
    '''32 FRAMES Walk Cycle For Rigify Human With Multiple Limbs.
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_magic_walk_multiple_limbs_32_ra"
    bl_label = "32"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)
 

                
    def execute(self, context):

        scene = context.scene
      
        # Ref
        exclude_arms = scene.animbox_ra_props.exclude_arms_from_anim

 

        # TOTAL RESET

        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        #bpy.ops.pose.transforms_clear()
        bpy.ops.anim.keyframe_clear_v3d() 
        bpy.ops.pose.select_all(action = 'DESELECT')
        bpy.ops.screen.frame_jump(end=False)
            


         
        bones = bpy.context.object.data.bones
        pose_bones = bpy.context.object.pose.bones

           
         
        # DEFINING FRAME RANGE

        # START
        bpy.context.scene.frame_start = 1

        # END
        bpy.context.scene.frame_end = 32
         


        # NAMES DEFINITION


        # Find matching Chest Name                
        Chest = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "chest*")]
         

        # Find matching Torso Name
        Torso = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "torso*")]


        # Find matching Arm_Parent Name
        Arm_Parent_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_parent.R*")]
        Arm_Parent_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_parent.L*")]


        # Find matching Arm Name
        Arm_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_fk.R*")]
        Arm_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "upper_arm_fk.L*")]
         


        # Find matching Feets Name
        Foot_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_ik.R*")]
        Foot_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_ik.L*")]     
         

        # Find matching Heels Name
        Heel_R = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_heel_ik.R*")]
        Heel_L = [obj for obj in pose_bones  if fnmatch.fnmatchcase(obj.name, "foot_heel_ik.L*")]     
                 

# =====================================================
#      DEFAULT SIZE   - 32 FRAMES Cycle
# =====================================================
       
        def walk_cycle_32_size_default():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                         
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                                        

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(17)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(33)


            for o in Torso:
                o.location=(0.000, 0.000, -0.070)
                insert_keys(1)
                o.location=(0.020, 0.000, -0.020)
                insert_keys(9)
                o.location=(-0.000, 0.000, -0.070)
                insert_keys(17)
                o.location=(-0.020, 0.000, -0.020)
                insert_keys(25)
                o.location=(0.000, 0.000, -0.070)
                insert_keys(33)


            for o in Foot_R:
                o.location=(0.00, 0.44, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, -0.38, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(17)
                o.location=(0.00, -0.31, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(20)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)
                o.location=(0.00, 0.44, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(33)


            for o in Foot_L:
                o.location=(0.00, -0.38, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.31, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(4)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(9)
                o.location=(0.00, 0.44, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(17)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(24)
                o.location=(0.00, -0.38, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(33)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(33)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(33)


            for o in Heel_R:
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(33)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(17)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(33)

                     
           #walk_cycle_32_size_default() 
                        
# =====================================================
#   END   DEFAULT SIZE   - 32 FRAMES Cycle
# =====================================================
               



# =====================================================
#      SIZE  << 0.1 - 0.3 >>  32 FRAMES Cycle
# =====================================================
 
        def walk_cycle_32_size_01_03():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            
            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(17)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(33)

        
            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.02, 0.00, -0.02)
                insert_keys(9)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(17)
                o.location=(-0.02, 0.00, -0.02)
                insert_keys(25)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(33)


            for o in Foot_R:
                o.location=(-0.00, 0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.00, 0.06)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, -0.10, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(20)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)
                o.location=(-0.00, 0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(33)


            for o in Foot_L:
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.10, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(4)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(9)
                o.location=(-0.00, 0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, 0.00, 0.06)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(24)
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(33)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.30, 0.00, 0.10)
                    insert_keys(1)
                    o.rotation_quaternion=(0.97, -0.19, -0.00, 0.15)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, 0.30, 0.00, 0.10)
                    insert_keys(33)


            for o in Arm_L:
                if not exclude_arms:       
                    o.rotation_quaternion=(1.00, -0.20, 0.00, -0.15)
                    insert_keys(1)
                    o.rotation_quaternion=(0.95, 0.29, -0.00, -0.10)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, -0.20, 0.00, -0.15)
                    insert_keys(33)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(33)

         
            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(17)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(33)
                         
            #walk_cycle_32_size_01_03() 
                      
# =====================================================
#   END  SIZE  << 0.1 - 0.3 >>  32 FRAMES Cycle
# =====================================================
 
  

# =====================================================
#      SIZE  << 0.3 - 0.5 >>  32 FRAMES Cycle
# =====================================================
 
        def walk_cycle_32_size_03_05():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(17)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(33)


            for o in Torso:
                o.location=(0.000, 0.000, -0.040)
                insert_keys(1)
                o.location=(0.020, 0.000, -0.010)
                insert_keys(9)
                o.location=(-0.000, 0.000, -0.040)
                insert_keys(17)
                o.location=(-0.020, 0.000, -0.010)
                insert_keys(25)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(33)


            for o in Foot_R:
                o.location=(0.00, 0.20, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.01, 0.08)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, -0.23, 0.00)
                o.rotation_quaternion=(0.98, -0.17, 0.00, -0.00)
                insert_keys(17)
                o.location=(0.00, -0.17, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(20)
                o.location=(0.00, 0.01, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)
                o.location=(0.00, 0.20, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(33)


            for o in Foot_L:
                o.location=(0.00, -0.23, 0.00)
                o.rotation_quaternion=(1.00, -0.18, -0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.17, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(4)
                o.location=(0.00, 0.01, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(9)
                o.location=(0.00, 0.20, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, 0.01, 0.08)
                o.rotation_quaternion=(0.98, 0.20, -0.00, 0.00)
                insert_keys(24)
                o.location=(0.00, -0.23, 0.00)
                o.rotation_quaternion=(1.00, -0.18, -0.00, 0.00)
                insert_keys(33)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(33)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(33)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(33)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(17)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(33)

        # walk_cycle_32_size_03_05()

# =====================================================
#     END SIZE  << 0.3 - 0.5 >>  32 FRAMES Cycle
# =====================================================
 


# =====================================================
#      SIZE  << 0.5 - 0.6 >>  32 FRAMES Cycle
# =====================================================
 
        def walk_cycle_32_size_05_06():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(17)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(33)


            for o in Torso:
                o.location=(0.000, 0.000, -0.040)
                insert_keys(1)
                o.location=(0.020, 0.000, -0.008)
                insert_keys(9)
                o.location=(-0.000, 0.000, -0.040)
                insert_keys(17)
                o.location=(-0.020, 0.000, -0.008)
                insert_keys(25)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(33)


            for o in Foot_R:
                o.location=(0.00, 0.27, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, -0.22, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(17)
                o.location=(0.00, -0.17, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(20)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)
                o.location=(0.00, 0.27, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(33)


            for o in Foot_L:
                o.location=(-0.00, -0.22, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.17, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(4)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(9)
                o.location=(-0.00, 0.27, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(24)
                o.location=(-0.00, -0.22, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(33)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(33)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(33)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(33)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(17)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(33)


        # walk_cycle_32_size_05_06()

# =====================================================
#    END  SIZE  << 0.5 - 0.6 >>  32 FRAMES Cycle
# =====================================================
 


# =====================================================
#      SIZE  << 0.6 - 0.7 >>  32 FRAMES Cycle
# =====================================================
 
        def walk_cycle_32_size_06_07():

            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(17)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(33)


            for o in Torso:
                o.location=(0.000, 0.000, -0.040)
                insert_keys(1)
                o.location=(0.020, 0.000, -0.010)
                insert_keys(9)
                o.location=(-0.000, 0.000, -0.040)
                insert_keys(17)
                o.location=(-0.020, 0.000, -0.010)
                insert_keys(25)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(33)


            for o in Foot_R:
                o.location=(0.00, 0.28, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, -0.26, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(17)
                o.location=(0.00, -0.17, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(20)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)
                o.location=(0.00, 0.28, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(33)


            for o in Foot_L:
                o.location=(-0.00, -0.26, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.17, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(4)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(9)
                o.location=(-0.00, 0.28, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(24)
                o.location=(-0.00, -0.26, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(33)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(33)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(33)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(33)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(17)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(33)


        # walk_cycle_32_size_06_07()

# =====================================================
#    END  SIZE  << 0.6 - 0.7 >>  32 FRAMES Cycle
# =====================================================
 
 

# =====================================================
#      SIZE  << 0.7 - 0.8 >>  32 FRAMES Cycle
# =====================================================
 
        def walk_cycle_32_size_07_08():

            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)

                       
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(17)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(33)


            for o in Torso:
                o.location=(0.000, 0.000, -0.040)
                insert_keys(1)
                o.location=(0.020, 0.000, -0.010)
                insert_keys(9)
                o.location=(-0.000, 0.000, -0.040)
                insert_keys(17)
                o.location=(-0.020, 0.000, -0.010)
                insert_keys(25)
                o.location=(0.000, 0.000, -0.040)
                insert_keys(33)


            for o in Foot_R:
                o.location=(0.00, 0.33, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, -0.25, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(17)
                o.location=(0.00, -0.17, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(20)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)
                o.location=(0.00, 0.33, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(33)


            for o in Foot_L:
                o.location=(-0.00, -0.25, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.17, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(4)
                o.location=(-0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(9)
                o.location=(-0.00, 0.33, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(24)
                o.location=(-0.00, -0.25, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(33)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(33)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(33)


            for o in Heel_R:
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(33)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.40, -0.00, -0.00)
                insert_keys(17)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(33)


        # walk_cycle_32_size_07_08()

# =====================================================
#     END SIZE  << 0.7 - 0.8 >>  32 FRAMES Cycle
# =====================================================
 


# =====================================================
#  SIZE  << 0.8 - 0.84 >>  32 FRAMES Cycle
# =====================================================
 
         
        def walk_cycle_32_size_08_084(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                      
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(17)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(33)


            for o in Torso:
                o.location=(0.000, 0.000, -0.070)
                insert_keys(1)
                o.location=(0.020, 0.000, -0.010)
                insert_keys(9)
                o.location=(-0.000, 0.000, -0.070)
                insert_keys(17)
                o.location=(-0.020, 0.000, -0.010)
                insert_keys(25)
                o.location=(0.000, 0.000, -0.070)
                insert_keys(33)


            for o in Foot_R:
                o.location=(0.00, 0.44, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, -0.34, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(17)
                o.location=(0.00, -0.31, 0.00)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.00)
                insert_keys(20)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)
                o.location=(0.00, 0.44, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(33)


            for o in Foot_L:
                o.location=(0.00, -0.34, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.31, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(4)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(9)
                o.location=(0.00, 0.44, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(17)
                o.location=(0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(24)
                o.location=(0.00, -0.34, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(33)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(33)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(33)


            for o in Heel_R:
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(33)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(17)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(33)


        # walk_cycle_32_size_08_084()

# =====================================================
#  END  SIZE  << 0.8 - 0.84 >>  32 FRAMES Cycle
# =====================================================
 
         
       
         


                    

# =====================================================
#  SIZE  << 0.84 - 0.9 >>  32 FRAMES Cycle
# =====================================================
 
         
        def walk_cycle_32_size_084_09(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                o.keyframe_insert(data_path = 'rotation_euler', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                      
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_keys(17)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_keys(33)


            for o in Torso:
                o.location=(-0.000, 0.000, -0.070)
                insert_keys(1)
                o.location=(0.020, 0.000, -0.020)
                insert_keys(9)
                o.location=(-0.000, 0.000, -0.070)
                insert_keys(17)
                o.location=(-0.020, 0.000, -0.020)
                insert_keys(25)
                o.location=(0.000, 0.000, -0.070)
                insert_keys(33)


            for o in Foot_R:
                o.location=(-0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.99, 0.20, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, -0.44, 0.00)
                o.rotation_quaternion=(0.98, -0.20, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, -0.36, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(20)
                o.location=(-0.00, -0.07, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(25)
                o.location=(-0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(33)


            for o in Foot_L:
                o.location=(-0.00, -0.44, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.36, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(4)
                o.location=(-0.00, -0.07, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(9)
                o.location=(-0.00, 0.35, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, 0.00, 0.10)
                o.rotation_quaternion=(0.98, 0.20, 0.00, -0.00)
                insert_keys(24)
                o.location=(-0.00, -0.44, 0.00)
                o.rotation_quaternion=(1.00, -0.20, 0.00, -0.00)
                insert_keys(33)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(1)
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_keys(33)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(1)
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_keys(17)
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_keys(33)


            for o in Heel_R:
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(33)


            for o in Heel_L:
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(1)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(9)
                o.rotation_euler=(0.50, -0.00, -0.00)
                insert_keys(17)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(25)
                o.rotation_euler=(0.00, -0.00, -0.00)
                insert_keys(33)


                        
             #walk_cycle_32_size_084_09() 
               

# =====================================================
#    END SIZE  << 0.84 - 0.9 >>  32 FRAMES Cycle
# =====================================================
 




# ========================================================================
#  MEASURING LEG LENGTH - a way of specifying the leg movement Amplitude
# ========================================================================
 
                   
        bones = bpy.context.object.data.bones
        pose_bones = bpy.context.object.pose.bones

        # Measuring Leg Length ( Left )
        def get_left_Leg_length(bonename_1, bonename_2, bonename_3, bonename_4):
               
            for  bone in pose_bones:
                if bone.name == bonename_1:
                    bonelength_1 = bone.length
                    
                if bone.name == bonename_2:
                    bonelength_2 = bone.length
             
                if bone.name == bonename_3:
                    bonelength_3 = bone.length    

                if bone.name == bonename_4:
                    bonelength_4 = bone.length    
             

            masterlength = bonelength_1 + bonelength_2 + bonelength_3 + bonelength_4        
                    
            # Size Default
            if masterlength > 0.9 and masterlength < 1:
                walk_cycle_32_size_default()    
                print("Length is","%.2f" % masterlength)


            # Size 0.1 to 0.3
            if masterlength > 0.1 and masterlength < 0.3:
                walk_cycle_32_size_01_03() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.3 to 0.5
            if masterlength > 0.3 and masterlength < 0.5:
                walk_cycle_32_size_03_05()
                print("Length is","%.2f" % masterlength)

 
            # Size 0.5 to 0.6
            if masterlength > 0.5 and masterlength < 0.6:
                walk_cycle_32_size_05_06()
                print("Length is","%.2f" % masterlength)
                


            # Size 0.6 to 0.7
            if masterlength > 0.6 and masterlength < 0.7:
                walk_cycle_32_size_06_07()
                print("Length is","%.2f" % masterlength)
                                       


            # Size 0.7 to 0.8
            if masterlength > 0.7 and masterlength < 0.8:
                walk_cycle_32_size_07_08()
                print("Length is","%.2f" % masterlength)
      

 
            # Size 0.8 to 0.84
            if masterlength > 0.8 and masterlength < 0.84:
                walk_cycle_32_size_08_084()    
                print("Length is","%.2f" % masterlength)



            # Size 0.84 to 0.9
            if masterlength > 0.84 and masterlength < 0.9:
                walk_cycle_32_size_084_09()    
                print("Length is","%.2f" % masterlength)


            # Size Bigger then "Default"
            if masterlength > 1:
                walk_cycle_32_size_default()   
                print("Length is","%.2f" % masterlength)
      

        get_left_Leg_length('DEF-shin.L','DEF-shin.L.001','DEF-thigh.L','DEF-thigh.L.001')
      
 
# ===========================================================================
#  END MEASURING LEG LENGTH - a way of specifying the leg movement Amplitude
# ===========================================================================
 

        # Add Cycles Modifier

        ob = bpy.context.object
        ob_fcurve = ob.animation_data.action.fcurves


        def add_cycle_modifier():
            
               
            for fc in ob_fcurve:
                d_path = ('location', 'rotation_quaternion', 'rotation_euler', 'scale',)
                     
                if fc.data_path.endswith((d_path)):
                    fc.modifiers.new(type='CYCLES')
                
                fc.update()


        add_cycle_modifier()
         
         

        # Action Name
        ob = bpy.context.object
        ob.animation_data.action.name = ob.name + '_Walk_32' 

    
        # JUMP TO START AND PLAY ANIMATION
        bpy.ops.screen.frame_jump(end=False)
        bpy.ops.screen.animation_play()



        # FRAME SELECTED RANGE IN TIMELINE

        for area in bpy.context.screen.areas:
            if area.type == 'DOPESHEET_EDITOR':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        ctx = bpy.context.copy()
                        ctx['area'] = area
                        ctx['region'] = region
                        bpy.ops.action.view_all(ctx)
                        break
                break
        # Frame selected range in GRAPH_EDITOR 
        for area in bpy.context.screen.areas:
            if area.type == 'GRAPH_EDITOR':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        ctx = bpy.context.copy()
                        ctx['area'] = area
                        ctx['region'] = region
                        bpy.ops.graph.view_all(ctx)
                        break
                break
      

        return {'FINISHED'}



# =====================================================
#      END  MULTIPLE LIMBS - 32 FRAMES  WALK CYCLE
# =====================================================  
  
  
  
  


classes = [ OBJECT_OT_rigify_magic_walk_multiple_limbs_18_ra,
            OBJECT_OT_rigify_magic_walk_multiple_limbs_24_ra,
            OBJECT_OT_rigify_magic_walk_multiple_limbs_32_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()




  
