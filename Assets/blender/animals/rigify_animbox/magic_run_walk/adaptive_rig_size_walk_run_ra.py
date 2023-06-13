import bpy
import math
import fnmatch

from bpy.props import (BoolProperty)



#=============================================================
#                          Walk
#=============================================================

 
class OBJECT_OT_walk_adaptive_animbox_ra(bpy.types.Operator):
    '''Rigify Walk Cycle - Unlimited Rig Size'''
    bl_idname = "object.walk_adaptive_animbox_ra"
    bl_label = "Walk"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)
 


    def execute(self, context):

        scene = context.scene 

        # Ref
        exclude_arms = scene.animbox_ra_props.exclude_arms_from_anim

        # Refs
        walk_18 = scene.animbox_ra_props.walk_cycle_18_frames_animbox_ra 
        walk_24 = scene.animbox_ra_props.walk_cycle_24_frames_animbox_ra 
        

        C = bpy.context  

        bones = C.object.data.bones
        pose_bones = C.object.pose.bones          
               
        sel_bones = bpy.context.selected_pose_bones
        sel_bone_name = sel_bones[0].name                 
               
        #-------------------------------------------

        # TOTAL RESET

        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        #bpy.ops.pose.transforms_clear()
        bpy.ops.anim.keyframe_clear_v3d() 
        bpy.ops.pose.select_all(action = 'DESELECT')
        bpy.ops.screen.frame_jump(end=False)
            
           
        # FRAME RANGE ----------------------------------------------------------

        
        if walk_18:
            C.scene.frame_start = 1
            C.scene.frame_end = 18
 
        if walk_24:
            C.scene.frame_start = 1
            C.scene.frame_end = 24

        if not walk_18 and not walk_24:
            # setting for 32 frame cycle
            C.scene.frame_start = 1
            C.scene.frame_end = 32                            
            
        start_fr = C.scene.frame_start
        end_fr = C.scene.frame_end
        mid_frame = int(C.scene.frame_start + C.scene.frame_end / 2)
        
        
        # -----------------------------------------------------------------------

        # NAMES -----------------------------------------------------------------

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
            
        # -----------------------------------------------------------------------            
            
            
            
        # Switch to FK ----------------------------------------------------------   
        for o in Arm_Parent_R:
            o["IK_FK"] = float(1)
                
        for o in Arm_Parent_L:
            o["IK_FK"] = float(1)            
                    

        #------------------------------------------------------------------------

        # Measuring Leg Length ( Left )
        def get_left_Leg_length_rigify(bonename_1, bonename_2, bonename_3, bonename_4):
               
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
                    
          
            print("Length is","%.2f" % masterlength)
            
            return masterlength

        #------------------------------------------------------------------------


        leg_length = get_left_Leg_length_rigify('DEF-shin.L','DEF-shin.L.001','DEF-thigh.L','DEF-thigh.L.001')
          
        num = (leg_length - (leg_length / 1.15 ))

        # Insert Keys
        def insert_keys(obj, frame):
            obj.keyframe_insert(data_path = 'location', frame= frame)
            obj.keyframe_insert(data_path = 'scale', frame= frame)
            obj.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
            obj.keyframe_insert(data_path = 'rotation_euler', frame= frame)

        def insert_rotation_keys(obj, frame):          
            obj.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
            obj.keyframe_insert(data_path = 'rotation_euler', frame= frame)
            
     
     
        #--------------------------- Arms Chest -------------------------------
        
        def arms_chest():
            
      
            # Chest --------------------------------------------------
            for o in Chest:
                # First Pose ------------
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)
                insert_rotation_keys(o, start_fr)
                
                # Middle Pose -----------
                o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
                insert_rotation_keys(o, mid_frame)
                    
                    
                # End Pose -------------    
                o.rotation_quaternion=(1.00, 0.00, 0.00, 0.10)     
                insert_rotation_keys(o, end_fr + 1)


            # Arm R --------------------------------------------------
            
            for o in Arm_R:
               if not exclude_arms:

                    # First Pose
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_rotation_keys(o, start_fr)
                    
                    # Middle Pose
                    o.rotation_quaternion=(0.94, -0.09, 0.00, 0.33)
                    insert_rotation_keys(o, mid_frame)                 
                         
                    # End Pose
                    o.rotation_quaternion=(1.00, 0.40, 0.00, 0.30)
                    insert_rotation_keys(o, end_fr + 1)



            # Arm R --------------------------------------------------
            
            for o in Arm_L:
               if not exclude_arms:

                    # First Pose
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_rotation_keys(o, start_fr)
                    
                    # Middle Pose
                    o.rotation_quaternion=(0.89, 0.36, 0.00, -0.27)
                    insert_rotation_keys(o, mid_frame) 
                                               
                    # End Pose
                    o.rotation_quaternion=(1.00, -0.10, 0.00, -0.35)
                    insert_rotation_keys(o, end_fr + 1)
        
                    
        #----------------------------------------------------------------------            
            
        def torso(): 

 
            def torso_inbetween_first_half_keys():
                
                if walk_18: 
                    insert_keys(o, start_fr + 4)  
                
                if walk_24: 
                    insert_keys(o, start_fr + 6) 
   
                if not walk_18 and not walk_24:
                    # setting for 32 frame cycle
                    insert_keys(o, start_fr + 8) 

               
            def torso_inbetween_second_half_keys():
                
                if walk_18: 
                    insert_keys(o, mid_frame + 4)  
                                      
                if walk_24: 
                    insert_keys(o, mid_frame + 6)                     
             
                
                if not walk_18 and not walk_24:
                    # setting for 32 frame cycle      
                    insert_keys(o, mid_frame + 8)                                  
                            
            
            # First - Middle - Last Pose
            for o in Torso:   
                o.location.z -= (num / 1.3)
                insert_keys(o, 1)
                insert_keys(o, mid_frame)
                insert_keys(o, end_fr + 1)            
            
            
            # 2 Pose / 4 Pose
            for o in Torso:
                o.location.z += (num / 1.6)
                torso_inbetween_first_half_keys()
                torso_inbetween_second_half_keys()

            # X Location => 2 and 4 Pose
            for o in Torso:   
                o.location.x += (num / 7)
                torso_inbetween_first_half_keys()
                o.location.x -= ((num / 7)  * 2)
                torso_inbetween_second_half_keys()           
            
        
        # Feet ---------------------------------------------------
        def left_foot():
            
 
            # First - Last Pose -------------------------------
            for o in Foot_L:
                o.location.y -= (leg_length / (math.pi - 0.9))
                o.rotation_quaternion[1] = -0.2
            
                insert_keys(o, 1)
                insert_keys(o, end_fr + 1)


            # Foot Down ----------------------------------------
            for o in Foot_L:
                o.rotation_quaternion[1] = 0.0
                
                if walk_18: 
                    insert_rotation_keys(o, start_fr + 2)    
                if walk_24: 
                    insert_rotation_keys(o, start_fr + 2)                                   
                      
                if not walk_18 and not walk_24: 
                    # setting for 32 frame cycle
                    insert_rotation_keys(o, start_fr + 3)            
                                
                                
            # Middle Pose ---------------------------------------
            for o in Foot_L:
                o.location.y += ((leg_length / (math.pi - 1)) * 2)
                o.rotation_quaternion[1] = 0.0
                insert_keys(o, mid_frame)
                 
                    
            # Passing Pose --------------------------------------
            for o in Foot_L:
                o.location.y = 0.0
                o.location.z += (num / 1.6)
                o.rotation_quaternion[1] = 0.2
                
                if walk_18: 
                    insert_keys(o, mid_frame + 4)     
                if walk_24: 
                    insert_keys(o, mid_frame + 6)                                   

                if not walk_18 and not walk_24: 
                    # setting for 32 frame cycle
                    insert_keys(o, mid_frame + 7)                  
               
                       
           
        # Right Foot ----------------------------------------------
        def right_foot():
            
            # First - Last Pose
            for o in Foot_R:
                o.location.y += (leg_length / (math.pi - 1.1))
                insert_keys(o, 1)
                insert_keys(o, end_fr + 1)
            
            # Foot Down --------------------------------------          
            for o in Foot_R:
                o.rotation_quaternion[1] = 0.0
                
                if walk_18: 
                    insert_rotation_keys(o, mid_frame + 2)    
                if walk_24: 
                    insert_rotation_keys(o, mid_frame + 2)                                   
   
                if not walk_18 and not walk_24: 
                    # setting for 32 frame cycle
                    insert_rotation_keys(o, mid_frame + 3)                   
                
                
                                      
            # Middle Pose --------------------------------------
            for o in Foot_R:
                o.location.y -= ((leg_length / (math.pi - 1)) * 2)
                o.rotation_quaternion[1] = -0.2
                insert_keys(o, mid_frame)                
                
                       
                       
            # Passing Pose --------------------------------------
            for o in Foot_R:
                o.location.y = 0.0
                o.location.z += (num / 1.6)
                o.rotation_quaternion[1] = 0.2
            

                if walk_18: 
                    insert_keys(o, start_fr + 4)     
                if walk_24: 
                    insert_keys(o, start_fr + 6)                                   
       
                if not walk_18 and not walk_24: 
                    # setting for 32 frame cycle
                    insert_keys(o, start_fr + 7)  
           

           
        def heel_r():
                       
            # First Last Pose
            for o in Heel_R:
                o.rotation_euler[0] = 0.5
                insert_rotation_keys(o, 1)
                insert_rotation_keys(o, end_fr + 1)
                
                
            # inbetween   
            for o in Heel_R:
                o.rotation_euler[0] = 0.0
              
   
                if walk_18: 
                    insert_rotation_keys(o, start_fr + 4)    
                    insert_rotation_keys(o, mid_frame + 4) 
                      
                if walk_24: 
                    insert_rotation_keys(o, start_fr + 5)    
                    insert_rotation_keys(o, mid_frame + 5)  
                                                      
                      
                if not walk_18 and not walk_24: 
                    # setting for 32 frame cycle
                    insert_rotation_keys(o, start_fr + 7)    
                    insert_rotation_keys(o, mid_frame + 7)    
                
                
        def heel_l():
            
            # First Last Pose
            for o in Heel_L:
                o.rotation_euler[0] = 0.0
                insert_rotation_keys(o, 1)
                insert_rotation_keys(o, end_fr + 1)
            
            
            # inbetween 
            for o in Heel_L:
                o.rotation_euler[0] = 0.0

        
                if walk_18: 
                    insert_rotation_keys(o, start_fr + 4)    
                    insert_rotation_keys(o, mid_frame + 4) 
                      
                if walk_24: 
                    insert_rotation_keys(o, start_fr + 5)    
                    insert_rotation_keys(o, mid_frame + 5)  
   
                      
                if not walk_18 and not walk_24: 
                    # setting for 32 frame cycle
                    insert_rotation_keys(o, start_fr + 7)    
                    insert_rotation_keys(o, mid_frame + 7)          
        
        
      
            # Middle Pose
            for o in Heel_L:
                o.rotation_euler[0] = 0.5
                insert_rotation_keys(o, mid_frame) 



        torso()
        left_foot()           
        right_foot()
        heel_r()
        heel_l() 
        arms_chest()
 
 

        #---------------------------------------------
        
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
        
        
        #---------------------------------------------
        # Action Name
        ob = bpy.context.object
        
        if walk_18:
            ob.animation_data.action.name = ob.name + '_Walk_18' 

        if walk_24:
            ob.animation_data.action.name = ob.name + '_Walk_24' 


        if not walk_18 and not walk_24:
            # setting for 32 frame cycle
            ob.animation_data.action.name = ob.name + '_Walk_32'


        # JUMP TO START AND PLAY ANIMATION
        bpy.ops.screen.frame_jump(end=False)      
        bpy.ops.screen.animation_play()


        # Select bones ----------------------------------------------------------
        
        for b in pose_bones:
            if b.name.startswith(sel_bone_name):
                b.bone.select = 1
                bpy.context.object.data.bones.active = b.bone 
            

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




