import bpy
from mathutils import Color






#=====================================================
#                   LEGS 
#=====================================================




# Add Rigify Samples => Legs 
class OBJECT_OT_human_metarig_legs_ra(bpy.types.Operator):
    '''Add Rigify Samples => Legs'''
    bl_idname = "object.human_metarig_legs_ra"
    bl_label = "Add Legs"
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


        bone = arm.edit_bones.new('thigh.L')
        bone.head = 0.0980, 0.0124, 1.0720
        bone.tail = 0.0980, -0.0286, 0.5372
        bone.roll = 0.0000
        bone.use_connect = False
        bones['thigh.L'] = bone.name
        bone = arm.edit_bones.new('thigh.R')
        bone.head = -0.0980, 0.0124, 1.0720
        bone.tail = -0.0980, -0.0286, 0.5372
        bone.roll = 0.0000
        bone.use_connect = False
        bones['thigh.R'] = bone.name
        bone = arm.edit_bones.new('shin.L')
        bone.head = 0.0980, -0.0286, 0.5372
        bone.tail = 0.0980, 0.0162, 0.0852
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.L']]
        bones['shin.L'] = bone.name
        bone = arm.edit_bones.new('shin.R')
        bone.head = -0.0980, -0.0286, 0.5372
        bone.tail = -0.0980, 0.0162, 0.0852
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.R']]
        bones['shin.R'] = bone.name
        bone = arm.edit_bones.new('foot.L')
        bone.head = 0.0980, 0.0162, 0.0852
        bone.tail = 0.0980, -0.0934, 0.0167
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.L']]
        bones['foot.L'] = bone.name
        bone = arm.edit_bones.new('foot.R')
        bone.head = -0.0980, 0.0162, 0.0852
        bone.tail = -0.0980, -0.0934, 0.0167
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.R']]
        bones['foot.R'] = bone.name
        bone = arm.edit_bones.new('toe.L')
        bone.head = 0.0980, -0.0934, 0.0167
        bone.tail = 0.0980, -0.1606, 0.0167
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['foot.L']]
        bones['toe.L'] = bone.name
        bone = arm.edit_bones.new('heel.02.L')
        bone.head = 0.0600, 0.0459, 0.0000
        bone.tail = 0.1400, 0.0459, 0.0000
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['foot.L']]
        bones['heel.02.L'] = bone.name
        bone = arm.edit_bones.new('toe.R')
        bone.head = -0.0980, -0.0934, 0.0167
        bone.tail = -0.0980, -0.1606, 0.0167
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['foot.R']]
        bones['toe.R'] = bone.name
        bone = arm.edit_bones.new('heel.02.R')
        bone.head = -0.0600, 0.0459, 0.0000
        bone.tail = -0.1400, 0.0459, 0.0000
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['foot.R']]
        bones['heel.02.R'] = bone.name
        

        obj = bpy.context.object 


        bpy.ops.object.mode_set(mode='OBJECT')
        pbone = obj.pose.bones[bones['thigh.L']]
        pbone.rigify_type = 'limbs.leg'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.limb_type = "leg"
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['thigh.R']]
        pbone.rigify_type = 'limbs.leg'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.limb_type = "leg"
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['shin.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['shin.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['foot.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['foot.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['toe.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['heel.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['toe.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['heel.02.R']]
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




        # use_mirror_x  
        bpy.context.object.data.use_mirror_x = True

        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
          
        # View - Frame Selected
        bpy.ops.view3d.view_selected(use_all_regions=0)

          
        return {'FINISHED'}
    
    
#=====================================================
#       END    LEGS  
#=====================================================
 





  
#=====================================================
#     LEGS / LEGS AND TORSO
#=====================================================
  

# Add Rigify Samples => Legs with Torso
class OBJECT_OT_human_metarig_legs_with_torso_ra(bpy.types.Operator):
    '''Add Rigify Samples => Legs with Torso'''
    bl_idname = "object.human_metarig_legs_with_torso_ra"
    bl_label = "Add Legs / Torso"
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


         
        bone = arm.edit_bones.new('torso')
        bone.head = 0.0000, 0.0000, 1.0792
        bone.tail = 0.0000, 0.4000, 1.0792
        bone.roll = 0.0000
        bone.use_connect = False
        bones['torso'] = bone.name
        bone = arm.edit_bones.new('thigh.L')
        bone.head = 0.0980, 0.0124, 1.0720
        bone.tail = 0.0980, -0.0286, 0.5372
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['torso']]
        bones['thigh.L'] = bone.name
        bone = arm.edit_bones.new('thigh.R')
        bone.head = -0.0980, 0.0124, 1.0720
        bone.tail = -0.0980, -0.0286, 0.5372
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['torso']]
        bones['thigh.R'] = bone.name
        bone = arm.edit_bones.new('shin.L')
        bone.head = 0.0980, -0.0286, 0.5372
        bone.tail = 0.0980, 0.0162, 0.0852
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.L']]
        bones['shin.L'] = bone.name
        bone = arm.edit_bones.new('shin.R')
        bone.head = -0.0980, -0.0286, 0.5372
        bone.tail = -0.0980, 0.0162, 0.0852
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.R']]
        bones['shin.R'] = bone.name
        bone = arm.edit_bones.new('foot.L')
        bone.head = 0.0980, 0.0162, 0.0852
        bone.tail = 0.0980, -0.0934, 0.0167
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.L']]
        bones['foot.L'] = bone.name
        bone = arm.edit_bones.new('foot.R')
        bone.head = -0.0980, 0.0162, 0.0852
        bone.tail = -0.0980, -0.0934, 0.0167
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.R']]
        bones['foot.R'] = bone.name
        bone = arm.edit_bones.new('toe.L')
        bone.head = 0.0980, -0.0934, 0.0167
        bone.tail = 0.0980, -0.1606, 0.0167
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['foot.L']]
        bones['toe.L'] = bone.name
        bone = arm.edit_bones.new('heel.02.L')
        bone.head = 0.0600, 0.0459, 0.0000
        bone.tail = 0.1400, 0.0459, 0.0000
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['foot.L']]
        bones['heel.02.L'] = bone.name
        bone = arm.edit_bones.new('toe.R')
        bone.head = -0.0980, -0.0934, 0.0167
        bone.tail = -0.0980, -0.1606, 0.0167
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['foot.R']]
        bones['toe.R'] = bone.name
        bone = arm.edit_bones.new('heel.02.R')
        bone.head = -0.0600, 0.0459, 0.0000
        bone.tail = -0.1400, 0.0459, 0.0000
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['foot.R']]
        bones['heel.02.R'] = bone.name



        obj = bpy.context.object 


        bpy.ops.object.mode_set(mode='OBJECT')
        pbone = obj.pose.bones[bones['torso']]
        pbone.rigify_type = 'basic.raw_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.optional_widget_type = "cube"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['thigh.L']]
        pbone.rigify_type = 'limbs.leg'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.limb_type = "leg"
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['thigh.R']]
        pbone.rigify_type = 'limbs.leg'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.limb_type = "leg"
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['shin.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['shin.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['foot.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['foot.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['toe.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['heel.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['toe.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['heel.02.R']]
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




        # use_mirror_x  
        bpy.context.object.data.use_mirror_x = True

        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
          


         
        sel_bones = bpy.context.selected_bones

        vis_bones = bpy.context.visible_bones

                   
                    


        bone_list = [ 'thigh.L', 'shin.L', 'foot.L', 'toe.L', 'heel.02.L', 'thigh.R', 'shin.R', 'foot.R', 'toe.R', 'heel.02.R']
        

        bone_list_001 = [ 'thigh.L.001', 'shin.L.001', 'foot.L.001', 'toe.L.001', 'heel.02.L.001', 'thigh.R.001', 'shin.R.001', 'foot.R.001', 'toe.R.001', 'heel.02.R.001']
         

        bone_list_002 = [ 'thigh.L.002', 'shin.L.002', 'foot.L.002', 'toe.L.002', 'heel.02.L.002', 'thigh.R.002', 'shin.R.002', 'foot.R.002', 'toe.R.002', 'heel.02.R.002']
         

        bone_list_003 = [ 'thigh.L.003', 'shin.L.003', 'foot.L.003', 'toe.L.003', 'heel.02.L.003', 'thigh.R.003', 'shin.R.003', 'foot.R.003', 'toe.R.003', 'heel.02.R.003']
         

        bone_list_004 = [ 'thigh.L.004', 'shin.L.004', 'foot.L.004', 'toe.L.004', 'heel.02.L.004', 'thigh.R.004', 'shin.R.004', 'foot.R.004', 'toe.R.004', 'heel.02.R.004']
 

        bone_list_005 = [ 'thigh.L.005', 'shin.L.005', 'foot.L.005', 'toe.L.005', 'heel.02.L.005', 'thigh.R.005', 'shin.R.005', 'foot.R.005', 'toe.R.005', 'heel.02.R.005']
 

        bone_list_006 = [ 'thigh.L.006', 'shin.L.006', 'foot.L.006', 'toe.L.006', 'heel.02.L.006', 'thigh.R.006', 'shin.R.006', 'foot.R.006', 'toe.R.006', 'heel.02.R.006']
 

        bone_list_007 = [ 'thigh.L.007', 'shin.L.007', 'foot.L.007', 'toe.L.007', 'heel.02.L.007', 'thigh.R.007', 'shin.R.007', 'foot.R.007', 'toe.R.007', 'heel.02.R.007']
 

        bone_list_008 = [ 'thigh.L.008', 'shin.L.008', 'foot.L.008', 'toe.L.008', 'heel.02.L.008', 'thigh.R.008', 'shin.R.008', 'foot.R.008', 'toe.R.008', 'heel.02.R.008']
 

        bone_list_009 = [ 'thigh.L.009', 'shin.L.009', 'foot.L.009', 'toe.L.009', 'heel.02.L.009', 'thigh.R.009', 'shin.R.009', 'foot.R.009', 'toe.R.009', 'heel.02.R.009']
 

        bone_list_010 = [ 'thigh.L.010', 'shin.L.010', 'foot.L.010', 'toe.L.010', 'heel.02.L.010', 'thigh.R.010', 'shin.R.010', 'foot.R.010', 'toe.R.010', 'heel.02.R.010']
 

        bone_list_011 = [ 'thigh.L.011', 'shin.L.011', 'foot.L.011', 'toe.L.011', 'heel.02.L.011', 'thigh.R.011', 'shin.R.011', 'foot.R.011', 'toe.R.011', 'heel.02.R.011']
 

        bone_list_012 = [ 'thigh.L.012', 'shin.L.012', 'foot.L.012', 'toe.L.012', 'heel.02.L.012', 'thigh.R.012', 'shin.R.012', 'foot.R.012', 'toe.R.012', 'heel.02.R.012']
 

        bone_list_013 = [ 'thigh.L.013', 'shin.L.013', 'foot.L.013', 'toe.L.013', 'heel.02.L.013', 'thigh.R.013', 'shin.R.013', 'foot.R.013', 'toe.R.013', 'heel.02.R.013']
 

        bone_list_014 = [ 'thigh.L.014', 'shin.L.014', 'foot.L.014', 'toe.L.014', 'heel.02.L.014', 'thigh.R.014', 'shin.R.014', 'foot.R.014', 'toe.R.014', 'heel.02.R.014']
 

        bone_list_015 = [ 'thigh.L.015', 'shin.L.015', 'foot.L.015', 'toe.L.015', 'heel.02.L.015', 'thigh.R.015', 'shin.R.015', 'foot.R.015', 'toe.R.015', 'heel.02.R.015']
 

        bone_list_016 = [ 'thigh.L.016', 'shin.L.016', 'foot.L.016', 'toe.L.016', 'heel.02.L.016', 'thigh.R.016', 'shin.R.016', 'foot.R.016', 'toe.R.016', 'heel.02.R.016']
 

        bone_list_017 = [ 'thigh.L.017', 'shin.L.017', 'foot.L.017', 'toe.L.017', 'heel.02.L.017', 'thigh.R.017', 'shin.R.017', 'foot.R.017', 'toe.R.017', 'heel.02.R.017']
 

        bone_list_018 = [ 'thigh.L.018', 'shin.L.018', 'foot.L.018', 'toe.L.018', 'heel.02.L.018', 'thigh.R.018', 'shin.R.018', 'foot.R.018', 'toe.R.018', 'heel.02.R.018']
 

        bone_list_019 = [ 'thigh.L.019', 'shin.L.019', 'foot.L.019', 'toe.L.019', 'heel.02.L.019', 'thigh.R.019', 'shin.R.019', 'foot.R.019', 'toe.R.019', 'heel.02.R.019']
 

        bone_list_020 = [ 'thigh.L.020', 'shin.L.020', 'foot.L.020', 'toe.L.020', 'heel.02.L.020', 'thigh.R.020', 'shin.R.020', 'foot.R.020', 'toe.R.020', 'heel.02.R.020']
 





        for bone in sel_bones:
            if bone.name.startswith('torso'):
                torso_name = bone.name
            
        

        children_of_torso = bpy.data.armatures[ob.name].bones[torso_name].children_recursive
        
        

        
        for ch in children_of_torso:
            if ch.name in bone_list:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso'
            


        for ch in children_of_torso:
            if ch.name in bone_list_001:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.001'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_002:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.002'
            
        for ch in children_of_torso:        
            if ch.name in bone_list_003:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.003'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_004:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.004'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_005:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.005'
                        
        for ch in children_of_torso:
            if ch.name in bone_list_006:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.006'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_007:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.007'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_008:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.008'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_009:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.009'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_010:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.010'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_011:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.011'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_012:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.012'          
        
        for ch in children_of_torso: 
            if ch.name in bone_list_013:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.013'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_014:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.014'
            
        for ch in children_of_torso: 
            if ch.name in bone_list_015:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.015'
                 
        for ch in children_of_torso: 
            if ch.name in bone_list_016:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.016'
                            
        for ch in children_of_torso: 
            if ch.name in bone_list_017:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.017'          

        for ch in children_of_torso: 
            if ch.name in bone_list_018:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.018'
                   
        for ch in children_of_torso: 
            if ch.name in bone_list_019:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.019'
                   
        for ch in children_of_torso: 
            if ch.name in bone_list_020:
                bpy.data.armatures[ob.name].bones[torso_name].name = 'torso.020'
            
                 
        # View - Frame Selected
        bpy.ops.view3d.view_selected(use_all_regions=0)

     


        return {'FINISHED'}

    




  
#=====================================================
#      END      LEGS / LEGS AND TORSO
#=====================================================
  




  
#=====================================================
#         LEGS / SPINE / HEAD
#=====================================================
  






# Add Rigify Samples => LEGS / SPINE / HEAD
class OBJECT_OT_human_metarig_legs_spine_head_ra(bpy.types.Operator):
    '''Add Rigify Samples => Legs - Spine - Head'''
    bl_idname = "object.human_metarig_legs_spine_head_ra"
    bl_label = "Add Legs / Spine / Head"
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
        bone = arm.edit_bones.new('thigh.L')
        bone.head = 0.0980, 0.0124, 1.0720
        bone.tail = 0.0980, -0.0286, 0.5372
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine']]
        bones['thigh.L'] = bone.name
        bone = arm.edit_bones.new('thigh.R')
        bone.head = -0.0980, 0.0124, 1.0720
        bone.tail = -0.0980, -0.0286, 0.5372
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine']]
        bones['thigh.R'] = bone.name
        bone = arm.edit_bones.new('spine.001')
        bone.head = 0.0000, 0.0172, 1.1573
        bone.tail = 0.0000, 0.0004, 1.2929
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine']]
        bones['spine.001'] = bone.name
        bone = arm.edit_bones.new('shin.L')
        bone.head = 0.0980, -0.0286, 0.5372
        bone.tail = 0.0980, 0.0162, 0.0852
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.L']]
        bones['shin.L'] = bone.name
        bone = arm.edit_bones.new('shin.R')
        bone.head = -0.0980, -0.0286, 0.5372
        bone.tail = -0.0980, 0.0162, 0.0852
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.R']]
        bones['shin.R'] = bone.name
        bone = arm.edit_bones.new('spine.002')
        bone.head = 0.0000, 0.0004, 1.2929
        bone.tail = 0.0000, 0.0059, 1.4657
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.001']]
        bones['spine.002'] = bone.name
        bone = arm.edit_bones.new('foot.L')
        bone.head = 0.0980, 0.0162, 0.0852
        bone.tail = 0.0980, -0.0934, 0.0167
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.L']]
        bones['foot.L'] = bone.name
        bone = arm.edit_bones.new('foot.R')
        bone.head = -0.0980, 0.0162, 0.0852
        bone.tail = -0.0980, -0.0934, 0.0167
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.R']]
        bones['foot.R'] = bone.name
        bone = arm.edit_bones.new('spine.003')
        bone.head = 0.0000, 0.0059, 1.4657
        bone.tail = 0.0000, 0.0114, 1.6582
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['spine.003'] = bone.name
        bone = arm.edit_bones.new('toe.L')
        bone.head = 0.0980, -0.0934, 0.0167
        bone.tail = 0.0980, -0.1606, 0.0167
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['foot.L']]
        bones['toe.L'] = bone.name
        bone = arm.edit_bones.new('heel.02.L')
        bone.head = 0.0600, 0.0459, 0.0000
        bone.tail = 0.1400, 0.0459, 0.0000
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['foot.L']]
        bones['heel.02.L'] = bone.name
        bone = arm.edit_bones.new('toe.R')
        bone.head = -0.0980, -0.0934, 0.0167
        bone.tail = -0.0980, -0.1606, 0.0167
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['foot.R']]
        bones['toe.R'] = bone.name
        bone = arm.edit_bones.new('heel.02.R')
        bone.head = -0.0600, 0.0459, 0.0000
        bone.tail = -0.1400, 0.0459, 0.0000
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['foot.R']]
        bones['heel.02.R'] = bone.name
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
        pbone = obj.pose.bones[bones['thigh.L']]
        pbone.rigify_type = 'limbs.leg'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.limb_type = "leg"
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['thigh.R']]
        pbone.rigify_type = 'limbs.leg'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.limb_type = "leg"
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.001']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['shin.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['shin.R']]
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
        pbone = obj.pose.bones[bones['foot.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['foot.R']]
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
        pbone = obj.pose.bones[bones['toe.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['heel.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['toe.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['heel.02.R']]
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




        # use_mirror_x  
        bpy.context.object.data.use_mirror_x = True

        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
          

        # View - Frame Selected
        bpy.ops.view3d.view_selected(use_all_regions=0)

     


        return {'FINISHED'}
    
    
    
  
#=====================================================
#      END      LEGS / SPINE / HEAD
#=====================================================







classes = [ OBJECT_OT_human_metarig_legs_ra,
            OBJECT_OT_human_metarig_legs_with_torso_ra,
            OBJECT_OT_human_metarig_legs_spine_head_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()







  
