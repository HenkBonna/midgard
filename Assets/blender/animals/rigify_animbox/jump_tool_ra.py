import bpy


# RIGIFY_JUMPER 




# =====================================================
#                    JUMPER JUMPER JUMPER
# =====================================================


# =====================================================
#                    JUMPER FOR RIGIFY HUMAN
# =====================================================



# Start Jump  with additional keys
class OBJECT_OT_rigify_jumper_start(bpy.types.Operator):
    '''This will Set Initial Keys before Take-Off -\n- and Teleport to Cursor'''
    bl_idname = "object.rigify_jumper_start"
    bl_label = "Start"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')



    def execute(self, context):


        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name


    	# To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True


        # Setting arms to FK
        bpy.context.object.pose.bones["upper_arm_parent.L"]["IK_FK"] = float(1)
        bpy.context.object.pose.bones["upper_arm_parent.R"]["IK_FK"] = float(1)

         
        # =====================================================
        #  	INSERT KEY IK_FK FOR ARMS
        # =====================================================

        ob = bpy.data.objects[ob.name]
        ob.data.bones["upper_arm_parent.L"].select = True
        ob.data.bones["upper_arm_parent.R"].select = True

        ikfk_left_arm = ob.pose.bones["upper_arm_parent.L"]
        ikfk_right_arm = ob.pose.bones["upper_arm_parent.R"]

        ikfk_left_arm.keyframe_insert(data_path= '["IK_FK"]')
        ikfk_right_arm.keyframe_insert(data_path= '["IK_FK"]')


        # Set Inicial Keys to Full Rig
        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        bpy.ops.pose.select_all(action = 'DESELECT')


        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
        
        
        # Select Bones (Controls) to move
        bpy.data.objects[ob.name].data.bones["torso"].select = True
        bpy.data.objects[ob.name].data.bones["hand_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["hand_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["foot_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_heel_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["foot_heel_ik.R"].select = True
        
        # Set Active Pose Bone
        bpy.context.object.data.bones.active = bpy.data.objects[ob.name].data.bones["torso"] 

        # 1: "NEUTRAL" POSE     
        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        
        # Move 4 Frames Forward 
        bpy.context.scene.frame_current += 7


        # 2: SQUASH POSE
        # Lower Position of a Torso

        torso_position = bpy.context.object.pose.bones["torso"]
        torso_position.location[2] -= 0.15

        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        
        # Move 3 Frames Forward 
        bpy.context.scene.frame_current += 3


        # 3: STRETCH POSE  

        torso_position = bpy.context.object.pose.bones["torso"]
        torso_position.location[2] += 0.15

    
         # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        
        # Move 4 Frames Forward 
        bpy.context.scene.frame_current += 6              


        # Reset "X" Location of 3D Cursor 
        bpy.context.scene.cursor.location[0] = 0

        
        # Jump to cursor
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)

      
        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        
     
        return {'FINISHED'}





# Jumper for Human Meta-Rig
class OBJECT_OT_rigify_jumper(bpy.types.Operator):
    '''Just Teleport to Cursor'''
    bl_idname = "object.rigify_jumper"
    bl_label = "Jump"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):

        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name


    	# To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True


        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'


        # Arms to FK
        bpy.context.object.pose.bones["upper_arm_parent.L"]["IK_FK"] = float(1)
        bpy.context.object.pose.bones["upper_arm_parent.R"]["IK_FK"] = float(1)

       
        # =====================================================
        #  	INSERT KEY IK_FK FOR ARMS
        # =====================================================

        ob = bpy.data.objects[ob.name]
        ob.data.bones["upper_arm_parent.L"].select = True
        ob.data.bones["upper_arm_parent.R"].select = True

        ikfk_left_arm = ob.pose.bones["upper_arm_parent.L"]
        ikfk_right_arm = ob.pose.bones["upper_arm_parent.R"]

        ikfk_left_arm.keyframe_insert(data_path= '["IK_FK"]')
        ikfk_right_arm.keyframe_insert(data_path= '["IK_FK"]')


        
        bpy.ops.pose.select_all(action = 'DESELECT')
        
        # Select Bones (Controls) to move
        bpy.data.objects[ob.name].data.bones["torso"].select = True
        bpy.data.objects[ob.name].data.bones["hand_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["hand_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["foot_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_heel_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["foot_heel_ik.R"].select = True
        
        # Set Active Pose Bone
        bpy.context.object.data.bones.active = bpy.data.objects[ob.name].data.bones["torso"] 
        

        # Reset "X" Location of 3D Cursor 
        # bpy.context.scene.cursor.location[0] = 0

      
        # Jump to cursor
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
        
        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        
  
        return {'FINISHED'}





# PUT DOWN ON THE GROUND - with additional keys
class OBJECT_OT_rigify_jumper_put_down(bpy.types.Operator):
    '''This will Teleport to Cursor, Put on the ground -\n- and Set Final Keys.'''
    bl_idname = "object.rigify_jumper_put_down"
    bl_label = "End"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):


        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name


    	# To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
      
        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'

         # Setting arms to FK
        bpy.context.object.pose.bones["upper_arm_parent.L"]["IK_FK"] = float(1)
        bpy.context.object.pose.bones["upper_arm_parent.R"]["IK_FK"] = float(1)

         
        # =====================================================
        #  	INSERT KEY IK_FK FOR ARMS
        # =====================================================

        ob = bpy.data.objects[ob.name]
        ob.data.bones["upper_arm_parent.L"].select = True
        ob.data.bones["upper_arm_parent.R"].select = True

        ikfk_left_arm = ob.pose.bones["upper_arm_parent.L"]
        ikfk_right_arm = ob.pose.bones["upper_arm_parent.R"]

        ikfk_left_arm.keyframe_insert(data_path= '["IK_FK"]')
        ikfk_right_arm.keyframe_insert(data_path= '["IK_FK"]')

       
        
        bpy.ops.pose.select_all(action = 'DESELECT')
        
        # Select Bones (Controls) to move
        bpy.data.objects[ob.name].data.bones["torso"].select = True
        bpy.data.objects[ob.name].data.bones["hand_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["hand_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["foot_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_heel_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["foot_heel_ik.R"].select = True
        
        # Set Active Pose Bone
        bpy.context.object.data.bones.active = bpy.data.objects[ob.name].data.bones["torso"] 
        
        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        
        # Move 4 Frames Forward 
        bpy.context.scene.frame_current += 6


        # Reset "X" Location of 3D Cursor 
        bpy.context.scene.cursor.location[0] = 0

            
        # Jump to cursor
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
        

        # Resetting some transformations  
        bpy.context.object.pose.bones["torso"].location[2] = 0
        bpy.context.object.pose.bones["foot_ik.L"].location[2] = 0
        bpy.context.object.pose.bones["foot_ik.R"].location[2] = 0
        bpy.context.object.pose.bones["foot_ik.L"].rotation_quaternion[1] = 0
        bpy.context.object.pose.bones["foot_ik.L"].rotation_quaternion[2] = 0
        bpy.context.object.pose.bones["foot_ik.R"].rotation_quaternion[1] = 0
        bpy.context.object.pose.bones["foot_ik.R"].rotation_quaternion[2] = 0
        

        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')


         # Move 3 Frames Forward 
        bpy.context.scene.frame_current += 3

        # RECOVERY POSE


        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        
        # Move 5 Frames Forward 
        bpy.context.scene.frame_current += 7

        # LAST NEUTRAL POSE


         # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
               
            
        return {'FINISHED'}



# =====================================================
#   DEFINE LENGTH OF A JUMP BY PLACING 3D CURSOR
# =====================================================


# Define Length of a Jump by placing 3D Cursor
class OBJECT_OT_rigify_jumper_length_cursor(bpy.types.Operator):
    '''Define Length of a Jump by Placing 3D Cursor'''
    bl_idname = "object.rigify_jumper_length_cursor"
    bl_label = "Def"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):


        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name

        
        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'

        # Arms to FK
        bpy.context.object.pose.bones["upper_arm_parent.L"]["IK_FK"] = float(1)
        bpy.context.object.pose.bones["upper_arm_parent.R"]["IK_FK"] = float(1)


         
        # =====================================================
        #  	INSERT KEY IK_FK FOR ARMS
        # =====================================================

        ob = bpy.data.objects[ob.name]
        ob.data.bones["upper_arm_parent.L"].select = True
        ob.data.bones["upper_arm_parent.R"].select = True

        ikfk_left_arm = ob.pose.bones["upper_arm_parent.L"]
        ikfk_right_arm = ob.pose.bones["upper_arm_parent.R"]

        ikfk_left_arm.keyframe_insert(data_path= '["IK_FK"]')
        ikfk_right_arm.keyframe_insert(data_path= '["IK_FK"]')



         
        # Set Initial Keys to Full Rig (Key All)
        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        bpy.ops.pose.select_all(action = 'DESELECT')


        # Select Bones (Controls) to move
        bpy.data.objects[ob.name].data.bones["torso"].select = True
        bpy.data.objects[ob.name].data.bones["hand_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["hand_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["foot_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_heel_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_heel_ik.L"].select = True

        
        # Set Active Pose Bone
        bpy.context.object.data.bones.active = bpy.data.objects[ob.name].data.bones["torso"] 
        

        # 1: "NEUTRAL" POSE     
        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        # Move 4 Frames Forward 
        bpy.context.scene.frame_current += 7

        # 2: SQUASH POSE
        # Lower Position of a Torso

        torso_position = bpy.context.object.pose.bones["torso"]
        torso_position.location[2] -= 0.15


        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        # Move 3 Frames Forward 
        bpy.context.scene.frame_current += 3


        # 3: STRETCH POSE  

        torso_position = bpy.context.object.pose.bones["torso"]
        torso_position.location[2] += 0.15

    
         # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        # Move 4 Frames Forward 
        bpy.context.scene.frame_current += 12 


        # =====================================================
        #                3D  CURSOR
        # =====================================================


        # Condition for 3D Cursor Position ( Set Cursor for Jump)
        cursor_var = bpy.context.scene.cursor

        # Zero Out "X" Position   (Reset "X" Location of 3D Cursor )
        cursor_var.location[0] = 0

        torso_position = bpy.context.object.pose.bones["torso"]
        cursor_var.location[2] = torso_position.location[2] + 1

         
       
        # JUMP TO CURSOR
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)

          

        # =====================================================
        #                RESETTING TORSO AND FOOTS
        # =====================================================


        # Resetting some transformations  
        bpy.context.object.pose.bones["torso"].location[2] = 0
        bpy.context.object.pose.bones["foot_ik.L"].location[2] = 0
        bpy.context.object.pose.bones["foot_ik.R"].location[2] = 0
        bpy.context.object.pose.bones["foot_ik.L"].rotation_quaternion[1] = 0
        bpy.context.object.pose.bones["foot_ik.L"].rotation_quaternion[2] = 0
        bpy.context.object.pose.bones["foot_ik.R"].rotation_quaternion[1] = 0
        bpy.context.object.pose.bones["foot_ik.R"].rotation_quaternion[2] = 0
        

        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        # RECOVERY POSE
         # Move 3 Frames Forward 
        bpy.context.scene.frame_current += 3


        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        # Move 5 Frames Forward 
        bpy.context.scene.frame_current += 7

        # LAST NEUTRAL POSE


         # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')


        # =====================================================
        #               MOVE 3D  CURSOR BACK 
        # =====================================================


        # Move Back
        bpy.context.scene.frame_current -= 16


        cursor_var.location[1] = cursor_var.location[1] / 2
        cursor_var.location[2] = cursor_var.location[2] + 1

           
        # Jump to cursor
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        
        # Cursor Back To World Center
        bpy.ops.view3d.snap_cursor_to_center()

  
        return {'FINISHED'}








# =====================================================
#  SIMPLE JUMP
# =====================================================


# Simple Jump
class OBJECT_OT_rigify_animbox_jump_simple_ra(bpy.types.Operator):
    '''Simple Jump\nSelect any Bone'''
    bl_idname = "object.rigify_animbox_jump_simple_ra"
    bl_label = "Simple Jump"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)
                

    def execute(self, context):


        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name

        
        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'

        # Arms to FK
        bpy.context.object.pose.bones["upper_arm_parent.L"]["IK_FK"] = float(1)
        bpy.context.object.pose.bones["upper_arm_parent.R"]["IK_FK"] = float(1)

         
        # =====================================================
        #   INSERT KEY IK_FK FOR ARMS
        # =====================================================

        ob = bpy.data.objects[ob.name]
        ob.data.bones["upper_arm_parent.L"].select = True
        ob.data.bones["upper_arm_parent.R"].select = True

        ikfk_left_arm = ob.pose.bones["upper_arm_parent.L"]
        ikfk_right_arm = ob.pose.bones["upper_arm_parent.R"]

        ikfk_left_arm.keyframe_insert(data_path= '["IK_FK"]')
        ikfk_right_arm.keyframe_insert(data_path= '["IK_FK"]')


         
        # Set Initial Keys to Full Rig (Key All)
        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        bpy.ops.pose.select_all(action = 'DESELECT')


        # Select Bones (Controls) to move
        bpy.data.objects[ob.name].data.bones["torso"].select = True
        bpy.data.objects[ob.name].data.bones["hand_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["hand_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_ik.L"].select = True
        bpy.data.objects[ob.name].data.bones["foot_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_heel_ik.R"].select = True
        bpy.data.objects[ob.name].data.bones["foot_heel_ik.L"].select = True

        
        # Set Active Pose Bone
        bpy.context.object.data.bones.active = bpy.data.objects[ob.name].data.bones["torso"] 
        

        # 1: "NEUTRAL" POSE     
        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')


        frame_number = bpy.context.scene.frame_current
          
        # Set FRAME - Move 7 Frames Forward         
        frame_number += 7
        bpy.context.scene.frame_set(frame_number)
        

        # 2: SQUASH POSE
        # Lower Position of a Torso

        bpy.context.object.pose.bones["torso"].location[1] = 0.02
        bpy.context.object.pose.bones["torso"].location[2] = -0.12
        bpy.context.object.pose.bones["torso"].rotation_quaternion[1] = 0.1


        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')


        # Set FRAME - Move 3 Frames Forward         
        frame_number += 3
        bpy.context.scene.frame_set(frame_number)
        
        
        # 3: STRETCH POSE  

        bpy.context.object.pose.bones["torso"].location[1] = 0
        bpy.context.object.pose.bones["torso"].location[2] = 0
        bpy.context.object.pose.bones["torso"].rotation_quaternion[1] = 0
 


         # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')


        # Set FRAME - Move 12 Frames Forward         
        frame_number += 12
        bpy.context.scene.frame_set(frame_number)
        


        
        # =====================================================
        #                3D  CURSOR
        # =====================================================


        # Condition for 3D Cursor Position ( Set Cursor for Jump)
        cursor_var = bpy.context.scene.cursor


        root_position = bpy.context.object.pose.bones["root"]

     
        cursor_var.location[0] = root_position.location[0]
        cursor_var.location[1] = root_position.location[1]
        cursor_var.location[2] = root_position.location[2] + 1

         
       
        # JUMP TO CURSOR
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)

          

        # =====================================================
        #                RESETTING TORSO AND FOOTS
        # =====================================================


        # Resetting some transformations  
        bpy.context.object.pose.bones["torso"].location[2] = 0
        bpy.context.object.pose.bones["foot_ik.L"].location[1] = 0
        bpy.context.object.pose.bones["foot_ik.L"].location[2] = 0
        bpy.context.object.pose.bones["foot_ik.R"].location[1] = 0
        bpy.context.object.pose.bones["foot_ik.R"].location[2] = 0
        bpy.context.object.pose.bones["foot_ik.L"].rotation_quaternion[1] = 0
        bpy.context.object.pose.bones["foot_ik.L"].rotation_quaternion[2] = 0
        bpy.context.object.pose.bones["foot_ik.R"].rotation_quaternion[1] = 0
        bpy.context.object.pose.bones["foot_ik.R"].rotation_quaternion[2] = 0
        

        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        # RECOVERY POSE
        

        # Set FRAME - Move 3 Frames Forward         
        frame_number += 3
        bpy.context.scene.frame_set(frame_number)
        

        # Lower Position of a Torso
        bpy.context.object.pose.bones["torso"].location[1] = 0.02
        bpy.context.object.pose.bones["torso"].location[2] = -0.12
        bpy.context.object.pose.bones["torso"].rotation_quaternion[1] = 0.1
        

        # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        
        # Set FRAME - Move 7 Frames Forward         
        frame_number += 7
        bpy.context.scene.frame_set(frame_number)        

        # LAST NEUTRAL POSE

        bpy.context.object.pose.bones["torso"].location[1] = 0
        bpy.context.object.pose.bones["torso"].location[2] = 0
        bpy.context.object.pose.bones["torso"].rotation_quaternion[1] = 0



         # Set Key
        bpy.ops.anim.keyframe_insert(type='LocRotScale')


        # =====================================================
        #               MOVE 3D  CURSOR BACK 
        # =====================================================


        # Move Back
        bpy.context.scene.frame_current -= 16

        # Cursor
        cursor_var.location[2] = cursor_var.location[2] + 1

          
        # Jump to cursor
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
        
   
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

  

  
        ob_fcurve = ob.animation_data.action.fcurves

        def scale_curve_handle(bone_name):
            
            
            
            for fc in ob_fcurve:
                if fc.data_path.endswith(('location')) and bone_name in fc.data_path:
                    if fc.array_index == 2:

                        fc.keyframe_points[3].handle_right_type = 'FREE'
                        fc.keyframe_points[3].handle_left_type = 'FREE'             
                        fc.keyframe_points[3].handle_right.x += 5
                        fc.keyframe_points[3].handle_left.x -= 5


                        fc.update()

        scale_curve_handle('torso')
        scale_curve_handle('foot_ik.L')
        scale_curve_handle('foot_ik.R')
        




        # Cursor Back To World Center
        bpy.ops.view3d.snap_cursor_to_center()

  
        return {'FINISHED'}


# =====================================================
#  END OF SIMPLE JUMP
# =====================================================








# =====================================================
#  END OF	JUMP PRESETS
# =====================================================






# ============================================================
#     TURNS SETUP
# ============================================================


# ============================================================
#  ADD CHILD OF CONSTRAINT  / CREATE CENTER OF ROTATION - COR
# ============================================================



# Create Center Of Rotation (COR)
class OBJECT_OT_rigify_create_turn_cor(bpy.types.Operator):
    '''Add  " Child Of "  Constraint.\nCreate Center Of Rotation'''
    bl_idname = "object.rigify_create_turn_cor"
    bl_label = "Turn Setup"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' )


    def execute(self, context):
        scene = context.scene


        # Select All
        bpy.ops.pose.select_all(action = 'SELECT')


        # Delete Constraint with name Front-Back Flip Child Of"
        for bone in bpy.context.selected_pose_bones:
            # Create a list of all constraints on this bone
            front_back_child_of_const = [ c for c in bone.constraints  if c.name == "Front-Back Flip Child Of" ]

            # Iterate over all the bone's constraints and delete them all
            for c in front_back_child_of_const:
                bone.constraints.remove( c ) # Remove constraint
                
                
        # Delete Constraint with name "Turn Child Of"
        for bone in bpy.context.selected_pose_bones:
            # Create a list of all constraints on this bone
            turn_child_of_const = [ c for c in bone.constraints  if c.name == "Turn Child Of" ]

            # Iterate over all the bone's constraints and delete them all
            for c in turn_child_of_const:
                bone.constraints.remove( c ) # Remove constraint
                
                       
        
        # Deselect All
        bpy.ops.pose.select_all(action = 'DESELECT')

        
        # Set active 'Scene Collection'
        scene_collection = bpy.context.view_layer.layer_collection
        bpy.context.view_layer.active_layer_collection = scene_collection
        act_col = bpy.context.view_layer.active_layer_collection

        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True


        # Set Mode
        current_mode = bpy.context.mode
        if current_mode == 'POSE':
            bpy.ops.object.mode_set(mode='OBJECT')



        # Removing center_of_mass_empty  ( if more clicks follow )
        for ob in scene.objects:
            if ob.type == 'EMPTY' and ob.name == "Center of Mass Empty":
                bpy.data.objects.remove(ob)    

         
        # Removing Front_Back_Flip Empty  ( if more clicks follow )
        for ob in scene.objects:
            if ob.type == 'EMPTY' and ob.name == "Front-Back Flip Empty":
                bpy.data.objects.remove(ob)    

         
        # Removing Empty and COR ( if more clicks follow )
        for ob in scene.objects:
            if ob.type == 'EMPTY' and ob.name == "Turn Empty":
                bpy.data.objects.remove(ob)    


        for ob in scene.objects:
            if ob.type == 'MESH' and ob.name == "Center of Rotation":
                bpy.data.objects.remove(ob)    


        # Positioning 3D Cursor == Torso Location
        cursor_var = bpy.context.scene.cursor
        torso_position = bpy.context.object.pose.bones["torso"]
        cursor_var.location = torso_position.location


        # Add Empty
        com_empty = bpy.data.objects.new( "Empty", None )   
        act_col.collection.objects.link(com_empty) 


        # Adding Cylinder
        bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=0.02, depth=2.5, enter_editmode=False, align='WORLD', location=(cursor_var.location), scale=(1, 1, 1))
        ob = bpy.context.object
        ob.name = 'Cylinder'

        # New Name 
        turns_empty = bpy.data.objects['Empty']
        turns_empty.name = "Turn Empty"

        # Center of Rotation
        cor = bpy.data.objects['Cylinder']
        cor.name = "Center of Rotation"
         
        cor.location[2] = 1
        cor.hide_render = True
             
        cor.select_set(0)         
         
         
        # Set Active Object
             
        ob = bpy.context.object

        obj = bpy.data.objects

        for ob in obj:
            if ob.type == 'ARMATURE':
                bpy.context.view_layer.objects.active = ob
                                

        # Set Mode
        current_mode = bpy.context.mode
        if current_mode == 'OBJECT':
            bpy.ops.object.mode_set(mode='POSE')



        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name

        sel_bones = bpy.data.objects[ob.name].data.bones    
         

        turns_child_of_list = [ "torso", 
                                "foot_ik.L", "foot_ik.R",]
        
        # "hand_ik.L", "hand_ik.R",                            
                               
        # Select and Insert Keys
        for bone in sel_bones:
            if bone.name in turns_child_of_list:
                bpy.context.object.data.bones.active = bone
                n_con = bpy.context.active_pose_bone.constraints.new('CHILD_OF')
                n_con.name = "Child Of"
                bpy.context.object.pose.bones[bone.name].constraints["Child Of"].target = bpy.data.objects["Turn Empty"]
                bpy.context.object.pose.bones[bone.name].constraints["Child Of"].name = "Turn Child Of"
                      

            else:
                pass   



        # Set Arms IK to FK

        bones = bpy.context.object.pose.bones
            
         
        for bone in bones:  

            if bone.name == "upper_arm_parent.L":
                bone["IK_FK"] = float(1)


            if bone.name == "upper_arm_parent.R":
                bone["IK_FK"] = float(1)


            else:
                pass



        bpy.ops.pose.select_all(action = 'DESELECT')


        return {'FINISHED'}



