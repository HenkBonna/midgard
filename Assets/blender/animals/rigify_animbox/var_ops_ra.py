import bpy

import rna_keymap_ui


# GRAPH_EDITOR 



# =====================================================
#                      GRAPH_EDITOR
# =====================================================

# Open GRAPH_EDITOR in new window
class OBJECT_OT_graph_editor_open_ra(bpy.types.Operator):
    '''Open GRAPH EDITOR in new window'''
    bl_idname = "object.graph_editor_open_ra"
    bl_label = "Graph Editor"
    
    def execute(self, context):
        render = bpy.context.scene.render
        render.resolution_x = 1024
        render.resolution_y = 480
        render.resolution_percentage = 100
        
        bpy.ops.render.view_show("INVOKE_DEFAULT")
        
        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.type = "GRAPH_EDITOR"
        
        # bpy.context.space_data.show_group_colors = False
        bpy.context.space_data.use_only_selected_curves_handles = True
        bpy.context.space_data.use_only_selected_keyframe_handles = True
        
        return {'FINISHED'}



 

# =====================================================
#                       KEY OPS
# =====================================================


# INSERT KEY ON SELECTED ('LocRotScale')
class OBJECT_OT_insert_key_ra(bpy.types.Operator):
    '''Key SELECTED'''
    bl_idname = "object.insert_key_ra"
    bl_label = "KS"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)



    def execute(self, context):
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        return {'FINISHED'}






# SELECT ALL AND INSERT KEY ('LocRotScale') , keep selection
class OBJECT_OT_insert_key_all_ra(bpy.types.Operator):
    '''Key ALL'''
    bl_idname = "object.insert_key_all_ra"
    bl_label = "All"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):

        pose_bn = bpy.context.pose_object.pose.bones
        sel_pb = bpy.context.selected_pose_bones

        bone_list = []

        if len(sel_pb) == 0:
            bpy.ops.pose.select_all(action = 'SELECT')
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.select_all(action = 'DESELECT')

        if len(sel_pb) == 1:
            bone_to_sel = sel_pb[0].bone
            bpy.ops.pose.select_all(action = 'SELECT')
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.select_all(action = 'DESELECT')   
            
            bone_to_sel.select = 1 

         
        if len(sel_pb) > 1:
            for bn in sel_pb:
                bone_list.append(bn.name) 
                bpy.ops.pose.select_all(action = 'SELECT')
                bpy.ops.anim.keyframe_insert(type='LocRotScale')
                bpy.ops.pose.select_all(action = 'DESELECT')
         
            for ob in pose_bn:
                if ob.name in bone_list:
                    ob.bone.select = 1


        return {'FINISHED'}





# INSERT KEY ON SELECTED MIRRORED ('LocRotScale')
class OBJECT_OT_duo_insert_key_ra(bpy.types.Operator):
    '''Key Mirrored\nSelected and Opposite Side'''
    bl_idname = "object.duo_insert_key_ra"
    bl_label = "KM"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    def execute(self, context):
        bpy.ops.pose.select_mirror(extend=True)
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

        return {'FINISHED'}







 
# POSE KEYFRAME
class OBJECT_OT_insert_pose_keyframe_animbox_ra(bpy.types.Operator):
    '''Insert and mirror Keyframe(s) only if -
- Bone Location, Rotation, or Scale value differs from the "Rest Pose"
- There is no need for selection '''

    bl_idname = "object.insert_pose_keyframe_animbox_ra"
    bl_label = "Pose Keyframe"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):


        sel_pb = bpy.context.selected_pose_bones
        pose_bn = bpy.context.object.pose.bones
  
  
        bone_list = []

        if len(sel_pb) == 1:
            bone_to_sel = sel_pb[0].bone
            
            bone_list.append(bone_to_sel.name)     
            
            
        if len(sel_pb) > 1: 
            for bn in sel_pb:
                bone_list.append(bn.name)            
            
            
        bpy.ops.pose.select_all(action = 'DESELECT')


        def key_posed_bone():
            

            for b in pose_bn:
                
            # loc
                if b.location[0] != 0:
                    b.bone.select = 1
                    

                if b.location[1] != 0:
                    b.bone.select = 1 


                if b.location[2] != 0:
                    b.bone.select = 1 


            # rot quat
                if b.rotation_quaternion[0] != 1:
                    b.bone.select = 1

                    
                if b.rotation_quaternion[1] != 0:
                    b.bone.select = 1

                    
                if b.rotation_quaternion[2] != 0:
                    b.bone.select = 1

                    
                if b.rotation_quaternion[3] != 0:
                    b.bone.select = 1

                    
            # rot euler
                if b.rotation_euler[0] != 0:
                    b.bone.select = 1


                if b.rotation_euler[1] != 0:
                    b.bone.select = 1

                    
                if b.rotation_euler[2] != 0:
                    b.bone.select = 1            

               
            # scale
                if b.scale[0] != 1:
                    b.bone.select = 1

     
                if b.scale[1] != 1:
                    b.bone.select = 1

   
                if b.scale[2] != 1:
                    b.bone.select = 1
                              
                                 
        key_posed_bone()


        #--------------------------

        sel_pb = bpy.context.selected_pose_bones
        
        if len(sel_pb) != 0:
        
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.select_mirror()
            
            sel_pb = bpy.context.selected_pose_bones
            
            if len(sel_pb) != 0:
                bpy.ops.anim.keyframe_insert(type='LocRotScale')
                
                bpy.ops.pose.select_all(action = 'DESELECT')

        #--------------------------

        # Restore initial Selection
        pose_bn = bpy.context.object.pose.bones
        for b in pose_bn:
            if b.name in bone_list:
                b.bone.select = 1
   
      
        # Auto Keyframe ON
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
 


        return {'FINISHED'}






