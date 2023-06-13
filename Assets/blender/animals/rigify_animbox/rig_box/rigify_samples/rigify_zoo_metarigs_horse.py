import bpy
from mathutils import Color



#=====================================================
#            RIGIFY SAMPLES 
#=====================================================
 

#=====================================================
#            RIGIFY ZOO METARIG - HORSE   
#=====================================================
 
 
 

# Add Rigify Metarig - Horse
class OBJECT_OT_rigify_zoo_horse_metarig_ra(bpy.types.Operator):
    '''Rigify ZOO Metarig - Horse'''
    bl_idname = "object.rigify_zoo_horse_metarig_ra"
    bl_label = "Horse Metarig"
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
        arm.rigify_colors[0].active = Color((0.5490000247955322, 1.0, 1.0))
        arm.rigify_colors[0].normal = Color((0.4352940022945404, 0.18431399762630463, 0.4156860113143921))
        arm.rigify_colors[0].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
        arm.rigify_colors[0].standard_colors_lock = True
        arm.rigify_colors[1].name = "IK"
        arm.rigify_colors[1].active = Color((0.5490000247955322, 1.0, 1.0))
        arm.rigify_colors[1].normal = Color((0.6039220094680786, 0.0, 0.0))
        arm.rigify_colors[1].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
        arm.rigify_colors[1].standard_colors_lock = True
        arm.rigify_colors[2].name = "Special"
        arm.rigify_colors[2].active = Color((0.5490000247955322, 1.0, 1.0))
        arm.rigify_colors[2].normal = Color((0.9568629860877991, 0.7882350087165833, 0.04705899953842163))
        arm.rigify_colors[2].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
        arm.rigify_colors[2].standard_colors_lock = True
        arm.rigify_colors[3].name = "Tweak"
        arm.rigify_colors[3].active = Color((0.5490000247955322, 1.0, 1.0))
        arm.rigify_colors[3].normal = Color((0.03921600058674812, 0.21176500618457794, 0.5803920030593872))
        arm.rigify_colors[3].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
        arm.rigify_colors[3].standard_colors_lock = True
        arm.rigify_colors[4].name = "FK"
        arm.rigify_colors[4].active = Color((0.5490000247955322, 1.0, 1.0))
        arm.rigify_colors[4].normal = Color((0.11764699965715408, 0.5686269998550415, 0.035294000059366226))
        arm.rigify_colors[4].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
        arm.rigify_colors[4].standard_colors_lock = True
        arm.rigify_colors[5].name = "Extra"
        arm.rigify_colors[5].active = Color((0.5490000247955322, 1.0, 1.0))
        arm.rigify_colors[5].normal = Color((0.9686279892921448, 0.2509799897670746, 0.09411799907684326))
        arm.rigify_colors[5].select = Color((0.3140000104904175, 0.7839999794960022, 1.0))
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
        arm.rigify_layers[1].group = 4
        arm.rigify_layers[2].name = " "
        arm.rigify_layers[2].row = 3
        arm.rigify_layers[2].selset = False
        arm.rigify_layers[2].group = 0
        arm.rigify_layers[3].name = "Spine"
        arm.rigify_layers[3].row = 4
        arm.rigify_layers[3].selset = False
        arm.rigify_layers[3].group = 3
        arm.rigify_layers[4].name = "Spine (Tweak)"
        arm.rigify_layers[4].row = 5
        arm.rigify_layers[4].selset = False
        arm.rigify_layers[4].group = 4
        arm.rigify_layers[5].name = " "
        arm.rigify_layers[5].row = 1
        arm.rigify_layers[5].selset = False
        arm.rigify_layers[5].group = 0
        arm.rigify_layers[6].name = " "
        arm.rigify_layers[6].row = 1
        arm.rigify_layers[6].selset = False
        arm.rigify_layers[6].group = 0
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
        arm.rigify_layers[20].name = " "
        arm.rigify_layers[20].row = 1
        arm.rigify_layers[20].selset = False
        arm.rigify_layers[20].group = 4
        arm.rigify_layers[21].name = "Hair"
        arm.rigify_layers[21].row = 14
        arm.rigify_layers[21].selset = False
        arm.rigify_layers[21].group = 6
        arm.rigify_layers[22].name = " "
        arm.rigify_layers[22].row = 1
        arm.rigify_layers[22].selset = False
        arm.rigify_layers[22].group = 0
        arm.rigify_layers[23].name = " "
        arm.rigify_layers[23].row = 1
        arm.rigify_layers[23].selset = False
        arm.rigify_layers[23].group = 0
        arm.rigify_layers[24].name = " "
        arm.rigify_layers[24].row = 1
        arm.rigify_layers[24].selset = False
        arm.rigify_layers[24].group = 0
        arm.rigify_layers[25].name = " "
        arm.rigify_layers[25].row = 1
        arm.rigify_layers[25].selset = False
        arm.rigify_layers[25].group = 0
        arm.rigify_layers[26].name = " "
        arm.rigify_layers[26].row = 1
        arm.rigify_layers[26].selset = False
        arm.rigify_layers[26].group = 0
        arm.rigify_layers[27].name = " "
        arm.rigify_layers[27].row = 1
        arm.rigify_layers[27].selset = False
        arm.rigify_layers[27].group = 0
        arm.rigify_layers[28].name = "Root"
        arm.rigify_layers[28].row = 14
        arm.rigify_layers[28].selset = False
        arm.rigify_layers[28].group = 1

        bones = {}

        bone = arm.edit_bones.new('spine.001')
        bone.head = -0.0000, 0.5403, 1.1974
        bone.tail = -0.0000, 0.3066, 1.2815
        bone.roll = -0.0000
        bone.use_connect = False
        bones['spine.001'] = bone.name
        bone = arm.edit_bones.new('tail.001')
        bone.head = -0.0000, 0.5947, 1.3219
        bone.tail = -0.0000, 0.7229, 1.2657
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.001']]
        bones['tail.001'] = bone.name
        bone = arm.edit_bones.new('spine.002')
        bone.head = -0.0000, 0.3066, 1.2815
        bone.tail = -0.0000, 0.1602, 1.2573
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.001']]
        bones['spine.002'] = bone.name
        bone = arm.edit_bones.new('tail.002')
        bone.head = -0.0000, 0.7229, 1.2657
        bone.tail = -0.0000, 0.8126, 1.1582
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['tail.001']]
        bones['tail.002'] = bone.name
        bone = arm.edit_bones.new('spine.003')
        bone.head = -0.0000, 0.1602, 1.2573
        bone.tail = -0.0000, -0.0226, 1.2225
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['spine.003'] = bone.name
        bone = arm.edit_bones.new('pelvis.L')
        bone.head = -0.0000, 0.5403, 1.1974
        bone.tail = 0.0980, 0.3514, 1.3329
        bone.roll = 0.3258
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['pelvis.L'] = bone.name
        bone = arm.edit_bones.new('pelvis.R')
        bone.head = 0.0000, 0.5403, 1.1974
        bone.tail = -0.0980, 0.3514, 1.3329
        bone.roll = -0.3258
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['pelvis.R'] = bone.name
        bone = arm.edit_bones.new('hip')
        bone.head = -0.0000, 0.5403, 1.1974
        bone.tail = 0.0000, 0.4636, 1.0212
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['hip'] = bone.name
        bone = arm.edit_bones.new('tail.003')
        bone.head = -0.0000, 0.8126, 1.1582
        bone.tail = 0.0000, 0.8662, 1.0289
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['tail.002']]
        bones['tail.003'] = bone.name
        bone = arm.edit_bones.new('spine.004')
        bone.head = -0.0000, -0.0226, 1.2225
        bone.tail = -0.0000, -0.2976, 1.2194
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['spine.004'] = bone.name
        bone = arm.edit_bones.new('abdomen')
        bone.head = 0.0000, 0.1503, 1.1819
        bone.tail = 0.0000, 0.1869, 0.9629
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['abdomen'] = bone.name
        bone = arm.edit_bones.new('thigh.L')
        bone.head = 0.1605, 0.4663, 1.1109
        bone.tail = 0.1616, 0.4541, 0.8213
        bone.roll = 3.1369
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['pelvis.L']]
        bones['thigh.L'] = bone.name
        bone = arm.edit_bones.new('thigh.R')
        bone.head = -0.1605, 0.4663, 1.1109
        bone.tail = -0.1616, 0.4541, 0.8213
        bone.roll = -3.1369
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['pelvis.R']]
        bones['thigh.R'] = bone.name
        bone = arm.edit_bones.new('tail.004')
        bone.head = 0.0000, 0.8662, 1.0289
        bone.tail = -0.0000, 0.8949, 0.8919
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['tail.003']]
        bones['tail.004'] = bone.name
        bone = arm.edit_bones.new('spine.005')
        bone.head = -0.0000, -0.2976, 1.2194
        bone.tail = -0.0000, -0.4757, 1.2471
        bone.roll = 0.0001
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.004']]
        bones['spine.005'] = bone.name
        bone = arm.edit_bones.new('lower_leg.L')
        bone.head = 0.1616, 0.4541, 0.8213
        bone.tail = 0.1616, 0.5796, 0.5283
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.L']]
        bones['lower_leg.L'] = bone.name
        bone = arm.edit_bones.new('lower_leg.R')
        bone.head = -0.1616, 0.4541, 0.8213
        bone.tail = -0.1616, 0.5796, 0.5283
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.R']]
        bones['lower_leg.R'] = bone.name
        bone = arm.edit_bones.new('tail.005')
        bone.head = -0.0000, 0.8949, 0.8919
        bone.tail = -0.0000, 0.9309, 0.7565
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['tail.004']]
        bones['tail.005'] = bone.name
        bone = arm.edit_bones.new('spine.006')
        bone.head = -0.0000, -0.4757, 1.2471
        bone.tail = -0.0000, -0.5908, 1.2785
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['spine.006'] = bone.name
        bone = arm.edit_bones.new('shoulder.L')
        bone.head = 0.0822, -0.4983, 1.4009
        bone.tail = 0.1346, -0.6484, 1.0838
        bone.roll = -0.1890
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['shoulder.L'] = bone.name
        bone = arm.edit_bones.new('breast.L')
        bone.head = 0.0719, -0.4916, 1.1731
        bone.tail = 0.0719, -0.6919, 0.9810
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['breast.L'] = bone.name
        bone = arm.edit_bones.new('shoulder.R')
        bone.head = -0.0822, -0.4983, 1.4009
        bone.tail = -0.1346, -0.6484, 1.0838
        bone.roll = 0.1890
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['shoulder.R'] = bone.name
        bone = arm.edit_bones.new('breast.R')
        bone.head = -0.0719, -0.4916, 1.1731
        bone.tail = -0.0719, -0.6919, 0.9810
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['breast.R'] = bone.name
        bone = arm.edit_bones.new('chest')
        bone.head = 0.0000, -0.2180, 1.2173
        bone.tail = 0.0000, -0.2239, 0.8605
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['chest'] = bone.name
        bone = arm.edit_bones.new('hind_foot.L')
        bone.head = 0.1616, 0.5796, 0.5283
        bone.tail = 0.1616, 0.6062, 0.1871
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['lower_leg.L']]
        bones['hind_foot.L'] = bone.name
        bone = arm.edit_bones.new('hind_foot.R')
        bone.head = -0.1616, 0.5796, 0.5283
        bone.tail = -0.1616, 0.6062, 0.1871
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['lower_leg.R']]
        bones['hind_foot.R'] = bone.name
        bone = arm.edit_bones.new('neck.001')
        bone.head = -0.0000, -0.5908, 1.2785
        bone.tail = -0.0000, -0.6699, 1.3504
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.006']]
        bones['neck.001'] = bone.name
        bone = arm.edit_bones.new('upper_arm.L')
        bone.head = 0.1539, -0.6429, 1.0469
        bone.tail = 0.1539, -0.5644, 0.8280
        bone.roll = 3.1416
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['shoulder.L']]
        bones['upper_arm.L'] = bone.name
        bone = arm.edit_bones.new('upper_arm.R')
        bone.head = -0.1539, -0.6429, 1.0469
        bone.tail = -0.1539, -0.5644, 0.8280
        bone.roll = -3.1416
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['shoulder.R']]
        bones['upper_arm.R'] = bone.name
        bone = arm.edit_bones.new('r_toe.L')
        bone.head = 0.1616, 0.6062, 0.1871
        bone.tail = 0.1616, 0.5767, 0.0861
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['hind_foot.L']]
        bones['r_toe.L'] = bone.name
        bone = arm.edit_bones.new('r_toe.R')
        bone.head = -0.1616, 0.6062, 0.1871
        bone.tail = -0.1616, 0.5767, 0.0861
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['hind_foot.R']]
        bones['r_toe.R'] = bone.name
        bone = arm.edit_bones.new('neck.002')
        bone.head = -0.0000, -0.6699, 1.3504
        bone.tail = -0.0000, -0.7487, 1.4479
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['neck.001']]
        bones['neck.002'] = bone.name
        bone = arm.edit_bones.new('forearm.L')
        bone.head = 0.1539, -0.5644, 0.8280
        bone.tail = 0.1539, -0.5499, 0.4490
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['upper_arm.L']]
        bones['forearm.L'] = bone.name
        bone = arm.edit_bones.new('forearm.R')
        bone.head = -0.1539, -0.5644, 0.8280
        bone.tail = -0.1539, -0.5499, 0.4490
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['upper_arm.R']]
        bones['forearm.R'] = bone.name
        bone = arm.edit_bones.new('r_hoof.L')
        bone.head = 0.1616, 0.5767, 0.0861
        bone.tail = 0.1616, 0.5170, 0.0007
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['r_toe.L']]
        bones['r_hoof.L'] = bone.name
        bone = arm.edit_bones.new('r_hoof.R')
        bone.head = -0.1616, 0.5767, 0.0861
        bone.tail = -0.1616, 0.5170, 0.0007
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['r_toe.R']]
        bones['r_hoof.R'] = bone.name
        bone = arm.edit_bones.new('neck.003')
        bone.head = -0.0000, -0.7487, 1.4479
        bone.tail = -0.0000, -0.8447, 1.5479
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['neck.002']]
        bones['neck.003'] = bone.name
        bone = arm.edit_bones.new('forefoot.L')
        bone.head = 0.1539, -0.5499, 0.4490
        bone.tail = 0.1539, -0.5221, 0.1579
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['forearm.L']]
        bones['forefoot.L'] = bone.name
        bone = arm.edit_bones.new('forefoot.R')
        bone.head = -0.1539, -0.5499, 0.4490
        bone.tail = -0.1539, -0.5221, 0.1579
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['forearm.R']]
        bones['forefoot.R'] = bone.name
        bone = arm.edit_bones.new('neck.004')
        bone.head = -0.0000, -0.8447, 1.5479
        bone.tail = -0.0000, -0.9814, 1.6223
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['neck.003']]
        bones['neck.004'] = bone.name
        bone = arm.edit_bones.new('f_toe.L')
        bone.head = 0.1539, -0.5221, 0.1579
        bone.tail = 0.1539, -0.5716, 0.0672
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['forefoot.L']]
        bones['f_toe.L'] = bone.name
        bone = arm.edit_bones.new('f_toe.R')
        bone.head = -0.1539, -0.5221, 0.1579
        bone.tail = -0.1539, -0.5716, 0.0672
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['forefoot.R']]
        bones['f_toe.R'] = bone.name
        bone = arm.edit_bones.new('head')
        bone.head = -0.0000, -0.9814, 1.6223
        bone.tail = -0.0000, -1.1679, 1.6885
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['neck.004']]
        bones['head'] = bone.name
        bone = arm.edit_bones.new('f_hoof.L')
        bone.head = 0.1539, -0.5716, 0.0672
        bone.tail = 0.1539, -0.6251, 0.0007
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_toe.L']]
        bones['f_hoof.L'] = bone.name
        bone = arm.edit_bones.new('f_hoof.R')
        bone.head = -0.1539, -0.5716, 0.0672
        bone.tail = -0.1539, -0.6251, 0.0007
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['f_toe.R']]
        bones['f_hoof.R'] = bone.name
        bone = arm.edit_bones.new('skull')
        bone.head = -0.0000, -1.0585, 1.5732
        bone.tail = 0.0000, -1.3560, 1.3327
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['head']]
        bones['skull'] = bone.name

        obj = bpy.context.object 

        bpy.ops.object.mode_set(mode='OBJECT')
        pbone = obj.pose.bones[bones['spine.001']]
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
        pbone = obj.pose.bones[bones['tail.001']]
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
            pbone.rigify_parameters.connect_chain = False
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
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['tail.002']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['spine.003']]
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
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_widget = False
        except AttributeError:
            pass
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
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_widget = False
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.make_control = False
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['hip']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['tail.003']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['spine.004']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['abdomen']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['thigh.L']]
        pbone.rigify_type = 'limbs.rear_paw'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.segments = 2
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.bbones = 10
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers_extra = True
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers_extra = True
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
            pbone.rigify_parameters.segments = 2
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.bbones = 10
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers_extra = True
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers_extra = True
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['tail.004']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['spine.005']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['lower_leg.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['lower_leg.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['tail.005']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['spine.006']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['shoulder.L']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['shoulder.R']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_widget = False
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['breast.R']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['chest']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['hind_foot.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['hind_foot.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['neck.001']]
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
        pbone = obj.pose.bones[bones['upper_arm.L']]
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
        try:
            pbone.rigify_parameters.front_paw_heel_influence = 0.6000000238418579
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['upper_arm.R']]
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
        try:
            pbone.rigify_parameters.front_paw_heel_influence = 0.6000000238418579
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['r_toe.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['r_toe.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['neck.002']]
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
        pbone = obj.pose.bones[bones['r_hoof.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['r_hoof.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['neck.003']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['forefoot.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['forefoot.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['neck.004']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_toe.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_toe.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['head']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_hoof.L']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['f_hoof.R']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['skull']]
        pbone.rigify_type = 'basic.super_copy'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_widget = False
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.make_control = False
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
#     END  -   RIGIFY ZOO METARIG - HORSE   
#=====================================================
  



classes = [ OBJECT_OT_rigify_zoo_horse_metarig_ra,

          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()







