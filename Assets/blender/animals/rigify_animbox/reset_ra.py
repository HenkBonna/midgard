import bpy


# AUTOMATIC FOOT DOWN FOR RIGIFY;
# RESET ...;



# =====================================================
#               AUTOMATIC FOOT DOWN FOR RIGIFY
# =====================================================


# AUTOMATIC FOOT DOWN FOR RIGIFY - LEFT
class OBJECT_OT_rigify_auto_foot_down_left_ra(bpy.types.Operator):
    '''Left Foot Down - Rigify.\nWithout Selection.'''
    bl_idname = "object.rigify_auto_foot_down_left_ra"
    bl_label = "L"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def execute(self, context):

        pose_bones = bpy.context.object.pose.bones
    
        bpy.ops.pose.select_all(action = 'DESELECT')
           
        for o in pose_bones:
            if o.name.startswith('foot_ik') and ".L" in o.name:
                o.bone.select = 1
                o.location[2] = 0  
                o.rotation_quaternion[1] = 0
                o.rotation_quaternion[2] = 0
                o.rotation_euler[0] = 0
                o.rotation_euler[1] = 0        


        for o in pose_bones:
            if o.name.startswith('foot_heel_ik') and ".L" in o.name: 
                o.bone.select = 1
                o.rotation_quaternion[1] = 0
                o.rotation_quaternion[2] = 0
                o.rotation_euler[0] = 0
                o.rotation_euler[1] = 0        

        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        bpy.ops.pose.select_all(action = 'DESELECT')

        for o in pose_bones:
            if o.name.startswith('foot_ik') and ".L" in o.name:
                o.bone.select = 1


        return {'FINISHED'}



# AUTOMATIC FOOT DOWN FOR RIGIFY - RIGHT
class OBJECT_OT_rigify_auto_foot_down_right_ra(bpy.types.Operator):
    '''Right Foot Down - Rigify.\nWithout Selection.'''
    bl_idname = "object.rigify_auto_foot_down_right_ra"
    bl_label = "R"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def execute(self, context):

        pose_bones = bpy.context.object.pose.bones
    
        bpy.ops.pose.select_all(action = 'DESELECT')
           
        for o in pose_bones:
            if o.name.startswith('foot_ik') and ".R" in o.name:
                o.bone.select = 1
                o.location[2] = 0  
                o.rotation_quaternion[1] = 0
                o.rotation_quaternion[2] = 0
                o.rotation_euler[0] = 0
                o.rotation_euler[1] = 0        


        for o in pose_bones:
            if o.name.startswith('foot_heel_ik') and ".R" in o.name: 
                o.bone.select = 1
                o.rotation_quaternion[1] = 0
                o.rotation_quaternion[2] = 0
                o.rotation_euler[0] = 0
                o.rotation_euler[1] = 0        

        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        bpy.ops.pose.select_all(action = 'DESELECT')

        for o in pose_bones:
            if o.name.startswith('foot_ik') and ".R" in o.name:
                o.bone.select = 1
                


        return {'FINISHED'}





# AUTOMATIC FOOT DOWN FOR RIGIFY - BOTH
class OBJECT_OT_rigify_auto_foot_down_both_ra(bpy.types.Operator):
    '''Both Feet Down - Rigify.\nWithout Selection.'''
    bl_idname = "object.rigify_auto_foot_down_both_ra"
    bl_label = "B"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def execute(self, context):

        pose_bones = bpy.context.object.pose.bones
    
        bpy.ops.pose.select_all(action = 'DESELECT')
           
        for o in pose_bones:
            if o.name.startswith('foot_ik') and ".R" in o.name:
                o.bone.select = 1
                o.location[2] = 0  
                o.rotation_quaternion[1] = 0
                o.rotation_quaternion[2] = 0
                o.rotation_euler[0] = 0
                o.rotation_euler[1] = 0        


        for o in pose_bones:
            if o.name.startswith('foot_heel_ik') and ".R" in o.name: 
                o.bone.select = 1
                o.rotation_quaternion[1] = 0
                o.rotation_quaternion[2] = 0
                o.rotation_euler[0] = 0
                o.rotation_euler[1] = 0        

    
        for o in pose_bones:
            if o.name.startswith('foot_ik') and ".L" in o.name:
                o.bone.select = 1
                o.location[2] = 0  
                o.rotation_quaternion[1] = 0
                o.rotation_quaternion[2] = 0
                o.rotation_euler[0] = 0
                o.rotation_euler[1] = 0        


        for o in pose_bones:
            if o.name.startswith('foot_heel_ik') and ".L" in o.name: 
                o.bone.select = 1
                o.rotation_quaternion[1] = 0
                o.rotation_quaternion[2] = 0
                o.rotation_euler[0] = 0
                o.rotation_euler[1] = 0   


        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        bpy.ops.pose.select_all(action = 'DESELECT')

        for o in pose_bones:
            if o.name.startswith('foot_ik') and ".R" in o.name:
                o.bone.select = 1
                
        for o in pose_bones:
            if o.name.startswith('foot_ik') and ".L" in o.name:
                o.bone.select = 1
                

        return {'FINISHED'}




# =====================================================
#                       RESET SELECTION MIRRORED
# =====================================================


