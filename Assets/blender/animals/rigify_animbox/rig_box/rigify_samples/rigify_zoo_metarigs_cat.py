import bpy
from mathutils import Color



#=====================================================
#            RIGIFY SAMPLES 
#=====================================================
 

#=====================================================
#            RIGIFY ZOO METARIG - CAT
#=====================================================
 
 
 

# Add Rigify Metarig - Cat
class OBJECT_OT_rigify_zoo_cat_metarig_ra(bpy.types.Operator):
    '''Rigify ZOO Metarig - Cat'''
    bl_idname = "object.rigify_zoo_cat_metarig_ra"
    bl_label = "Cat Metarig"
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
        arm.rigify_layers[9].name = "Arm,L (Tweak)"
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
        arm.rigify_layers[19].group = 3
        arm.rigify_layers[20].name = "Tail (Tweaks)"
        arm.rigify_layers[20].row = 14
        arm.rigify_layers[20].selset = False
        arm.rigify_layers[20].group = 4
        arm.rigify_layers[21].name = " "
        arm.rigify_layers[21].row = 1
        arm.rigify_layers[21].selset = False
        arm.rigify_layers[21].group = 0
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
        arm.rigify_layers[28].row = 16
        arm.rigify_layers[28].selset = False
        arm.rigify_layers[28].group = 1

        bones = {}

        bone = arm.edit_bones.new('spine')
        bone.head = -0.0000, 0.1229, 0.2479
        bone.tail = 0.0000, 0.0699, 0.2416
        bone.roll = -0.0000
        bone.use_connect = False
        bones['spine'] = bone.name
        bone = arm.edit_bones.new('tail.001')
        bone.head = -0.0000, 0.1229, 0.2479
        bone.tail = -0.0000, 0.2111, 0.2302
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine']]
        bones['tail.001'] = bone.name
        bone = arm.edit_bones.new('spine.001')
        bone.head = 0.0000, 0.0699, 0.2416
        bone.tail = -0.0000, 0.0090, 0.2323
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine']]
        bones['spine.001'] = bone.name
        bone = arm.edit_bones.new('pelvis.L')
        bone.head = -0.0000, 0.1229, 0.2479
        bone.tail = 0.0238, 0.1368, 0.2194
        bone.roll = -2.0314
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine']]
        bones['pelvis.L'] = bone.name
        bone = arm.edit_bones.new('pelvis.R')
        bone.head = 0.0000, 0.1229, 0.2479
        bone.tail = -0.0238, 0.1368, 0.2194
        bone.roll = 2.0314
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine']]
        bones['pelvis.R'] = bone.name
        bone = arm.edit_bones.new('pelvis.C')
        bone.head = -0.0000, 0.1229, 0.2479
        bone.tail = 0.0000, 0.1571, 0.2007
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine']]
        bones['pelvis.C'] = bone.name
        bone = arm.edit_bones.new('tail.002')
        bone.head = -0.0000, 0.2111, 0.2302
        bone.tail = -0.0000, 0.2770, 0.2066
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['tail.001']]
        bones['tail.002'] = bone.name
        bone = arm.edit_bones.new('spine.002')
        bone.head = -0.0000, 0.0090, 0.2323
        bone.tail = -0.0000, -0.0551, 0.2284
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.001']]
        bones['spine.002'] = bone.name
        bone = arm.edit_bones.new('thigh.L')
        bone.head = 0.0363, 0.1345, 0.2125
        bone.tail = 0.0365, 0.1141, 0.1186
        bone.roll = 3.1390
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['pelvis.L']]
        bones['thigh.L'] = bone.name
        bone = arm.edit_bones.new('thigh.R')
        bone.head = -0.0363, 0.1345, 0.2125
        bone.tail = -0.0365, 0.1141, 0.1186
        bone.roll = -3.1390
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['pelvis.R']]
        bones['thigh.R'] = bone.name
        bone = arm.edit_bones.new('tail.003')
        bone.head = -0.0000, 0.2770, 0.2066
        bone.tail = -0.0000, 0.3386, 0.1733
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['tail.002']]
        bones['tail.003'] = bone.name
        bone = arm.edit_bones.new('spine.003')
        bone.head = -0.0000, -0.0551, 0.2284
        bone.tail = -0.0000, -0.1408, 0.2343
        bone.roll = -0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['spine.003'] = bone.name
        bone = arm.edit_bones.new('belly.C')
        bone.head = 0.0000, 0.0128, 0.2056
        bone.tail = 0.0000, 0.0133, 0.1466
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.002']]
        bones['belly.C'] = bone.name
        bone = arm.edit_bones.new('shin.L')
        bone.head = 0.0365, 0.1141, 0.1186
        bone.tail = 0.0365, 0.1771, 0.0647
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.L']]
        bones['shin.L'] = bone.name
        bone = arm.edit_bones.new('shin.R')
        bone.head = -0.0365, 0.1141, 0.1186
        bone.tail = -0.0365, 0.1771, 0.0647
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['thigh.R']]
        bones['shin.R'] = bone.name
        bone = arm.edit_bones.new('tail.004')
        bone.head = -0.0000, 0.3386, 0.1733
        bone.tail = -0.0000, 0.3992, 0.1382
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['tail.003']]
        bones['tail.004'] = bone.name
        bone = arm.edit_bones.new('spine.004')
        bone.head = -0.0000, -0.1408, 0.2343
        bone.tail = 0.0000, -0.1636, 0.2493
        bone.roll = 0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['spine.004'] = bone.name
        bone = arm.edit_bones.new('Breast.C')
        bone.head = 0.0000, -0.0881, 0.2067
        bone.tail = 0.0000, -0.1205, 0.1670
        bone.roll = -0.0000
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['Breast.C'] = bone.name
        bone = arm.edit_bones.new('shoulder.L')
        bone.head = 0.0111, -0.0806, 0.2566
        bone.tail = 0.0399, -0.1103, 0.2030
        bone.roll = 2.1511
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['shoulder.L'] = bone.name
        bone = arm.edit_bones.new('shoulder.R')
        bone.head = -0.0111, -0.0806, 0.2566
        bone.tail = -0.0399, -0.1103, 0.2030
        bone.roll = -2.1511
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['spine.003']]
        bones['shoulder.R'] = bone.name
        bone = arm.edit_bones.new('foot.L')
        bone.head = 0.0365, 0.1771, 0.0647
        bone.tail = 0.0365, 0.1574, 0.0051
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.L']]
        bones['foot.L'] = bone.name
        bone = arm.edit_bones.new('foot.R')
        bone.head = -0.0365, 0.1771, 0.0647
        bone.tail = -0.0365, 0.1574, 0.0051
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['shin.R']]
        bones['foot.R'] = bone.name
        bone = arm.edit_bones.new('spine.005')
        bone.head = 0.0000, -0.1636, 0.2493
        bone.tail = 0.0000, -0.1882, 0.2738
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.004']]
        bones['spine.005'] = bone.name
        bone = arm.edit_bones.new('upper_arm.L')
        bone.head = 0.0385, -0.1105, 0.1946
        bone.tail = 0.0385, -0.0726, 0.1071
        bone.roll = 3.1416
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['shoulder.L']]
        bones['upper_arm.L'] = bone.name
        bone = arm.edit_bones.new('upper_arm.R')
        bone.head = -0.0385, -0.1105, 0.1946
        bone.tail = -0.0385, -0.0726, 0.1071
        bone.roll = -3.1416
        bone.use_connect = False
        bone.parent = arm.edit_bones[bones['shoulder.R']]
        bones['upper_arm.R'] = bone.name
        bone = arm.edit_bones.new('r_toe.L')
        bone.head = 0.0365, 0.1574, 0.0051
        bone.tail = 0.0365, 0.1275, 0.0017
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['foot.L']]
        bones['r_toe.L'] = bone.name
        bone = arm.edit_bones.new('r_toe.R')
        bone.head = -0.0365, 0.1574, 0.0051
        bone.tail = -0.0365, 0.1275, 0.0017
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['foot.R']]
        bones['r_toe.R'] = bone.name
        bone = arm.edit_bones.new('spine.006')
        bone.head = 0.0000, -0.1882, 0.2738
        bone.tail = 0.0000, -0.2537, 0.3277
        bone.roll = 0.0000
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['spine.005']]
        bones['spine.006'] = bone.name
        bone = arm.edit_bones.new('forearm.L')
        bone.head = 0.0385, -0.0726, 0.1071
        bone.tail = 0.0385, -0.0885, 0.0363
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['upper_arm.L']]
        bones['forearm.L'] = bone.name
        bone = arm.edit_bones.new('forearm.R')
        bone.head = -0.0385, -0.0726, 0.1071
        bone.tail = -0.0385, -0.0885, 0.0363
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['upper_arm.R']]
        bones['forearm.R'] = bone.name
        bone = arm.edit_bones.new('hand.L')
        bone.head = 0.0385, -0.0885, 0.0363
        bone.tail = 0.0385, -0.1072, 0.0071
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['forearm.L']]
        bones['hand.L'] = bone.name
        bone = arm.edit_bones.new('hand.R')
        bone.head = -0.0385, -0.0885, 0.0363
        bone.tail = -0.0385, -0.1072, 0.0071
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['forearm.R']]
        bones['hand.R'] = bone.name
        bone = arm.edit_bones.new('f_toe.L')
        bone.head = 0.0385, -0.1072, 0.0071
        bone.tail = 0.0385, -0.1370, 0.0018
        bone.roll = 3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['hand.L']]
        bones['f_toe.L'] = bone.name
        bone = arm.edit_bones.new('f_toe.R')
        bone.head = -0.0385, -0.1072, 0.0071
        bone.tail = -0.0385, -0.1370, 0.0018
        bone.roll = -3.1416
        bone.use_connect = True
        bone.parent = arm.edit_bones[bones['hand.R']]
        bones['f_toe.R'] = bone.name

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
            pbone.rigify_parameters.tweak_layers = [False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
            pbone.rigify_parameters.tweak_layers = [False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.copy_rotation_axes = [True, True, True]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.connect_chain = True
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
        pbone.rotation_mode = 'QUATERNION'
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
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_control = False
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['pelvis.C']]
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
        pbone = obj.pose.bones[bones['tail.002']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['spine.002']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        pbone = obj.pose.bones[bones['thigh.L']]
        pbone.rigify_type = 'limbs.super_limb'
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
        try:
            pbone.rigify_parameters.segments = 2
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
            pbone.rigify_parameters.limb_type = "paw"
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        pbone = obj.pose.bones[bones['tail.003']]
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
        pbone = obj.pose.bones[bones['belly.C']]
        pbone.rigify_type = 'basic.super_copy'
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
        pbone = obj.pose.bones[bones['tail.004']]
        pbone.rigify_type = ''
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]
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
        pbone = obj.pose.bones[bones['Breast.C']]
        pbone.rigify_type = 'basic.super_copy'
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
        pbone.rotation_mode = 'YXZ'
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_control = True
        except AttributeError:
            pass
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
        pbone.bone.layers = [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.make_control = True
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.make_widget = False
        except AttributeError:
            pass
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
        pbone = obj.pose.bones[bones['upper_arm.R']]
        pbone.rigify_type = 'limbs.super_limb'
        pbone.lock_location = (False, False, False)
        pbone.lock_rotation = (False, False, False)
        pbone.lock_rotation_w = False
        pbone.lock_scale = (False, False, False)
        pbone.rotation_mode = 'QUATERNION'
        pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        try:
            pbone.rigify_parameters.fk_layers = [False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.tweak_layers = [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        except AttributeError:
            pass
        try:
            pbone.rigify_parameters.limb_type = "paw"
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

        arm.layers = [(x in [3, 7, 10, 13, 16, 19]) for x in range(32)]


        
 
        # View - Frame Selected
        bpy.ops.view3d.view_selected(use_all_regions=0)

     

        return {'FINISHED'}



#=====================================================
#     END  -   RIGIFY ZOO METARIG - CAT 
#=====================================================
  
 


classes = [ OBJECT_OT_rigify_zoo_cat_metarig_ra,

          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()







 
