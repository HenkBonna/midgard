import bpy






# =======================================================================
#  SELECT  FINGERS
# =======================================================================


#  Select Left Fingers
class OBJECT_OT_rigify_sel_fingers_left(bpy.types.Operator):
    '''Select Left Fingers
Ctrl-Click - Select and Insert Keyframes
Shift-Click - Deselect Other'''
    bl_idname = "object.rigify_sel_fingers_left"
    bl_label = "Fingers L"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def invoke(self, context, event):   

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'

        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # bpy.ops.pose.select_all(action = 'DESELECT')
       
        pose_bones = bpy.context.object.pose.bones
        

        def select_left_fingers():

            for o in pose_bones:
                if o.name.startswith('thumb') and ".L" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_index') and ".L" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_middle') and ".L" in o.name:
                    o.bone.select = 1
         
            for o in pose_bones:
                if o.name.startswith('f_ring') and ".L" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_pinky') and ".L" in o.name:
                    o.bone.select = 1

            for o in pose_bones:
                if o.name.startswith('palm') and ".L" in o.name:
                    o.bone.select = 1

 
        if event: 
            select_left_fingers()                         
 

        if event.ctrl: 
            select_left_fingers()
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
 
        if event.shift:
            bpy.ops.pose.select_all(action = 'DESELECT')
            select_left_fingers()
   
        return {'FINISHED'}






#  Select Right Fingers
class OBJECT_OT_rigify_sel_fingers_right(bpy.types.Operator):
    '''Select Right Fingers
Ctrl-Click - Select and Insert Keyframes
Shift-Click - Deselect Other'''
    bl_idname = "object.rigify_sel_fingers_right"
    bl_label = "Fingers R"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def invoke(self, context, event):   

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'

        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # bpy.ops.pose.select_all(action = 'DESELECT')
        
        pose_bones = bpy.context.object.pose.bones
        

        def select_right_fingers():

            for o in pose_bones:
                if o.name.startswith('thumb') and ".R" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_index') and ".R" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_middle') and ".R" in o.name:
                    o.bone.select = 1
         
            for o in pose_bones:
                if o.name.startswith('f_ring') and ".R" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_pinky') and ".R" in o.name:
                    o.bone.select = 1

            for o in pose_bones:
                if o.name.startswith('palm') and ".R" in o.name:
                    o.bone.select = 1

 

        if event: 
            select_right_fingers()                         
 


        if event.ctrl: 
            select_right_fingers()
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
 
 
        if event.shift:
            bpy.ops.pose.select_all(action = 'DESELECT')
            select_right_fingers()      
   
        return {'FINISHED'}








#  Select Right and Left Fingers
class OBJECT_OT_rigify_sel_fingers_both_hands_ra(bpy.types.Operator):
    '''Select Right and Left Fingers
Ctrl-Click - Select and Insert Keyframes
Shift-Click - Deselect Other'''
    bl_idname = "object.rigify_sel_fingers_both_hands_ra"
    bl_label = "Fingers RL"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def invoke(self, context, event):   

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'

        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # bpy.ops.pose.select_all(action = 'DESELECT')
        
        pose_bones = bpy.context.object.pose.bones
        

        def select_right_fingers():

            for o in pose_bones:
                if o.name.startswith('thumb') and ".R" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_index') and ".R" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_middle') and ".R" in o.name:
                    o.bone.select = 1
         
            for o in pose_bones:
                if o.name.startswith('f_ring') and ".R" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_pinky') and ".R" in o.name:
                    o.bone.select = 1

            for o in pose_bones:
                if o.name.startswith('palm') and ".R" in o.name:
                    o.bone.select = 1

 

        def select_left_fingers():

            for o in pose_bones:
                if o.name.startswith('thumb') and ".L" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_index') and ".L" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_middle') and ".L" in o.name:
                    o.bone.select = 1
         
            for o in pose_bones:
                if o.name.startswith('f_ring') and ".L" in o.name:
                    o.bone.select = 1
             
            for o in pose_bones:
                if o.name.startswith('f_pinky') and ".L" in o.name:
                    o.bone.select = 1

            for o in pose_bones:
                if o.name.startswith('palm') and ".L" in o.name:
                    o.bone.select = 1

 

        if event: 
            select_right_fingers() 
            select_left_fingers()                        
 

        if event.ctrl: 
            select_right_fingers()
            select_left_fingers()
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
 
 
        if event.shift:
            bpy.ops.pose.select_all(action = 'DESELECT')
            select_right_fingers()
            select_left_fingers()  
        
   
        return {'FINISHED'}



# =======================================================================
#  END OF  SELECT FINGERS
# =======================================================================










# =============================================================
# SELECT HEAD
# =============================================================