# reset all transform, scale, rotate for Selected
class OBJECT_OT_duo_reset_pose_selected_ra(bpy.types.Operator):
    '''Reset Mirrored.'''
    bl_idname = "object.duo_reset_pose_selected_ra"
    bl_label = "RM"
    bl_options = {'REGISTER', 'UNDO'}
    

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')

    
    def execute(self, context):

        bpy.ops.pose.select_mirror(extend=True)

        sel_bone = bpy.context.selected_pose_bones

        for i in sel_bone:
                bpy.ops.pose.rot_clear()
                bpy.ops.pose.loc_clear()
                bpy.ops.pose.scale_clear()
                bpy.ops.anim.keyframe_insert(type='LocRotScale')

       
        return {'FINISHED'}


# =====================================================
#                       RESET SELECTED
# =====================================================


# reset all transform, scale, rotate for Selected
class OBJECT_OT_reset_pose_selected_ra(bpy.types.Operator):
    '''Reset Selected.'''
    bl_idname = "object.reset_pose_selected_ra"
    bl_label = "RS"
    bl_options = {'REGISTER', 'UNDO'}
    

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def execute(self, context):

        sel_bone = bpy.context.selected_pose_bones

        for i in sel_bone:
                bpy.ops.pose.rot_clear()
                bpy.ops.pose.loc_clear()
                bpy.ops.pose.scale_clear()
                bpy.ops.anim.keyframe_insert(type='LocRotScale')

       
        return {'FINISHED'}


# =====================================================
#                       RESET WHOLE POSE
# =====================================================


# reset all transform, scale, rotate
class OBJECT_OT_reset_pose_all_ra(bpy.types.Operator):
    '''Reset Whole Pose'''
    bl_idname = "object.reset_pose_all_ra"
    bl_label = "RP"
    bl_options = {'REGISTER', 'UNDO'}
    

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def execute(self, context):
        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        bpy.ops.pose.select_all(action = 'DESELECT')
              
        return {'FINISHED'}


# =====================================================
#                       TOTAL RESET 
# =====================================================

# RESET ALL TRANSFORMATIONS, DELETE ALL KEYS, GO TO START 
class OBJECT_OT_qpf_total_reset_ra(bpy.types.Operator):
    '''TOTAL RESET !\nReset All Transformations, Delete All Keys, Go to Start.'''
    bl_idname = "object.qpf_total_reset_ra"
    bl_label = "TR"
    bl_options = {'REGISTER', 'UNDO'}
    

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')

   
    def execute(self, context):
        bpy.ops.pose.select_all(action = 'SELECT')

        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        
        bpy.ops.anim.keyframe_clear_v3d()

        bpy.ops.pose.select_all(action = 'DESELECT')

        bpy.ops.screen.frame_jump(end=False)

        # Clear Pose Motion Path
        bpy.ops.pose.paths_clear()
              
        return {'FINISHED'}





# =====================================================
#                PUT SELECTED FOOT DOWN
# =====================================================



# PUT FOOT ON FLOOR (PLANT) FOR RIGIFY_LIKE RIGS
class OBJECT_OT_plant_sel_foot_down_rigify_ra(bpy.types.Operator):
    '''Put Selected Foot Down - Rigify'''
    bl_idname = "object.plant_sel_foot_down_rigify_ra"
    bl_label = "Foot Down Rigify"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    def execute(self, context):
        #rig_bones = bpy.context.object.pose.bones
        sel_bones = bpy.context.selected_pose_bones_from_active_object
        for bones in sel_bones:
            bones.location[2] = 0
            bones.rotation_quaternion[1] = 0
            bones.rotation_quaternion[2] = 0
            bones.rotation_euler[0] = 0 
            bones.rotation_euler[1] = 0
            bpy.ops.anim.keyframe_insert(type='LocRotScale')

        return {'FINISHED'}






# PUT FOOT ON FLOOR (PLANT) FOR OTHER RIGS
class OBJECT_OT_plant_sel_foot_down_not_rigify_ra(bpy.types.Operator):
    '''Put Selected Foot Down  - Non Rigify'''
    bl_idname = "object.plant_sel_foot_down_not_rigify_ra"
    bl_label = "Foot Down - Non Rigify"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    def execute(self, context):
        #rig_bones = bpy.context.object.pose.bones
        sel_bones = bpy.context.selected_pose_bones_from_active_object
        for bones in sel_bones:
            bones.location[1] = 0
            bones.rotation_quaternion[1] = 0
            bones.rotation_quaternion[2] = 0
            bones.rotation_euler[0] = 0 
            bones.rotation_euler[1] = 0
            bpy.ops.anim.keyframe_insert(type='LocRotScale')

        return {'FINISHED'}











classes = [ OBJECT_OT_duo_reset_pose_selected_ra, OBJECT_OT_reset_pose_selected_ra,
            OBJECT_OT_reset_pose_all_ra, OBJECT_OT_qpf_total_reset_ra,

            # Auto Foot/Feet Down
            OBJECT_OT_rigify_auto_foot_down_both_ra,
            OBJECT_OT_rigify_auto_foot_down_right_ra,
            OBJECT_OT_rigify_auto_foot_down_left_ra,

            # Selected Foot/Feet Down
            OBJECT_OT_plant_sel_foot_down_rigify_ra,
            OBJECT_OT_plant_sel_foot_down_not_rigify_ra,


          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()







        
