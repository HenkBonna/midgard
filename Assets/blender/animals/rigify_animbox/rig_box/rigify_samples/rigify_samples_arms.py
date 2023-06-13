import bpy
from mathutils import Color



#=====================================================
#                      ARMS  HANDS
#=====================================================


# Add Rigify Samples => Arms and Hands
class OBJECT_OT_human_metarig_arms_with_hands_ra(bpy.types.Operator):
    '''Add Rigify Samples => Arms with Hands'''
    bl_idname = "object.human_metarig_arms_with_hands_ra"
    bl_label = "Add Arms / Hands"
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



        bone = arm.edit_bones.new('upper_arm.L')
        bone.head = 0.1953, 0.0267, 1.5846
        bone.tail = 0.4424, 0.0885, 1.4491
        bone.roll = 2.0724
        bone.use_connect = False
        bones['upper_arm.L'] = bone.name
        bone = arm.edit_bones.new('upper_arm.R')
        bone.head = -0.1953, 0.0267, 1.5846
        bone.tail = -0.4424, 0.0885, 1.4491
        bone.roll = -2.0724
        bone.use_connect = False
        bones['upper_arm.R'] = bone.name
        bone = arm.edit_bones.new('forearm.L')
        bone.head = 0.4424, 0.0885, 1.4491
        bone.tail = 0.6594, 0.0492, 1.3061
        bone.roll = 2.1535
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['upper_arm.L']]
        bones['forearm.L'] = bone.name
        bone = arm.edit_bones.new('forearm.R')
        bone.head = -0.4424, 0.0885, 1.4491
        bone.tail = -0.6594, 0.0492, 1.3061
        bone.roll = -2.1535
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['upper_arm.R']]
        bones['forearm.R'] = bone.name
        bone = arm.edit_bones.new('hand.L')
        bone.head = 0.6594, 0.0492, 1.3061
        bone.tail = 0.7234, 0.0412, 1.2585
        bone.roll = 2.2103
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['forearm.L']]
        bones['hand.L'] = bone.name
        bone = arm.edit_bones.new('hand.R')
        bone.head = -0.6594, 0.0492, 1.3061
        bone.tail = -0.7234, 0.0412, 1.2585
        bone.roll = -2.2103
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['forearm.R']]
        bones['hand.R'] = bone.name
        bone = arm.edit_bones.new('palm.01.L')
        bone.head = 0.6921, 0.0224, 1.2882
        bone.tail = 0.7441, 0.0057, 1.2467
        bone.roll = -2.2772
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['hand.L']]
        bones['palm.01.L'] = bone.name
        bone = arm.edit_bones.new('palm.02.L')
        bone.head = 0.6970, 0.0389, 1.2877
        bone.tail = 0.7490, 0.0297, 1.2471
        bone.roll = -2.3710
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['hand.L']]
        bones['palm.02.L'] = bone.name
        bone = arm.edit_bones.new('palm.03.L')
        bone.head = 0.6963, 0.0545, 1.2874
        bone.tail = 0.7511, 0.0520, 1.2471
        bone.roll = -2.4812
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['hand.L']]
        bones['palm.03.L'] = bone.name
        bone = arm.edit_bones.new('palm.04.L')
        bone.head = 0.6947, 0.0696, 1.2843
        bone.tail = 0.7506, 0.0773, 1.2438
        bone.roll = -2.5949
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['hand.L']]
        bones['palm.04.L'] = bone.name
        bone = arm.edit_bones.new('palm.01.R')
        bone.head = -0.6921, 0.0224, 1.2882
        bone.tail = -0.7441, 0.0057, 1.2467
        bone.roll = 2.2772
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['hand.R']]
        bones['palm.01.R'] = bone.name
        bone = arm.edit_bones.new('palm.02.R')
        bone.head = -0.6970, 0.0389, 1.2877
        bone.tail = -0.7490, 0.0297, 1.2471
        bone.roll = 2.3710
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['hand.R']]
        bones['palm.02.R'] = bone.name
        bone = arm.edit_bones.new('palm.03.R')
        bone.head = -0.6963, 0.0544, 1.2874
        bone.tail = -0.7511, 0.0520, 1.2471
        bone.roll = 2.4812
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['hand.R']]
        bones['palm.03.R'] = bone.name
        bone = arm.edit_bones.new('palm.04.R')
        bone.head = -0.6947, 0.0696, 1.2843
        bone.tail = -0.7506, 0.0773, 1.2438
        bone.roll = 2.5949
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['hand.R']]
        bones['palm.04.R'] = bone.name
        bone = arm.edit_bones.new('f_index.01.L')
        bone.head = 0.7441, 0.0057, 1.2467
        bone.tail = 0.7746, -0.0042, 1.2145
        bone.roll = -2.1019
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['palm.01.L']]
        bones['f_index.01.L'] = bone.name
        bone = arm.edit_bones.new('thumb.01.L')
        bone.head = 0.6691, 0.0117, 1.2751
        bone.tail = 0.6910, -0.0082, 1.2483
        bone.roll = -0.7854
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['palm.01.L']]
        bones['thumb.01.L'] = bone.name
        bone = arm.edit_bones.new('f_middle.01.L')
        bone.head = 0.7490, 0.0297, 1.2471
        bone.tail = 0.7819, 0.0235, 1.2111
        bone.roll = -2.1746
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['palm.02.L']]
        bones['f_middle.01.L'] = bone.name
        bone = arm.edit_bones.new('f_ring.01.L')
        bone.head = 0.7511, 0.0520, 1.2471
        bone.tail = 0.7815, 0.0505, 1.2131
        bone.roll = -2.2625
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['palm.03.L']]
        bones['f_ring.01.L'] = bone.name
        bone = arm.edit_bones.new('f_pinky.01.L')
        bone.head = 0.7506, 0.0773, 1.2438
        bone.tail = 0.7715, 0.0800, 1.2221
        bone.roll = -2.4309
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['palm.04.L']]
        bones['f_pinky.01.L'] = bone.name
        bone = arm.edit_bones.new('f_index.01.R')
        bone.head = -0.7441, 0.0057, 1.2467
        bone.tail = -0.7746, -0.0042, 1.2145
        bone.roll = 2.1019
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['palm.01.R']]
        bones['f_index.01.R'] = bone.name
        bone = arm.edit_bones.new('thumb.01.R')
        bone.head = -0.6691, 0.0117, 1.2751
        bone.tail = -0.6910, -0.0082, 1.2483
        bone.roll = 0.7854
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['palm.01.R']]
        bones['thumb.01.R'] = bone.name
        bone = arm.edit_bones.new('f_middle.01.R')
        bone.head = -0.7490, 0.0297, 1.2471
        bone.tail = -0.7819, 0.0235, 1.2111
        bone.roll = 2.1746
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['palm.02.R']]
        bones['f_middle.01.R'] = bone.name
        bone = arm.edit_bones.new('f_ring.01.R')
        bone.head = -0.7511, 0.0520, 1.2471
        bone.tail = -0.7815, 0.0505, 1.2131
        bone.roll = 2.2625
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['palm.03.R']]
        bones['f_ring.01.R'] = bone.name
        bone = arm.edit_bones.new('f_pinky.01.R')
        bone.head = -0.7506, 0.0773, 1.2438
        bone.tail = -0.7715, 0.0800, 1.2221
        bone.roll = 2.4309
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['palm.04.R']]
        bones['f_pinky.01.R'] = bone.name
        bone = arm.edit_bones.new('f_index.02.L')
        bone.head = 0.7746, -0.0042, 1.2145
        bone.tail = 0.7911, -0.0096, 1.1926
        bone.roll = -1.9643
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_index.01.L']]
        bones['f_index.02.L'] = bone.name
        bone = arm.edit_bones.new('thumb.02.L')
        bone.head = 0.6910, -0.0082, 1.2483
        bone.tail = 0.7104, -0.0187, 1.2233
        bone.roll = -0.7854
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thumb.01.L']]
        bones['thumb.02.L'] = bone.name
        bone = arm.edit_bones.new('f_middle.02.L')
        bone.head = 0.7819, 0.0235, 1.2111
        bone.tail = 0.7999, 0.0198, 1.1851
        bone.roll = -2.0099
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_middle.01.L']]
        bones['f_middle.02.L'] = bone.name
        bone = arm.edit_bones.new('f_ring.02.L')
        bone.head = 0.7815, 0.0505, 1.2131
        bone.tail = 0.7998, 0.0494, 1.1869
        bone.roll = -2.1299
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_ring.01.L']]
        bones['f_ring.02.L'] = bone.name
        bone = arm.edit_bones.new('f_pinky.02.L')
        bone.head = 0.7715, 0.0800, 1.2221
        bone.tail = 0.7857, 0.0816, 1.2043
        bone.roll = -2.3280
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_pinky.01.L']]
        bones['f_pinky.02.L'] = bone.name
        bone = arm.edit_bones.new('f_index.02.R')
        bone.head = -0.7746, -0.0042, 1.2145
        bone.tail = -0.7911, -0.0096, 1.1926
        bone.roll = 1.9643
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_index.01.R']]
        bones['f_index.02.R'] = bone.name
        bone = arm.edit_bones.new('thumb.02.R')
        bone.head = -0.6910, -0.0082, 1.2483
        bone.tail = -0.7104, -0.0187, 1.2233
        bone.roll = 0.7854
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thumb.01.R']]
        bones['thumb.02.R'] = bone.name
        bone = arm.edit_bones.new('f_middle.02.R')
        bone.head = -0.7819, 0.0235, 1.2111
        bone.tail = -0.7999, 0.0198, 1.1851
        bone.roll = 2.0099
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_middle.01.R']]
        bones['f_middle.02.R'] = bone.name
        bone = arm.edit_bones.new('f_ring.02.R')
        bone.head = -0.7815, 0.0505, 1.2131
        bone.tail = -0.7998, 0.0494, 1.1869
        bone.roll = 2.1299
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_ring.01.R']]
        bones['f_ring.02.R'] = bone.name
        bone = arm.edit_bones.new('f_pinky.02.R')
        bone.head = -0.7715, 0.0800, 1.2221
        bone.tail = -0.7857, 0.0816, 1.2043
        bone.roll = 2.3280
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_pinky.01.R']]
        bones['f_pinky.02.R'] = bone.name
        bone = arm.edit_bones.new('f_index.03.L')
        bone.head = 0.7911, -0.0096, 1.1926
        bone.tail = 0.8038, -0.0140, 1.1731
        bone.roll = -1.8718
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_index.02.L']]
        bones['f_index.03.L'] = bone.name
        bone = arm.edit_bones.new('thumb.03.L')
        bone.head = 0.7104, -0.0187, 1.2233
        bone.tail = 0.7234, -0.0227, 1.2061
        bone.roll = -0.7854
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thumb.02.L']]
        bones['thumb.03.L'] = bone.name
        bone = arm.edit_bones.new('f_middle.03.L')
        bone.head = 0.7999, 0.0198, 1.1851
        bone.tail = 0.8126, 0.0171, 1.1658
        bone.roll = -1.9834
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_middle.02.L']]
        bones['f_middle.03.L'] = bone.name
        bone = arm.edit_bones.new('f_ring.03.L')
        bone.head = 0.7998, 0.0494, 1.1869
        bone.tail = 0.8087, 0.0487, 1.1702
        bone.roll = -1.9904
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_ring.02.L']]
        bones['f_ring.03.L'] = bone.name
        bone = arm.edit_bones.new('f_pinky.03.L')
        bone.head = 0.7857, 0.0816, 1.2043
        bone.tail = 0.7943, 0.0824, 1.1903
        bone.roll = -2.2009
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_pinky.02.L']]
        bones['f_pinky.03.L'] = bone.name
        bone = arm.edit_bones.new('f_index.03.R')
        bone.head = -0.7911, -0.0096, 1.1926
        bone.tail = -0.8038, -0.0140, 1.1731
        bone.roll = 1.8718
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_index.02.R']]
        bones['f_index.03.R'] = bone.name
        bone = arm.edit_bones.new('thumb.03.R')
        bone.head = -0.7104, -0.0187, 1.2233
        bone.tail = -0.7234, -0.0227, 1.2061
        bone.roll = 0.7854
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thumb.02.R']]
        bones['thumb.03.R'] = bone.name
        bone = arm.edit_bones.new('f_middle.03.R')
        bone.head = -0.7999, 0.0198, 1.1851
        bone.tail = -0.8126, 0.0171, 1.1658
        bone.roll = 1.9834
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_middle.02.R']]
        bones['f_middle.03.R'] = bone.name
        bone = arm.edit_bones.new('f_ring.03.R')
        bone.head = -0.7998, 0.0494, 1.1869
        bone.tail = -0.8087, 0.0487, 1.1702
        bone.roll = 1.9904
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_ring.02.R']]
        bones['f_ring.03.R'] = bone.name
        bone = arm.edit_bones.new('f_pinky.03.R')
        bone.head = -0.7857, 0.0816, 1.2043
        bone.tail = -0.7943, 0.0824, 1.1903
        bone.roll = 2.2009
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_pinky.02.R']]
        bones['f_pinky.03.R'] = bone.name

        obj = bpy.context.object

        bpy.ops.object.mode_set(mode='OBJECT')
        pbone = obj.pose.bones[bones['upper_arm.L']]
        pbone.rigify_type = 'limbs.super_limb'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.rotation_axis = "x"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['upper_arm.R']]
        pbone.rigify_type = 'limbs.super_limb'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.rotation_axis = "x"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['forearm.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['forearm.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['hand.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['hand.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['palm.01.L']]
        pbone.rigify_type = 'limbs.super_palm'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone = obj.pose.bones[bones['palm.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone = obj.pose.bones[bones['palm.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone = obj.pose.bones[bones['palm.04.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone = obj.pose.bones[bones['palm.01.R']]
        pbone.rigify_type = 'limbs.super_palm'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone = obj.pose.bones[bones['palm.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone = obj.pose.bones[bones['palm.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone = obj.pose.bones[bones['palm.04.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone = obj.pose.bones[bones['f_index.01.L']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.primary_rotation_axis = "X"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['thumb.01.L']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.primary_rotation_axis = "X"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['f_middle.01.L']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.primary_rotation_axis = "X"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['f_ring.01.L']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.primary_rotation_axis = "X"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['f_pinky.01.L']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.primary_rotation_axis = "X"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['f_index.01.R']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.primary_rotation_axis = "X"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['thumb.01.R']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.primary_rotation_axis = "X"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['f_middle.01.R']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.primary_rotation_axis = "X"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['f_ring.01.R']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.primary_rotation_axis = "X"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['f_pinky.01.R']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.primary_rotation_axis = "X"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['f_index.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['thumb.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_middle.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_ring.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_pinky.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_index.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['thumb.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_middle.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_ring.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_pinky.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_index.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['thumb.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_middle.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_ring.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_pinky.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_index.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['thumb.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_middle.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_ring.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone = obj.pose.bones[bones['f_pinky.03.R']]
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
#               END    ARMS  HANDS
#=====================================================







classes = [ OBJECT_OT_human_metarig_arms_with_hands_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()








       