#=============================================================
#                       End  Walk
#=============================================================

#=============================================================
#                          Run
#=============================================================

 
class OBJECT_OT_run_adaptive_animbox_ra(bpy.types.Operator):
    '''Rigify Run Cycle - Unlimited Rig Size'''
    bl_idname = "object.run_adaptive_animbox_ra"
    bl_label = "Run"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    def execute(self, context):
        scene = context.scene 

        # Ref
        exclude_arms = scene.animbox_ra_props.exclude_arms_from_anim        
  
        # Refs
        run_14 = scene.animbox_ra_props.run_cycle_14_frames_animbox_ra 
        run_18 = scene.animbox_ra_props.run_cycle_18_frames_animbox_ra 
 

        C = bpy.context  

        bones = C.object.data.bones
        pose_bones = C.object.pose.bones          
               
        sel_bones = bpy.context.selected_pose_bones
        sel_bone_name = sel_bones[0].name                  
               
        #-------------------------------------------

        # TOTAL RESET

        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        #bpy.ops.pose.transforms_clear()
        bpy.ops.anim.keyframe_clear_v3d() 
        bpy.ops.pose.select_all(action = 'DESELECT')
        bpy.ops.screen.frame_jump(end=False)
            
           
        # FRAME RANGE ----------------------------------------------------------

        if run_14:
            C.scene.frame_start = 1
            C.scene.frame_end = 14
 
        if run_18:
            C.scene.frame_start = 1
            C.scene.frame_end = 18

            
        if not run_14 and not run_18:
            # setting for 22 frame cycle
            C.scene.frame_start = 1
            C.scene.frame_end = 22                            
            
        start_fr = C.scene.frame_start
        end_fr = C.scene.frame_end
        mid_frame = int(C.scene.frame_start + C.scene.frame_end / 2)
        
        
        # -----------------------------------------------------------------------

        # NAMES -----------------------------------------------------------------

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
            
        # NAMES -----------------------------------------------------------------            
            
            
            
        # Switch to FK ----------------------------------------------------------   
        for o in Arm_Parent_R:
            o["IK_FK"] = float(1)
                
        for o in Arm_Parent_L:
            o["IK_FK"] = float(1)            
                    

        #------------------------------------------------------------------------

        # Measuring Leg Length ( Left )
        def get_left_Leg_length_rigify(bonename_1, bonename_2, bonename_3, bonename_4):
               
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
                    
          
            print("Length is","%.2f" % masterlength)
            
            return masterlength

        #------------------------------------------------------------------------


        leg_length = get_left_Leg_length_rigify('DEF-shin.L','DEF-shin.L.001','DEF-thigh.L','DEF-thigh.L.001')
          
        num = (leg_length - (leg_length / 1.15 ))

        # Insert Keys
        def insert_keys(obj, frame):
            obj.keyframe_insert(data_path = 'location', frame= frame)
            obj.keyframe_insert(data_path = 'scale', frame= frame)
            obj.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
            obj.keyframe_insert(data_path = 'rotation_euler', frame= frame)

        def insert_rotation_keys(obj, frame):          
            obj.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
            obj.keyframe_insert(data_path = 'rotation_euler', frame= frame)
            
     

        #----------------------------------------------------------
        
        def chest_arms():


            def chest(): 
                for o in Chest:
                    # First Pose ------------
                    o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)
                    insert_rotation_keys(o, start_fr)
                    
                    # Middle Pose -----------
                    o.rotation_quaternion=(1.00, 0.00, 0.00, -0.14)
                    insert_rotation_keys(o, mid_frame)
                        
                        
                    # End Pose -------------    
                    o.rotation_quaternion=(1.00, 0.00, 0.00, 0.14)    
                    insert_rotation_keys(o, end_fr + 1)

            chest()

    #---------------------------- Arms ----------------------------
                
            def arms():

                for o in Arm_R:
                    if not exclude_arms:                
                        o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                        insert_keys(o, start_fr)
                        o.rotation_quaternion=(0.92, -0.25, -0.11, 0.27)
                        insert_keys(o, mid_frame)
                        o.rotation_quaternion=(1.00, 0.37, 0.25, 0.41)
                        insert_keys(o, end_fr + 1)


                for o in Arm_L:
                    if not exclude_arms:                
                        o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                        insert_keys(o, start_fr)
                        o.rotation_quaternion=(0.86, 0.32, -0.21, -0.35)
                        insert_keys(o, mid_frame)
                        o.rotation_quaternion=(1.00, -0.27, 0.12, -0.29)
                        insert_keys(o, end_fr + 1)



            def arms_extended():
                for o in Arm_R:
                    if not exclude_arms:                 
                        o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                        insert_rotation_keys(o, start_fr)
                        o.rotation_quaternion=(1.00, 0.05, -0.09, 0.30)
                        insert_rotation_keys(o, start_fr + 4)
                        o.rotation_quaternion=(0.95, -0.14, -0.10, 0.26)
                        insert_rotation_keys(o, mid_frame)
                        o.rotation_quaternion=(0.91, 0.35, -0.02, 0.21)
                        insert_rotation_keys(o, mid_frame + 4)
                        o.rotation_quaternion=(1.00, 0.60, 0.04, 0.25)
                        insert_rotation_keys(o, end_fr + 1)


                for o in Arm_L:
                    if not exclude_arms:                 
                        o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                        insert_rotation_keys(o, start_fr)
                        o.rotation_quaternion=(0.87, 0.33, 0.02, -0.20)
                        insert_rotation_keys(o, start_fr + 4)
                        o.rotation_quaternion=(0.84, 0.50, -0.03, -0.21)
                        insert_rotation_keys(o, mid_frame)
                        o.rotation_quaternion=(0.95, 0.05, 0.09, -0.29)
                        insert_rotation_keys(o, mid_frame + 4)
                        o.rotation_quaternion=(1.00, -0.15, 0.10, -0.27)
                        insert_rotation_keys(o, end_fr + 1)

        

            if run_14:
                arms()

            if run_18:
                arms()

            if not run_14 and not run_18:
                # setting for 22 frame cycle
                arms_extended()



