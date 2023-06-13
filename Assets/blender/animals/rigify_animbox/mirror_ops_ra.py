import bpy
import rna_keymap_ui




# MIRROR POSE AFTER


# =====================================================
#               MIRROR POSE AFTER
# =====================================================




# Mirror Pose after choosen amount of frames (with keys set)
class OBJECT_OT_mirror_pose_after_num_ra(bpy.types.Operator):
    '''Mirror Pose After Number of Frames

If Nothing is Selected : 
    Mirror all bones that are NOT in the Rest Pose -

If Selected (Just One Side): Mirror Only Selected'''
    bl_idname = "object.mirror_pose_after_num_ra"
    bl_label = "Mirror Pose After :"
    bl_options = {'REGISTER', 'UNDO'} 


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' )



    def execute(self, context):

        scene = context.scene      
        frame_int =  scene.animbox_ra_props.frame_int 


        # Mirror After All Bones that are NOT in Rest Pose  
        def mirror_after_all_that_not_in_restpose(): 
                            
            pose_bones = bpy.context.object.pose.bones
      
            for o in pose_bones:

            # Location
                if o.location.x != 0:
                    o.bone.select = 1
                
                if o.location.z != 0:
                    o.bone.select = 1
                    
                if o.location.y != 0:
                    o.bone.select = 1
                        

            # Quaternion
                if o.rotation_quaternion.x != 0:
                    o.bone.select = 1

                if o.rotation_quaternion.y != 0:
                    o.bone.select = 1

                if o.rotation_quaternion.z != 0:
                    o.bone.select = 1

            # Euler
                if o.rotation_euler.x != 0:
                    o.bone.select = 1

                if o.rotation_euler.y != 0:
                    o.bone.select = 1

                if o.rotation_euler.z != 0:
                    o.bone.select = 1


            # Scale
                if o.scale.x !=1:
                    o.bone.select = 1
                if o.scale.y !=1:
                    o.bone.select = 1
                if o.scale.z !=1:
                    o.bone.select = 1
                                                  
              

            bpy.ops.pose.select_mirror(extend=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.copy()
            bpy.context.scene.frame_current += frame_int
            bpy.ops.pose.paste(flipped=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')


 
        # Mirror After ONLY SELECTED 
        def mirror_after_only_selected(): 
          
            bpy.ops.pose.select_mirror(extend=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.copy()
            bpy.context.scene.frame_current += frame_int
            bpy.ops.pose.paste(flipped=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')



        # Condition
        sel_bones = bpy.context.selected_pose_bones

        if len(sel_bones) == 0:
            mirror_after_all_that_not_in_restpose() 

        if len(sel_bones) != 0:
            mirror_after_only_selected()



        return {'FINISHED'}






 
# Mirror SELECTED to Opposite Side -  (with keys set)
class OBJECT_OT_copy_sel_to_opposite_ra(bpy.types.Operator):
    '''Copy -> Paste Selected To Opposite Side'''
    bl_idname = "object.copy_sel_to_opposite_ra"
    bl_label = "Selected to Opposite"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    def execute(self, context):
    
        bpy.ops.pose.copy()
        bpy.ops.pose.paste(flipped=True)
        bpy.ops.pose.select_mirror(extend=True)
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        

        return {'FINISHED'}








# Mirror Both Sides of a Pose - WITH ONLY ONE SELECTED SIDE (keys set)
class OBJECT_OT_mirror_pose_in_place_ra(bpy.types.Operator):
    '''If Nothing is Selected : 
    Mirror all bones that are NOT in the Rest Pose -

If Selected (Just One Side) - Mirror Only Selected'''
    bl_idname = "object.mirror_pose_in_place_ra"
    bl_label = "Mirror Pose"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def execute(self, context):


        # Mirror All Bones that are NOT in Rest Pose  
        def mirror_all_that_not_in_restpose(): 
                            
            pose_bones = bpy.context.object.pose.bones
      
            for o in pose_bones:

            # Location
                if o.location.x != 0:
                    o.bone.select = 1
                
                if o.location.z != 0:
                    o.bone.select = 1
                    
                if o.location.y != 0:
                    o.bone.select = 1
                        

            # Quaternion
                if o.rotation_quaternion.x != 0:
                    o.bone.select = 1

                if o.rotation_quaternion.y != 0:
                    o.bone.select = 1

                if o.rotation_quaternion.z != 0:
                    o.bone.select = 1

            # Euler
                if o.rotation_euler.x != 0:
                    o.bone.select = 1

                if o.rotation_euler.y != 0:
                    o.bone.select = 1

                if o.rotation_euler.z != 0:
                    o.bone.select = 1


            # Scale
                if o.scale.x !=1:
                    o.bone.select = 1
                if o.scale.y !=1:
                    o.bone.select = 1
                if o.scale.z !=1:
                    o.bone.select = 1
                                                  
              

            bpy.ops.pose.select_mirror(extend=True)
            bpy.ops.pose.copy()
            bpy.ops.pose.paste(flipped=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')


        # Mirror ONLY SELECTED 
        def mirror_only_selected(): 

            bpy.ops.pose.select_mirror(extend=True)
            bpy.ops.pose.copy()
            bpy.ops.pose.paste(flipped=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')


        # Condition
        sel_bones = bpy.context.selected_pose_bones

        if len(sel_bones) == 0:
            mirror_all_that_not_in_restpose()

        if len(sel_bones) != 0:
            mirror_only_selected()



        return {'FINISHED'}
       









# =====================================================
#                      COPY POSE
# =====================================================




# COPY Pose after choosen amount of frames 
class OBJECT_OT_copy_pose_after_num_ra(bpy.types.Operator):
    '''Copy Pose After Number of Frames

If Nothing is Selected : 
    Copy all bones that are NOT in the Rest Pose -

If Selected : Copy Only Selected'''
    bl_idname = "object.copy_pose_after_num_ra"
    bl_label = "Copy Pose After :"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def execute(self, context):
        scene = context.scene      
        frame_int =  scene.animbox_ra_props.frame_int    
   
 
        # COPY After All Bones that are NOT in Rest Pose  
        def copy_after_all_that_not_in_restpose(): 
                            
            pose_bones = bpy.context.object.pose.bones
      
            for o in pose_bones:

            # Location
                if o.location.x != 0:
                    o.bone.select = 1
                
                if o.location.z != 0:
                    o.bone.select = 1
                    
                if o.location.y != 0:
                    o.bone.select = 1
                        

            # Quaternion
                if o.rotation_quaternion.x != 0:
                    o.bone.select = 1

                if o.rotation_quaternion.y != 0:
                    o.bone.select = 1

                if o.rotation_quaternion.z != 0:
                    o.bone.select = 1

            # Euler
                if o.rotation_euler.x != 0:
                    o.bone.select = 1

                if o.rotation_euler.y != 0:
                    o.bone.select = 1

                if o.rotation_euler.z != 0:
                    o.bone.select = 1


            # Scale
                if o.scale.x !=1:
                    o.bone.select = 1
                if o.scale.y !=1:
                    o.bone.select = 1
                if o.scale.z !=1:
                    o.bone.select = 1
                                                  
              
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.copy()
            bpy.context.scene.frame_current += frame_int  
            bpy.ops.pose.paste(flipped=False)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')



        # COPY After Only Selected 
        def copy_after_only_selected(): 

            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.copy()
            bpy.context.scene.frame_current += frame_int  
            bpy.ops.pose.paste(flipped=False)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')



        # Condition
        sel_bones = bpy.context.selected_pose_bones

        if len(sel_bones) == 0:
            copy_after_all_that_not_in_restpose() 

        if len(sel_bones) != 0:
            copy_after_only_selected()



        return {'FINISHED'}



# =====================================================
#             END    COPY POSE
# =====================================================







# =====================================================
#   RIGIFY  MIRROR FEET IK / HAND IK / ARMS + FOREARMS
# =====================================================

# FEET IK


# Mirror Rigify FEET IK  Without Selection
class OBJECT_OT_auto_mirror_rigify_feet_ik_ra(bpy.types.Operator):
    '''Auto Mirror Rigify Feet IK - without Selection
Auto Insert Keys => Loc-Rot-Scale
Ctrl-Click - Mirror Feet IK + Heel IK'''
    bl_idname = "object.auto_mirror_rigify_feet_ik_ra"
    bl_label = "Feet IK"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def invoke(self, context, event):

        pose_bones = bpy.context.object.pose.bones

        # Click and Mirror only Feet IK
        if event: 
            for o in pose_bones:
                if o.name.startswith('foot_ik'):
                    o.bone.select = 1  

 

        # Ctrl + Click and Mirror Feet IK + Heel IK
        if event.ctrl:
            for o in pose_bones:
                if o.name.startswith(('foot_ik', 'foot_heel_ik')):
                    o.bone.select = 1  



        sel_bones = bpy.context.selected_pose_bones

        if len(sel_bones) != 0:

            bpy.ops.pose.select_mirror(extend=True)
            bpy.ops.pose.copy()
            bpy.ops.pose.paste(flipped=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.select_all(action = 'DESELECT')
     
 
        return {'FINISHED'}
       

# END FEET IK



# HANDS IK


# Mirror Rigify HANDS IK  Without Selection
class OBJECT_OT_auto_mirror_rigify_hands_ik_ra(bpy.types.Operator):
    '''Auto Mirror Rigify Hand IK - without Selection
Auto Insert Keys => Loc-Rot-Scale'''
    bl_idname = "object.auto_mirror_rigify_hands_ik_ra"
    bl_label = "Hands IK"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def execute(self, context):

        pose_bones = bpy.context.object.pose.bones

        for o in pose_bones:
            if o.name.startswith('hand_ik'):
                o.bone.select = 1
                

        sel_bones = bpy.context.selected_pose_bones

        if len(sel_bones) != 0:

            bpy.ops.pose.select_mirror(extend=True)
            bpy.ops.pose.copy()
            bpy.ops.pose.paste(flipped=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.select_all(action = 'DESELECT')


        return {'FINISHED'}
       

# END HANDS IK




# ARMS + FOREARMS


# Mirror Rigify ARMS + FOREARMS Without Selection
class OBJECT_OT_auto_mirror_rigify_arms_forearms_ra(bpy.types.Operator):
    '''Auto Mirror Rigify Arms + Forearms - without Selection
Auto Insert Keys => Loc-Rot-Scale'''
    bl_idname = "object.auto_mirror_rigify_arms_forearms_ra"
    bl_label = "Arms"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def execute(self, context):


        pose_bones = bpy.context.object.pose.bones

        for o in pose_bones:
            
            if o.name.startswith('upper_arm_fk'):
                o.bone.select = 1
                            
            if o.name.startswith('forearm_fk'):
                o.bone.select = 1
        
        sel_bones = bpy.context.selected_pose_bones

        if len(sel_bones) != 0:
            
            bpy.ops.pose.select_mirror(extend=True)
            bpy.ops.pose.copy()
            bpy.ops.pose.paste(flipped=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.select_all(action = 'DESELECT')


        return {'FINISHED'}
       

# END ARMS + FOREARMS







#==============================================
#  SMART MIRROR AFTER SELECTED
#==============================================


# This will mirror selected in the second half of the Timeline with an equal number of Frames
class OBJECT_OT_smart_mirror_pose_after_sel_ra(bpy.types.Operator):
    '''Mirror Selected in the Second Half of the Timeline -
with an Equal Number of Frames'''

    bl_idname = "object.smart_mirror_pose_after_sel_ra"
    bl_label = "Smart Mirror-Selected"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE'
                and len(context.selected_pose_bones) != 0 
                and context.scene.frame_start >= 1 )


    def execute(self, context):


        def not_central_bone():
            sel_bones = bpy.context.selected_pose_bones
            for b in sel_bones:
                if '.L' in b.name or '.R' in b.name:
                    return True
                

        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        bpy.ops.pose.copy()

        if not_central_bone():
            bpy.ops.pose.select_mirror(extend=False) 
        else:
            bpy.ops.pose.select_mirror(extend=True) 
         


        def middle_of_timeline():
            
            #  TIMELINE / 2 (CONDITION)
            
            fs = bpy.context.scene.frame_start
            fe = bpy.context.scene.frame_end
                     
            if fs == 1:
                if fe % 2 == 0:        
                    bpy.context.scene.frame_current = int(fe / 2 + 1)
                    
                if fe % 2 != 0:
                    bpy.context.scene.frame_current = int(fe / 2 + 1)
                    
                          
            if fs > 1:
                f_num = (fs + fe) - 1
                if f_num % 2 == 0:
                    bpy.context.scene.frame_current  = int(f_num / 2 + 1)

                if f_num % 2 != 0:
                    bpy.context.scene.frame_current  = int(f_num / 2 + 1)
           
           
        #middle_of_timeline()   
           
                                           
         
        def middle_of_timeline_plus():

            fs = bpy.context.scene.frame_start
            fe = bpy.context.scene.frame_end
            

            if fs == 1:
                        
                if fe % 2 == 0:
                    f_num = int(fe / 2 + 1)
                else:
                    f_num = int(fe / 2 + 1)

                bpy.context.scene.frame_set(f_num + (bpy.context.scene.frame_current - 1))
                        
                
            if fs > 1:

                f_num = ((fs + fe) - (bpy.context.scene.frame_current + fe)) * -1
    
                middle_of_timeline() 
                
                bpy.context.scene.frame_current += f_num
                 

        middle_of_timeline_plus()


            
        bpy.ops.pose.paste(flipped=True)
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        bpy.ops.pose.select_all(action='DESELECT')
         
        return {'FINISHED'}


#==============================================
# END SMART MIRROR AFTER SELECTED
#==============================================








classes = [ 
            OBJECT_OT_mirror_pose_after_num_ra, OBJECT_OT_copy_sel_to_opposite_ra,
            OBJECT_OT_mirror_pose_in_place_ra,

            # Rigify Auto Mirror Feet IK, Hands IK, Arms + Forearms
            OBJECT_OT_auto_mirror_rigify_feet_ik_ra,
            OBJECT_OT_auto_mirror_rigify_hands_ik_ra,
            OBJECT_OT_auto_mirror_rigify_arms_forearms_ra,

            # Smart Mirror Selected
            OBJECT_OT_smart_mirror_pose_after_sel_ra,

            # Copy Pose
            OBJECT_OT_copy_pose_after_num_ra,


          ]



addon_keymaps = []

def register():

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        # Mirror Tools Shortcuts

        km = kc.keymaps.new(name='3D View', space_type= 'VIEW_3D')
        kmi = km.keymap_items.new("object.mirror_pose_in_place_ra", type = 'NONE', value = 'PRESS', shift=1, ctrl=1, alt=1)
        km = kc.keymaps.new(name='3D View', space_type= 'VIEW_3D')
        kmi = km.keymap_items.new("object.copy_sel_to_opposite_ra", type = 'NONE', value = 'PRESS', shift=1, ctrl=1, alt=1)

        addon_keymaps.append((km, kmi))




    for cls in classes:
        bpy.utils.register_class(cls)






def unregister():

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()




    for cls in classes:
        bpy.utils.unregister_class(cls)





if __name__ == "__main__":
    register()