#  HEAD Selection 
class OBJECT_OT_rigify_head_sel(bpy.types.Operator):
    '''Select HEAD
Ctrl + Click = Select Neck
Shift-Click - Deselect Other'''
    bl_idname = "object.rigify_head_sel"
    bl_label = "Head"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def invoke(self, context, event):


        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
       
        # bpy.ops.pose.select_all(action = 'DESELECT')
        
        # Select Head

        pose_bones = bpy.context.object.pose.bones


        def select_head():
            for o in pose_bones:
                if o.name.startswith('head'):
                    o.bone.select = 1


        def select_neck():
            for o in pose_bones:
                if o.name.startswith('neck'):
                    o.bone.select = 1


        if event:
            select_head()


        if event.ctrl:
            select_head()
            select_neck()
    
 
        if event.shift:
            bpy.ops.pose.select_all(action = 'DESELECT')
            select_head()     
                    
        return {'FINISHED'}




# =============================================================
#  SELECT TORSO
# =============================================================



#  TORSO Selection 
class OBJECT_OT_rigify_torso_sel(bpy.types.Operator):
    '''Select TORSO
Shift-Click - Deselect Other'''
    bl_idname = "object.rigify_torso_sel"
    bl_label = "Torso"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def invoke(self, context, event):


        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
       
        # bpy.ops.pose.select_all(action = 'DESELECT')
        
        # Select Torso

        pose_bones = bpy.context.object.pose.bones

        def select_torso():
            for o in pose_bones:
                if o.name.startswith('torso'):
                    o.bone.select = 1


        if event:
            select_torso()
        
        if event.shift:
            bpy.ops.pose.select_all(action = 'DESELECT')
            select_torso()     
                    
                    
        return {'FINISHED'}





# =============================================================
#  SELECT CHEST
# =============================================================



#  CHEST Selection 
class OBJECT_OT_rigify_chest_sel(bpy.types.Operator):
    '''Select CHEST
Shift-Click - Deselect Other'''
    bl_idname = "object.rigify_chest_sel"
    bl_label = "Chest"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def invoke(self, context, event):


        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
       
        # bpy.ops.pose.select_all(action = 'DESELECT')
        
        # Select Chest

        pose_bones = bpy.context.object.pose.bones
        
        def select_chest():
            for o in pose_bones:
                if o.name.startswith('chest'):
                    o.bone.select = 1


        if event:
            select_chest()
        
        if event.shift:
            bpy.ops.pose.select_all(action = 'DESELECT')
            select_chest()    
                  
                    
        return {'FINISHED'}




# =======================================================================
#  SELECTION SET TO MOVE / JUMP/ FRONTFLIP / BACKFLIP / SOMERSAULT 
# =======================================================================


#  Selection Set - MOVE WHOLE RIG
class OBJECT_OT_rigify_sel_set_move_rig(bpy.types.Operator):
    '''Selection Set - MOVE WHOLE RIG'''
    bl_idname = "object.rigify_sel_set_move_rig"
    bl_label = "Set"
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
        
        bpy.ops.pose.select_all(action = 'DESELECT')
        
        sel_bones = bpy.data.objects[ob.name].data.bones   
           
        # Select Bones (Controls) to move
        sel_set_to_move = ["torso", "hand_ik.L", "hand_ik.R", 
                           "foot_ik.L", "foot_ik.R",
                           "foot_heel_ik.L", "foot_heel_ik.R"]

        for bone in sel_bones:
            if bone.name in sel_set_to_move:
                bone.select = True
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


    
        # Set Active Pose Bone

        for bone in sel_bones:
            if bone.name == "torso":
                bpy.context.object.data.bones.active = bpy.data.objects[ob.name].data.bones[bone.name] 

            else:
                pass   

   
        return {'FINISHED'}



# =============================================================
#   FEET SELECTION 
# =============================================================



#   Feet Selection 
class OBJECT_OT_rigify_feet_sel(bpy.types.Operator):
    '''Select Feet
LMB = Both Feet
Ctrl = Right Foot
Alt = Left Foot
Shift-Click - Deselect Other'''

    bl_idname = "object.rigify_feet_sel"
    bl_label = "Feet IK"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def invoke(self, context, event):


        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
       
        # bpy.ops.pose.select_all(action = 'DESELECT')

        
        # Select Left Foot

        pose_bones = bpy.context.object.pose.bones

        def select_foot_R():
       
            for o in pose_bones:
                if o.name.startswith('foot_ik') and ".R" in o.name:
                    o.bone.select = 1


        def select_foot_L():
            
            for o in pose_bones:
                if o.name.startswith('foot_ik') and ".L" in o.name:
                    o.bone.select = 1

 
        def deselect_foot_R():
       
            for o in pose_bones:
                if o.name.startswith('foot_ik') and ".R" in o.name:
                    o.bone.select = 0


        def deselect_foot_L():
            
            for o in pose_bones:
                if o.name.startswith('foot_ik') and ".L" in o.name:
                    o.bone.select = 0

            
        ev = []

    
        if event: 
            select_foot_R()
            select_foot_L()
                               
                
        if event.ctrl:
            select_foot_R()
            deselect_foot_L()
            
                                        
        if event.alt: 
            select_foot_L()
            deselect_foot_R()
                                                                 
        
        if event.shift:
            bpy.ops.pose.select_all(action = 'DESELECT')
            select_foot_L()
            select_foot_R() 
                  
               
        return {'FINISHED'}



