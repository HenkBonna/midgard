import bpy
import fnmatch



# RIGIFY AUTOMATION TOOLS


# =====================================================
#                     RIGIFY MAGIC RUN
# =====================================================


# Navigation :
#  MULTIPLE LIMBS - 18 FRAMES  RUN CYCLE  => line 1320
#  MULTIPLE LIMBS - 22 FRAMES  RUN CYCLE  => line 2600




# =====================================================
#          MULTIPLE LIMBS - 14 FRAMES  RUN CYCLE
# =====================================================




# 14 FRAMES RUN CYCLE FOR RIGIFY HUMAN WITH MULTIPLE LIMBS. 
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_magic_run_multiple_limbs_14_ra(bpy.types.Operator):
    '''14 Frames Run Cycle For Rigify Human With Multiple Limbs.
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_magic_run_multiple_limbs_14_ra"
    bl_label = "ML-14"
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
        bpy.context.scene.frame_end = 14
         



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
         

 
# =====================================================
#      DEFAULT SIZE   - 14 Frames Cycle
# =====================================================

  
        def run_cycle_14_size_default():
                               
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)

                
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                                  
            
            for o in Chest:
                o.rotation_quaternion = (1, 0, 0, 0.15)
                insert_keys(1)
                o.rotation_quaternion = (1, 0, 0, -0.15)
                insert_keys(8)
                o.rotation_quaternion = (1, 0, 0, 0.15)
                insert_keys(15)
                 
             
           
            for o in Torso:
                o.location = (0, 0, -0.04)
                insert_keys(1)
                o.location = (0, 0, -0.09)
                insert_keys(3)
                o.location = (0, 0, -0.01)
                insert_keys(6)
                o.location = (0, 0, -0.04)
                insert_keys(8)
                o.location = (0, 0, -0.09)
                insert_keys(10)
                o.location = (0, 0, -0.01)
                insert_keys(13)
                o.location = (0, 0, -0.04)
                insert_keys(15) 



            for o in Foot_R:
                o.location = (0, 0.75, 0.6)
                o.rotation_quaternion = (0.5, 1.15, 0, 0)        
                insert_keys(1)
                o.location = (0, 0.41, 0.46)
                o.rotation_quaternion = (0.6, 1.1, 0, 0) 
                insert_keys(3)
                o.location = (0, -0.56, 0.22)
                o.rotation_quaternion = (1, -0.22, 0, 0)
                insert_keys(6)      
                o.location = (0, -0.48, 0.08)  
                o.rotation_quaternion = (0.95, -0.28, 0, 0)
                insert_keys(8)  
                o.location = (0, -0.15, 0)  
                o.rotation_quaternion = (1, 0, 0, 0)
                insert_keys(10)   
                o.location = (0, 0.67, 0.45)  
                o.rotation_quaternion = (0.75, 0.67, 0, 0)
                insert_keys(13)   
                o.location = (0, 0.75, 0.6)
                o.rotation_quaternion = (0.5, 1.15, 0, 0)        
                insert_keys(15)  
         
         
                    
            for o in Foot_L:
                o.location = (0, -0.48, 0.08)
                o.rotation_quaternion = (1, -0.3, 0, 0)
                insert_keys(1)
                o.location = (0, -0.15, 0)
                o.rotation_quaternion = (1, 0, 0, 0)
                insert_keys(3)
                o.location = (0, 0.67, 0.45) 
                o.rotation_quaternion = (0.5, 0.45, 0, 0) 
                insert_keys(6) 
                o.location = (0, 0.75, 0.6)
                o.rotation_quaternion = (0.4, 0.9, 0, 0)               
                insert_keys(8)
                o.location = (0, 0.41, 0.46)
                o.rotation_quaternion = (0.5, 0.87, 0, 0)               
                insert_keys(10)
                o.location = (0, -0.56, 0.22)
                o.rotation_quaternion = (0.97, -0.215, 0, 0)               
                insert_keys(13)
                o.location = (0, -0.48, 0.08)
                o.rotation_quaternion = (1, -0.3, 0, 0)
                insert_keys(15)    


         
            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion = (1, 0.37, 0.25, 0.41)
                    insert_keys(1) 
                    o.rotation_quaternion = (0.92, -0.24, -0.11, 0.26)
                    insert_keys(8)                       
                    o.rotation_quaternion = (1, 0.37, 0.25, 0.41)
                    insert_keys(15)        
                                 
                
            for o in Arm_L:
                if not exclude_arms:                
                    o.rotation_quaternion = (1, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion = (0.85, 0.31, -0.21, -0.35 )
                    insert_keys(8)                
                    o.rotation_quaternion = (1, -0.27, 0.12, -0.29)
                    insert_keys(15)
                           
                            
        #run_cycle_14_size_default()
               
                 

# =====================================================
#   END   DEFAULT SIZE   - 14 Frames Cycle
# =====================================================
 
                  


                   


# =====================================================
#      SIZE  << 0.1 - 0.3 >>  14 Frames Cycle
# =====================================================

         
        def run_cycle_14_size_01_03():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                       
            
            for o in Chest:
                o.rotation_quaternion = (1, 0, 0, 0.15)
                insert_keys(1)
                o.rotation_quaternion = (1, 0, 0, -0.15)
                insert_keys(8)
                o.rotation_quaternion = (1, 0, 0, 0.15)
                insert_keys(15)
                  
            
            for o in Torso:
                o.location = (0, 0, -0.04)
                insert_keys(1)
                o.location = (0, 0, -0.07)
                insert_keys(3)
                o.location = (0, 0, -0.01)
                insert_keys(6)
                o.location = (0, 0, -0.04)
                insert_keys(8)
                o.location = (0, 0, -0.07)
                insert_keys(10)
                o.location = (0, 0, -0.01)
                insert_keys(13)
                o.location = (0, 0, -0.04)
                insert_keys(15) 


            for o in Foot_R:
                o.location = (0, 0.21, 0.14)
                o.rotation_quaternion = (0.5, 0.95, 0, 0)        
                insert_keys(1)
                o.location = (0, 0.12, 0.1)
                o.rotation_quaternion = (0.6, 1.2, 0, 0) 
                insert_keys(3)
                o.location = (0, -0.16, 0.06)
                o.rotation_quaternion = (1, -0.32, 0, 0)
                insert_keys(6)      
                o.location = (0, -0.15, 0.02)  
                o.rotation_quaternion = (0.98, -0.196, 0, 0)
                insert_keys(8)  
                o.location = (0, -0.02, 0)  
                o.rotation_quaternion = (1, 0, 0, 0)
                insert_keys(10)   
                o.location = (0, 0.21, 0.2)  
                o.rotation_quaternion = (0.46, 0.88, 0, 0)
                insert_keys(13)   
                o.location = (0, 0.21, 0.14)
                o.rotation_quaternion = (0.5, 0.95, 0, 0)         
                insert_keys(15)
                          

            for o in Foot_L:
                o.location = (0, -0.15, 0.02)
                o.rotation_quaternion = (1, -0.2, 0, 0)
                insert_keys(1)
                o.location = (0, -0.02, 0)
                o.rotation_quaternion = (1, 0, 0, 0)
                insert_keys(3)
                o.location = (0, 0.21, 0.2) 
                o.rotation_quaternion = (0.5, 0.95, 0, 0) 
                insert_keys(6) 
                o.location = (0, 0.21, 0.14)
                o.rotation_quaternion = (0.46, 0.88, 0, 0)               
                insert_keys(8)
                o.location = (0, 0.12, 0.1)
                o.rotation_quaternion = (0.44, 0.89, 0, 0)               
                insert_keys(10)
                o.location = (0, -0.16, 0.06)
                o.rotation_quaternion = (0.95, -0.3, 0, 0)               
                insert_keys(13)
                o.location = (0, -0.15, 0.02)
                o.rotation_quaternion = (1, -0.2, 0, 0)
                insert_keys(15)    
          
         
            for o in Arm_R:
                if not exclude_arms:                
                    o.rotation_quaternion = (1, 0.37, 0.15, 0.11)
                    insert_keys(1)
                    o.rotation_quaternion = (0.97, -0.16, -0.11, 0.08)
                    insert_keys(8)                   
                    o.rotation_quaternion = (1, 0.37, 0.15, 0.11)
                    insert_keys(15)        
                                  
                
            for o in Arm_L:
                if not exclude_arms:                
                    o.rotation_quaternion = (1, -0.17, 0.12, -0.09)
                    insert_keys(1)
                    o.rotation_quaternion = (0.92, 0.34, -0.14, -0.1 )
                    insert_keys(8)                
                    o.rotation_quaternion = (1, -0.17, 0.12, -0.09)
                    insert_keys(15)
                       
                            
        #run_cycle_14_size_01_03() 
               
                 
# =====================================================
#   END  SIZE  << 0.1 - 0.3 >>  14 Frames Cycle
# =====================================================
 
  

  
# =====================================================
#  SIZE  << 0.3 - 0.5 >>  14 Frames Cycle
# =====================================================
 
  
          
        def run_cycle_14_size_03_05(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                  

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(8)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(15)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(6)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(13)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(15)


            for o in Foot_R:
                o.location=(-0.00, 0.28, 0.20)
                o.rotation_quaternion=(0.57, 0.81, -0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, 0.18, 0.17)
                o.rotation_quaternion=(0.53, 0.76, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, -0.36, 0.14)
                o.rotation_quaternion=(1.00, -0.32, 0.00, -0.00)
                insert_keys(6)
                o.location=(-0.00, -0.29, 0.04)
                o.rotation_quaternion=(0.97, -0.23, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, -0.07, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, 0.21, 0.18)
                o.rotation_quaternion=(0.64, 0.77, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, 0.28, 0.20)
                o.rotation_quaternion=(0.57, 0.81, -0.00, 0.00)
                insert_keys(15)


            for o in Foot_L:
                o.location=(0.00, -0.29, 0.04)
                o.rotation_quaternion=(1.02, -0.24, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.12, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.21, 0.18)
                o.rotation_quaternion=(0.52, 0.63, -0.00, 0.00)
                insert_keys(6)
                o.location=(0.00, 0.28, 0.20)
                o.rotation_quaternion=(0.58, 0.82, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, 0.18, 0.17)
                o.rotation_quaternion=(0.57, 0.82, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, -0.36, 0.14)
                o.rotation_quaternion=(0.95, -0.30, 0.00, -0.00)
                insert_keys(13)
                o.location=(0.00, -0.29, 0.04)
                o.rotation_quaternion=(1.02, -0.24, 0.00, -0.00)
                insert_keys(15)


            for o in Arm_R:
                if not exclude_arms:                
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(8)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(15)


            for o in Arm_L:
                if not exclude_arms:                
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(8)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(15)


        # run_cycle_14_size_03_05()



  
# =====================================================
#  END SIZE  << 0.3 - 0.5 >>  14 Frames Cycle
# =====================================================
 
 
  
# =====================================================
#  SIZE  << 0.5 - 0.6 >>  14 Frames Cycle
# =====================================================
 
  
          
        def run_cycle_14_size_05_06(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                   

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(8)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(15)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(6)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(13)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(15)


            for o in Foot_R:
                o.location=(0.00, 0.47, 0.32)
                o.rotation_quaternion=(0.50, 0.85, -0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, 0.20, 0.18)
                o.rotation_quaternion=(0.60, 0.70, -0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, -0.38, 0.14)
                o.rotation_quaternion=(1.00, -0.32, -0.00, 0.00)
                insert_keys(6)
                o.location=(-0.00, -0.35, 0.07)
                o.rotation_quaternion=(0.96, -0.29, -0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, -0.05, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, 0.45, 0.30)
                o.rotation_quaternion=(0.61, 0.79, -0.00, 0.00)
                insert_keys(13)
                o.location=(0.00, 0.47, 0.32)
                o.rotation_quaternion=(0.50, 0.85, -0.00, 0.00)
                insert_keys(15)


            for o in Foot_L:
                o.location=(0.00, -0.35, 0.07)
                o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.05, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(-0.00, 0.45, 0.30)
                o.rotation_quaternion=(0.50, 0.65, 0.00, 0.00)
                insert_keys(6)
                o.location=(-0.00, 0.47, 0.32)
                o.rotation_quaternion=(0.51, 0.86, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, 0.20, 0.18)
                o.rotation_quaternion=(0.65, 0.76, 0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, -0.38, 0.14)
                o.rotation_quaternion=(0.95, -0.30, 0.00, 0.00)
                insert_keys(13)
                o.location=(0.00, -0.35, 0.07)
                o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
                insert_keys(15)


            for o in Arm_R:
                if not exclude_arms:                
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(8)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(15)


            for o in Arm_L:
                if not exclude_arms:                
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(8)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(15)


        # run_cycle_14_size_05_06()


# =====================================================
#  END SIZE  << 0.5 - 0.6 >>  14 Frames Cycle
# =====================================================
 

  
# =====================================================
#  SIZE  << 0.6 - 0.7 >>  14 Frames Cycle
# =====================================================
 
          
        def run_cycle_14_size_06_07(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                   


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(8)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(15)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(6)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(13)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(15)


            for o in Foot_R:
                o.location=(0.00, 0.38, 0.29)
                o.rotation_quaternion=(0.51, 0.84, -0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, 0.20, 0.18)
                o.rotation_quaternion=(0.63, 0.67, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, -0.45, 0.19)
                o.rotation_quaternion=(1.00, -0.32, 0.00, 0.00)
                insert_keys(6)
                o.location=(-0.00, -0.35, 0.03)
                o.rotation_quaternion=(0.97, -0.23, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, -0.02, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, 0.37, 0.29)
                o.rotation_quaternion=(0.61, 0.79, 0.00, 0.00)
                insert_keys(13)
                o.location=(0.00, 0.38, 0.29)
                o.rotation_quaternion=(0.51, 0.84, -0.00, 0.00)
                insert_keys(15)


            for o in Foot_L:
                o.location=(0.00, -0.35, 0.03)
                o.rotation_quaternion=(1.01, -0.25, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.02, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(-0.00, 0.37, 0.29)
                o.rotation_quaternion=(0.50, 0.65, 0.00, 0.00)
                insert_keys(6)
                o.location=(-0.00, 0.38, 0.29)
                o.rotation_quaternion=(0.52, 0.85, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, 0.20, 0.18)
                o.rotation_quaternion=(0.69, 0.73, 0.00, 0.00)
                insert_keys(10)
                o.location=(-0.00, -0.45, 0.19)
                o.rotation_quaternion=(0.95, -0.30, 0.00, 0.00)
                insert_keys(13)
                o.location=(0.00, -0.35, 0.03)
                o.rotation_quaternion=(1.01, -0.25, 0.00, 0.00)
                insert_keys(15)


            for o in Arm_R:
                if not exclude_arms:                
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(8)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(15)


            for o in Arm_L:
                if not exclude_arms:                
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(8)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(15)



        # run_cycle_14_size_06_07()


  
# =====================================================
#  END SIZE  << 0.6 - 0.7 >>  14 Frames Cycle
# =====================================================
 



  
# =====================================================
#  SIZE  << 0.7 - 0.8 >>  14 Frames Cycle
# =====================================================
 
  
          
        def run_cycle_14_size_07_08(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                   

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(8)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(15)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(6)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(13)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(15)


            for o in Foot_R:
                o.location=(-0.00, 0.53, 0.38)
                o.rotation_quaternion=(0.50, 0.85, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.20, 0.18)
                o.rotation_quaternion=(0.60, 0.70, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, -0.40, 0.12)
                o.rotation_quaternion=(1.00, -0.32, 0.00, -0.00)
                insert_keys(6)
                o.location=(-0.00, -0.33, 0.03)
                o.rotation_quaternion=(0.96, -0.29, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, -0.14, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, 0.47, 0.30)
                o.rotation_quaternion=(0.61, 0.79, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, 0.53, 0.38)
                o.rotation_quaternion=(0.50, 0.85, 0.00, -0.00)
                insert_keys(15)


            for o in Foot_L:
                o.location=(-0.00, -0.33, 0.03)
                o.rotation_quaternion=(1.00, -0.30, -0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, -0.14, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(3)
                o.location=(-0.00, 0.47, 0.30)
                o.rotation_quaternion=(0.50, 0.65, -0.00, 0.00)
                insert_keys(6)
                o.location=(-0.00, 0.53, 0.38)
                o.rotation_quaternion=(0.51, 0.86, -0.00, 0.00)
                insert_keys(8)
                o.location=(-0.00, 0.20, 0.18)
                o.rotation_quaternion=(0.65, 0.76, -0.00, 0.00)
                insert_keys(10)
                o.location=(-0.00, -0.40, 0.12)
                o.rotation_quaternion=(0.95, -0.30, -0.00, 0.00)
                insert_keys(13)
                o.location=(-0.00, -0.33, 0.03)
                o.rotation_quaternion=(1.00, -0.30, -0.00, 0.00)
                insert_keys(15)


            for o in Arm_R:
                if not exclude_arms:                
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(8)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(15)


            for o in Arm_L:
                if not exclude_arms:                
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(8)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(15)




        # run_cycle_14_size_07_08()


  
# =====================================================
#    END SIZE  << 0.7 - 0.8 >>  14 Frames Cycle
# =====================================================
 

# =====================================================
#  SIZE  << 0.8 - 0.84 >>  14 Frames Cycle
# =====================================================
 
  
          
        def run_cycle_14_size_08_084(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(8)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(15)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(6)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(13)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(15)


            for o in Foot_R:
                o.location=(-0.00, 0.59, 0.41)
                o.rotation_quaternion=(0.50, 0.85, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.20, 0.18)
                o.rotation_quaternion=(0.60, 0.70, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, -0.43, 0.18)
                o.rotation_quaternion=(1.00, -0.32, 0.00, -0.00)
                insert_keys(6)
                o.location=(-0.00, -0.35, 0.05)
                o.rotation_quaternion=(0.96, -0.29, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, 0.53, 0.35)
                o.rotation_quaternion=(0.61, 0.79, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, 0.59, 0.41)
                o.rotation_quaternion=(0.50, 0.85, 0.00, -0.00)
                insert_keys(15)


            for o in Foot_L:
                o.location=(-0.00, -0.35, 0.05)
                o.rotation_quaternion=(1.00, -0.30, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.53, 0.35)
                o.rotation_quaternion=(0.50, 0.65, 0.00, -0.00)
                insert_keys(6)
                o.location=(-0.00, 0.59, 0.41)
                o.rotation_quaternion=(0.51, 0.86, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, 0.20, 0.18)
                o.rotation_quaternion=(0.65, 0.76, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, -0.43, 0.18)
                o.rotation_quaternion=(0.95, -0.30, 0.00, -0.00)
                insert_keys(13)
                o.location=(-0.00, -0.35, 0.05)
                o.rotation_quaternion=(1.00, -0.30, 0.00, -0.00)
                insert_keys(15)


            for o in Arm_R:
                if not exclude_arms:                
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(8)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(15)


            for o in Arm_L:
                if not exclude_arms:                
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(8)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(15)



        # run_cycle_14_size_08_084()



# =====================================================
#  END SIZE  << 0.8 - 0.84 >>  14 Frames Cycle
# =====================================================
 
  


# =====================================================
#  SIZE  << 0.84 - 0.9 >>  14 Frames Cycle
# =====================================================
 
  
          
        def run_cycle_14_size_084_09(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                      
            
            for o in Chest:
                o.rotation_quaternion = (1, 0, 0, 0.15)
                insert_keys(1)
                o.rotation_quaternion = (1, 0, 0, -0.15)
                insert_keys(8)
                o.rotation_quaternion = (1, 0, 0, 0.15)
                insert_keys(15)
         
         
            for o in Torso:
                o.location = (0.00, 0.00, -0.04)
                insert_keys(1)
                o.location = (0.00, 0.00, -0.09)
                insert_keys(3)
                o.location = (0.00, 0.00, -0.01)
                insert_keys(6)
                o.location = (0.00, 0.00, -0.04)
                insert_keys(8)
                o.location = (0.00, 0.00, -0.09)
                insert_keys(10)
                o.location = (0.00, 0.00, -0.01)
                insert_keys(13)
                o.location = (0.00, 0.00, -0.04)
                insert_keys(15)


            for o in Foot_R:
                o.location = (0.00, 0.50, 0.50)
                o.rotation_quaternion = (0.50, 0.85, -0.00, 0.00)
                insert_keys(1)
                o.location = (0.00, 0.34, 0.40)
                o.rotation_quaternion = (0.60, 0.80, -0.00, 0.00)
                insert_keys(3)
                o.location = (0.00, -0.60, 0.25)
                o.rotation_quaternion = (1.00, -0.22, -0.00, 0.00)
                insert_keys(6)
                o.location = (0.00, -0.48, 0.04)
                o.rotation_quaternion = (0.96, -0.29, -0.00, 0.00)
                insert_keys(8)
                o.location = (0.00, -0.20, 0.00)
                o.rotation_quaternion = (1.00, 0.00, -0.00, 0.00)
                insert_keys(10)
                o.location = (0.00, 0.50, 0.45)
                o.rotation_quaternion = (0.67, 0.74, -0.00, 0.00)
                insert_keys(13)
                o.location = (0.00, 0.50, 0.50)
                o.rotation_quaternion = (0.50, 0.85, -0.00, 0.00)
                insert_keys(15)


            for o in Foot_L:
                o.location = (0.00, -0.48, 0.04)
                o.rotation_quaternion = (1.00, -0.30, 0.00, 0.00)
                insert_keys(1)
                o.location = (0.00, -0.20, 0.00)
                o.rotation_quaternion = (1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location = (0.00, 0.50, 0.45)
                o.rotation_quaternion = (0.50, 0.55, 0.00, 0.00)
                insert_keys(6)
                o.location = (0.00, 0.50, 0.50)
                o.rotation_quaternion = (0.51, 0.86, 0.00, 0.00)
                insert_keys(8)
                o.location = (0.00, 0.34, 0.40)
                o.rotation_quaternion = (0.60, 0.80, 0.00, 0.00)
                insert_keys(10)
                o.location = (0.00, -0.60, 0.25)
                o.rotation_quaternion = (0.98, -0.21, 0.00, 0.00)
                insert_keys(13)
                o.location = (0.00, -0.48, 0.04)
                o.rotation_quaternion = (1.00, -0.30, 0.00, 0.00)
                insert_keys(15)

         
            for o in Arm_R:
                if not exclude_arms:                
                    o.rotation_quaternion = (1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion = (0.92, -0.25, -0.11, 0.27)
                    insert_keys(8)
                    o.rotation_quaternion = (1.00, 0.37, 0.25, 0.41)
                    insert_keys(15)

               
            for o in Arm_L:
                if not exclude_arms:                
                    o.rotation_quaternion = (1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion = (0.86, 0.32, -0.21, -0.35)
                    insert_keys(8)
                    o.rotation_quaternion = (1.00, -0.27, 0.12, -0.29)
                    insert_keys(15)

                        
        #run_cycle_14_size_084_09() 
               

# =====================================================
#    END SIZE  << 0.84 - 0.9 >>  14 Frames Cycle
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
                run_cycle_14_size_default()    
                print("Length is","%.2f" % masterlength)


            # Size 0.1 to 0.3
            if masterlength > 0.1 and masterlength < 0.3:
                run_cycle_14_size_01_03() 
                print("Length is","%.2f" % masterlength)


            # Size 0.3 to 0.5
            if masterlength > 0.3 and masterlength < 0.5:
                run_cycle_14_size_03_05()
                print("Length is","%.2f" % masterlength)


            # Size 0.5 to 0.6
            if masterlength > 0.5 and masterlength < 0.6:
                run_cycle_14_size_05_06()
                print("Length is","%.2f" % masterlength)


            # Size 0.6 to 0.7
            if masterlength > 0.6 and masterlength < 0.7:
                run_cycle_14_size_06_07()
                print("Length is","%.2f" % masterlength)



            # Size 0.7 to 0.8
            if masterlength > 0.7 and masterlength < 0.8:
                run_cycle_14_size_07_08() 
                print("Length is","%.2f" % masterlength)
            
           

            # Size 0.8 to 0.84
            if masterlength > 0.8 and masterlength < 0.84:
                run_cycle_14_size_08_084()    
                print("Length is","%.2f" % masterlength)



            # Size 0.84 to 0.9
            if masterlength > 0.84 and masterlength < 0.9:
                run_cycle_14_size_084_09()    
                print("Length is","%.2f" % masterlength)


            # Size Bigger then "Default"
            if masterlength > 1:
                run_cycle_14_size_default()    
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
        ob.animation_data.action.name = ob.name +'_Run_14'

         
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
#      END   MULTIPLE LIMBS - 14 FRAMES  RUN CYCLE
# =====================================================








# =====================================================
#          MULTIPLE LIMBS - 18 FRAMES  RUN CYCLE
# =====================================================




# 18 FRAMES RUN CYCLE FOR RIGIFY HUMAN WITH MULTIPLE LIMBS. 
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_magic_run_multiple_limbs_18_ra(bpy.types.Operator):
    '''18 Frames Run Cycle For Rigify Human With Multiple Limbs.
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_magic_run_multiple_limbs_18_ra"
    bl_label = "ML-18"
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
         


