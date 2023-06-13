import bpy

from bpy.props import EnumProperty
from bpy.types import Operator, Panel
from bpy.utils import register_class, unregister_class




# =====================================================
#             Object To Bone (No Constraints)
# =====================================================




# Selected Object ( Mesh ) to Bone
class OBJECT_OT_send_object_to_bone_without_constraint_ra(bpy.types.Operator):
    '''Send Selected Object to Chosen Bone'''
    bl_idname = "object.send_object_to_bone_without_constraint_ra"
    bl_label = "Object To Bone"
    bl_options = {'REGISTER', 'UNDO'}



    action: EnumProperty(
        items=[
            ('HEAD', 'to head', 'to head' ),
            ('NECK', 'to neck', 'to neck' ),
            ('CHEST', 'to chest', 'to chest'),
            ('TORSO', 'to torso', 'to torso'),        
            ('HAND LEFT FK', 'to hand left fk', 'to hand left fk'),
            ('HAND RIGHT FK', 'to hand right fk', 'to hand right fk'),
            ('HAND LEFT IK', 'to hand left ik', 'to hand left ik'),
            ('HAND RIGHT IK', 'to hand right ik', 'to hand right ik'),
            ('FOOT LEFT', 'to foot left', 'to foot left'),
            ('FOOT RIGHT', 'to foot right', 'to foot right'),
            ('ARM LEFT', 'to arm left', 'to arm left'),
            ('ARM RIGHT', 'to arm right', 'to arm right'),
            ('FOREARM LEFT', 'to forearm left', 'to forearm left'),
            ('FOREARM RIGHT', 'to forearm right', 'to forearm right'),
        ]
    )




    @classmethod
    def poll(cls, context):
        return (context.object is not None
                and context.object.mode == 'OBJECT'
                and bpy.context.object.type != 'ARMATURE'
                and len(context.selected_objects) != 0 )



    def execute(self, context):
        scene = context.scene
        

        
        # Creating 'COPY_LOCATION' Constraint to bring Object to the Bone
        # Apply Visual Transformation (Object stay in Place) and Delete 'COPY_LOCATION' Constraint
        
        # Name of (Parent) Bone 
        bone_name = ""

        def object_to_bone(bone_name):
                 
            for o in bpy.data.objects:
                    if o.type == 'ARMATURE':
                        o.name = o.name
                        
                        bpy.ops.object.constraint_add(type='COPY_LOCATION')
                        bpy.context.object.constraints["Copy Location"].target = bpy.data.objects[o.name]
                        bpy.context.object.constraints["Copy Location"].subtarget = bone_name
                        
                        # Apply Visual Transformation (Object stay in Place)
                        bpy.ops.object.visual_transform_apply()
                        # Delete 'COPY_LOCATION' Constraint
                        bpy.ops.constraint.delete(constraint="Copy Location", owner='OBJECT')

      
            else:
                print(o.name +  " not found")
                pass

#        object_to_bone("head")



        # Send All Selected Objects to Active
        def selected_objects_to_active():
            sel_obj = bpy.context.selected_objects

            act_obj_loc = bpy.context.active_object.location


            # Send All Selected Objects to Active
            for obj in sel_obj:
                obj.location = act_obj_loc

    
            



# Defining Action for Calling Multiple Functions             
                                      

        if self.action == 'HEAD':
            object_to_bone("head")
            selected_objects_to_active()
            
            
        elif self.action == 'NECK':
            object_to_bone("neck")
            selected_objects_to_active()
            

        elif self.action == 'CHEST':
            object_to_bone("chest")
            selected_objects_to_active()
            
            
        elif self.action == 'TORSO':
            object_to_bone("torso")
            selected_objects_to_active()
            

        elif self.action == 'HAND LEFT FK':
            object_to_bone("hand_fk.L")
            selected_objects_to_active()
            

        elif self.action == 'HAND RIGHT FK':
            object_to_bone("hand_fk.R")
            selected_objects_to_active()
            

        elif self.action == 'HAND LEFT IK':
            object_to_bone("hand_ik.L")
            selected_objects_to_active()
            

        elif self.action == 'HAND RIGHT IK':
            object_to_bone("hand_ik.R")
            selected_objects_to_active()
            

        elif self.action == 'ARM LEFT':
            object_to_bone("upper_arm_fk.L")
            selected_objects_to_active()
            

        elif self.action == 'ARM RIGHT':
            object_to_bone("upper_arm_fk.R")
            selected_objects_to_active()
            
            
        elif self.action == 'FOREARM RIGHT':
            object_to_bone("forearm_fk.R")
            selected_objects_to_active()
            

        elif self.action == 'FOREARM LEFT':
            object_to_bone("forearm_fk.L")
            selected_objects_to_active()
            

        elif self.action == 'FOOT LEFT':
            object_to_bone("foot_ik.L")
            selected_objects_to_active()
          
        elif self.action == 'FOOT RIGHT':
            object_to_bone("foot_ik.R")
            selected_objects_to_active()
          


        return {'FINISHED'}