# ================================================================
# END  ADD CHILD OF CONSTRAINT  / CREATE CENTER OF ROTATION - COR
# ================================================================





# ============================================================
#    FRONT_BACK FLIP SETUP
# ============================================================

# ============================================================
#   ADD "CHILD OF" CONSTRAINT  FOR FRONT_BACK FLIP JUMP
# ============================================================




#  Front_Back_Flip_Ready
class OBJECT_OT_front_back_flip_ready(bpy.types.Operator):
    '''This will create Empty with "Child Of" Constraint -\nfor Torso, Hands and Feet'''
    bl_idname = "object.front_back_flip_ready"
    bl_label = "Front-Back Flip Setup"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' )



    def execute(self, context):
        scene = context.scene


        # Select All
        bpy.ops.pose.select_all(action = 'SELECT')

        
        # Delete Constraint with name Front-Back Flip Child Of"
        for bone in bpy.context.selected_pose_bones:
            # Create a list of all constraints on this bone
            front_back_child_of_const = [ c for c in bone.constraints  if c.name == "Front-Back Flip Child Of" ]

            # Iterate over all the bone's constraints and delete them all
            for c in front_back_child_of_const:
                bone.constraints.remove( c ) # Remove constraint
                
                
        # Delete Constraint with name "Turn Child Of"
        for bone in bpy.context.selected_pose_bones:
            # Create a list of all constraints on this bone
            turn_child_of_const = [ c for c in bone.constraints  if c.name == "Turn Child Of" ]

            # Iterate over all the bone's constraints and delete them all
            for c in turn_child_of_const:
                bone.constraints.remove( c ) # Remove constraint
                       

        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name
            
            
        #  Select Torso
        bpy.data.objects[ob.name].data.bones["torso"].select = True
        
        # Snap 3D Cursor to Torso
        bpy.ops.view3d.snap_cursor_to_selected()



        # Set active 'Scene Collection'
        scene_collection = bpy.context.view_layer.layer_collection
        bpy.context.view_layer.active_layer_collection = scene_collection
        act_col = bpy.context.view_layer.active_layer_collection

        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True


        # Set Mode
        current_mode = bpy.context.mode
        if current_mode == 'POSE':
            bpy.ops.object.mode_set(mode='OBJECT')


        # Removing Front-Back Flip Empty  ( if more clicks follow )
        for ob in scene.objects:
            if ob.type == 'EMPTY' and ob.name == "Front-Back Flip Empty":
                bpy.data.objects.remove(ob)    

    
    
        # Removing "Center of Mass Empty"  ( if more clicks follow )
        for ob in scene.objects:
            if ob.type == 'EMPTY' and ob.name == "Center of Mass Empty":
                bpy.data.objects.remove(ob)    

    

        #Removing Empty and COR ( if more clicks follow )
        for ob in scene.objects:
            if ob.type == 'EMPTY' and ob.name == "Turn Empty":
                bpy.data.objects.remove(ob)    


        for ob in scene.objects:
            if ob.type == 'MESH' and ob.name == "Center of Rotation":
                bpy.data.objects.remove(ob)    


          
        # Adding Empty to 3D Cursor Location
        ca_empty = bpy.data.objects.new( "Empty", None )   
        act_col.collection.objects.link(ca_empty) 
        cursor = bpy.context.scene.cursor
        ca_empty.location = cursor.location


        # New Name 
        front_back_flip_empty = bpy.data.objects['Empty']
        front_back_flip_empty.name = "Front-Back Flip Empty"
        
        cursor_location = bpy.context.scene.cursor.location

        # Adding additional Spherical Empty as "Center of Mass" Orientation
        com_empty = bpy.data.objects.new( "Empty", None )   
        act_col.collection.objects.link(com_empty) 
        e_type = bpy.types.Object.bl_rna.properties['empty_display_type'].enum_items.keys()
        com_empty.empty_display_type = e_type[-3]
   
    

        # New Name  for "Center of Mass" Empty
        center_of_mass_empty = bpy.data.objects['Empty']
        center_of_mass_empty.name = "Center of Mass Empty"
        center_of_mass_empty.scale[0] = 0.8
        center_of_mass_empty.scale[1] = 0.8
        center_of_mass_empty.scale[2] = 0.8
        center_of_mass_empty.location = cursor_location

              
        # Parenting Empties
        empty_obj = bpy.data.objects
        a = bpy.data.objects['Front-Back Flip Empty']
        b = bpy.data.objects['Center of Mass Empty']


        bpy.ops.object.select_all(action='DESELECT') # deselect all object

        a.select_set(True)
        b.select_set(True)     # select the object for the 'parenting'

        bpy.context.view_layer.objects.active = a    # the active object will be the parent of all selected object

        bpy.ops.object.parent_set()
        # Now The parent of b is a


              
        # Set Active Object
             
        ob = bpy.context.object
        obj = bpy.data.objects

        for ob in obj:
            if ob.type == 'ARMATURE':
                bpy.context.view_layer.objects.active = ob
                                

        # Set Mode
        current_mode = bpy.context.mode
        if current_mode == 'OBJECT':
            bpy.ops.object.mode_set(mode='POSE')



        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name

        sel_bones = bpy.data.objects[ob.name].data.bones    
         

        turns_child_of_list = [ "torso",
                                "foot_ik.L", "foot_ik.R",]
                   
         # "hand_ik.L", "hand_ik.R",                           
                               
        # Select and Add Constraint
        for bone in sel_bones:
            if bone.name in turns_child_of_list:
                bpy.context.object.data.bones.active = bone
                n_con = bpy.context.active_pose_bone.constraints.new('CHILD_OF')
                n_con.name = "Child Of"
                bpy.context.object.pose.bones[bone.name].constraints["Child Of"].target = bpy.data.objects["Front-Back Flip Empty"]
                bpy.context.object.pose.bones[bone.name].constraints["Child Of"].name = "Front-Back Flip Child Of"

                      
            else:
                pass   


        # Set Arms IK to FK

        bones = bpy.context.object.pose.bones
            
         
        for bone in bones:  

            if bone.name == "upper_arm_parent.L":
                bone["IK_FK"] = float(1)


            if bone.name == "upper_arm_parent.R":
                bone["IK_FK"] = float(1)


            else:
                pass


        bpy.ops.pose.select_all(action = 'DESELECT')


        return {'FINISHED'}