# =====================================================
#  HANDS SELECTION
# =====================================================

#  Hands Selection 
class OBJECT_OT_rigify_hands_sel(bpy.types.Operator):
    '''Select Hands
LMB = Both Hands
Ctrl = Right Hand
Alt = Left Hand
Shift-Click - Deselect Other'''

    bl_idname = "object.rigify_hands_sel"
    bl_label = "Hands IK"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def invoke(self, context, event):


        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
       
        # bpy.ops.pose.select_all(action = 'DESELECT')

        
         # Selecting Hands

        pose_bones = bpy.context.object.pose.bones

        def select_hand_R():
       
            for o in pose_bones:
                if o.name.startswith('hand_ik') and ".R" in o.name:
                    o.bone.select = 1


        def select_hand_L():
            
            for o in pose_bones:
                if o.name.startswith('hand_ik') and ".L" in o.name:
                    o.bone.select = 1

 
        def deselect_hand_R():
       
            for o in pose_bones:
                if o.name.startswith('hand_ik') and ".R" in o.name:
                    o.bone.select = 0


        def deselect_hand_L():
            
            for o in pose_bones:
                if o.name.startswith('hand_ik') and ".L" in o.name:
                    o.bone.select = 0

 
        ev = []

    
        if event: 
            select_hand_R()
            select_hand_L()

                                               
        if event.ctrl:
            select_hand_R()
            deselect_hand_L()
            
                                        
        if event.alt: 
            select_hand_L()
            deselect_hand_R()
               

        if event.shift:
            bpy.ops.pose.select_all(action = 'DESELECT')
            select_hand_R()
            select_hand_L() 
                       


        return {'FINISHED'}






#    Left Arm Selection 
class OBJECT_OT_rigify_left_arm_sel(bpy.types.Operator):
    '''Select Left Arm
LMB = Upper Arm
Ctrl = Forearm
Alt = Hand FK
Shift-Click - Select Upper Arm_L / Deselect Other'''

    bl_idname = "object.rigify_left_arm_sel"
    bl_label = "Arm L (FK)"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def invoke(self, context, event):


        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
       
        # bpy.ops.pose.select_all(action = 'DESELECT')

        
        # Select Left Arm  


        pose_bones = bpy.context.object.pose.bones

        def select_upper_arm_L():
       
            for o in pose_bones:
                if o.name.startswith('upper_arm_fk') and ".L" in o.name:
                    o.bone.select = 1

        def deselect_upper_arm_L():
       
            for o in pose_bones:
                if o.name.startswith('upper_arm_fk') and ".L" in o.name:
                    o.bone.select = 0


        def select_forearm_L():
            
            for o in pose_bones:
                if o.name.startswith('forearm_fk') and ".L" in o.name:
                    o.bone.select = 1

 
        def deselect_forearm_L():
            
            for o in pose_bones:
                if o.name.startswith('forearm_fk') and ".L" in o.name:
                    o.bone.select = 0
 
 
        def select_hand_fk_L():
       
            for o in pose_bones:
                if o.name.startswith('hand_fk') and ".L" in o.name:
                    o.bone.select = 1

 
        def deselect_hand_fk_L():
       
            for o in pose_bones:
                if o.name.startswith('hand_fk') and ".L" in o.name:
                    o.bone.select = 0

            
        ev = []

    
        if event: 
            select_upper_arm_L()
            deselect_forearm_L()
            deselect_hand_fk_L()
                                   
                
        if event.ctrl:
            select_forearm_L()
            deselect_upper_arm_L()
            deselect_hand_fk_L()

                                        
        if event.alt: 
            select_hand_fk_L()
            deselect_upper_arm_L()
            deselect_forearm_L()

 
        if event.shift:
            bpy.ops.pose.select_all(action = 'DESELECT')
            select_upper_arm_L()


        return {'FINISHED'}