# =====================================================
#  MOTION PATH (In Range / Scene Frame Range)
# =====================================================



class OBJECT_OT_motion_path_cfpr_objects_bones_ra(bpy.types.Operator):
    '''Motion Path (In Range / Scene Frame Range)
    
Alt + Click to Clear'''

    bl_idname = "object.motion_path_cfpr_objects_bones_ra"
    bl_label = "Motion Path"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None )
 

    def invoke(self, context, event):  
        

        # Auto Keys ON
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True         


        def motion_path_blender_33():   
            
            if bpy.context.object.mode == 'OBJECT':
                
                if event:       
                    bpy.ops.object.paths_calculate(display_type='RANGE', range='SCENE')


                if event.alt:
                    # Clear Motion Path
                    bpy.ops.object.paths_clear()


            if bpy.context.object.mode == 'POSE':    
                        
                if event:
                    bpy.ops.pose.paths_calculate(display_type='RANGE', range='SCENE')
       

                if event.alt:
                    # Clear Motion Path
                    bpy.ops.pose.paths_clear()
                

        def motion_path_blender_29_31():

            cur_frame = bpy.context.scene.frame_current 

            if cur_frame > 2:
                if bpy.context.object.mode == 'OBJECT':
                    if event:
                        bpy.ops.object.paths_calculate(start_frame=1, end_frame=cur_frame)
            

                    if event.alt:
                        # Clear Motion Path
                        bpy.ops.object.paths_clear()


                if bpy.context.object.mode == 'POSE':
                    if event:
                        bpy.ops.pose.paths_calculate(start_frame=1, end_frame=cur_frame)
                        

                    if event.alt:
                        # Clear Motion Path
                        bpy.ops.pose.paths_clear()
                        

        bv = bpy.app.version_string

        if bv[0] == '3' and bv[2] == '1':
            motion_path_blender_29_31()

        if bv[0] == '2' and bv[2] == '9':
            motion_path_blender_29_31()

        if bv[0] == '3' and bv[2] == '3':
            motion_path_blender_33()

        if bv[0] == '3' and bv[2] == '4':
            motion_path_blender_33()

        if bv[0] == '3' and bv[2] == '5':
            motion_path_blender_33()



        return {'FINISHED'}



# =====================================================
#  END  MOTION PATH
# =====================================================








# =====================================================
#  BAKE OBJECT AND CLEAR PARENT / CONSTRAINT 'CHILD OF'
# =====================================================




# Bake and Clear Parent / Constraint 'Child Of' ( Without Keyframes on Object)
class OBJECT_OT_bake_clear_parent_constraint_object_ra(bpy.types.Operator):
    '''Bake Parent/Constraint ( "Child Of" ) Animation'''
    bl_idname = "object.bake_clear_parent_constraint_object_ra"
    bl_label = "Bake Parent/Constraint - Object"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None 
                and context.object.mode == 'OBJECT' 
                and len(context.selected_objects) != 0)
    


    def execute(self, context):
        
             
        # Bake and Clear Constraint 'Child Of'        
        def bake_and_clear_constraint():
            
              
            ob_constraint = bpy.context.active_object.constraints.active

            if ob_constraint is not None and ob_constraint.type == 'CHILD_OF':
                
                ob_constraint_anim_data = bpy.context.active_object.constraints.active.target.animation_data.action

                if ob_constraint_anim_data is not None:
                    frame_0 = int(bpy.context.active_object.constraints.active.target.animation_data.action.frame_range[0])
                    frame_1 =int(bpy.context.active_object.constraints.active.target.animation_data.action.frame_range[1])

 


                    if frame_1 > (frame_0 + 3):
                        
                    
                        bpy.ops.nla.bake(frame_start= frame_0, frame_end= frame_1,
                                        only_selected=True,use_current_action=True,
                                        visual_keying=True,
                                        clear_constraints=True,
                                        clear_parents=True, 
                                        bake_types={'OBJECT'})
                                        

            else:
                pass


        # Bake and Clear Parent
        def bake_and_clear_parent():
            

            ob_parent = bpy.context.active_object.parent

            if ob_parent is not None:
                ob_parent_anim_data = bpy.context.active_object.parent.animation_data.action

                f_parent_0 = int(bpy.context.active_object.parent.animation_data.action.frame_range[0])
                f_parent_1 = int(bpy.context.active_object.parent.animation_data.action.frame_range[1])
                   


            if ob_parent and ob_parent_anim_data is not None: 
                if f_parent_1 > (f_parent_0 + 3): 
                    
                  
                    bpy.ops.nla.bake(frame_start=f_parent_0, frame_end=f_parent_1,
                                    only_selected=True,use_current_action=True,
                                    visual_keying=True,
                                    clear_constraints=True,
                                    clear_parents=True, 
                                    bake_types={'OBJECT'})
                    

            else:
                pass
                 
        
        
        if bpy.context.active_object.parent is not None:
            bake_and_clear_parent()

        if bpy.context.active_object.constraints is not None:
            bake_and_clear_constraint()

        else:
            pass
            
                
        return {'FINISHED'}