# =====================================================
#      DEFAULT SIZE   - 18 Frames Cycle
# =====================================================

         
        def run_cycle_18_size_default():
                               
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)

            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                    
            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(12)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(17)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(-0.00, 0.78, 0.53)
                o.rotation_quaternion=(0.66, 1.07, -0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, 0.23, 0.35)
                o.rotation_quaternion=(0.81, 0.96, -0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, -0.65, 0.27)
                o.rotation_quaternion=(1.00, -0.22, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, -0.48, 0.08)
                o.rotation_quaternion=(0.96, -0.29, 0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(12)
                o.location=(-0.00, 0.73, 0.48)
                o.rotation_quaternion=(0.61, 0.80, -0.00, 0.00)
                insert_keys(17)
                o.location=(-0.00, 0.78, 0.53)
                o.rotation_quaternion=(0.66, 1.07, -0.00, 0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.48, 0.08)
                o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, 0.03, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, 0.73, 0.48)
                o.rotation_quaternion=(0.41, 0.54, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, 0.78, 0.53)
                o.rotation_quaternion=(0.53, 0.85, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, 0.23, 0.35)
                o.rotation_quaternion=(0.64, 0.77, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, -0.65, 0.27)
                o.rotation_quaternion=(0.98, -0.21, 0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, -0.48, 0.08)
                o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.24, -0.11, 0.26)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.85, 0.31, -0.21, -0.35)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(19)
         
                            
        #run_cycle_18_size_default() 
               
                

