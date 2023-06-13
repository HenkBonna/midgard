import bpy
from mathutils import Color



#=====================================================
#            RIGIFY SAMPLES
#=====================================================


#=====================================================
#            RIGIFY ZOO METARIG - DOG
#=====================================================




# Add Rigify Metarig - Dog
class OBJECT_OT_rigify_zoo_dog_metarig_ra(bpy.types.Operator):
    '''Rigify ZOO Metarig - Dog
Based on Wolf Metarig'''
    bl_idname = "object.rigify_zoo_dog_metarig_ra"
    bl_label = "Dog Metarig"
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

        arm = bpy.data.objects[ob.name].data



        for i in range(6):
            arm.rigify_colors.add()

        arm.rigify_colors[0].name = "Root"
        arm.rigify_colors[0].active = Color((0.5490196347236633, 1.0, 1.0))
        arm.rigify_colors[0].normal = Color((0.4352940022945404, 0.18431399762630463, 0.4156860113143921))
        arm.rigify_colors[0].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
        arm.rigify_colors[0].standard_colors_lock = True
        arm.rigify_colors[1].name = "IK"
        arm.rigify_colors[1].active = Color((0.5490196347236633, 1.0, 1.0))
        arm.rigify_colors[1].normal = Color((0.6039220094680786, 0.0, 0.0))
        arm.rigify_colors[1].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
        arm.rigify_colors[1].standard_colors_lock = True
        arm.rigify_colors[2].name = "Special"
        arm.rigify_colors[2].active = Color((0.5490196347236633, 1.0, 1.0))
        arm.rigify_colors[2].normal = Color((0.9568629860877991, 0.7882350087165833, 0.04705899953842163))
        arm.rigify_colors[2].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
        arm.rigify_colors[2].standard_colors_lock = True
        arm.rigify_colors[3].name = "Tweak"
        arm.rigify_colors[3].active = Color((0.5490196347236633, 1.0, 1.0))
        arm.rigify_colors[3].normal = Color((0.03921600058674812, 0.21176500618457794, 0.5803920030593872))
        arm.rigify_colors[3].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
        arm.rigify_colors[3].standard_colors_lock = True
        arm.rigify_colors[4].name = "FK"
        arm.rigify_colors[4].active = Color((0.5490196347236633, 1.0, 1.0))
        arm.rigify_colors[4].normal = Color((0.11764699965715408, 0.5686269998550415, 0.035294000059366226))
        arm.rigify_colors[4].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
        arm.rigify_colors[4].standard_colors_lock = True
        arm.rigify_colors[5].name = "Extra"
        arm.rigify_colors[5].active = Color((0.5490196347236633, 1.0, 1.0))
        arm.rigify_colors[5].normal = Color((0.9686279892921448, 0.2509799897670746, 0.09411799907684326))
        arm.rigify_colors[5].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
        arm.rigify_colors[5].standard_colors_lock = True

        for i in range(29):
            arm.rigify_layers.add()

        arm.rigify_layers[0].name = "Face"
        arm.rigify_layers[0].row = 1
        arm.rigify_layers[0].selset = False
        arm.rigify_layers[0].group = 5
        arm.rigify_layers[1].name = "Face (Primary)"
        arm.rigify_layers[1].row = 2
        arm.rigify_layers[1].selset = False
        arm.rigify_layers[1].group = 2
        arm.rigify_layers[2].name = "Face (Secondary)"
        arm.rigify_layers[2].row = 2
        arm.rigify_layers[2].selset = False
        arm.rigify_layers[2].group = 3
        arm.rigify_layers[3].name = "Spine"
        arm.rigify_layers[3].row = 3
        arm.rigify_layers[3].selset = False
        arm.rigify_layers[3].group = 3
        arm.rigify_layers[4].name = "Spine (Tweak)"
        arm.rigify_layers[4].row = 4
        arm.rigify_layers[4].selset = False
        arm.rigify_layers[4].group = 4
        arm.rigify_layers[5].name = "Paws"
        arm.rigify_layers[5].row = 5
        arm.rigify_layers[5].selset = False
        arm.rigify_layers[5].group = 6
        arm.rigify_layers[6].name = "Paws (Tweak)"
        arm.rigify_layers[6].row = 6
        arm.rigify_layers[6].selset = False
        arm.rigify_layers[6].group = 4
        arm.rigify_layers[7].name = "Arm.L (IK)"
        arm.rigify_layers[7].row = 7
        arm.rigify_layers[7].selset = False
        arm.rigify_layers[7].group = 2
        arm.rigify_layers[8].name = "Arm.L (FK)"
        arm.rigify_layers[8].row = 8
        arm.rigify_layers[8].selset = False
        arm.rigify_layers[8].group = 5
        arm.rigify_layers[9].name = "Arm.L (Tweak)"
        arm.rigify_layers[9].row = 9
        arm.rigify_layers[9].selset = False
        arm.rigify_layers[9].group = 4
        arm.rigify_layers[10].name = "Arm.R (IK)"
        arm.rigify_layers[10].row = 7
        arm.rigify_layers[10].selset = False
        arm.rigify_layers[10].group = 2
        arm.rigify_layers[11].name = "Arm.R (FK)"
        arm.rigify_layers[11].row = 8
        arm.rigify_layers[11].selset = False
        arm.rigify_layers[11].group = 5
        arm.rigify_layers[12].name = "Arm.R (Tweak)"
        arm.rigify_layers[12].row = 9
        arm.rigify_layers[12].selset = False
        arm.rigify_layers[12].group = 4
        arm.rigify_layers[13].name = "Leg.L (IK)"
        arm.rigify_layers[13].row = 10
        arm.rigify_layers[13].selset = False
        arm.rigify_layers[13].group = 2
        arm.rigify_layers[14].name = "Leg.L (FK)"
        arm.rigify_layers[14].row = 11
        arm.rigify_layers[14].selset = False
        arm.rigify_layers[14].group = 5
        arm.rigify_layers[15].name = "Leg.L (Tweak)"
        arm.rigify_layers[15].row = 12
        arm.rigify_layers[15].selset = False
        arm.rigify_layers[15].group = 4
        arm.rigify_layers[16].name = "Leg.R (IK)"
        arm.rigify_layers[16].row = 10
        arm.rigify_layers[16].selset = False
        arm.rigify_layers[16].group = 2
        arm.rigify_layers[17].name = "Leg.R (FK)"
        arm.rigify_layers[17].row = 11
        arm.rigify_layers[17].selset = False
        arm.rigify_layers[17].group = 5
        arm.rigify_layers[18].name = "Leg.R (Tweak)"
        arm.rigify_layers[18].row = 12
        arm.rigify_layers[18].selset = False
        arm.rigify_layers[18].group = 4
        arm.rigify_layers[19].name = "Tail"
        arm.rigify_layers[19].row = 13
        arm.rigify_layers[19].selset = False
        arm.rigify_layers[19].group = 6
        arm.rigify_layers[20].name = ""
        arm.rigify_layers[20].row = 1
        arm.rigify_layers[20].selset = False
        arm.rigify_layers[20].group = 0
        arm.rigify_layers[21].name = ""
        arm.rigify_layers[21].row = 13
        arm.rigify_layers[21].selset = False
        arm.rigify_layers[21].group = 0
        arm.rigify_layers[22].name = ""
        arm.rigify_layers[22].row = 13
        arm.rigify_layers[22].selset = False
        arm.rigify_layers[22].group = 0
        arm.rigify_layers[23].name = ""
        arm.rigify_layers[23].row = 1
        arm.rigify_layers[23].selset = False
        arm.rigify_layers[23].group = 0
        arm.rigify_layers[24].name = ""
        arm.rigify_layers[24].row = 1
        arm.rigify_layers[24].selset = False
        arm.rigify_layers[24].group = 0
        arm.rigify_layers[25].name = ""
        arm.rigify_layers[25].row = 1
        arm.rigify_layers[25].selset = False
        arm.rigify_layers[25].group = 0
        arm.rigify_layers[26].name = ""
        arm.rigify_layers[26].row = 1
        arm.rigify_layers[26].selset = False
        arm.rigify_layers[26].group = 0
        arm.rigify_layers[27].name = ""
        arm.rigify_layers[27].row = 1
        arm.rigify_layers[27].selset = False
        arm.rigify_layers[27].group = 0
        arm.rigify_layers[28].name = "Root"
        arm.rigify_layers[28].row = 14
        arm.rigify_layers[28].selset = False
        arm.rigify_layers[28].group = 1

        bones = {}

        bone = arm.edit_bones.new('spine.004')
        bone.head = -0.0000, 0.4032, 0.7801
        bone.tail = 0.0000, 0.2575, 0.8023
        bone.roll = 0.0000
        bone.use_connect = False
        bones['spine.004'] = bone.name
        bone = arm.edit_bones.new('spine.003')
        bone.head = -0.0000, 0.4032, 0.7801
        bone.tail = -0.0000, 0.5397, 0.7179
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.004']]
        bones['spine.003'] = bone.name
        bone = arm.edit_bones.new('spine.005')
        bone.head = 0.0000, 0.2575, 0.8023
        bone.tail = 0.0000, 0.1170, 0.8102
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.004']]
        bones['spine.005'] = bone.name
        bone = arm.edit_bones.new('spine.002')
        bone.head = -0.0000, 0.5397, 0.7179
        bone.tail = -0.0000, 0.6573, 0.6248
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['spine.002'] = bone.name
        bone = arm.edit_bones.new('spine.006')
        bone.head = 0.0000, 0.1170, 0.8102
        bone.tail = 0.0000, 0.0001, 0.7985
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['spine.006'] = bone.name
        bone = arm.edit_bones.new('pelvis.L')
        bone.head = 0.0000, 0.4061, 0.6873
        bone.tail = 0.0751, 0.2830, 0.8023
        bone.roll = -1.1657
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['pelvis.L'] = bone.name
        bone = arm.edit_bones.new('pelvis.R')
        bone.head = -0.0000, 0.4061, 0.6873
        bone.tail = -0.0751, 0.2830, 0.8023
        bone.roll = 1.1657
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['pelvis.R'] = bone.name
        bone = arm.edit_bones.new('thigh.L')
        bone.head = 0.1249, 0.4062, 0.6768
        bone.tail = 0.1249, 0.3205, 0.4807
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['thigh.L'] = bone.name
        bone = arm.edit_bones.new('thigh.R')
        bone.head = -0.1249, 0.4062, 0.6768
        bone.tail = -0.1249, 0.3205, 0.4807
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['thigh.R'] = bone.name
        bone = arm.edit_bones.new('spine.001')
        bone.head = -0.0000, 0.6573, 0.6248
        bone.tail = -0.0000, 0.7667, 0.5221
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['spine.001'] = bone.name
        bone = arm.edit_bones.new('spine.007')
        bone.head = 0.0000, 0.0001, 0.7985
        bone.tail = -0.0000, -0.1521, 0.7934
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.006']]
        bones['spine.007'] = bone.name
        bone = arm.edit_bones.new('shin.L')
        bone.head = 0.1249, 0.3205, 0.4807
        bone.tail = 0.1114, 0.5094, 0.2193
        bone.roll = 0.0167
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.L']]
        bones['shin.L'] = bone.name
        bone = arm.edit_bones.new('shin.R')
        bone.head = -0.1249, 0.3205, 0.4807
        bone.tail = -0.1114, 0.5094, 0.2193
        bone.roll = -0.0167
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.R']]
        bones['shin.R'] = bone.name
        bone = arm.edit_bones.new('spine')
        bone.head = -0.0000, 0.7667, 0.5221
        bone.tail = -0.0000, 0.8866, 0.4321
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.001']]
        bones['spine'] = bone.name
        bone = arm.edit_bones.new('spine.008')
        bone.head = -0.0000, -0.1521, 0.7934
        bone.tail = -0.0000, -0.3353, 0.7962
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.007']]
        bones['spine.008'] = bone.name
        bone = arm.edit_bones.new('foot.L')
        bone.head = 0.1114, 0.5094, 0.2193
        bone.tail = 0.1088, 0.5210, 0.0398
        bone.roll = 0.0179
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.L']]
        bones['foot.L'] = bone.name
        bone = arm.edit_bones.new('foot.R')
        bone.head = -0.1114, 0.5094, 0.2193
        bone.tail = -0.1088, 0.5210, 0.0398
        bone.roll = -0.0179
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.R']]
        bones['foot.R'] = bone.name
        bone = arm.edit_bones.new('spine.009')
        bone.head = -0.0000, -0.3353, 0.7962
        bone.tail = -0.0000, -0.3940, 0.8475
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.008']]
        bones['spine.009'] = bone.name
        bone = arm.edit_bones.new('shoulder.L')
        bone.head = 0.0596, -0.2345, 0.8155
        bone.tail = 0.1249, -0.3439, 0.6623
        bone.roll = -0.4077
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.008']]
        bones['shoulder.L'] = bone.name
        bone = arm.edit_bones.new('shoulder.R')
        bone.head = -0.0596, -0.2345, 0.8155
        bone.tail = -0.1249, -0.3439, 0.6623
        bone.roll = 0.4077
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.008']]
        bones['shoulder.R'] = bone.name
        bone = arm.edit_bones.new('breast.L')
        bone.head = 0.0340, -0.1652, 0.6856
        bone.tail = 0.0340, -0.2969, 0.5311
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.008']]
        bones['breast.L'] = bone.name
        bone = arm.edit_bones.new('breast.R')
        bone.head = -0.0340, -0.1652, 0.6856
        bone.tail = -0.0340, -0.2969, 0.5311
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.008']]
        bones['breast.R'] = bone.name
        bone = arm.edit_bones.new('toe.L')
        bone.head = 0.1088, 0.5210, 0.0398
        bone.tail = 0.1088, 0.4344, 0.0000
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['foot.L']]
        bones['toe.L'] = bone.name
        bone = arm.edit_bones.new('toe.R')
        bone.head = -0.1088, 0.5210, 0.0398
        bone.tail = -0.1088, 0.4344, 0.0000
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['foot.R']]
        bones['toe.R'] = bone.name
        bone = arm.edit_bones.new('spine.010')
        bone.head = -0.0000, -0.3940, 0.8475
        bone.tail = 0.0000, -0.4621, 0.9229
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.009']]
        bones['spine.010'] = bone.name
        bone = arm.edit_bones.new('front_thigh.L')
        bone.head = 0.1249, -0.3521, 0.6347
        bone.tail = 0.1174, -0.2245, 0.4418
        bone.roll = 0.0175
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['shoulder.L']]
        bones['front_thigh.L'] = bone.name
        bone = arm.edit_bones.new('front_thigh.R')
        bone.head = -0.1249, -0.3521, 0.6347
        bone.tail = -0.1174, -0.2245, 0.4418
        bone.roll = -0.0175
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['shoulder.R']]
        bones['front_thigh.R'] = bone.name
        bone = arm.edit_bones.new('spine.011')
        bone.head = 0.0000, -0.4621, 0.9229
        bone.tail = 0.0000, -0.5972, 1.0323
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.010']]
        bones['spine.011'] = bone.name
        bone = arm.edit_bones.new('front_shin.L')
        bone.head = 0.1174, -0.2245, 0.4418
        bone.tail = 0.1106, -0.2158, 0.1422
        bone.roll = -0.0165
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['front_thigh.L']]
        bones['front_shin.L'] = bone.name
        bone = arm.edit_bones.new('front_shin.R')
        bone.head = -0.1174, -0.2245, 0.4418
        bone.tail = -0.1106, -0.2158, 0.1422
        bone.roll = 0.0165
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['front_thigh.R']]
        bones['front_shin.R'] = bone.name
        bone = arm.edit_bones.new('front_foot.L')
        bone.head = 0.1106, -0.2158, 0.1422
        bone.tail = 0.1088, -0.2462, 0.0280
        bone.roll = 0.0262
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['front_shin.L']]
        bones['front_foot.L'] = bone.name
        bone = arm.edit_bones.new('front_foot.R')
        bone.head = -0.1106, -0.2158, 0.1422
        bone.tail = -0.1088, -0.2462, 0.0280
        bone.roll = -0.0262
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['front_shin.R']]
        bones['front_foot.R'] = bone.name
        bone = arm.edit_bones.new('front_toe.L')
        bone.head = 0.1088, -0.2462, 0.0280
        bone.tail = 0.1088, -0.3259, 0.0000
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['front_foot.L']]
        bones['front_toe.L'] = bone.name
        bone = arm.edit_bones.new('front_toe.R')
        bone.head = -0.1088, -0.2462, 0.0280
        bone.tail = -0.1088, -0.3259, 0.0000
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['front_foot.R']]
        bones['front_toe.R'] = bone.name

        obj = bpy.context.object

        bpy.ops.object.mode_set(mode='OBJECT')
        pbone = obj.pose.bones[bones['spine.004']]
        pbone.rigify_type = 'spines.basic_spine'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.pivot_pos = 2
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.003']]
        pbone.rigify_type = 'spines.basic_tail'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.copy_rotation_axes = [True, False, True]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.connect_chain = True
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.005']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.neck_pos = 5
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.002']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.tweak_layers = [False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.006']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['pelvis.L']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_control = False
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['pelvis.R']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_control = False
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['thigh.L']]
        pbone.rigify_type = 'limbs.rear_paw'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.limb_type = "paw"
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
        pbone.rigify_type = 'limbs.rear_paw'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.limb_type = "paw"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.001']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['spine.007']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['shin.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['shin.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['spine']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['spine.008']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['foot.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['foot.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['spine.009']]
        pbone.rigify_type = 'spines.super_head'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.connect_chain = True
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['shoulder.L']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_widget = False
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['shoulder.R']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_widget = False
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['breast.L']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['breast.R']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['toe.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.limb_type = "paw"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['toe.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.limb_type = "paw"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.010']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['front_thigh.L']]
        pbone.rigify_type = 'limbs.front_paw'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.limb_type = "paw"
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['front_thigh.R']]
        pbone.rigify_type = 'limbs.front_paw'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.limb_type = "paw"
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.011']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['front_shin.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['front_shin.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['front_foot.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['front_foot.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['front_toe.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.limb_type = "paw"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['front_toe.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.rotation_axis = "x"
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.limb_type = "paw"
        except AttributeError:
            pass

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

        arm.layers = [(x in [3, 4, 7, 10, 13, 16, 19]) for x in range(32)]




        # View - Frame Selected
        bpy.ops.view3d.view_selected(use_all_regions=0)




        return {'FINISHED'}



#=====================================================
#     END  -   RIGIFY ZOO METARIG - DOG
#=====================================================








classes = [ OBJECT_OT_rigify_zoo_dog_metarig_ra,

          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()