# =============================================================
#         
# =============================================================






# =============================================================
#         Object To Bone (With Constraints "Child Of" )
# =============================================================




# Selected Object ( Mesh ) to Bone with Constraint "Child Of"
class OBJECT_OT_send_object_to_bone_with_child_of_constraint_ra(bpy.types.Operator):
    '''Send Selected Object to Chosen Bone\nAdd "Child Of" Constraint'''
    bl_idname = "object.send_object_to_bone_with_child_of_constraint_ra"
    bl_label = "Object To Bone + Constraint"
    bl_options = {'REGISTER', 'UNDO'}



    action: EnumProperty(
        items=[
            ('HEAD', 'to head', 'to head' ),
            ('NECK', 'to neck', 'to neck' ),
            ('CHEST', 'to chest', 'to chest'),
            ('TORSO', 'to torso', 'to torso'),        
            ('HAND LEFT FK', 'to hand left fk', 'to hand left fk'),
            ('HAND RIGHT FK', 'to hand right fk', 'to hand right fk'),
            ('HAND LEFT IK', 'to hand left ik', 'to hand left ik'),
            ('HAND RIGHT IK', 'to hand right ik', 'to hand right ik'),
            ('FOOT LEFT', 'to foot left', 'to foot left'),
            ('FOOT RIGHT', 'to foot right', 'to foot right'),
            ('ARM LEFT', 'to arm left', 'to arm left'),
            ('ARM RIGHT', 'to arm right', 'to arm right'),
            ('FOREARM LEFT', 'to forearm left', 'to forearm left'),
            ('FOREARM RIGHT', 'to forearm right', 'to forearm right'),
        ]
    )




    @classmethod
    def poll(cls, context):
        return (context.object is not None
                and context.object.mode == 'OBJECT'
                and bpy.context.object.type != 'ARMATURE'
                and len(context.selected_objects) != 0 )



    def execute(self, context):
        scene = context.scene
        


        bone_name = ""

        def object_to_bone_with_child_of_constraint(bone_name):
                 
            for o in bpy.data.objects:
                    if o.type == 'ARMATURE':
                        o.name = o.name
                        
                                
                        # Creating 'COPY_LOCATION' Constraint to bring Object to the Bone
                        # Apply Visual Transformation (Object stay in Place) and Delete 'COPY_LOCATION' Constraint
                        
                        
                        bpy.ops.object.constraint_add(type='COPY_LOCATION')
                        bpy.context.object.constraints["Copy Location"].target = bpy.data.objects[o.name]
                        bpy.context.object.constraints["Copy Location"].subtarget = bone_name
                   
                        # Apply Visual Transformation (Object stay in Place)
                        bpy.ops.object.visual_transform_apply()
                        # Delete 'COPY_LOCATION' Constraint
                        bpy.ops.constraint.delete(constraint="Copy Location", owner='OBJECT')




                        # Delete Existing "Child Of" Constraints 

                        for obj in bpy.context.selected_objects:
                            # Create a list of all constraints on this object
                            obj_child_of_const = [ c for c in obj.constraints if c.type == 'CHILD_OF' ]

                            # Iterate over all the object's constraints and delete them all
                            for c in obj_child_of_const:
                                obj.constraints.remove( c ) # Remove constraint
                                  
  

                        # Creating 'CHILD_OF' Constraint
                        
                        bpy.ops.object.constraint_add(type='CHILD_OF')
                        bpy.context.object.constraints["Child Of"].target = bpy.data.objects[o.name]
                        bpy.context.object.constraints["Child Of"].subtarget = bone_name

        
            else:
                pass





        # Send All Selected Objects to Active and Copy Constraint
        def selected_objects_to_active_constrain_copy():
            sel_obj = bpy.context.selected_objects

            act_obj_loc = bpy.context.active_object.location


            # Send All Selected Objects to Active
            for obj in sel_obj:
                obj.location = act_obj_loc
                bpy.ops.object.constraints_copy()

    
            



#        object_to_bone_with_child_of_constraint("chest")