#    Right Arm Selection 
class OBJECT_OT_rigify_right_arm_sel(bpy.types.Operator):
    '''Select Right Arm
LMB = Upper Arm
Ctrl = Forearm
Alt = Hand FK
Shift-Click - Select Upper Arm_R / Deselect Other'''

    bl_idname = "object.rigify_right_arm_sel"
    bl_label = "Arm R (FK)"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def invoke(self, context, event):



        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
       
        # bpy.ops.pose.select_all(action = 'DESELECT')

        
        # Select Right Arm  


        pose_bones = bpy.context.object.pose.bones

        def select_upper_arm_R():
       
            for o in pose_bones:
                if o.name.startswith('upper_arm_fk') and ".R" in o.name:
                    o.bone.select = 1

        def deselect_upper_arm_R():
       
            for o in pose_bones:
                if o.name.startswith('upper_arm_fk') and ".R" in o.name:
                    o.bone.select = 0


        def select_forearm_R():
            
            for o in pose_bones:
                if o.name.startswith('forearm_fk') and ".R" in o.name:
                    o.bone.select = 1

 
        def deselect_forearm_R():
            
            for o in pose_bones:
                if o.name.startswith('forearm_fk') and ".R" in o.name:
                    o.bone.select = 0
 
 
        def select_hand_fk_R():
       
            for o in pose_bones:
                if o.name.startswith('hand_fk') and ".R" in o.name:
                    o.bone.select = 1

 
        def deselect_hand_fk_R():
       
            for o in pose_bones:
                if o.name.startswith('hand_fk') and ".R" in o.name:
                    o.bone.select = 0

            
        ev = []

    
        if event: 
            select_upper_arm_R()
            deselect_forearm_R()
            deselect_hand_fk_R()
                                   
                
        if event.ctrl:
            select_forearm_R()
            deselect_upper_arm_R()
            deselect_hand_fk_R()

                                        
        if event.alt: 
            select_hand_fk_R()
            deselect_upper_arm_R()
            deselect_forearm_R()
    
        if event.shift:
            bpy.ops.pose.select_all(action = 'DESELECT')
            select_upper_arm_R()

        return {'FINISHED'}



# =============================================================
#  SELECTOR END
# =============================================================









# =============================================================
#  ARMS POSITIONS: DOWN, IN FRONT, UP
# =============================================================


#  ARMS DOWN
class OBJECT_OT_rigify_arms_down_pos(bpy.types.Operator):
    '''ARMS DOWN POSITION'''
    bl_idname = "object.rigify_arms_down_pos"
    bl_label = "Down"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')



    def execute(self, context):

        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS' 

         
        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.context.selected_pose_bones


        # =====================================================
        #   ARMS DOWN - ALL
        # =====================================================

           
        def arms_down_pos():
            
            bpy.ops.pose.select_all(action='DESELECT')
            
            # Arms to FK
            for o in pose_bones:
                if o.name.startswith('upper_arm_parent') and ".L" in o.name:
                    o["IK_FK"] = float(1)
                    o.keyframe_insert(data_path= '["IK_FK"]')

            for o in pose_bones:
                if o.name.startswith('upper_arm_parent') and ".R" in o.name:
                    o["IK_FK"] = float(1)
                    o.keyframe_insert(data_path= '["IK_FK"]')

            
            for o in pose_bones:
                if o.name.startswith('upper_arm_fk') and ".L" in o.name:
                    o.rotation_quaternion[0] = 0.9
                    o.rotation_quaternion[1] = 0.13
                    o.rotation_quaternion[2] = 0
                    o.rotation_quaternion[3] = -0.43
                    o.keyframe_insert(data_path='rotation_quaternion')
                    o.bone.select = 1
                
            
            for o in pose_bones:
                if o.name.startswith('upper_arm_fk') and ".R" in o.name:
                    o.rotation_quaternion[0] = 0.9
                    o.rotation_quaternion[1] = 0.13
                    o.rotation_quaternion[2] = 0
                    o.rotation_quaternion[3] = 0.43
                    o.keyframe_insert(data_path='rotation_quaternion')
                    o.bone.select = 1
                
              
            for o in pose_bones:
                if o.name.startswith('forearm_fk') and ".L" in o.name:
                    o.rotation_quaternion[0] = 1
                    o.rotation_quaternion[1] = 0
                    o.rotation_quaternion[2] = 0
                    o.rotation_quaternion[3] = 0
                    o.keyframe_insert(data_path='rotation_quaternion')
                
           
            for o in pose_bones:
                if o.name.startswith('forearm_fk') and ".R" in o.name:
                    o.rotation_quaternion[0] = 1
                    o.rotation_quaternion[1] = 0
                    o.rotation_quaternion[2] = 0
                    o.rotation_quaternion[3] = 0
                    o.keyframe_insert(data_path='rotation_quaternion')
                
               
        arms_down_pos()


        return {'FINISHED'}