# =====================================================
#   END   DEFAULT SIZE   - 18 Frames Cycle
# =====================================================
 
                  

        
# =====================================================
#      SIZE  << 0.1 - 0.3 >>  18 Frames Cycle
# =====================================================

         
        def run_cycle_18_size_01_03():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                       
 
            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.07)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.07)
                insert_keys(12)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(17)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(0.00, 0.21, 0.16)
                o.rotation_quaternion=(0.45, 0.98, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.12, 0.10)
                o.rotation_quaternion=(0.60, 1.20, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, -0.16, 0.06)
                o.rotation_quaternion=(1.00, -0.32, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, -0.15, 0.02)
                o.rotation_quaternion=(0.98, -0.20, 0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, 0.05, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, 0.21, 0.20)
                o.rotation_quaternion=(0.46, 0.88, 0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, 0.21, 0.16)
                o.rotation_quaternion=(0.45, 0.98, 0.00, -0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.15, 0.02)
                o.rotation_quaternion=(1.00, -0.20, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, 0.05, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, 0.21, 0.20)
                o.rotation_quaternion=(0.50, 0.95, 0.00, 0.00)
                insert_keys(8)
                o.location=(-0.00, 0.21, 0.16)
                o.rotation_quaternion=(0.41, 0.91, -0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, 0.12, 0.10)
                o.rotation_quaternion=(0.45, 0.89, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, -0.16, 0.06)
                o.rotation_quaternion=(0.95, -0.30, 0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, -0.15, 0.02)
                o.rotation_quaternion=(1.00, -0.20, 0.00, 0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, 0.37, 0.15, 0.11)
                    insert_keys(1)
                    o.rotation_quaternion=(0.97, -0.16, -0.11, 0.08)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.37, 0.15, 0.11)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, -0.17, 0.12, -0.09)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, 0.34, -0.14, -0.10)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.17, 0.12, -0.09)
                    insert_keys(19)

                         
        #run_cycle_18_size_01_03() 
               
         
