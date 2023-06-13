import bpy




# =====================================================
#                   CYCLE CREATOR
# =====================================================


# Cycle Creator
class WM_OT_custom_pose_cycle_ra(bpy.types.Operator):
    '''Extended Cycle - Unlimited Frame Range'''
    bl_idname = "wm.custom_pose_cycle_ra"
    bl_label = "Define : "
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    times : bpy.props.IntProperty(name="Times to repeat:", default=12)
    steps : bpy.props.IntProperty(name="Steps / Interval:", default=12)

    def execute(self, context):
        t = self.times
        s = self.steps
        for _ in range(t):
            bpy.ops.pose.select_mirror(extend=True)     
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.pose.copy()      
            bpy.context.scene.frame_current += s
            bpy.ops.pose.paste(flipped=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
        bpy.ops.screen.frame_jump(end=False)
        bpy.ops.screen.animation_play()

        return {'FINISHED'}

    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self)









#==============================================
#  3-POSE CYCLE
#==============================================


# This will select all bones that are NOT in the 'Rest Pose'
# and create 3-Pose Cycle according to Timeline Length
class OBJECT_OT_smart_three_pose_cycle_auto_ra(bpy.types.Operator):
    ''' Place Timeline Cursor on the first frame !

If Nothing is Selected : 
    this will select all bones that are NOT in the Rest Pose - 
    and create 3-Pose Cycle according to the Timeline Length.

If Selected : 
    3-Pose Cycle - Only for Selected'''

    bl_idname = "object.smart_three_pose_cycle_auto_ra"
    bl_label = "3-Pose Cycle"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' 
                and context.scene.frame_current == context.scene.frame_start)


    def execute(self, context):


        bone_list = []

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
           


        def smart_three_pose_cycle(): 
                            
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
            bpy.context.scene.frame_current = bpy.context.scene.frame_start
            bpy.ops.pose.copy()
            bpy.ops.anim.keyframe_insert(type='LocRotScale')

            #------------------------------
               
            middle_of_timeline()
            
            #------------------------------

            bpy.ops.pose.paste(flipped=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')

            bpy.context.scene.frame_current = bpy.context.scene.frame_end  + 1
            bpy.ops.pose.paste(flipped=False)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.screen.frame_jump(end=False)
            bpy.ops.screen.animation_play()

            bpy.ops.pose.select_all(action='DESELECT')



        def smart_three_pose_cycle_selected(): 
            
            # store selected bone name
            sel_pb = bpy.context.selected_pose_bones
            for bn in sel_pb:
                bone_list.append(bn.name)            
            
                             
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.context.scene.frame_current = bpy.context.scene.frame_start
            bpy.ops.pose.select_mirror(extend=True)
            bpy.ops.pose.copy()
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            

            #------------------------------
               
            middle_of_timeline() 
            
            #------------------------------    
            
            bpy.ops.pose.paste(flipped=True)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')

            bpy.context.scene.frame_current = bpy.context.scene.frame_end  + 1
            bpy.ops.pose.paste(flipped=False)
            bpy.ops.anim.keyframe_insert(type='LocRotScale')
            bpy.ops.screen.frame_jump(end=False)
            bpy.ops.screen.animation_play()
            


        def frame_timeline():
                      
            # Frame selected range in Timeline
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
            


        sel_bones = bpy.context.selected_pose_bones

        # ----------------------------------------------

        fs = bpy.context.scene.frame_start
        if len(sel_bones) == 0:
            smart_three_pose_cycle() 
            frame_timeline()

        if len(sel_bones) != 0:
            smart_three_pose_cycle_selected()

            bpy.ops.pose.select_all(action = 'DESELECT')

            # restore selected bone
            pose_bn = bpy.context.object.pose.bones
            for b in pose_bn:  
                if b.name in bone_list:
                    b.bone.select = 1 
                        
                        
            frame_timeline()  



        return {'FINISHED'}


#==============================================
# END  3-POSE CYCLE
#==============================================







#==============================================
#  ADD CYCLES MODIFIER - "PRE POST INFINITY"
#==============================================


# Add CYCLES Modifier ( "Pre_Post_Infinity" ) to Selected
class OBJECT_OT_add_cycles_modifier_to_selected_ra(bpy.types.Operator):
    '''Add " Pre-Post Infinity " Cycle (CYCLES Modifier) TO SELECTED
    
LOCATION / ROTATION / SCALE

Alt + Click to Remove'''
    bl_idname = "object.add_cycles_modifier_to_selected_ra"
    bl_label = "Pre_Post Infinity - Selected"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        
        return (context.object is not None and
                 context.object.mode == 'POSE' 
                 and context.object.animation_data.action is not None
                 and len(context.selected_pose_bones) != 0)
                 
        
    def invoke(self, context, event):
        
          
        anim_data = bpy.context.object.animation_data 
        ob = bpy.context.object

        sel_bones = bpy.context.selected_pose_bones
 
            
        def add_pre_post_infinity_sel():
               
            for bone in sel_bones:
                bone_name = bone.name  

                if anim_data.action is not None:
                    ob_fcurve = ob.animation_data.action.fcurves
                   
                    for fc in ob_fcurve:
                        d_path = ('location', 'rotation_quaternion', 'rotation_euler', 'scale')
                        if fc.data_path.endswith((d_path)) and bone_name in fc.data_path:
                            for m in fc.modifiers:
                               if (m.type == 'CYCLES'): 
                                   fc.modifiers.remove(m)
                            fc.modifiers.new(type='CYCLES')
                     
                        fc.update()     


        def remove_pre_post_infinity_sel():

            for bone in sel_bones:
                bone_name = bone.name  

                if anim_data.action is not None:
                    ob_fcurve = ob.animation_data.action.fcurves
                   
                    for fc in ob_fcurve:
                        d_path = ('location', 'rotation_quaternion', 'rotation_euler', 'scale')
                        if fc.data_path.endswith((d_path)) and bone_name in fc.data_path:
                            for m in fc.modifiers:
                               if (m.type == 'CYCLES'): 
                                   fc.modifiers.remove(m)

                     
                        fc.update()     



 
        if event: 
            add_pre_post_infinity_sel()  
                     
 

        if event.alt:
            remove_pre_post_infinity_sel()
            
            

        return {'FINISHED'}


#==============================================
# END - ADD CYCLES MODIFIER - PRE POST INFINITY
#==============================================









classes = [ WM_OT_custom_pose_cycle_ra,
            OBJECT_OT_smart_three_pose_cycle_auto_ra,
            OBJECT_OT_add_cycles_modifier_to_selected_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()