#  ARMS DOWN FOR SELECTED
class OBJECT_OT_rigify_arms_down_pos_selected(bpy.types.Operator):
    '''ARMS DOWN POSITION - SELECTED
Please Select  < upper_arm_fk >  - any Side'''
    bl_idname = "object.rigify_arms_down_pos_selected"
    bl_label = "Down Sel"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')



    def execute(self, context):

 
        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS' 
         
         
        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.context.selected_pose_bones



        # =====================================================
        #   ARMS DOWN FOR "SELECT RELATED" (Selected)
        # =====================================================


        def arms_down_for_selected():
            

            for bone in pose_bones:
                if bone.name.startswith('upper_arm_parent') and ".L" in bone.name:
                    bone["IK_FK"] = float(1)
                    bone.keyframe_insert(data_path= '["IK_FK"]')



            for bone in pose_bones:
                if bone.name.startswith('upper_arm_parent') and ".R" in bone.name:
                    bone["IK_FK"] = float(1)
                    bone.keyframe_insert(data_path= '["IK_FK"]')
            
            
            
            bpy.ops.pose.select_all(action='DESELECT') 
            
            for bone in sel_bones:
                if bone.name.startswith('upper_arm_fk') and ".L" in bone.name:    
                    bone.rotation_quaternion[0] = 0.9
                    bone.rotation_quaternion[1] = 0.13
                    bone.rotation_quaternion[2] = 0
                    bone.rotation_quaternion[3] = -0.43
                    bone.keyframe_insert(data_path='rotation_quaternion')
                    bone.bone.select = 1
                     

            for bone in sel_bones:
                if bone.name.startswith('upper_arm_fk') and ".R" in bone.name:    
                    bone.rotation_quaternion[0] = 0.9
                    bone.rotation_quaternion[1] = 0.13
                    bone.rotation_quaternion[2] = 0
                    bone.rotation_quaternion[3] = 0.43
                    bone.keyframe_insert(data_path='rotation_quaternion')
                    bone.bone.select = 1


            for bone in sel_bones:
                if bone.name.startswith('forearm_fk') and ".L" in bone.name:    
                    bone.rotation_quaternion[0] = 1
                    bone.rotation_quaternion[1] = 0
                    bone.rotation_quaternion[2] = 0
                    bone.rotation_quaternion[3] = 0
                    bone.keyframe_insert(data_path='rotation_quaternion')
                     

            for bone in sel_bones:
                if bone.name.startswith('forearm_fk') and ".R" in bone.name:    
                    bone.rotation_quaternion[0] = 1
                    bone.rotation_quaternion[1] = 0
                    bone.rotation_quaternion[2] = 0
                    bone.rotation_quaternion[3] = 0
                    bone.keyframe_insert(data_path='rotation_quaternion')
                                       
           
        arms_down_for_selected()


        return {'FINISHED'}





#  ARMS IN FRONT POSITION
class OBJECT_OT_rigify_arms_in_front_pos(bpy.types.Operator):
    '''ARMS IN FRONT POSITION'''
    bl_idname = "object.rigify_arms_in_front_pos"
    bl_label = "In Front"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):

        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS' 

         
        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.context.selected_pose_bones


# =====================================================
#   ARMS IN FRONT - ALL
# =====================================================

           
        def arms_in_front_pos():
            
            bpy.ops.pose.select_all(action='DESELECT')
            
            # Arms to FK
            for o in pose_bones:
                if o.name.startswith('upper_arm_parent') and ".L" in o.name:
                    o["IK_FK"] = float(1)
                    o.keyframe_insert(data_path= '["IK_FK"]')

            for o in pose_bones:
                if o.name.startswith('upper_arm_parent') and ".R" in o.name:
                    o["IK_FK"] = float(1)
                    o.keyframe_insert(data_path= '["IK_FK"]')

            
            for o in pose_bones:
                if o.name.startswith('upper_arm_fk') and ".L" in o.name:
                    o.rotation_quaternion[0] = 0.7
                    o.rotation_quaternion[1] = 0.5
                    o.rotation_quaternion[2] = -0.33
                    o.rotation_quaternion[3] = -0.28
                    o.keyframe_insert(data_path='rotation_quaternion')
                    o.bone.select = 1
                
            
            for o in pose_bones:
                if o.name.startswith('upper_arm_fk') and ".R" in o.name:
                    o.rotation_quaternion[0] = 0.7
                    o.rotation_quaternion[1] = 0.5
                    o.rotation_quaternion[2] = 0.33
                    o.rotation_quaternion[3] = 0.28
                    o.keyframe_insert(data_path='rotation_quaternion')
                    o.bone.select = 1
                
              
            for o in pose_bones:
                if o.name.startswith('forearm_fk') and ".L" in o.name:
                    o.rotation_quaternion[0] = 1
                    o.rotation_quaternion[1] = 0
                    o.rotation_quaternion[2] = 0
                    o.rotation_quaternion[3] = 0
                    o.keyframe_insert(data_path='rotation_quaternion')
                
           
            for o in pose_bones:
                if o.name.startswith('forearm_fk') and ".R" in o.name:
                    o.rotation_quaternion[0] = 1
                    o.rotation_quaternion[1] = 0
                    o.rotation_quaternion[2] = 0
                    o.rotation_quaternion[3] = 0
                    o.keyframe_insert(data_path='rotation_quaternion')
                
               
        arms_in_front_pos()



        return {'FINISHED'}