#----------------------------------------------------------------------            
            
        def torso(): 


            # First / Mid / Last Pose
            for o in Torso:
                
                o.location.z -= (num / (math.pi - 0.67))
                insert_keys(o, 1)
                insert_keys(o, mid_frame)
                insert_keys(o, end_fr + 1)

            # Second Pose 
            for o in Torso:  
                o.location.z -= (num / (math.pi))  
                insert_keys(o, start_fr + 2)
                insert_keys(o, mid_frame + 2)


            # 3 Pose 
            for o in Torso:  
                o.location.z += (num / (math.pi / 2))  

                if run_14:
                    insert_keys(o, start_fr + 5)
                    insert_keys(o, mid_frame + 5)

                if run_18:
                    insert_keys(o, start_fr + 6)
                    insert_keys(o, mid_frame + 6)


                if not run_14 and not run_18:
                    
                    # setting for 22 frame cycle
                    insert_keys(o, start_fr + 7)
                    insert_keys(o, mid_frame + 7)

 

#------------------------------- Legs 14 -----------------------------  


        def foot_L_14_18():
            
            # First / Last Pose
            for o in Foot_L:
                o.location.y -= (leg_length / (math.pi - 1.7))
                o.location.z += (num / (math.pi / 5.2))
         
                o.rotation_quaternion[1] = -0.3
                insert_keys(o, 1)
                insert_keys(o, end_fr + 1) 

                
            # Mid Pose
            for o in Foot_L:
                o.location.y = 0.0
                o.location.z = 0.0        
                o.location.y += (leg_length / (math.pi - 1.9))
                o.location.z += (num *  (math.pi * 1.5))
                o.rotation_quaternion[1] = 0.0
                o.rotation_quaternion[1] += 1.2
                insert_keys(o, mid_frame)
               
                
            # Second Frame ( First Half )  
            for o in Foot_L:                     
                o.location.x = 0.0
                o.location.z = 0.0  
                o.location.y = (-num * 2)
                o.rotation_quaternion[1] = 0.0
                insert_keys(o, start_fr + 2)
                
                
            # Second Frame ( Second Half )
            for o in Foot_L:
                o.location.y = 0.0
                o.location.z = 0.0  
                o.location.y += (num * 3)  
                o.location.z += (num * (math.pi ))                
                o.rotation_quaternion[1] = 0.0
                o.rotation_quaternion[1] += 1.3
                insert_keys(o, mid_frame + 2)                


            # 3 Frame  ( Second Half )
            for o in Foot_L:
                       
                o.rotation_quaternion[1] = 0.0
                if run_14:
                    insert_rotation_keys(o, mid_frame + 5)
                if run_18:
                    insert_rotation_keys(o, mid_frame + 7)                    
         
         
        def foot_R_14_18():
            
            # First /  Last Pose
            for o in Foot_R:
                o.location.y += (leg_length / (math.pi - 1.9))
                o.location.z += (num *  (math.pi * 1.5))
                o.rotation_quaternion[1] += 1.2
                insert_keys(o, 1)
                insert_keys(o, end_fr + 1) 


            # Second Frame   ( First Half )
            for o in Foot_R:
                o.location.y = 0.0
                o.location.z = 0.0  
                o.location.y += (num * 3)  
                o.location.z += (num * (math.pi ))                
                o.rotation_quaternion[1] = 0.0
                o.rotation_quaternion[1] += 1.3
                insert_keys(o, start_fr + 2)


            # 3 Frame   ( First Half )
            for o in Foot_R:
                       
                o.rotation_quaternion[1] = 0.0
                if run_14:                
                    insert_rotation_keys(o, start_fr + 5)
                if run_18:
                    insert_rotation_keys(o, start_fr + 7)    

            # Mid Pose
            for o in Foot_R:
                o.location.y = 0.0
                o.location.z = 0.0
                o.location.y -= (leg_length / (math.pi - 1.7))
                o.location.z += (num /  (math.pi  / 5.2))
                o.rotation_quaternion[1] = -0.3
                insert_keys(o, mid_frame) 


            # Second Frame  ( Second Half )
            for o in Foot_R:                     
                o.location.x = 0.0
                o.location.z = 0.0  
                o.location.y = (-num * 2)
                o.rotation_quaternion[1] = 0.0
                insert_keys(o, mid_frame + 2)

