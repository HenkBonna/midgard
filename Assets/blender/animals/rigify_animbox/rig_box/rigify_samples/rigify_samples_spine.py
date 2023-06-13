
import bpy
from mathutils import Color



#=====================================================
#                  SPINE
#=====================================================




# Add Rigify Samples => Spine
class OBJECT_OT_human_metarig_simple_spine_ra(bpy.types.Operator):
    '''Add Rigify Samples => Spine'''
    bl_idname = "object.human_metarig_simple_spine_ra"
    bl_label = "Add Spine"
    bl_options = {'REGISTER', 'UNDO'}

 

    def execute(self, context):
        

        # Check Rigify in preferences

        disable_Rigify = bpy.ops.preferences.addon_disable(module="rigify")

        if disable_Rigify:
            bpy.ops.preferences.addon_enable(module="rigify")

        else:
            pass
                    
  
        if bpy.context.mode == 'OBJECT':
            
            # Create single bone / go to Edot Mode / select and delete bone
            bpy.ops.object.armature_add(enter_editmode=0, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) 
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            bpy.ops.armature.select_all(action='SELECT')
            bpy.ops.armature.delete()    
         
             
        else:
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)



        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name

        # CREATE SAMPLE

        bones = {}

        arm = bpy.data.objects[ob.name].data


        bone = arm.edit_bones.new('spine')
        bone.head = 0.0000, 0.0552, 1.0099
        bone.tail = 0.0000, 0.0172, 1.1573
        bone.roll = 0.0000
        bone.use_connect = False
        bones['spine'] = bone.name
        bone = arm.edit_bones.new('spine.001')
        bone.head = 0.0000, 0.0172, 1.1573
        bone.tail = 0.0000, 0.0004, 1.2929
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine']]
        bones['spine.001'] = bone.name
        bone = arm.edit_bones.new('spine.002')
        bone.head = 0.0000, 0.0004, 1.2929
        bone.tail = 0.0000, 0.0059, 1.4657
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.001']]
        bones['spine.002'] = bone.name
        bone = arm.edit_bones.new('spine.003')
        bone.head = 0.0000, 0.0059, 1.4657
        bone.tail = 0.0000, 0.0114, 1.6582
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['spine.003'] = bone.name

        obj = bpy.context.object 

        bpy.ops.object.mode_set(mode='OBJECT')
        pbone = obj.pose.bones[bones['spine']]
        pbone.rigify_type = 'spines.basic_spine'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.001']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['spine.002']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['spine.003']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'

        bpy.ops.object.mode_set(mode='EDIT')
        for bone in arm.edit_bones:
            bone.select = False
            bone.select_head = False
            bone.select_tail = False
        for b in bones:
            bone = arm.edit_bones[bones[b]]
            bone.select = True
            bone.select_head = True
            bone.select_tail = True
            bone.bbone_x = bone.bbone_z = bone.length * 0.05
            arm.edit_bones.active = bone

        # View - Frame Selected
        bpy.ops.view3d.view_selected(use_all_regions=0)


        return {'FINISHED'}  




#=====================================================
#        END      SPINE
#=====================================================



#=====================================================
#                  SPINE AND HEAD
#=====================================================



# Add Rigify Samples => Spine with Head
class OBJECT_OT_human_metarig_simple_spine_with_head_ra(bpy.types.Operator):
    '''Add Rigify Samples => Spine with Head'''
    bl_idname = "object.human_metarig_simple_spine_with_head_ra"
    bl_label = "Add Spine / Head"
    bl_options = {'REGISTER', 'UNDO'}
 
 
 
    def execute(self, context):
        

        # Check Rigify in preferences

        disable_Rigify = bpy.ops.preferences.addon_disable(module="rigify")

        if disable_Rigify:
            bpy.ops.preferences.addon_enable(module="rigify")

        else:
            pass
                    
  
        if bpy.context.mode == 'OBJECT':
            
            # Create single bone / go to Edot Mode / select and delete bone
            bpy.ops.object.armature_add(enter_editmode=0, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) 
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            bpy.ops.armature.select_all(action='SELECT')
            bpy.ops.armature.delete()    
         
             
        else:
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)



        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name

        # CREATE SAMPLE

        bones = {}

        arm = bpy.data.objects[ob.name].data

        

        bone = arm.edit_bones.new('spine')
        bone.head = 0.0000, 0.0552, 1.0099
        bone.tail = 0.0000, 0.0172, 1.1573
        bone.roll = 0.0000
        bone.use_connect = False
        bones['spine'] = bone.name
        bone = arm.edit_bones.new('spine.001')
        bone.head = 0.0000, 0.0172, 1.1573
        bone.tail = 0.0000, 0.0004, 1.2929
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine']]
        bones['spine.001'] = bone.name
        bone = arm.edit_bones.new('spine.002')
        bone.head = 0.0000, 0.0004, 1.2929
        bone.tail = 0.0000, 0.0059, 1.4657
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.001']]
        bones['spine.002'] = bone.name
        bone = arm.edit_bones.new('spine.003')
        bone.head = 0.0000, 0.0059, 1.4657
        bone.tail = 0.0000, 0.0114, 1.6582
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['spine.003'] = bone.name
        bone = arm.edit_bones.new('neck')
        bone.head = 0.0000, 0.0114, 1.6582
        bone.tail = 0.0000, -0.0130, 1.7197
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['neck'] = bone.name
        bone = arm.edit_bones.new('neck.001')
        bone.head = 0.0000, -0.0130, 1.7197
        bone.tail = 0.0000, -0.0247, 1.7813
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['neck']]
        bones['neck.001'] = bone.name
        bone = arm.edit_bones.new('head')
        bone.head = 0.0000, -0.0247, 1.7813
        bone.tail = 0.0000, -0.0247, 1.9796
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['neck.001']]
        bones['head'] = bone.name

        obj = bpy.context.object 

        bpy.ops.object.mode_set(mode='OBJECT')
        pbone = obj.pose.bones[bones['spine']]
        pbone.rigify_type = 'spines.basic_spine'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.001']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['spine.002']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['spine.003']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['neck']]
        pbone.rigify_type = 'spines.super_head'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.connect_chain = False
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['neck.001']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['head']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'

        bpy.ops.object.mode_set(mode='EDIT')
        for bone in arm.edit_bones:
            bone.select = False
            bone.select_head = False
            bone.select_tail = False
        for b in bones:
            bone = arm.edit_bones[bones[b]]
            bone.select = True
            bone.select_head = True
            bone.select_tail = True
            bone.bbone_x = bone.bbone_z = bone.length * 0.05
            arm.edit_bones.active = bone


        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
          
        # View - Frame Selected
        bpy.ops.view3d.view_selected(use_all_regions=0)


        return {'FINISHED'}  




#=====================================================
#              END    SPINE AND HEAD
#=====================================================






classes = [ OBJECT_OT_human_metarig_simple_spine_ra,
            OBJECT_OT_human_metarig_simple_spine_with_head_ra,

          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()