# Defining Action for Calling Multiple Functions             
                                      

        if self.action == 'HEAD':
            object_to_bone_with_child_of_constraint("head")
            selected_objects_to_active_constrain_copy()
            
            
        elif self.action == 'NECK':
            object_to_bone_with_child_of_constraint("neck")
            selected_objects_to_active_constrain_copy()
            

        elif self.action == 'CHEST':
            object_to_bone_with_child_of_constraint("chest")
            selected_objects_to_active_constrain_copy()
            
            
        elif self.action == 'TORSO':
            object_to_bone_with_child_of_constraint("torso")
            selected_objects_to_active_constrain_copy()
            

        elif self.action == 'HAND LEFT FK':
            object_to_bone_with_child_of_constraint("hand_fk.L")
            selected_objects_to_active_constrain_copy()
            

        elif self.action == 'HAND RIGHT FK':
            object_to_bone_with_child_of_constraint("hand_fk.R")
            selected_objects_to_active_constrain_copy()
            

        elif self.action == 'HAND LEFT IK':
            object_to_bone_with_child_of_constraint("hand_ik.L")
            selected_objects_to_active_constrain_copy()
            

        elif self.action == 'HAND RIGHT IK':
            object_to_bone_with_child_of_constraint("hand_ik.R")
            selected_objects_to_active_constrain_copy()
            

        elif self.action == 'ARM LEFT':
            object_to_bone_with_child_of_constraint("upper_arm_fk.L")
            selected_objects_to_active_constrain_copy()
            

        elif self.action == 'ARM RIGHT':
            object_to_bone_with_child_of_constraint("upper_arm_fk.R")
            selected_objects_to_active_constrain_copy()
            
            
        elif self.action == 'FOREARM RIGHT':
            object_to_bone_with_child_of_constraint("forearm_fk.R")
            selected_objects_to_active_constrain_copy()
            

        elif self.action == 'FOREARM LEFT':
            object_to_bone_with_child_of_constraint("forearm_fk.L")
            selected_objects_to_active_constrain_copy()
            

        elif self.action == 'FOOT LEFT':
            object_to_bone_with_child_of_constraint("foot_ik.L")
            selected_objects_to_active_constrain_copy()
          
        elif self.action == 'FOOT RIGHT':
            object_to_bone_with_child_of_constraint("foot_ik.R")
            selected_objects_to_active_constrain_copy()
          


        return {'FINISHED'}




# =============================================================
#   END OF      Object To Bone (With Constraints "Child Of" )
# =============================================================








# =============================================================
#    MENU - Object to Bone  Without Constraints
# =============================================================

class OBJECT_MT_rigify_object_to_bone_menu_ra(bpy.types.Menu):
    bl_label = "Object to Bone"
    bl_idname = "OBJECT_MT_rigify_object_to_bone_menu_ra"

    def draw(self, context):
        layout = self.layout

           
        row = layout.row()
       

        row.operator('object.send_object_to_bone_without_constraint_ra', text='Head').action = 'HEAD'
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Neck').action = 'NECK'
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Chest').action = 'CHEST'
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Torso').action = 'TORSO'
        
        layout.separator()
        
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Hand.L FK').action = 'HAND LEFT FK'
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Hand.R FK').action = 'HAND RIGHT FK'
        
        layout.separator()
        
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Hand.L IK').action = 'HAND LEFT IK'
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Hand.R IK').action = 'HAND RIGHT IK'
        
        layout.separator()
        
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Arm.L').action = 'ARM LEFT'
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Arm.R').action = 'ARM RIGHT'
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Forearm.L').action = 'FOREARM LEFT'
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Forearm.R').action = 'FOREARM RIGHT'
        
        layout.separator()
        
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Foot.L').action = 'FOOT LEFT'
        row = layout.row()
        row.operator('object.send_object_to_bone_without_constraint_ra', text='Foot.R').action = 'FOOT RIGHT'   
        row = layout.row()







# =============================================================
#    MENU - Object to Bone  With "Child Of" Constraints
# =============================================================