#------------------------------- Legs 14 ----------------------------- 





#------------------------------- Legs 22 -----------------------------  
        def foot_L_22():
            
            # First / Last Pose
            for o in Foot_L:
                o.location.y -= (leg_length / (math.pi - 1.7))
                o.location.z += (num / (math.pi / 5.2))
         
                o.rotation_quaternion[1] = -0.3
                insert_keys(o, 1)
                insert_keys(o, end_fr + 1)        
                
            # Mid Pose
            for o in Foot_L:
                o.location.y = 0.0
                o.location.z = 0.0        
                o.location.y += (leg_length / (math.pi - 1.9))
                o.location.z += (num *  (math.pi * 1.5))
                o.rotation_quaternion[1] = 0.0
                o.rotation_quaternion[1] += 1.2
                insert_keys(o, mid_frame)
               
                
            # Second Frame ( First Half )  
            for o in Foot_L:                     
                o.location.x = 0.0
                o.location.z = 0.0  
                o.location.y = (-num * 2)
                o.rotation_quaternion[1] = 0.0
                insert_keys(o, start_fr + 2)
                
                
            # 3 Frame ( First Half )   
            for o in Foot_L:                      
                o.location.y = (num * 2)
                o.rotation_quaternion[1] = 0.0
                insert_keys(o, start_fr + 4)
                        

            # 4 Frame  ( First Half )   
            for o in Foot_L:                     
                o.location.y += (leg_length / (math.pi - 0.8))
                o.location.z += (num *  (math.pi))
                o.rotation_quaternion[1] += 0.9
                insert_keys(o, start_fr + 7)

   
            # Second Frame   ( Second Half )
            for o in Foot_L:
                o.location.y = 0.0
                o.location.z = 0.0  
                o.location.y += (num * 3)  
                o.location.z += (num * (math.pi ))                
                o.rotation_quaternion[1] = 0.0
                o.rotation_quaternion[1] += 1.3
                insert_keys(o, mid_frame + 2)                


            # 3 Frame   ( Second Half )
            for o in Foot_L:
                       
                o.rotation_quaternion[1] = 0.0
                insert_rotation_keys(o, mid_frame + 8)
         
         
         
        def foot_R_22():
            
            # First /  Last Pose
            for o in Foot_R:
                o.location.y += (leg_length / (math.pi - 1.9))
                o.location.z += (num *  (math.pi * 1.5))
                o.rotation_quaternion[1] += 1.2
                insert_keys(o, 1)
                insert_keys(o, end_fr + 1) 


            # Second Frame   ( First Half )
            for o in Foot_R:
                o.location.y = 0.0
                o.location.z = 0.0  
                o.location.y += (num * 3)  
                o.location.z += (num * (math.pi ))                
                o.rotation_quaternion[1] = 0.0
                o.rotation_quaternion[1] += 1.3
                insert_keys(o, start_fr + 2)


            # 3 Frame   ( First Half )
            for o in Foot_R:
                       
                o.rotation_quaternion[1] = 0.0
                insert_rotation_keys(o, start_fr + 8)


            # Mid Pose
            for o in Foot_R:
                o.location.y = 0.0
                o.location.z = 0.0
                o.location.y -= (leg_length / (math.pi - 1.7))
                o.location.z += (num /  (math.pi  / 5.2))
                o.rotation_quaternion[1] = -0.3
                insert_keys(o, mid_frame) 


            # Second Frame   ( Second Half )
            for o in Foot_R:                     
                o.location.x = 0.0
                o.location.z = 0.0  
                o.location.y = (-num * 2)
                o.rotation_quaternion[1] = 0.0
                insert_keys(o, mid_frame + 2)


            # 3 Frame   ( Second Half )
            for o in Foot_R:                     
                o.location.y = (num * 2)
                o.rotation_quaternion[1] = 0.0
                insert_keys(o, mid_frame + 4)


            # 4 Frame  ( Second Half )  
            for o in Foot_R:                     
                o.location.y += (leg_length / (math.pi - 0.8))
                o.location.z += (num *  (math.pi))
                o.rotation_quaternion[1] += 0.9
                insert_keys(o, mid_frame + 7)
                