# =======================================================
# END BAKE OBJECT AND CLEAR PARENT / CONSTRAINT 'CHILD OF'
# =======================================================





# ================================================================================
#   OFFSET KEYFRAMES
# ================================================================================




# Offset Keyframes ( 1 Frame )
class OBJECT_OT_selected_object_offset_keyframes_ra(bpy.types.Operator):
    '''Offset Keyframes of Selected Object'''
    bl_idname = "object.selected_object_offset_keyframes_ra"
    bl_label = "Offset Keyframes"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None 
                and context.object.mode == 'OBJECT' 
                and len(context.selected_objects) != 0)
    


    def execute(self, context):
        

        # Offset Keyframes of Selected Objects ( 1 Frame )
        def offset_keyframes_after_bake():
            

            offset = 1 ## offset in frames
            #noise = 50 ## add some offset variation (set to 0 to disable)
            reset = False ## enable to align actions to frame 0


            #import bpy, random
            objs = [o for o in bpy.context.selected_objects if o.animation_data]


            for i,o in enumerate(objs):
                act = o.animation_data.action
                delta = offset * i
                delta += 1
                if reset: delta = act.frame_range[0] * -1


                for fcu in act.fcurves:
                    for k in fcu.keyframe_points:
                        k.co[0] += delta
                        k.handle_left[0] += delta
                        k.handle_right[0] += delta
                        
                                         

        # Calling Function 
        # Offset Keyframes of Selected Objects ( 1 Frame )
        offset_keyframes_after_bake()

                       

        return {'FINISHED'}



# ===================================================================================
# END  OFFSET KEYFRAMES
# ===================================================================================








#================================================
# Parent-Unparent Selected Objects    
#================================================


# Parent / Unparent Selected Objects to Objects or to Bone
class OBJECT_OT_selected_parent_unparent_obj_bone_ra(bpy.types.Operator):
    '''Parent to : Object / Bone / Vertex\nAlt-Click to Unparent'''
    bl_idname = "object.selected_parent_unparent_obj_bone_ra"
    bl_label = "Parent - Unparent"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None 
                and len(context.selected_objects) != 0)



    def invoke(self, context, event):
        
        
        # Parent Selected Objects to Objects or Bone
        def parent_to_obj_bone():
          
            sel_ob = bpy.context.selected_objects

            for ob in sel_ob:
                if bpy.context.object.mode == 'OBJECT':
                    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

                if bpy.context.object.mode == 'POSE':                  
                    bpy.ops.object.parent_set(type='BONE', keep_transform=True)
  
                
                if bpy.context.object.mode == 'EDIT':             
                    bpy.ops.object.vertex_parent_set()

                else:
                    pass
                
                
        # Unparent ( and keep transformation )
        def unparent_obj_bone():
            
            for a in bpy.context.selected_objects:
                if a.parent:
                    matrixcopy = a.matrix_world.copy()
                    a.parent = None
                    a.matrix_world = matrixcopy


        
        if event:
            parent_to_obj_bone()
    
  
        if event.alt:
            unparent_obj_bone()
                  

        return {'FINISHED'}


#================================================
# End Parent-Unparent Selected Objects    
#================================================





classes = [ OBJECT_OT_graph_editor_open_ra, OBJECT_OT_insert_key_ra,
           OBJECT_OT_duo_insert_key_ra, OBJECT_OT_insert_key_all_ra,
           OBJECT_OT_insert_pose_keyframe_animbox_ra,

           # Motion Path Before Current Frame / Preview Range
           OBJECT_OT_motion_path_cfpr_objects_bones_ra,

           # BAKE ANIMATION
           # Bake Clear Parent / Constraint
           OBJECT_OT_bake_clear_parent_constraint_object_ra,
           OBJECT_OT_selected_object_offset_keyframes_ra,
           OBJECT_OT_selected_parent_unparent_obj_bone_ra,

          ]



addon_keymaps = []


def register():

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        # Mirror Tools Shortcuts

        km = kc.keymaps.new(name='3D View', space_type= 'VIEW_3D')
        kmi = km.keymap_items.new("object.graph_editor_open_ra", type = 'NONE', value = 'PRESS', shift=1, ctrl=1, alt=1)


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