class OBJECT_MT_rigify_object_to_bone_with_child_of_menu_ra(bpy.types.Menu):
    bl_label = "Object to Bone with Constraint"
    bl_idname = "OBJECT_MT_rigify_object_to_bone_with_child_of_menu_ra"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()

         

        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Head').action = 'HEAD'
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Neck').action = 'NECK'
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Chest').action = 'CHEST'
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Torso').action = 'TORSO'
        
        layout.separator()
        
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Hand.L FK').action = 'HAND LEFT FK'
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Hand.R FK').action = 'HAND RIGHT FK'
        
        layout.separator()
        
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Hand.L IK').action = 'HAND LEFT IK'
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Hand.R IK').action = 'HAND RIGHT IK'
        
        layout.separator()
        
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Arm.L').action = 'ARM LEFT'
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Arm.R').action = 'ARM RIGHT'
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Forearm.L').action = 'FOREARM LEFT'
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Forearm.R').action = 'FOREARM RIGHT'
        
        layout.separator()
        
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Foot.L').action = 'FOOT LEFT'
        row = layout.row()
        row.operator('object.send_object_to_bone_with_child_of_constraint_ra', text='Foot.R').action = 'FOOT RIGHT'   
        row = layout.row()





# =============================================================
#  OPERATOR FOR CALLING  " Object to Bone Without Constraint " MENU 
# =============================================================

# Call Menu Operator
class OBJECT_OT_call_rigify_object_to_bone_menu_ra(bpy.types.Operator):
    '''Send Selected Object To Chosen Bone'''
    bl_idname = "object.call_rigify_object_to_bone_menu_ra"
    bl_label = "No Constraint"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        
        bpy.ops.wm.call_menu(name=OBJECT_MT_rigify_object_to_bone_menu_ra.bl_idname)
        


        return {'FINISHED'}





# ==========================================================================
#  OPERATOR FOR CALLING  " Object to Bone With "Child Of" Constraint " MENU 
# ==========================================================================

# Call Menu Operator
class OBJECT_OT_call_rigify_object_to_bone_child_of_menu_ra(bpy.types.Operator):
    '''Send Selected Object To Chosen Bone'''
    bl_idname = "object.call_rigify_object_to_bone_child_of_menu_ra"
    bl_label = "With Constraint"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        
        
        bpy.ops.wm.call_menu(name=OBJECT_MT_rigify_object_to_bone_with_child_of_menu_ra.bl_idname)
            

        return {'FINISHED'}




# =============================================================
#  
# =============================================================





# ================================================================
#  Selected Object to Selected Bone (With "Child Of" Constraint)
# ================================================================



# First select Object you wish to parent to a specific Armature Bone, 
# then Shift-RMB select the Armature Object and switch it into Pose Mode 
# and then select the specific bone you wish to be the Parent Bone


# Send Selected Object to Selected Bone With "Child Of" Constraint
class OBJECT_OT_sel_obj_to_sel_bone_child_of_ra(bpy.types.Operator):
    '''First select Object, then Target-Bone\nSend only 1 Object !!!'''
    bl_idname = "object.sel_obj_to_sel_bone_child_of_ra"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None 
                and  context.object.mode == 'POSE'
                and len(context.selected_objects) == 2 
                and len(context.selected_pose_bones) != 0)

    def execute(self, context):
        
        # Invert ( Toggle ) Active Object 

        sel_obj = bpy.context.selected_objects

        act_obj = bpy.context.view_layer.objects

        if act_obj.active == sel_obj[0]:
            act_obj.active = sel_obj[-1]

        elif act_obj.active == sel_obj[-1]:
            act_obj.active = sel_obj[0]
            
                              
        # Add "Copy Location" Constraint and apply Transform (Obj stay in place)
        bpy.ops.object.constraint_add_with_targets(type='COPY_LOCATION')
        bpy.ops.object.visual_transform_apply()

        # Delete "Copy Location" Constraint
        bpy.ops.constraint.delete(constraint="Copy Location", owner='OBJECT')

        # Delete Existing "Child Of" Constraints 
        for obj in bpy.context.selected_objects:
            # Create a list of all constraints on this object
            obj_child_of_const = [ c for c in obj.constraints if c.type == 'CHILD_OF' ]

            # Iterate over all the object's constraints and delete them all
            for c in obj_child_of_const:
                obj.constraints.remove( c ) # Remove constraint
                  
  
        # Add "Child Of" Constraint with target
        bpy.ops.object.constraint_add_with_targets(type='CHILD_OF')

        bpy.ops.object.select_all(action='DESELECT')

        # Select Object
        bpy.context.active_object.select_set(True)


        return {'FINISHED'}

         
# ===================================================================
#  End Selected Object to Selected Bone (With "Child Of" Constraint)
# ===================================================================






#================================================
# Selected Objects to Bone  
#================================================