#------------------------------- Legs 22 -----------------------------         

        chest_arms()
        torso()


        if run_14:
            foot_L_14_18()
            foot_R_14_18()

        if run_18:
            foot_L_14_18()
            foot_R_14_18()

        if not run_14 and not run_18:
            # setting for 22 frame cycle
            foot_L_22()
            foot_R_22()


        #---------------------------------------------
        
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
        
        
        #---------------------------------------------
        # Action Name
        ob = bpy.context.object
        
        if run_14:
            ob.animation_data.action.name = ob.name + '_run_14' 

        if run_18:
            ob.animation_data.action.name = ob.name + '_run_18' 


        if not run_14 and not run_18:
            # setting for 22 frame cycle
            ob.animation_data.action.name = ob.name + '_run_22'


        # JUMP TO START AND PLAY ANIMATION
        bpy.ops.screen.frame_jump(end=False)
        bpy.ops.screen.animation_play()


        # Select bones ----------------------------------------------------------
        
        for b in pose_bones:
            if b.name.startswith(sel_bone_name):
                b.bone.select = 1
                bpy.context.object.data.bones.active = b.bone 
            

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




#=============================================================
#                       End  Run
#=============================================================





 


classes = [ OBJECT_OT_walk_adaptive_animbox_ra,
            OBJECT_OT_run_adaptive_animbox_ra,

            
          ]
 
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        


 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

 
 
if __name__ == "__main__":
    register() 