# =====================================================
#   END  SIZE  << 0.1 - 0.3 >>  18 Frames Cycle
# =====================================================
 
  
  
# =====================================================
#      SIZE  << 0.3 - 0.5 >>  18 Frames Cycle
# =====================================================

         
        def run_cycle_18_size_03_05():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                  

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(12)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(17)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(-0.00, 0.30, 0.22)
                o.rotation_quaternion=(0.50, 0.85, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.11, 0.14)
                o.rotation_quaternion=(0.60, 0.70, 0.00, -0.00)
                insert_keys(3)
                o.location=(0.00, -0.34, 0.10)
                o.rotation_quaternion=(1.00, -0.32, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, -0.31, 0.04)
                o.rotation_quaternion=(0.97, -0.23, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, -0.10, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(12)
                o.location=(0.00, 0.25, 0.20)
                o.rotation_quaternion=(0.61, 0.79, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, 0.30, 0.22)
                o.rotation_quaternion=(0.50, 0.85, 0.00, -0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.31, 0.04)
                o.rotation_quaternion=(1.02, -0.24, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.10, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(-0.00, 0.25, 0.20)
                o.rotation_quaternion=(0.50, 0.65, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, 0.30, 0.22)
                o.rotation_quaternion=(0.51, 0.86, 0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, 0.11, 0.14)
                o.rotation_quaternion=(0.65, 0.76, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, -0.34, 0.10)
                o.rotation_quaternion=(0.95, -0.30, 0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, -0.31, 0.04)
                o.rotation_quaternion=(1.02, -0.24, 0.00, 0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(19)



        # run_cycle_18_size_03_05()


# =====================================================
#    END  SIZE  << 0.3 - 0.5 >>  18 Frames Cycle
# =====================================================



# =====================================================
#      SIZE  << 0.5 - 0.6 >>  18 Frames Cycle
# =====================================================

         
        def run_cycle_18_size_05_06():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                  

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(12)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(17)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(0.00, 0.44, 0.31)
                o.rotation_quaternion=(0.50, 0.85, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, 0.20, 0.18)
                o.rotation_quaternion=(0.60, 0.70, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, -0.38, 0.14)
                o.rotation_quaternion=(1.00, -0.32, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, -0.28, 0.02)
                o.rotation_quaternion=(0.97, -0.24, -0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, 0.01, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(12)
                o.location=(-0.00, 0.46, 0.32)
                o.rotation_quaternion=(0.60, 0.80, -0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, 0.44, 0.31)
                o.rotation_quaternion=(0.50, 0.85, 0.00, 0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.28, 0.02)
                o.rotation_quaternion=(1.01, -0.25, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, 0.01, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, 0.46, 0.32)
                o.rotation_quaternion=(0.50, 0.65, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, 0.44, 0.31)
                o.rotation_quaternion=(0.51, 0.86, 0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, 0.20, 0.18)
                o.rotation_quaternion=(0.65, 0.76, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, -0.38, 0.14)
                o.rotation_quaternion=(0.95, -0.30, 0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, -0.28, 0.02)
                o.rotation_quaternion=(1.01, -0.25, 0.00, 0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(19)



        # run_cycle_18_size_05_06()

# =====================================================
#   END   SIZE  << 0.5 - 0.6 >>  18 Frames Cycle
# =====================================================



# =====================================================
#      SIZE  << 0.6 - 0.7 >>  18 Frames Cycle
# =====================================================

         
        def run_cycle_18_size_06_07():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                  

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(12)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(17)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(0.00, 0.37, 0.32)
                o.rotation_quaternion=(0.50, 0.85, 0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, 0.14, 0.16)
                o.rotation_quaternion=(0.66, 0.65, -0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, -0.45, 0.15)
                o.rotation_quaternion=(1.00, -0.32, 0.00, 0.00)
                insert_keys(8)
                o.location=(-0.00, -0.37, 0.05)
                o.rotation_quaternion=(0.96, -0.29, 0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, -0.05, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, 0.37, 0.30)
                o.rotation_quaternion=(0.61, 0.79, 0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, 0.37, 0.32)
                o.rotation_quaternion=(0.50, 0.85, 0.00, 0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.37, 0.05)
                o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.05, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(-0.00, 0.37, 0.30)
                o.rotation_quaternion=(0.50, 0.65, 0.00, 0.00)
                insert_keys(8)
                o.location=(-0.00, 0.37, 0.32)
                o.rotation_quaternion=(0.51, 0.86, 0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, 0.14, 0.16)
                o.rotation_quaternion=(0.71, 0.70, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, -0.45, 0.15)
                o.rotation_quaternion=(0.95, -0.30, 0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, -0.37, 0.05)
                o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(19)


        # run_cycle_18_size_06_07()


# =====================================================
#    END  SIZE  << 0.6 - 0.7 >>  18 Frames Cycle
# =====================================================



# =====================================================
#  SIZE  << 0.7 - 0.8 >>  18 Frames Cycle
# =====================================================
 
          
          
        def run_cycle_18_size_07_08(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                   




            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(12)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(17)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(-0.00, 0.56, 0.44)
                o.rotation_quaternion=(0.47, 0.87, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.14, 0.16)
                o.rotation_quaternion=(0.66, 0.65, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, -0.48, 0.18)
                o.rotation_quaternion=(1.00, -0.32, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, -0.41, 0.08)
                o.rotation_quaternion=(0.96, -0.29, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, -0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, 0.56, 0.36)
                o.rotation_quaternion=(0.58, 0.81, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, 0.56, 0.44)
                o.rotation_quaternion=(0.47, 0.87, 0.00, -0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(-0.00, -0.41, 0.08)
                o.rotation_quaternion=(1.00, -0.30, -0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, -0.18, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(3)
                o.location=(-0.00, 0.56, 0.36)
                o.rotation_quaternion=(0.48, 0.67, -0.00, 0.00)
                insert_keys(8)
                o.location=(-0.00, 0.56, 0.44)
                o.rotation_quaternion=(0.47, 0.88, -0.00, 0.00)
                insert_keys(10)
                o.location=(-0.00, 0.14, 0.16)
                o.rotation_quaternion=(0.71, 0.70, -0.00, 0.00)
                insert_keys(12)
                o.location=(-0.00, -0.48, 0.18)
                o.rotation_quaternion=(0.95, -0.30, -0.00, 0.00)
                insert_keys(17)
                o.location=(-0.00, -0.41, 0.08)
                o.rotation_quaternion=(1.00, -0.30, -0.00, 0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(19)





        # run_cycle_18_size_07_08()


# =====================================================
#  END SIZE  << 0.7 - 0.8 >>  18 Frames Cycle
# =====================================================
 



# =====================================================
#  SIZE  << 0.8 - 0.84 >>  18 Frames Cycle
# =====================================================
 
          
          
        def run_cycle_18_size_08_084(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(12)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(17)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(-0.00, 0.61, 0.42)
                o.rotation_quaternion=(0.50, 0.85, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.27, 0.24)
                o.rotation_quaternion=(0.60, 0.80, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, -0.51, 0.20)
                o.rotation_quaternion=(1.00, -0.22, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, -0.47, 0.10)
                o.rotation_quaternion=(0.96, -0.29, 0.00, -0.00)
                insert_keys(10)
                o.location=(-0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, 0.56, 0.37)
                o.rotation_quaternion=(0.67, 0.74, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, 0.61, 0.42)
                o.rotation_quaternion=(0.50, 0.85, 0.00, -0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.47, 0.10)
                o.rotation_quaternion=(1.00, -0.30, -0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.13, 0.00)
                o.rotation_quaternion=(1.00, 0.00, -0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, 0.56, 0.37)
                o.rotation_quaternion=(0.50, 0.55, -0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, 0.61, 0.42)
                o.rotation_quaternion=(0.51, 0.86, -0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, 0.27, 0.24)
                o.rotation_quaternion=(0.60, 0.80, -0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, -0.51, 0.20)
                o.rotation_quaternion=(0.98, -0.21, -0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, -0.47, 0.10)
                o.rotation_quaternion=(1.00, -0.30, -0.00, 0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(19)



        # run_cycle_18_size_08_084()



# =====================================================
#    END SIZE  << 0.8 - 0.84 >>  18 Frames Cycle
# =====================================================
 



# =====================================================
#  SIZE  << 0.84 - 0.9 >>  18 Frames Cycle
# =====================================================
 
          
          
        def run_cycle_18_size_084_09(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(1)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.15)
                insert_keys(10)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.15)
                insert_keys(19)


            for o in Torso:
                o.location=(0.00, 0.00, -0.04)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(10)
                o.location=(0.00, 0.00, -0.09)
                insert_keys(12)
                o.location=(0.00, 0.00, -0.01)
                insert_keys(17)
                o.location=(0.00, 0.00, -0.04)
                insert_keys(19)


            for o in Foot_R:
                o.location=(-0.00, 0.47, 0.33)
                o.rotation_quaternion=(0.59, 0.79, -0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, 0.08, 0.29)
                o.rotation_quaternion=(0.85, 0.53, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, -0.52, 0.21)
                o.rotation_quaternion=(1.00, -0.21, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, -0.51, 0.06)
                o.rotation_quaternion=(0.98, -0.21, 0.00, 0.00)
                insert_keys(10)
                o.location=(0.00, -0.25, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, 0.42, 0.27)
                o.rotation_quaternion=(0.71, 0.70, 0.00, -0.00)
                insert_keys(17)
                o.location=(-0.00, 0.47, 0.33)
                o.rotation_quaternion=(0.59, 0.79, -0.00, 0.00)
                insert_keys(19)


            for o in Foot_L:
                o.location=(0.00, -0.51, 0.06)
                o.rotation_quaternion=(1.02, -0.22, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.25, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(-0.00, 0.42, 0.27)
                o.rotation_quaternion=(0.53, 0.52, -0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, 0.47, 0.33)
                o.rotation_quaternion=(0.60, 0.80, 0.00, -0.00)
                insert_keys(10)
                o.location=(0.00, 0.08, 0.29)
                o.rotation_quaternion=(0.85, 0.53, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, -0.52, 0.21)
                o.rotation_quaternion=(0.98, -0.21, 0.00, 0.00)
                insert_keys(17)
                o.location=(0.00, -0.51, 0.06)
                o.rotation_quaternion=(1.02, -0.22, 0.00, 0.00)
                insert_keys(19)


            for o in Arm_R:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(1)
                    o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                    insert_keys(19)


            for o in Arm_L:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(1)
                    o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                    insert_keys(10)
                    o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                    insert_keys(19)


              
        #run_cycle_18_size_084_09() 
               

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
                run_cycle_18_size_default()    
                print("Length is","%.2f" % masterlength)


            # Size 0.1 to 0.3
            if masterlength > 0.1 and masterlength < 0.3:
                run_cycle_18_size_01_03() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.3 to 0.5
            if masterlength > 0.3 and masterlength < 0.5:
                run_cycle_18_size_03_05() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.5 to 0.6
            if masterlength > 0.5 and masterlength < 0.6:
                run_cycle_18_size_05_06() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.6 to 0.7
            if masterlength > 0.6 and masterlength < 0.7:
                run_cycle_18_size_06_07() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.7 to 0.8
            if masterlength > 0.7 and masterlength < 0.8:
                run_cycle_18_size_07_08() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.8 to 0.84
            if masterlength > 0.8 and masterlength < 0.84:
                run_cycle_18_size_08_084()    
                print("Length is","%.2f" % masterlength)


            # Size 0.84 to 0.9
            if masterlength > 0.84 and masterlength < 0.9:
                run_cycle_18_size_084_09()    
                print("Length is","%.2f" % masterlength)


            # Size Bigger then "Default"
            if masterlength > 1:
                run_cycle_18_size_default()    
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
        ob.animation_data.action.name = ob.name +'_Run_18' 
       

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
#   END   MULTIPLE LIMBS - 18 FRAMES  RUN CYCLE
# =====================================================






# =====================================================
#          MULTIPLE LIMBS - 22 FRAMES  RUN CYCLE
# =====================================================



# 22 FRAMES RUN CYCLE FOR RIGIFY HUMAN WITH MULTIPLE LIMBS. 
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_magic_run_multiple_limbs_22_ra(bpy.types.Operator):
    '''22 Frames Run Cycle For Rigify Human With Multiple Limbs.
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_magic_run_multiple_limbs_22_ra"
    bl_label = "ML-22"
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
        bpy.context.scene.frame_end = 22
         


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
#      DEFAULT SIZE   - 22 Frames Cycle
# =====================================================

         
        def run_cycle_22_size_default():
                               
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)

                

            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                      

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(1)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.14)
                insert_keys(12)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(23)


            for o in Torso:
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(1)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(3)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(5)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(12)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(14)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(16)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(19)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(23)


            for o in Foot_R:
                o.location=(0.00, 0.79, 0.57)
                o.rotation_quaternion=(0.50, 0.90, 0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, 0.12, 0.32)
                o.rotation_quaternion=(1.00, 1.40, 0.00, 0.00)
                insert_keys(3)
                o.location=(-0.00, -0.41, 0.35)
                o.rotation_quaternion=(1.00, 0.14, 0.00, 0.00)
                insert_keys(5)
                o.location=(-0.00, -0.76, 0.42)
                o.rotation_quaternion=(1.00, -0.18, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, -0.57, 0.12)
                o.rotation_quaternion=(0.96, -0.28, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(14)
                o.location=(0.00, 0.29, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(16)
                o.location=(0.00, 0.72, 0.44)
                o.rotation_quaternion=(0.53, 0.85, 0.00, 0.00)
                insert_keys(19)
                o.location=(0.00, 0.79, 0.57)
                o.rotation_quaternion=(0.50, 0.90, 0.00, 0.00)
                insert_keys(23)


            for o in Foot_L:
                o.location=(0.00, -0.57, 0.12)
                o.rotation_quaternion=(1.00, -0.29, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(0.00, 0.29, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(5)
                o.location=(0.00, 0.72, 0.44)
                o.rotation_quaternion=(1.00, 1.60, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, 0.79, 0.57)
                o.rotation_quaternion=(0.49, 0.87, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, 0.12, 0.32)
                o.rotation_quaternion=(0.58, 0.81, 0.00, -0.00)
                insert_keys(14)
                o.location=(-0.00, -0.41, 0.35)
                o.rotation_quaternion=(0.99, 0.14, 0.00, -0.00)
                insert_keys(16)
                o.location=(0.00, -0.76, 0.42)
                o.rotation_quaternion=(0.98, -0.18, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, -0.57, 0.12)
                o.rotation_quaternion=(1.00, -0.29, 0.00, -0.00)
                insert_keys(23)


            for o in Arm_R:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(1)
                    o.rotation_quaternion=(1.00, 0.05, -0.09, 0.30)
                    insert_keys(5)
                    o.rotation_quaternion=(0.95, -0.14, -0.10, 0.26)
                    insert_keys(12)
                    o.rotation_quaternion=(0.91, 0.35, -0.02, 0.21)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(23)


            for o in Arm_L:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(1)
                    o.rotation_quaternion=(0.87, 0.33, 0.02, -0.20)
                    insert_keys(5)
                    o.rotation_quaternion=(0.84, 0.50, -0.03, -0.21)
                    insert_keys(12)
                    o.rotation_quaternion=(0.95, 0.05, 0.09, -0.29)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(23)

                            
        #run_cycle_22_size_default() 
                            

# =====================================================
#   END   DEFAULT SIZE   - 22 Frames Cycle
# =====================================================
 
                  

                      
# =====================================================
#      SIZE  << 0.1 - 0.3 >>  22 Frames Cycle
# =====================================================

 
        def run_cycle_22_size_01_03():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                       
            
            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(1)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.14)
                insert_keys(12)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(23)
  
           
            for o in Torso: 
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(1)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(3)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(5)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(12)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(14)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(16)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(19)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(23)


            for o in Foot_R:
                o.location=(-0.00, 0.22, 0.16)
                o.rotation_quaternion=(0.50, 1.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.17, 0.10)
                o.rotation_quaternion=(1.00, 2.30, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, -0.17, 0.06)
                o.rotation_quaternion=(1.00, -0.16, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, -0.17, 0.07)
                o.rotation_quaternion=(1.00, -0.28, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, -0.16, 0.02)
                o.rotation_quaternion=(0.96, -0.28, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, -0.10, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(14)
                o.location=(-0.00, 0.16, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(16)
                o.location=(-0.00, 0.20, 0.15)
                o.rotation_quaternion=(0.53, 0.85, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, 0.22, 0.16)
                o.rotation_quaternion=(0.50, 1.00, 0.00, -0.00)
                insert_keys(23)

                       
            for o in Foot_L:
                o.location=(-0.00, -0.16, 0.02)
                o.rotation_quaternion=(1.00, -0.29, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, -0.10, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, 0.16, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, 0.20, 0.15)
                o.rotation_quaternion=(0.50, 0.80, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, 0.22, 0.16)
                o.rotation_quaternion=(0.45, 0.89, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, 0.17, 0.10)
                o.rotation_quaternion=(0.40, 0.92, 0.00, -0.00)
                insert_keys(14)
                o.location=(-0.00, -0.17, 0.06)
                o.rotation_quaternion=(0.99, -0.16, 0.00, -0.00)
                insert_keys(16)
                o.location=(-0.00, -0.17, 0.07)
                o.rotation_quaternion=(0.96, -0.27, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, -0.16, 0.02)
                o.rotation_quaternion=(1.00, -0.29, 0.00, -0.00)
                insert_keys(23)

      
            for o in Arm_R:
                if not exclude_arms:                 
                    o.rotation_quaternion=(1.00, 0.60, 0.14, -0.05)
                    insert_keys(1)
                    o.rotation_quaternion=(1.00, 0.05, -0.09, 0.10)
                    insert_keys(5)
                    o.rotation_quaternion=(0.97, -0.24, -0.10, -0.03)
                    insert_keys(12)
                    o.rotation_quaternion=(0.93, 0.35, -0.02, 0.11)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, 0.60, 0.14, -0.05)
                    insert_keys(23)

                
            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.25, 0.10, 0.03)
                    insert_keys(1)
                    o.rotation_quaternion=(0.87, 0.33, 0.02, -0.10)
                    insert_keys(5)
                    o.rotation_quaternion=(0.85, 0.51, -0.12, 0.04)
                    insert_keys(12)
                    o.rotation_quaternion=(0.99, 0.05, 0.09, -0.10)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, -0.25, 0.10, 0.03)
                    insert_keys(23)


        #run_cycle_22_size_01_03() 
               
                 
# =====================================================
#   END  SIZE  << 0.1 - 0.3 >>  22 Frames Cycle
# =====================================================
 
          
   



# =====================================================
#      SIZE  << 0.3 - 0.5 >>  22 Frames Cycle
# =====================================================

 
        def run_cycle_22_size_03_05():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                       

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(1)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.14)
                insert_keys(12)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(23)


            for o in Torso:
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(1)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(3)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(5)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(12)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(14)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(16)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(19)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(23)


            for o in Foot_R:
                o.location=(-0.00, 0.30, 0.26)
                o.rotation_quaternion=(0.50, 1.00, 0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, 0.19, 0.17)
                o.rotation_quaternion=(1.00, 1.60, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, -0.29, 0.12)
                o.rotation_quaternion=(1.00, -0.06, 0.00, 0.00)
                insert_keys(5)
                o.location=(0.00, -0.36, 0.12)
                o.rotation_quaternion=(1.00, -0.28, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, -0.28, 0.02)
                o.rotation_quaternion=(0.96, -0.28, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(14)
                o.location=(0.00, 0.10, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(16)
                o.location=(0.00, 0.28, 0.23)
                o.rotation_quaternion=(0.49, 0.87, -0.00, 0.00)
                insert_keys(19)
                o.location=(-0.00, 0.30, 0.26)
                o.rotation_quaternion=(0.50, 1.00, 0.00, 0.00)
                insert_keys(23)


            for o in Foot_L:
                o.location=(-0.00, -0.28, 0.02)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, 0.10, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(5)
                o.location=(-0.00, 0.28, 0.23)
                o.rotation_quaternion=(0.46, 0.82, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, 0.30, 0.26)
                o.rotation_quaternion=(0.45, 0.89, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, 0.19, 0.17)
                o.rotation_quaternion=(0.53, 0.85, 0.00, 0.00)
                insert_keys(14)
                o.location=(0.00, -0.29, 0.12)
                o.rotation_quaternion=(1.00, -0.06, 0.00, 0.00)
                insert_keys(16)
                o.location=(-0.00, -0.36, 0.12)
                o.rotation_quaternion=(0.96, -0.27, 0.00, 0.00)
                insert_keys(19)
                o.location=(-0.00, -0.28, 0.02)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(23)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(1)
                    o.rotation_quaternion=(1.00, 0.05, -0.09, 0.30)
                    insert_keys(5)
                    o.rotation_quaternion=(0.95, -0.14, -0.10, 0.26)
                    insert_keys(12)
                    o.rotation_quaternion=(0.91, 0.35, -0.02, 0.21)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(23)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(1)
                    o.rotation_quaternion=(0.87, 0.33, 0.02, -0.20)
                    insert_keys(5)
                    o.rotation_quaternion=(0.84, 0.50, -0.03, -0.21)
                    insert_keys(12)
                    o.rotation_quaternion=(0.95, 0.05, 0.09, -0.29)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(23)


        # run_cycle_22_size_03_05()

# =====================================================
#   END   SIZE  << 0.3 - 0.5 >>  22 Frames Cycle
# =====================================================





# =====================================================
#      SIZE  << 0.5 - 0.6 >>  22 Frames Cycle
# =====================================================

 
        def run_cycle_22_size_05_06():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(1)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.14)
                insert_keys(12)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(23)


            for o in Torso:
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(1)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(3)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(5)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(12)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(14)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(16)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(19)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(23)


            for o in Foot_R:
                o.location=(0.00, 0.46, 0.34)
                o.rotation_quaternion=(0.50, 1.00, 0.00, -0.00)
                insert_keys(1)
                o.location=(0.00, 0.22, 0.22)
                o.rotation_quaternion=(1.00, 1.60, 0.00, -0.00)
                insert_keys(3)
                o.location=(0.00, -0.29, 0.12)
                o.rotation_quaternion=(1.00, -0.06, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, -0.40, 0.14)
                o.rotation_quaternion=(1.00, -0.28, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, -0.30, 0.03)
                o.rotation_quaternion=(0.96, -0.28, 0.00, -0.00)
                insert_keys(12)
                o.location=(0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(14)
                o.location=(0.00, 0.16, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(16)
                o.location=(0.00, 0.41, 0.31)
                o.rotation_quaternion=(0.53, 0.85, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, 0.46, 0.34)
                o.rotation_quaternion=(0.50, 1.00, 0.00, -0.00)
                insert_keys(23)


            for o in Foot_L:
                o.location=(0.00, -0.30, 0.03)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, 0.16, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(5)
                o.location=(0.00, 0.41, 0.31)
                o.rotation_quaternion=(0.50, 0.80, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, 0.46, 0.34)
                o.rotation_quaternion=(0.45, 0.89, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, 0.22, 0.22)
                o.rotation_quaternion=(0.53, 0.85, 0.00, 0.00)
                insert_keys(14)
                o.location=(0.00, -0.29, 0.12)
                o.rotation_quaternion=(1.00, -0.06, 0.00, 0.00)
                insert_keys(16)
                o.location=(0.00, -0.40, 0.14)
                o.rotation_quaternion=(0.96, -0.27, 0.00, 0.00)
                insert_keys(19)
                o.location=(0.00, -0.30, 0.03)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(23)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(1)
                    o.rotation_quaternion=(1.00, 0.05, -0.09, 0.30)
                    insert_keys(5)
                    o.rotation_quaternion=(0.95, -0.14, -0.10, 0.26)
                    insert_keys(12)
                    o.rotation_quaternion=(0.91, 0.35, -0.02, 0.21)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(23)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(1)
                    o.rotation_quaternion=(0.87, 0.33, 0.02, -0.20)
                    insert_keys(5)
                    o.rotation_quaternion=(0.84, 0.50, -0.03, -0.21)
                    insert_keys(12)
                    o.rotation_quaternion=(0.95, 0.05, 0.09, -0.29)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(23)


        # run_cycle_22_size_05_06()        


# =====================================================
#    END  SIZE  << 0.5 - 0.6 >>  22 Frames Cycle
# =====================================================






# =====================================================
#      SIZE  << 0.6 - 0.7 >>  22 Frames Cycle
# =====================================================

 
        def run_cycle_22_size_06_07():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                                  

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(1)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.14)
                insert_keys(12)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(23)


            for o in Torso:
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(1)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(3)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(5)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(12)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(14)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(16)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(19)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(23)


            for o in Foot_R:
                o.location=(0.00, 0.39, 0.32)
                o.rotation_quaternion=(0.50, 1.00, 0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, 0.22, 0.22)
                o.rotation_quaternion=(1.00, 1.60, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, -0.38, 0.15)
                o.rotation_quaternion=(1.00, -0.07, -0.00, -0.00)
                insert_keys(5)
                o.location=(0.00, -0.48, 0.16)
                o.rotation_quaternion=(1.00, -0.28, 0.00, 0.00)
                insert_keys(8)
                o.location=(-0.00, -0.38, 0.04)
                o.rotation_quaternion=(0.96, -0.28, 0.00, 0.00)
                insert_keys(12)
                o.location=(-0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(14)
                o.location=(-0.00, 0.10, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(16)
                o.location=(0.00, 0.36, 0.26)
                o.rotation_quaternion=(0.63, 0.78, 0.00, -0.00)
                insert_keys(19)
                o.location=(0.00, 0.39, 0.32)
                o.rotation_quaternion=(0.50, 1.00, 0.00, 0.00)
                insert_keys(23)


            for o in Foot_L:
                o.location=(0.00, -0.38, 0.04)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(-0.00, 0.10, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(5)
                o.location=(-0.00, 0.36, 0.26)
                o.rotation_quaternion=(0.59, 0.73, -0.00, 0.00)
                insert_keys(8)
                o.location=(-0.00, 0.39, 0.32)
                o.rotation_quaternion=(0.45, 0.89, 0.00, 0.00)
                insert_keys(12)
                o.location=(-0.00, 0.22, 0.22)
                o.rotation_quaternion=(0.53, 0.85, 0.00, 0.00)
                insert_keys(14)
                o.location=(-0.00, -0.38, 0.15)
                o.rotation_quaternion=(1.00, -0.07, 0.00, 0.00)
                insert_keys(16)
                o.location=(-0.00, -0.48, 0.16)
                o.rotation_quaternion=(0.96, -0.27, 0.00, 0.00)
                insert_keys(19)
                o.location=(0.00, -0.38, 0.04)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(23)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(1)
                    o.rotation_quaternion=(1.00, 0.05, -0.09, 0.30)
                    insert_keys(5)
                    o.rotation_quaternion=(0.95, -0.14, -0.10, 0.26)
                    insert_keys(12)
                    o.rotation_quaternion=(0.91, 0.35, -0.02, 0.21)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(23)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(1)
                    o.rotation_quaternion=(0.87, 0.33, 0.02, -0.20)
                    insert_keys(5)
                    o.rotation_quaternion=(0.84, 0.50, -0.03, -0.21)
                    insert_keys(12)
                    o.rotation_quaternion=(0.95, 0.05, 0.09, -0.29)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(23)



        # run_cycle_22_size_06_07()


# =====================================================
#     END SIZE  << 0.6 - 0.7 >>  22 Frames Cycle
# =====================================================





# =====================================================
#      SIZE  << 0.7 - 0.8 >>  22 Frames Cycle
# =====================================================

 
        def run_cycle_22_size_07_08():
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(1)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.14)
                insert_keys(12)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(23)


            for o in Torso:
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(1)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(3)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(5)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(8)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(12)
                o.location=(-0.00, 0.00, -0.11)
                insert_keys(14)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(16)
                o.location=(-0.00, 0.00, -0.01)
                insert_keys(19)
                o.location=(-0.00, 0.00, -0.05)
                insert_keys(23)


            for o in Foot_R:
                o.location=(0.00, 0.55, 0.40)
                o.rotation_quaternion=(0.50, 1.00, 0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, 0.22, 0.22)
                o.rotation_quaternion=(1.00, 1.60, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, -0.35, 0.21)
                o.rotation_quaternion=(1.00, -0.07, 0.00, 0.00)
                insert_keys(5)
                o.location=(0.00, -0.53, 0.22)
                o.rotation_quaternion=(1.00, -0.28, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, -0.38, 0.04)
                o.rotation_quaternion=(0.96, -0.28, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(14)
                o.location=(0.00, 0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(16)
                o.location=(-0.00, 0.49, 0.35)
                o.rotation_quaternion=(0.57, 0.82, -0.00, 0.00)
                insert_keys(19)
                o.location=(0.00, 0.55, 0.40)
                o.rotation_quaternion=(0.50, 1.00, 0.00, 0.00)
                insert_keys(23)


            for o in Foot_L:
                o.location=(0.00, -0.38, 0.04)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, 0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(5)
                o.location=(0.00, 0.49, 0.35)
                o.rotation_quaternion=(0.54, 0.77, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, 0.55, 0.40)
                o.rotation_quaternion=(0.45, 0.89, 0.00, 0.00)
                insert_keys(12)
                o.location=(-0.00, 0.22, 0.22)
                o.rotation_quaternion=(0.53, 0.85, 0.00, 0.00)
                insert_keys(14)
                o.location=(-0.00, -0.35, 0.21)
                o.rotation_quaternion=(1.00, -0.07, 0.00, 0.00)
                insert_keys(16)
                o.location=(-0.00, -0.53, 0.22)
                o.rotation_quaternion=(0.96, -0.27, 0.00, 0.00)
                insert_keys(19)
                o.location=(0.00, -0.38, 0.04)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(23)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(1)
                    o.rotation_quaternion=(1.00, 0.05, -0.09, 0.30)
                    insert_keys(5)
                    o.rotation_quaternion=(0.95, -0.14, -0.10, 0.26)
                    insert_keys(12)
                    o.rotation_quaternion=(0.91, 0.35, -0.02, 0.21)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(23)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(1)
                    o.rotation_quaternion=(0.87, 0.33, 0.02, -0.20)
                    insert_keys(5)
                    o.rotation_quaternion=(0.84, 0.50, -0.03, -0.21)
                    insert_keys(12)
                    o.rotation_quaternion=(0.95, 0.05, 0.09, -0.29)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(23)

        # run_cycle_22_size_07_08()

# =====================================================
#     END SIZE  << 0.7 - 0.8 >>  22 Frames Cycle
# =====================================================

 
        





# =====================================================
#  SIZE  << 0.8 - 0.84 >>  22 Frames Cycle
# =====================================================
 
        
        def run_cycle_22_size_08_084(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                


            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(1)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.14)
                insert_keys(12)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(23)


            for o in Torso:
                o.location=(0.00, 0.00, -0.05)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.11)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.06)
                insert_keys(5)
                o.location=(0.00, 0.00, 0.01)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.05)
                insert_keys(12)
                o.location=(0.00, 0.00, -0.11)
                insert_keys(14)
                o.location=(0.00, 0.00, -0.05)
                insert_keys(16)
                o.location=(0.00, 0.00, 0.01)
                insert_keys(19)
                o.location=(0.00, 0.00, -0.05)
                insert_keys(23)


            for o in Foot_R:
                o.location=(-0.00, 0.69, 0.56)
                o.rotation_quaternion=(0.50, 0.80, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.29, 0.32)
                o.rotation_quaternion=(1.00, 1.10, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, -0.41, 0.27)
                o.rotation_quaternion=(1.00, 0.04, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, -0.58, 0.27)
                o.rotation_quaternion=(1.00, -0.28, 0.00, -0.00)
                insert_keys(8)
                o.location=(-0.00, -0.47, 0.10)
                o.rotation_quaternion=(0.96, -0.28, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(14)
                o.location=(-0.00, 0.11, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(16)
                o.location=(-0.00, 0.60, 0.50)
                o.rotation_quaternion=(0.64, 0.77, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, 0.69, 0.56)
                o.rotation_quaternion=(0.50, 0.80, 0.00, -0.00)
                insert_keys(23)


            for o in Foot_L:
                o.location=(0.00, -0.47, 0.10)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(1)
                o.location=(0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(0.00, 0.11, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(5)
                o.location=(0.00, 0.60, 0.50)
                o.rotation_quaternion=(1.00, 1.20, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, 0.69, 0.56)
                o.rotation_quaternion=(0.53, 0.85, 0.00, 0.00)
                insert_keys(12)
                o.location=(0.00, 0.29, 0.32)
                o.rotation_quaternion=(0.67, 0.74, 0.00, 0.00)
                insert_keys(14)
                o.location=(0.00, -0.41, 0.27)
                o.rotation_quaternion=(1.00, 0.04, 0.00, 0.00)
                insert_keys(16)
                o.location=(0.00, -0.58, 0.27)
                o.rotation_quaternion=(0.96, -0.27, 0.00, 0.00)
                insert_keys(19)
                o.location=(0.00, -0.47, 0.10)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(23)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(1)
                    o.rotation_quaternion=(1.00, 0.05, -0.09, 0.30)
                    insert_keys(5)
                    o.rotation_quaternion=(0.95, -0.14, -0.10, 0.26)
                    insert_keys(12)
                    o.rotation_quaternion=(0.91, 0.35, -0.02, 0.21)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(23)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(1)
                    o.rotation_quaternion=(0.87, 0.33, 0.02, -0.20)
                    insert_keys(5)
                    o.rotation_quaternion=(0.84, 0.50, -0.03, -0.21)
                    insert_keys(12)
                    o.rotation_quaternion=(0.95, 0.05, 0.09, -0.29)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(23)



        # run_cycle_22_size_08_084()


# =====================================================
#    END SIZE  << 0.8 - 0.84 >>  22 Frames Cycle
# =====================================================
 




# =====================================================
#  SIZE  << 0.84 - 0.9 >>  22 Frames Cycle
# =====================================================
 
        
        def run_cycle_22_size_084_09(): 
         
            
            # Insert Keys
            def insert_keys(frame):
                o.keyframe_insert(data_path = 'location', frame= frame)
                o.keyframe_insert(data_path = 'scale', frame= frame)
                o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
                       
            
            for o in Arm_Parent_R:
                o["IK_FK"] = float(1)
                    
            for o in Arm_Parent_L:
                o["IK_FK"] = float(1)
                    
                            

            for o in Chest:
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(1)
                o.rotation_quaternion=(0.99, 0.00, 0.00, -0.14)
                insert_keys(12)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                insert_keys(23)


            for o in Torso:
                o.location=(0.00, 0.00, -0.05)
                insert_keys(1)
                o.location=(0.00, 0.00, -0.11)
                insert_keys(3)
                o.location=(0.00, 0.00, -0.06)
                insert_keys(5)
                o.location=(0.00, 0.00, 0.01)
                insert_keys(8)
                o.location=(0.00, 0.00, -0.05)
                insert_keys(12)
                o.location=(0.00, 0.00, -0.11)
                insert_keys(14)
                o.location=(0.00, 0.00, -0.05)
                insert_keys(16)
                o.location=(0.00, 0.00, 0.01)
                insert_keys(19)
                o.location=(0.00, 0.00, -0.05)
                insert_keys(23)


            for o in Foot_R:
                o.location=(-0.00, 0.50, 0.48)
                o.rotation_quaternion=(0.50, 0.80, 0.00, -0.00)
                insert_keys(1)
                o.location=(-0.00, 0.29, 0.32)
                o.rotation_quaternion=(1.00, 1.10, 0.00, -0.00)
                insert_keys(3)
                o.location=(-0.00, -0.41, 0.27)
                o.rotation_quaternion=(1.00, 0.04, 0.00, -0.00)
                insert_keys(5)
                o.location=(-0.00, -0.61, 0.28)
                o.rotation_quaternion=(1.00, -0.28, 0.00, -0.00)
                insert_keys(8)
                o.location=(0.00, -0.53, 0.06)
                o.rotation_quaternion=(0.96, -0.28, 0.00, -0.00)
                insert_keys(12)
                o.location=(-0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(14)
                o.location=(-0.00, 0.11, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.00)
                insert_keys(16)
                o.location=(0.00, 0.49, 0.44)
                o.rotation_quaternion=(0.64, 0.77, 0.00, -0.00)
                insert_keys(19)
                o.location=(-0.00, 0.50, 0.48)
                o.rotation_quaternion=(0.50, 0.80, 0.00, -0.00)
                insert_keys(23)


            for o in Foot_L:
                o.location=(-0.00, -0.53, 0.06)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(1)
                o.location=(-0.00, -0.15, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(3)
                o.location=(-0.00, 0.11, 0.00)
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
                insert_keys(5)
                o.location=(-0.00, 0.49, 0.44)
                o.rotation_quaternion=(1.00, 1.20, 0.00, 0.00)
                insert_keys(8)
                o.location=(0.00, 0.50, 0.48)
                o.rotation_quaternion=(0.53, 0.85, 0.00, 0.00)
                insert_keys(12)
                o.location=(-0.00, 0.29, 0.32)
                o.rotation_quaternion=(0.67, 0.74, 0.00, 0.00)
                insert_keys(14)
                o.location=(-0.00, -0.41, 0.27)
                o.rotation_quaternion=(1.00, 0.04, 0.00, 0.00)
                insert_keys(16)
                o.location=(-0.00, -0.61, 0.28)
                o.rotation_quaternion=(0.96, -0.27, 0.00, 0.00)
                insert_keys(19)
                o.location=(-0.00, -0.53, 0.06)
                o.rotation_quaternion=(1.00, -0.29, 0.00, 0.00)
                insert_keys(23)


            for o in Arm_R:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(1)
                    o.rotation_quaternion=(1.00, 0.05, -0.09, 0.30)
                    insert_keys(5)
                    o.rotation_quaternion=(0.95, -0.14, -0.10, 0.26)
                    insert_keys(12)
                    o.rotation_quaternion=(0.91, 0.35, -0.02, 0.21)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                    insert_keys(23)


            for o in Arm_L:
                if not exclude_arms:
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(1)
                    o.rotation_quaternion=(0.87, 0.33, 0.02, -0.20)
                    insert_keys(5)
                    o.rotation_quaternion=(0.84, 0.50, -0.03, -0.21)
                    insert_keys(12)
                    o.rotation_quaternion=(0.95, 0.05, 0.09, -0.29)
                    insert_keys(16)
                    o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                    insert_keys(23)


        #run_cycle_22_size_084_09() 
               

# =====================================================
#    END SIZE  << 0.84 - 0.9 >>  22 Frames Cycle
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
                run_cycle_22_size_default()    
                print("Length is","%.2f" % masterlength)


            # Size 0.1 to 0.3
            elif masterlength > 0.1 and masterlength < 0.3:
                run_cycle_22_size_01_03() 
                print("Length is","%.2f" % masterlength)
            


            # Size 0.3 to 0.5
            elif masterlength > 0.3 and masterlength < 0.5:
                run_cycle_22_size_03_05() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.5 to 0.6
            elif masterlength > 0.5 and masterlength < 0.6:
                run_cycle_22_size_05_06() 
                print("Length is","%.2f" % masterlength)
            

            # Size 0.6 to 0.7
            elif masterlength > 0.6 and masterlength < 0.7:
                run_cycle_22_size_06_07() 
                print("Length is","%.2f" % masterlength)
   

            # Size 0.7 to 0.8
            elif masterlength > 0.7 and masterlength < 0.8:
                run_cycle_22_size_07_08() 
                print("Length is","%.2f" % masterlength)
   

             # Size 0.8 to 0.84
            elif masterlength > 0.8 and masterlength < 0.84:
                run_cycle_22_size_08_084()    
                print("Length is","%.2f" % masterlength)
           

            # Size 0.85 to 0.9
            elif masterlength > 0.84 and masterlength < 0.9:
                run_cycle_22_size_084_09()    
                print("Length is","%.2f" % masterlength)


            # Size Bigger then "Default"
            elif masterlength > 1:
                run_cycle_22_size_default()    
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
        ob.animation_data.action.name = ob.name +'_Run_22'  

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
#      END     MULTIPLE LIMBS - 22 FRAMES  RUN CYCLE
# =====================================================







classes = [ OBJECT_OT_rigify_magic_run_multiple_limbs_14_ra,
            OBJECT_OT_rigify_magic_run_multiple_limbs_18_ra,
            OBJECT_OT_rigify_magic_run_multiple_limbs_22_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()



 
  