#  ARMS IN FRONT POSITION FOR SELECTED
class OBJECT_OT_rigify_arms_in_front_pos_selected(bpy.types.Operator):
    '''ARMS IN FRONT POSITION - SELECTED
Please Select  < upper_arm_fk >  - any Side'''
    bl_idname = "object.rigify_arms_in_front_pos_selected"
    bl_label = "In Front Sel"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')



    def execute(self, context):

 
        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS' 
         
         
        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.context.selected_pose_bones



        # =====================================================
        #   ARMS IN FRONT FOR "SELECT RELATED" (Selected)
        # =====================================================


        def arms_in_front_for_selected():
            

            for bone in pose_bones:
                if bone.name.startswith('upper_arm_parent') and ".L" in bone.name:
                    bone["IK_FK"] = float(1)
                    bone.keyframe_insert(data_path= '["IK_FK"]')



            for bone in pose_bones:
                if bone.name.startswith('upper_arm_parent') and ".R" in bone.name:
                    bone["IK_FK"] = float(1)
                    bone.keyframe_insert(data_path= '["IK_FK"]')
            
            
            
            bpy.ops.pose.select_all(action='DESELECT') 
            
            for bone in sel_bones:
                if bone.name.startswith('upper_arm_fk') and ".L" in bone.name:    
                    bone.rotation_quaternion[0] = 0.7
                    bone.rotation_quaternion[1] = 0.5
                    bone.rotation_quaternion[2] = -0.33
                    bone.rotation_quaternion[3] = -0.28
                    bone.keyframe_insert(data_path='rotation_quaternion')
                    bone.bone.select = 1
                     

            for bone in sel_bones:
                if bone.name.startswith('upper_arm_fk') and ".R" in bone.name:    
                    bone.rotation_quaternion[0] = 0.7
                    bone.rotation_quaternion[1] = 0.5
                    bone.rotation_quaternion[2] = 0.33
                    bone.rotation_quaternion[3] = 0.28
                    bone.keyframe_insert(data_path='rotation_quaternion')
                    bone.bone.select = 1


            for bone in sel_bones:
                if bone.name.startswith('forearm_fk') and ".L" in bone.name:    
                    bone.rotation_quaternion[0] = 1
                    bone.rotation_quaternion[1] = 0
                    bone.rotation_quaternion[2] = 0
                    bone.rotation_quaternion[3] = 0
                    bone.keyframe_insert(data_path='rotation_quaternion')
                     

            for bone in sel_bones:
                if bone.name.startswith('forearm_fk') and ".R" in bone.name:    
                    bone.rotation_quaternion[0] = 1
                    bone.rotation_quaternion[1] = 0
                    bone.rotation_quaternion[2] = 0
                    bone.rotation_quaternion[3] = 0
                    bone.keyframe_insert(data_path='rotation_quaternion')
                                       
           
        arms_in_front_for_selected()


        return {'FINISHED'}










#  ARMS UP POSITION
class OBJECT_OT_rigify_arms_up_pos(bpy.types.Operator):
    '''ARMS UP POSITION'''
    bl_idname = "object.rigify_arms_up_pos"
    bl_label = "Up"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):

        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS' 

         
        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.context.selected_pose_bones


# =====================================================
#   ARMS UP - ALL
# =====================================================

           
        def arms_up_pos():
            
            bpy.ops.pose.select_all(action='DESELECT')
            
            # Arms to FK
            for o in pose_bones:
                if o.name.startswith('upper_arm_parent') and ".L" in o.name:
                    o["IK_FK"] = float(1)
                    o.keyframe_insert(data_path= '["IK_FK"]')

            for o in pose_bones:
                if o.name.startswith('upper_arm_parent') and ".R" in o.name:
                    o["IK_FK"] = float(1)
                    o.keyframe_insert(data_path= '["IK_FK"]')

            
            for o in pose_bones:
                if o.name.startswith('upper_arm_fk') and ".L" in o.name:
                    o.rotation_quaternion[0] = 0.3
                    o.rotation_quaternion[1] = 0.7
                    o.rotation_quaternion[2] = -0.6
                    o.rotation_quaternion[3] = 0.05
                    o.keyframe_insert(data_path='rotation_quaternion')
                    o.bone.select = 1
                
            
            for o in pose_bones:
                if o.name.startswith('upper_arm_fk') and ".R" in o.name:
                    o.rotation_quaternion[0] = 0.3
                    o.rotation_quaternion[1] = 0.7
                    o.rotation_quaternion[2] = 0.6
                    o.rotation_quaternion[3] = -0.05
                    o.keyframe_insert(data_path='rotation_quaternion')
                    o.bone.select = 1
                
              
            for o in pose_bones:
                if o.name.startswith('forearm_fk') and ".L" in o.name:
                    o.rotation_quaternion[0] = 1
                    o.rotation_quaternion[1] = 0
                    o.rotation_quaternion[2] = 0
                    o.rotation_quaternion[3] = 0
                    o.keyframe_insert(data_path='rotation_quaternion')
                
           
            for o in pose_bones:
                if o.name.startswith('forearm_fk') and ".R" in o.name:
                    o.rotation_quaternion[0] = 1
                    o.rotation_quaternion[1] = 0
                    o.rotation_quaternion[2] = 0
                    o.rotation_quaternion[3] = 0
                    o.keyframe_insert(data_path='rotation_quaternion')
                
               
        arms_up_pos()

        return {'FINISHED'}