# ============================================================
# END   ADD "CHILD OF" CONSTRAINT  FOR FRONT_BACK FLIP JUMP
# ============================================================




 


# =============================================================================================
#   ADD EMPTY WITH "CHILD OF" CONSTRAINT  TO 'RELATED' (Connected Rigify Selected Bones)
# =============================================================================================




# Add 'Move Empty' to selected ('related') with 'child of' constraint
class OBJECT_OT_adding_move_empty_to_selected_ra(bpy.types.Operator):
    '''Add 'Move Empty' as Parent to 'Related' (Connected Rigify Bones) -
With 'child of' constraint.
" Mobility System " for Multi-Limbs'''
    bl_idname = "object.adding_move_empty_to_selected_ra"
    bl_label = "Add Parent Empty to Related"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) > 2)
                

    def execute(self, context):
        
        scene = bpy.context.scene

        pose_bones = bpy.context.object.pose.bones
        sel_bones = bpy.context.selected_pose_bones


        # 3D Cursor to Selected
        bpy.ops.view3d.snap_cursor_to_selected()


        # Delete Constraint with name "Move Child Of"
        for bone in sel_bones:
            # Create a list of all constraints on this bone
            move_child_of_const = [ c for c in bone.constraints  if c.name == "Move Child Of" ]

            # Iterate over all the bone's constraints and delete them all
            for c in move_child_of_const:
                bone.constraints.remove( c ) # Remove constraint
                


        cursor_location = bpy.context.scene.cursor.location

        # Adding 'Move Empty'


        o = bpy.data.objects.new( "Move Empty", None )

        # link to "collection"
        bpy.context.scene.collection.objects.link( o )

        # empty parameters

        o.empty_display_size = 0.5
        o.empty_display_type = 'PLAIN_AXES' 
        o.scale[2] = 2.5
        o.location = cursor_location 
        
 
        if o.location == cursor_location:
            Empty_Name = o.name
  

        sel_list = ('torso', 'foot_ik',  'hand_ik', 'front_foot_ik', 'hind_foot_ik', 'forefoot_ik',)

            
        for bone in sel_bones:
            if bone.name.startswith(tuple(b for b in sel_list)):
         
                bpy.context.object.data.bones.active =  bone.bone 
            
                print(bone.name)
                
                bc = bone.constraints.new(type='CHILD_OF')
                
                bc.target = bpy.data.objects[Empty_Name]
                
                bc.subtarget = bone.name 
                
                bc.name = "Move Child Of"

                
                # 3D Cursor to Center
                
                bpy.ops.view3d.snap_cursor_to_center()

         

        return {'FINISHED'}