# Selected Object to Bone 
class OBJECT_OT_send_sel_obj_to_bone_ra(bpy.types.Operator):
    '''Send Selected Objects to Selected Bone'''
    bl_idname = "object.send_sel_obj_to_bone_ra"
    bl_label = "O2B"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    def execute(self, context):

        # Scene Pivot Point Type
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'

        bpy.ops.view3d.snap_cursor_to_active()

        # Deselect Active and make selected active
        bpy.context.active_object.select_set(False)
        for obj in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = obj


        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        bpy.ops.view3d.snap_cursor_to_center()
        

        return {'FINISHED'}


#=======================================================
# End Selected Object to Bone 
#=======================================================




#=======================================================
# Selected Object to Bone + Parent 
#=======================================================


# Selected Object to Bone and Parent
class OBJECT_OT_send_sel_obj_to_sel_bone_parent_ra(bpy.types.Operator):
    '''Send and Parent Selected Objects to Selected Bone'''
    bl_idname = "object.send_sel_obj_to_sel_bone_parent_ra"
    bl_label = "O2B + Parent"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    def execute(self, context):

        # Scene Pivot Point Type
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'

        sel_ob = bpy.context.selected_objects

        for ob in sel_ob:
            bpy.ops.object.parent_set(type='BONE', keep_transform=True)

        bpy.ops.view3d.snap_cursor_to_active()

        # Deselect Active and make selected active
        bpy.context.active_object.select_set(False)
        for obj in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = obj


        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        bpy.ops.view3d.snap_cursor_to_center()
        

        return {'FINISHED'}


#============================================================
# End Selected Object to Bone + Parent
#============================================================



#=============================================
# Selected Object to Bone - Maintain Offset  
#=============================================


# Selected Object to Bone - Maintain Offset
class OBJECT_OT_sel_obj_to_bone_keep_offset_ra(bpy.types.Operator):
    '''Send Selected Objects to Selected Bone\nMaintain Offset'''
    bl_idname = "object.sel_obj_to_bone_keep_offset_ra"
    bl_label = "O2B - Keep Offset"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    def execute(self, context):

        # Scene Pivot Point Type     
        bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'

        bpy.ops.view3d.snap_cursor_to_active()

        # Deselect Active and make selected active
        bpy.context.active_object.select_set(False)
        for obj in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = obj

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
        bpy.ops.view3d.snap_cursor_to_center()
        

        return {'FINISHED'}


#=================================================
# End Selected Object to Bone - Maintain Offset  
#=================================================




#=====================================================
# Selected Object to Bone - Maintain Offset + Parent 
#=====================================================


# Selected Object to Bone - Maintain Offset + Parent
class OBJECT_OT_sel_obj_to_bone_keep_offset_parent_ra(bpy.types.Operator):
    '''Send and Parent Selected Objects to Selected Bone\nMaintain Offset'''
    bl_idname = "object.sel_obj_to_bone_keep_offset_parent_ra"
    bl_label = "O2B - Keep Offset + Parent"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    def execute(self, context):

        # Scene Pivot Point Type     
        bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'

        sel_ob = bpy.context.selected_objects

        for ob in sel_ob:
            bpy.ops.object.parent_set(type='BONE', keep_transform=True)

        bpy.ops.view3d.snap_cursor_to_active()

        # Deselect Active and make selected active
        bpy.context.active_object.select_set(False)
        for obj in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = obj

        bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
        bpy.ops.view3d.snap_cursor_to_center()
        

        return {'FINISHED'}


#===========================================================
# End Selected Object to Bone - Maintain Offset - Parent
#===========================================================



classes = [
            # OBJECT TO BONE

            # Selected Object to chosen Bone without Constraints
            OBJECT_OT_send_object_to_bone_without_constraint_ra,
            OBJECT_MT_rigify_object_to_bone_menu_ra,
            OBJECT_OT_call_rigify_object_to_bone_menu_ra,

            # Selected Object to chosen Bone with "Child Of" Constraint
            OBJECT_OT_send_object_to_bone_with_child_of_constraint_ra,
            OBJECT_MT_rigify_object_to_bone_with_child_of_menu_ra,
            OBJECT_OT_call_rigify_object_to_bone_child_of_menu_ra,

            # Selected Object to Selected Bone with "Child Of" Constraint
            OBJECT_OT_sel_obj_to_sel_bone_child_of_ra,

            # Objects to Bone (Multiple Objects to Bone)
            OBJECT_OT_send_sel_obj_to_bone_ra,
            OBJECT_OT_send_sel_obj_to_sel_bone_parent_ra,
            OBJECT_OT_sel_obj_to_bone_keep_offset_ra,
            OBJECT_OT_sel_obj_to_bone_keep_offset_parent_ra,

          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()