#  ARMS UP POSITION FOR SELECTED
class OBJECT_OT_rigify_arms_up_pos_selected(bpy.types.Operator):
    '''ARMS UP POSITION - SELECTED
Please Select  < upper_arm_fk >  - any Side'''
    bl_idname = "object.rigify_arms_up_pos_selected"
    bl_label = "Up Sel"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')



    def execute(self, context):

 
        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Set Pivot Point 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS' 
         
         
        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.context.selected_pose_bones



        # =====================================================
        #   ARMS UP FOR "SELECT RELATED" (Selected)
        # =====================================================


        def arms_up_pos_for_selected():
            

            for bone in pose_bones:
                if bone.name.startswith('upper_arm_parent') and ".L" in bone.name:
                    bone["IK_FK"] = float(1)
                    bone.keyframe_insert(data_path= '["IK_FK"]')



            for bone in pose_bones:
                if bone.name.startswith('upper_arm_parent') and ".R" in bone.name:
                    bone["IK_FK"] = float(1)
                    bone.keyframe_insert(data_path= '["IK_FK"]')
            
            
            
            bpy.ops.pose.select_all(action='DESELECT') 
            
            for bone in sel_bones:
                if bone.name.startswith('upper_arm_fk') and ".L" in bone.name:    
                    bone.rotation_quaternion[0] = 0.3
                    bone.rotation_quaternion[1] = 0.7
                    bone.rotation_quaternion[2] = -0.6
                    bone.rotation_quaternion[3] = 0.05
                    bone.keyframe_insert(data_path='rotation_quaternion')
                    bone.bone.select = 1
                     

            for bone in sel_bones:
                if bone.name.startswith('upper_arm_fk') and ".R" in bone.name:    
                    bone.rotation_quaternion[0] = 0.3
                    bone.rotation_quaternion[1] = 0.7
                    bone.rotation_quaternion[2] = 0.6
                    bone.rotation_quaternion[3] = -0.05
                    bone.keyframe_insert(data_path='rotation_quaternion')
                    bone.bone.select = 1

            for bone in sel_bones:
                if bone.name.startswith('forearm_fk') and ".L" in bone.name:    
                    bone.rotation_quaternion[0] = 1
                    bone.rotation_quaternion[1] = 0
                    bone.rotation_quaternion[2] = 0
                    bone.rotation_quaternion[3] = 0
                    bone.keyframe_insert(data_path='rotation_quaternion')
                     

            for bone in sel_bones:
                if bone.name.startswith('forearm_fk') and ".R" in bone.name:    
                    bone.rotation_quaternion[0] = 1
                    bone.rotation_quaternion[1] = 0
                    bone.rotation_quaternion[2] = 0
                    bone.rotation_quaternion[3] = 0
                    bone.keyframe_insert(data_path='rotation_quaternion')
                                       
           
        arms_up_pos_for_selected()


        return {'FINISHED'}



# =============================================================
#  ARMS POSITIONS: END
# =============================================================









# =============================================================
#  SELECT "RELATED"
# =============================================================




