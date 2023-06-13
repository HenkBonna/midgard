import bpy
from mathutils import Color



#=====================================================
#            HUMAN METARIG WITH HANDS (NO FACE)
#=====================================================
 
 

# Add Rigify Human Metarig with Hands
class OBJECT_OT_human_metarig_no_face_with_hands_ra(bpy.types.Operator):
    '''Human Metarig with Hands '''
    bl_idname = "object.human_metarig_no_face_with_hands_ra"
    bl_label = "Add Metarig"
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
        arm.rigify_layers[3].name = "Torso"
        arm.rigify_layers[3].row = 3
        arm.rigify_layers[3].selset = False
        arm.rigify_layers[3].group = 3
        arm.rigify_layers[4].name = "Torso (Tweak)"
        arm.rigify_layers[4].row = 4
        arm.rigify_layers[4].selset = False
        arm.rigify_layers[4].group = 4
        arm.rigify_layers[5].name = "Fingers"
        arm.rigify_layers[5].row = 5
        arm.rigify_layers[5].selset = False
        arm.rigify_layers[5].group = 6
        arm.rigify_layers[6].name = "Fingers (Detail)"
        arm.rigify_layers[6].row = 6
        arm.rigify_layers[6].selset = False
        arm.rigify_layers[6].group = 5
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
        arm.rigify_layers[19].name = ""
        arm.rigify_layers[19].row = 1
        arm.rigify_layers[19].selset = False
        arm.rigify_layers[19].group = 0
        arm.rigify_layers[20].name = ""
        arm.rigify_layers[20].row = 1
        arm.rigify_layers[20].selset = False
        arm.rigify_layers[20].group = 0
        arm.rigify_layers[21].name = ""
        arm.rigify_layers[21].row = 1
        arm.rigify_layers[21].selset = False
        arm.rigify_layers[21].group = 0
        arm.rigify_layers[22].name = ""
        arm.rigify_layers[22].row = 1
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
        bone = arm.edit_bones.new('pelvis.L')
        bone.head = 0.0000, 0.0552, 1.0099
        bone.tail = 0.1112, -0.0451, 1.1533
        bone.roll = -1.0756
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine']]
        bones['pelvis.L'] = bone.name
        bone = arm.edit_bones.new('pelvis.R')
        bone.head = -0.0000, 0.0552, 1.0099
        bone.tail = -0.1112, -0.0451, 1.1533
        bone.roll = 1.0756
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine']]
        bones['pelvis.R'] = bone.name
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
        bone = arm.edit_bones.new('spine.002')
        bone.head = 0.0000, 0.0004, 1.2929
        bone.tail = 0.0000, 0.0059, 1.4657
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.001']]
        bones['spine.002'] = bone.name
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
        bone = arm.edit_bones.new('spine.003')
        bone.head = 0.0000, 0.0059, 1.4657
        bone.tail = 0.0000, 0.0114, 1.6582
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['spine.003'] = bone.name
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
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.R']]
        bones['foot.R'] = bone.name
        bone = arm.edit_bones.new('spine.004')
        bone.head = 0.0000, 0.0114, 1.6582
        bone.tail = 0.0000, -0.0130, 1.7197
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['spine.004'] = bone.name
        bone = arm.edit_bones.new('shoulder.L')
        bone.head = 0.0183, -0.0684, 1.6051
        bone.tail = 0.1694, 0.0205, 1.6050
        bone.roll = 0.0004
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['shoulder.L'] = bone.name
        bone = arm.edit_bones.new('shoulder.R')
        bone.head = -0.0183, -0.0684, 1.6051
        bone.tail = -0.1694, 0.0205, 1.6050
        bone.roll = -0.0004
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['shoulder.R'] = bone.name
        bone = arm.edit_bones.new('breast.L')
        bone.head = 0.1184, 0.0485, 1.4596
        bone.tail = 0.1184, -0.0907, 1.4596
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['breast.L'] = bone.name
        bone = arm.edit_bones.new('breast.R')
        bone.head = -0.1184, 0.0485, 1.4596
        bone.tail = -0.1184, -0.0907, 1.4596
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['breast.R'] = bone.name
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
        bone.roll = 0.0000
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
        bone = arm.edit_bones.new('spine.005')
        bone.head = 0.0000, -0.0130, 1.7197
        bone.tail = 0.0000, -0.0247, 1.7813
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.004']]
        bones['spine.005'] = bone.name
        bone = arm.edit_bones.new('upper_arm.L')
        bone.head = 0.1953, 0.0267, 1.5846
        bone.tail = 0.4424, 0.0885, 1.4491
        bone.roll = 2.0724
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['shoulder.L']]
        bones['upper_arm.L'] = bone.name
        bone = arm.edit_bones.new('upper_arm.R')
        bone.head = -0.1953, 0.0267, 1.5846
        bone.tail = -0.4424, 0.0885, 1.4491
        bone.roll = -2.0724
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['shoulder.R']]
        bones['upper_arm.R'] = bone.name
        bone = arm.edit_bones.new('spine.006')
        bone.head = 0.0000, -0.0247, 1.7813
        bone.tail = 0.0000, -0.0247, 1.9796
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['spine.006'] = bone.name
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
        pbone = obj.pose.bones[bones['spine']]
        pbone.rigify_type = 'spines.basic_spine'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.001']]
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
        pbone.rigify_type = 'limbs.super_limb'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.rigify_type = 'limbs.super_limb'
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
            pbone.rigify_parameters.limb_type = "leg"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['spine.002']]
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
        pbone = obj.pose.bones[bones['spine.003']]
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
        pbone = obj.pose.bones[bones['spine.004']]
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
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_widget = True
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.super_copy_widget_type = "shoulder"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['shoulder.R']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_widget = True
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.super_copy_widget_type = "shoulder"
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['breast.L']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['breast.R']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['toe.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['heel.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['toe.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['heel.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['spine.005']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['upper_arm.L']]
        pbone.rigify_type = 'limbs.super_limb'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone = obj.pose.bones[bones['spine.006']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['forearm.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['forearm.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['hand.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['hand.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['palm.01.L']]
        pbone.rigify_type = 'limbs.super_palm'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['palm.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['palm.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['palm.04.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['palm.01.R']]
        pbone.rigify_type = 'limbs.super_palm'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['palm.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['palm.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['palm.04.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_index.01.L']]
        pbone.rigify_type = 'limbs.super_finger'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['thumb.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_middle.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_ring.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_pinky.02.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_index.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['thumb.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_middle.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_ring.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_pinky.02.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_index.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['thumb.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_middle.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_ring.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_pinky.03.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_index.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['thumb.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_middle.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_ring.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_pinky.03.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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

        arm.layers = [(x in [3, 5, 7, 10, 13, 16]) for x in range(32)]


        # View - Frame Selected
        bpy.ops.view3d.view_selected(use_all_regions=0)

     

        return {'FINISHED'}



#=====================================================
#     END  - HUMAN METARIG WITH HANDS (NO FACE)
#=====================================================










classes = [ OBJECT_OT_human_metarig_no_face_with_hands_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()














 