# ============================================================================================
#  END  ADD EMPTY WITH "CHILD OF" CONSTRAINT  TO 'RELATED' (Connected Rigify Selected Bones)
# ============================================================================================




#=======================================================
# ADD 'PARENT EMPTY' TO ANY SELECTED BONE/BONES 
#=======================================================


# Add 'Parent Empty' to any selected Bone  with 'child of' constraint
class OBJECT_OT_add_parent_empty_to_any_selected_bone_ra(bpy.types.Operator):
    '''Add Parent Empty to Selected Bone/Bones -
With ' child of ' constraint'''
    bl_idname = "object.add_parent_empty_to_any_selected_bone_ra"
    bl_label = "Add Parent Empty to Selected"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)
                

    def execute(self, context):
        
        scene = bpy.context.scene

        sel_bones = bpy.context.selected_pose_bones


        # 3D Cursor to Selected
        bpy.ops.view3d.snap_cursor_to_selected()



        # Delete  Existing Empty with name 'Parent Empty'
        for emp in bpy.data.objects:
            if emp.type == 'EMPTY' and emp.name.startswith('Parent Empty'):
                bpy.data.objects.remove(emp)    

     

        # Delete Constraint with name "Child Of Parent Empty"
        for bone in sel_bones:
            # Create a list of all constraints on this bone
            child_of_empty_const = [ c for c in bone.constraints  if c.name == "Child Of Parent Empty" ]

            # Iterate over all the bone's constraints and delete them all
            for c in child_of_empty_const:
                bone.constraints.remove( c ) # Remove constraint
                


        cursor_location = bpy.context.scene.cursor.location

        # Adding 'Parent Empty'

        o_empty = bpy.data.objects.new( "Parent Empty", None )

        # link to "collection"
        bpy.context.scene.collection.objects.link( o_empty )


        o_empty.empty_display_type = 'PLAIN_AXES' 

        o_empty.location = cursor_location 
        
 
        if o_empty.location == cursor_location:
            Empty_Name = o_empty.name
  

        for bone in sel_bones:

            bpy.context.object.data.bones.active =  bone.bone 
        
            print(bone.name)
            
            bc = bone.constraints.new(type='CHILD_OF')
            
            bc.target = bpy.data.objects[Empty_Name]
            
            bc.subtarget = bone.name 
            
            bc.name = "Child Of Parent Empty"

            
            # 3D Cursor to Center
            
            bpy.ops.view3d.snap_cursor_to_center()

     

        return {'FINISHED'}




classes = [
            OBJECT_OT_rigify_jumper_start, OBJECT_OT_rigify_jumper, OBJECT_OT_rigify_jumper_put_down,
            OBJECT_OT_rigify_jumper_length_cursor,	OBJECT_OT_rigify_animbox_jump_simple_ra,
            OBJECT_OT_rigify_create_turn_cor, OBJECT_OT_front_back_flip_ready,
            OBJECT_OT_adding_move_empty_to_selected_ra, OBJECT_OT_add_parent_empty_to_any_selected_bone_ra,

          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()