#  SELECT "RELATED"  
class OBJECT_OT_rigify_select_related_ra(bpy.types.Operator):
    '''SELECT RELATED ( CONNECTED )'''
    bl_idname = "object.rigify_select_related_ra"
    bl_label = "Select Related"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')



    def execute(self, context):


        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.context.selected_pose_bones


        bone_list = ('head', 'neck', 'chest', 'hips', 'torso',
                     'shoulder.R', 'shoulder.L',
                     'upper_arm_parent.R', 'upper_arm_parent.L',
                     'upper_arm_ik.R', 'upper_arm_ik.L', 'hand_ik.R', 'hand_ik.L', 
                     'upper_arm_fk.R', 'upper_arm_fk.L', 
                     'forearm_fk.R', 'forearm_fk.L', 'hand_fk.R', 'hand_fk.L',
                     'thigh_ik.R', 'thigh_ik.L',  'leg_L', 'leg_R', 'foot_L', 'foot_R',
                     'foot_ik.R', 'foot_ik.L', 'foot_heel_ik.R', 'foot_heel_ik.L',
                     'toe.R', 'toe.L', 'front_foot_ik.R', 'front_foot_ik.L', 'front_foot_heel_ik.R',
                     'front_foot_heel_ik.L', 'front_toe.R', 'front_toe.L', 'front_thigh_ik.R','front_thigh_ik.L',
                     'hind_foot_ik.L', 'hind_foot_ik.R', 'forefoot_ik.R', 'forefoot_ik.L',)



        # Selecting "Related" without numeric suffix
        for bone in sel_bones:
            if bone.name in bone_list:
                for o in pose_bones:
                    if o.name in bone_list:
                        o.bone.select = 1
                  
            
        # Selecting "Related" with numeric suffix 
        for i in sel_bones:
            name = i.name.split('.')
            name_spl = name[-1]  
           
            for o in pose_bones:        
                for i in bone_list:
                    if o.name.startswith(i) and o.name.endswith(name_spl):
                       o.bone.select = 1 
                    
 
        if len(sel_bones) == 0:
            for o in pose_bones:
                if o.name in bone_list:
                    o.bone.select = 1
                    
        


        return {'FINISHED'}







# =============================================================
#  SELECT "NEXT"
# =============================================================




#  SELECT "NEXT"  
class OBJECT_OT_rigify_select_next_ra(bpy.types.Operator):
    '''SELECT NEXT => RELATED ( CONNECTED )'''
    bl_idname = "object.rigify_select_next_ra"
    bl_label = "Select Next"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)



    def execute(self, context):


        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.context.selected_pose_bones


        bone_list = ('head', 'neck', 'chest', 'hips', 'torso',
                     'shoulder.R', 'shoulder.L',
                     'upper_arm_parent.R', 'upper_arm_parent.L',
                     'upper_arm_ik.R', 'upper_arm_ik.L', 'hand_ik.R', 'hand_ik.L', 
                     'upper_arm_fk.R', 'upper_arm_fk.L', 
                     'forearm_fk.R', 'forearm_fk.L', 'hand_fk.R', 'hand_fk.L',
                     'thigh_ik.R', 'thigh_ik.L',  'leg_L', 'leg_R', 'foot_L', 'foot_R',
                     'foot_ik.R', 'foot_ik.L', 'foot_heel_ik.R', 'foot_heel_ik.L',
                     'toe.R', 'toe.L', 'front_foot_ik.R', 'front_foot_ik.L', 'front_foot_heel_ik.R',
                     'front_foot_heel_ik.L', 'front_toe.R', 'front_toe.L', 'front_thigh_ik.R','front_thigh_ik.L',)


        # Selecting "Related" without numeric suffix
                     
        for bone in sel_bones:
            if bone.name in bone_list:
                for o in pose_bones:
                    o.bone.select = 0
                    for i in bone_list:
                        if o.name.startswith(i) and '.001' in o.name:
                            o.bone.select = 1

                            
        # Selecting "Related" with numeric suffix 
        try:
            
            for i in sel_bones:
                name = i.name.split('.')
                i.bone.select = 0 
                    
                name_spl = int(name[-1]) + int(1) 
           
                for o in pose_bones:        
                    for i in bone_list:
                        if o.name.startswith(i) and o.name.endswith(str(name_spl)):
                           o.bone.select = 1 
                         

        except ValueError:
            pass        

                
            
        return {'FINISHED'}







classes = [
            # Select Fingers
            OBJECT_OT_rigify_sel_fingers_left, OBJECT_OT_rigify_sel_fingers_right,
            OBJECT_OT_rigify_sel_fingers_both_hands_ra,

            # SET
            OBJECT_OT_rigify_head_sel, OBJECT_OT_rigify_torso_sel, OBJECT_OT_rigify_chest_sel,
            OBJECT_OT_rigify_sel_set_move_rig,

            # FEET
            OBJECT_OT_rigify_feet_sel,

            # Arms Hands
            OBJECT_OT_rigify_hands_sel, OBJECT_OT_rigify_left_arm_sel, OBJECT_OT_rigify_right_arm_sel,

            # ARMS POSITIONS
            OBJECT_OT_rigify_arms_down_pos, OBJECT_OT_rigify_arms_down_pos_selected,
            OBJECT_OT_rigify_arms_in_front_pos, OBJECT_OT_rigify_arms_in_front_pos_selected,
            OBJECT_OT_rigify_arms_up_pos, OBJECT_OT_rigify_arms_up_pos_selected,

            # SELECT RELATED
            OBJECT_OT_rigify_select_related_ra,

            #SELECT NEXT
            OBJECT_OT_rigify_select_next_ra,

          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()








