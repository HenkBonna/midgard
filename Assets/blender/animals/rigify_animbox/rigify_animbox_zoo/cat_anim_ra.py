import bpy


# =====================================================
#          RIGIFY ZOO
# =====================================================


# =====================================================
#          CAT - 32 FRAMES  WALK CYCLE
# =====================================================



# 32 FRAMES WALK CYCLE FOR RIGIFY ZOO - CAT
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_zoo_cat_walk_32_ra(bpy.types.Operator):
    '''32 Frames Walk Cycle For Rigify Zoo - Cat.
Rig Name must begin with: 'cat'
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_zoo_cat_walk_32_ra"
    bl_label = "Cat Walk"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and context.object.name.startswith(('Cat', 'cat', 'CAT'))
                and context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)
                
             
              

    def execute(self, context):



        # TOTAL RESET

        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        #bpy.ops.pose.transforms_clear()
        bpy.ops.anim.keyframe_clear_v3d() 
        bpy.ops.pose.select_all(action = 'DESELECT')
        bpy.ops.screen.frame_jump(end=False)
            


 
        pose_bones = bpy.context.object.pose.bones

           
         
        # DEFINING FRAME RANGE

        # START
        bpy.context.scene.frame_start = 1

        # END
        bpy.context.scene.frame_end = 32
         



        # NAMES 

        Head = [pb for pb in pose_bones  if pb.name.startswith('head')]

        Neck = [pb for pb in pose_bones  if pb.name.startswith('neck')]
                    
        Chest = [pb for pb in pose_bones  if pb.name.startswith('chest')]

        Torso = [pb for pb in pose_bones  if pb.name.startswith('torso')]

        Hips  = [pb for pb in pose_bones  if pb.name.startswith('hips')]



        Tail_001  = [pb for pb in pose_bones  if pb.name.startswith('tail.001') ]
        Tail_002  = [pb for pb in pose_bones  if pb.name.startswith('tail.002') ]
        Tail_003  = [pb for pb in pose_bones  if pb.name.startswith('tail.003') ]
        Tail_004  = [pb for pb in pose_bones  if pb.name.startswith('tail.004') ]
 
        Tail_Master_001 = [pb for pb in pose_bones  if pb.name.startswith('tail_master.001') ]
 
 
        # Legs/Feet

        # Front
        Hand_R  = [pb for pb in pose_bones  if pb.name.startswith('hand_ik.R')]
        Hand_Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('hand_heel_ik.R')]
        Front_Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('f_toe.R')]


        Hand_L  = [pb for pb in pose_bones  if pb.name.startswith('hand_ik.L')]
        Hand_Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('hand_heel_ik.L')]
        Front_Toe_L  = [pb for pb in pose_bones  if pb.name.startswith('f_toe.L')]

        # Rear

        Foot_R  = [pb for pb in pose_bones  if pb.name.startswith('foot_ik.R')]
        Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('foot_heel_ik.R')]
        Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('r_toe.R')]


        Foot_L  = [pb for pb in pose_bones  if pb.name.startswith('foot_ik.L')]
        Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('foot_heel_ik.L')]
        Toe_L = [pb for pb in pose_bones  if pb.name.startswith('r_toe.L')]







        # Insert Keys

        def insert_keys(frame):
            o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
            o.keyframe_insert(data_path = 'location', frame= frame)






        for o in Hand_R:
            o.location=(0.000, -0.100, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, 0.095, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(17)
            o.location=(0.000, -0.060, 0.040)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(24)
            o.location=(0.000, -0.120, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(29)
            o.location=(0.000, -0.100, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(33)


        for o in Hand_L:
            o.location=(0.000, 0.095, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, -0.060, 0.040)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(8)
            o.location=(0.000, -0.120, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(13)
            o.location=(0.000, 0.095, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(33)


        for o in Hand_Heel_R:
            o.rotation_quaternion=(1.000, 0.279, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, -0.300, 0.000, 0.000)
            insert_keys(20)
            o.rotation_quaternion=(1.000, 0.279, 0.000, 0.000)
            insert_keys(33)


        for o in Hand_Heel_L:
            o.rotation_quaternion=(1.000, -0.300, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.300, 0.000, 0.000)
            insert_keys(20)
            o.rotation_quaternion=(1.000, -0.300, 0.000, 0.000)
            insert_keys(33)


        for o in Front_Toe_R:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(18)
            o.rotation_quaternion=(1.000, -1.000, 0.000, 0.000)
            insert_keys(24)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(29)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(33)


        for o in Front_Toe_L:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(2)
            o.rotation_quaternion=(1.000, -1.000, 0.000, 0.000)
            insert_keys(8)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(13)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(33)


        for o in Foot_R:
            o.location=(0.000, 0.016, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, 0.100, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(9)
            o.location=(0.000, -0.010, 0.030)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(15)
            o.location=(0.000, -0.145, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(21)
            o.location=(0.000, -0.020, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(31)
            o.location=(0.000, 0.016, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(33)


        for o in Foot_L:
            o.location=(0.000, -0.072, 0.022)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, -0.145, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(5)
            o.location=(0.000, 0.100, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(25)
            o.location=(0.000, -0.010, 0.030)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(31)
            o.location=(0.000, -0.072, 0.022)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(33)


        for o in Heel_R:
            o.rotation_quaternion=(1.000, 0.099, -0.003, 0.002)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(0.997, -0.100, -0.002, 0.002)
            insert_keys(18)
            o.rotation_quaternion=(0.995, -0.250, -0.004, 0.004)
            insert_keys(25)
            o.rotation_quaternion=(1.000, -0.014, -0.003, 0.003)
            insert_keys(31)
            o.rotation_quaternion=(1.000, 0.099, -0.003, 0.002)
            insert_keys(33)


        for o in Heel_L:
            o.rotation_quaternion=(1.000, 0.119, -0.002, 0.001)
            insert_keys(1)
            o.rotation_quaternion=(0.999, -0.100, -0.003, 0.002)
            insert_keys(3)
            o.rotation_quaternion=(0.995, -0.250, -0.004, 0.004)
            insert_keys(10)
            o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
            insert_keys(26)
            o.rotation_quaternion=(1.000, 0.321, -0.001, 0.001)
            insert_keys(31)
            o.rotation_quaternion=(1.000, 0.119, -0.002, 0.001)
            insert_keys(33)


        for o in Toe_R:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(11)
            o.rotation_quaternion=(1.000, 0.800, 0.000, 0.000)
            insert_keys(15)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(19)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(31)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(33)


        for o in Toe_L:
            o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(3)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(27)
            o.rotation_quaternion=(1.000, 0.800, 0.000, 0.000)
            insert_keys(31)
            o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
            insert_keys(33)


        for o in Torso:
            o.location=(0.000, 0.000, -0.010)
            insert_keys(1)
            o.location=(0.000, 0.000, -0.010)
            insert_keys(33)


        for o in Hips:
            o.location=(-0.007, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.030, 0.050, -0.018)
            insert_keys(1)
            o.location=(0.001, 0.000, 0.000)
            o.rotation_quaternion=(1.000, -0.015, -0.015, -0.050)
            insert_keys(7)
            o.location=(0.007, 0.000, 0.000)
            o.rotation_quaternion=(1.000, -0.040, -0.050, -0.034)
            insert_keys(11)
            o.location=(0.008, 0.000, 0.000)
            o.rotation_quaternion=(1.000, -0.005, -0.050, -0.009)
            insert_keys(14)
            o.location=(0.007, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.030, -0.050, 0.018)
            insert_keys(17)
            o.location=(-0.001, 0.000, 0.000)
            o.rotation_quaternion=(1.000, -0.015, 0.015, 0.050)
            insert_keys(23)
            o.location=(-0.007, 0.000, 0.000)
            o.rotation_quaternion=(1.000, -0.040, 0.050, 0.034)
            insert_keys(27)
            o.location=(-0.008, 0.000, 0.000)
            o.rotation_quaternion=(1.000, -0.005, 0.050, 0.009)
            insert_keys(30)
            o.location=(-0.007, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.030, 0.050, -0.018)
            insert_keys(33)


        for o in Chest:
            o.location=(0.000, 0.000, -0.015)
            o.rotation_quaternion=(1.000, -0.010, -0.055, 0.050)
            insert_keys(1)
            o.location=(0.000, 0.000, -0.010)
            o.rotation_quaternion=(1.000, -0.020, 0.055, -0.069)
            insert_keys(9)
            o.location=(0.000, 0.000, -0.013)
            o.rotation_quaternion=(1.000, -0.015, 0.080, -0.100)
            insert_keys(13)
            o.location=(0.000, 0.000, -0.015)
            o.rotation_quaternion=(1.000, -0.010, 0.055, -0.050)
            insert_keys(17)
            o.location=(0.000, 0.000, -0.010)
            o.rotation_quaternion=(1.000, -0.020, -0.055, 0.078)
            insert_keys(25)
            o.location=(0.000, 0.000, -0.013)
            o.rotation_quaternion=(1.000, -0.015, -0.080, 0.100)
            insert_keys(29)
            o.location=(0.000, 0.000, -0.015)
            o.rotation_quaternion=(1.000, -0.010, -0.055, 0.050)
            insert_keys(33)


        for o in Neck:
            o.rotation_quaternion=(1.000, 0.108, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.150, 0.000, 0.000)
            insert_keys(7)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(15)
            o.rotation_quaternion=(1.000, 0.150, 0.000, 0.000)
            insert_keys(23)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(31)
            o.rotation_quaternion=(1.000, 0.108, 0.000, 0.000)
            insert_keys(33)


        for o in Head:
            o.rotation_quaternion=(1.000, 0.050, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(8)
            o.rotation_quaternion=(1.000, 0.050, 0.000, 0.000)
            insert_keys(16)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(24)
            o.rotation_quaternion=(1.000, 0.050, 0.000, 0.000)
            insert_keys(33)


        for o in Tail_001:
            o.rotation_quaternion=(1.000, -0.032, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, -0.030, 0.000, 0.000)
            insert_keys(2)
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(1.000, -0.030, 0.000, 0.000)
            insert_keys(18)
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.000)
            insert_keys(26)
            o.rotation_quaternion=(1.000, -0.048, 0.000, 0.000)
            insert_keys(31)
            o.rotation_quaternion=(1.000, -0.032, 0.000, 0.000)
            insert_keys(33)


        for o in Tail_002:
            o.rotation_quaternion=(1.000, 0.005, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.010, 0.000, 0.000)
            insert_keys(4)
            o.rotation_quaternion=(1.000, -0.010, 0.000, 0.000)
            insert_keys(12)
            o.rotation_quaternion=(1.000, 0.010, 0.000, 0.000)
            insert_keys(20)
            o.rotation_quaternion=(1.000, -0.010, 0.000, 0.000)
            insert_keys(28)
            o.rotation_quaternion=(1.000, -0.002, 0.000, 0.000)
            insert_keys(31)
            o.rotation_quaternion=(1.000, 0.005, 0.000, 0.000)
            insert_keys(33)


        for o in Tail_003:
            o.rotation_quaternion=(1.000, 0.106, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.150, 0.000, 0.000)
            insert_keys(8)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(17)
            o.rotation_quaternion=(1.000, 0.150, 0.000, 0.000)
            insert_keys(25)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(31)
            o.rotation_quaternion=(1.000, 0.106, 0.000, 0.000)
            insert_keys(33)


        for o in Tail_004:
            o.rotation_quaternion=(1.000, 0.006, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(6)
            o.rotation_quaternion=(1.000, -0.050, 0.000, 0.000)
            insert_keys(15)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(23)
            o.rotation_quaternion=(1.000, -0.018, 0.000, 0.000)
            insert_keys(31)
            o.rotation_quaternion=(1.000, 0.006, 0.000, 0.000)
            insert_keys(33)


        for o in Tail_Master_001:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.045)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.050)
            insert_keys(15)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.049)
            insert_keys(31)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.045)
            insert_keys(33)







        # Add Cycles Modifier

        ob = bpy.context.object
        ob_fcurve = ob.animation_data.action.fcurves


        def add_cycle_modifier():
            
               
            for fc in ob_fcurve:
                d_path = ('location', 'rotation_quaternion')
                     
                if fc.data_path.endswith((d_path)):
                    fc.modifiers.new(type='CYCLES')
                
                fc.update()


        add_cycle_modifier()
         

        # Action Name
        ob = bpy.context.object
        ob.animation_data.action.name = ob.name + '_Walk' 

         
        # JUMP TO START AND PLAY ANIMATION
        bpy.ops.screen.frame_jump(end=False)
        bpy.ops.screen.animation_play()



        # FRAME SELECTED RANGE IN TIMELINE

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

              

        return {'FINISHED'}



# =====================================================
#      END  - CAT - 32 FRAMES  WALK CYCLE
# =====================================================

 
 



# =====================================================
#          CAT - 14 FRAMES  RUN CYCLE
# =====================================================




# 14 FRAMES RUN CYCLE FOR RIGIFY ZOO - CAT
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_zoo_cat_run_14_ra(bpy.types.Operator):
    '''14 Frames Run Cycle For Rigify Zoo - Cat.
Rig Name must begin with: 'cat' 
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_zoo_cat_run_14_ra"
    bl_label = "Cat Run"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and context.object.name.startswith(('Cat', 'cat', 'CAT'))
                and context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)
                
                
              

    def execute(self, context):



        # TOTAL RESET

        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        #bpy.ops.pose.transforms_clear()
        bpy.ops.anim.keyframe_clear_v3d() 
        bpy.ops.pose.select_all(action = 'DESELECT')
        bpy.ops.screen.frame_jump(end=False)
            


 
        pose_bones = bpy.context.object.pose.bones

           
         
        # DEFINING FRAME RANGE

        # START
        bpy.context.scene.frame_start = 1

        # END
        bpy.context.scene.frame_end = 14
         



        # NAMES 

        Head = [pb for pb in pose_bones  if pb.name.startswith('head')]

        Neck = [pb for pb in pose_bones  if pb.name.startswith('neck')]
                    
        Chest = [pb for pb in pose_bones  if pb.name.startswith('chest')]

        Torso = [pb for pb in pose_bones  if pb.name.startswith('torso')]

        Hips  = [pb for pb in pose_bones  if pb.name.startswith('hips')]



        Tail_Master_001 = [pb for pb in pose_bones  if pb.name.startswith('tail_master.001') ]
 
 
        # Legs/Feet

        # Front
        Hand_R  = [pb for pb in pose_bones  if pb.name.startswith('hand_ik.R')]
        Hand_Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('hand_heel_ik.R')]
        Front_Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('f_toe.R')]


        Hand_L  = [pb for pb in pose_bones  if pb.name.startswith('hand_ik.L')]
        Hand_Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('hand_heel_ik.L')]
        Front_Toe_L  = [pb for pb in pose_bones  if pb.name.startswith('f_toe.L')]

        # Rear

        Foot_R  = [pb for pb in pose_bones  if pb.name.startswith('foot_ik.R')]
        Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('foot_heel_ik.R')]
        Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('r_toe.R')]


        Foot_L  = [pb for pb in pose_bones  if pb.name.startswith('foot_ik.L')]
        Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('foot_heel_ik.L')]
        Toe_L = [pb for pb in pose_bones  if pb.name.startswith('r_toe.L')]


        # Extra
        Spine_FK_001  = [pb for pb in pose_bones  if pb.name.startswith('spine_fk.001')]
        Spine_FK_003  = [pb for pb in pose_bones  if pb.name.startswith('spine_fk.003')]




        # Insert Keys

        def insert_keys(frame):
            o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
            o.keyframe_insert(data_path = 'location', frame= frame)







        for o in Hand_R:
            o.location=(0.000, -0.200, 0.190)
            o.rotation_quaternion=(1.000, -0.200, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, -0.050, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(4)
            o.location=(0.000, 0.100, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(6)
            o.location=(0.000, 0.170, 0.020)
            o.rotation_quaternion=(1.000, 0.600, 0.000, 0.000)
            insert_keys(7)
            o.location=(0.000, 0.160, 0.040)
            o.rotation_quaternion=(1.000, 0.700, 0.000, 0.000)
            insert_keys(8)
            o.location=(0.000, -0.040, 0.080)
            o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
            insert_keys(11)
            o.location=(0.000, -0.110, 0.110)
            o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
            insert_keys(12)
            o.location=(0.000, -0.200, 0.190)
            o.rotation_quaternion=(1.000, -0.200, 0.000, 0.000)
            insert_keys(15)


        for o in Hand_L:
            o.location=(0.000, -0.200, 0.176)
            o.rotation_quaternion=(1.000, 0.015, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, -0.190, 0.190)
            o.rotation_quaternion=(1.000, -0.300, 0.000, 0.000)
            insert_keys(4)
            o.location=(0.000, -0.175, 0.100)
            o.rotation_quaternion=(1.000, -0.045, 0.000, 0.000)
            insert_keys(5)
            o.location=(0.000, -0.080, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(6)
            o.location=(0.000, 0.045, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(7)
            o.location=(0.000, 0.160, 0.041)
            o.rotation_quaternion=(1.000, 0.700, 0.000, 0.000)
            insert_keys(8)
            o.location=(0.000, 0.070, 0.060)
            o.rotation_quaternion=(1.000, 0.600, 0.000, 0.000)
            insert_keys(10)
            o.location=(0.000, -0.120, 0.090)
            o.rotation_quaternion=(1.000, 0.240, 0.000, 0.000)
            insert_keys(12)
            o.location=(0.000, -0.200, 0.176)
            o.rotation_quaternion=(1.000, 0.015, 0.000, 0.000)
            insert_keys(15)


        for o in Hand_Heel_R:
            o.rotation_quaternion=(1.000, 0.300, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(4)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(5)
            o.rotation_quaternion=(1.000, -0.300, 0.000, 0.000)
            insert_keys(6)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(7)
            o.rotation_quaternion=(1.000, 0.300, 0.000, 0.000)
            insert_keys(15)


        for o in Hand_Heel_L:
            o.rotation_quaternion=(1.000, 0.500, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
            insert_keys(5)
            o.rotation_quaternion=(1.000, 0.150, 0.000, 0.000)
            insert_keys(6)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(8)
            o.rotation_quaternion=(1.000, 0.500, 0.000, 0.000)
            insert_keys(15)


        for o in Front_Toe_R:
            o.rotation_quaternion=(1.000, -0.200, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(4)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(6)
            o.rotation_quaternion=(1.000, -0.600, 0.000, 0.000)
            insert_keys(7)
            o.rotation_quaternion=(1.000, -0.200, 0.000, 0.000)
            insert_keys(15)


        for o in Front_Toe_L:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(7)
            o.rotation_quaternion=(1.000, -0.600, 0.000, 0.000)
            insert_keys(8)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(15)


        for o in Foot_R:
            o.location=(0.000, 0.260, 0.140)
            o.rotation_quaternion=(1.000, 1.000, 0.000, 0.000)
            insert_keys(1)
            o.location=(-0.024, 0.024, 0.090)
            o.rotation_quaternion=(1.000, 0.300, 0.000, -0.036)
            insert_keys(5)
            o.location=(-0.032, -0.100, 0.075)
            o.rotation_quaternion=(1.000, 0.010, 0.000, -0.040)
            insert_keys(6)
            o.location=(-0.040, -0.200, 0.060)
            o.rotation_quaternion=(1.000, -0.040, 0.000, -0.036)
            insert_keys(8)
            o.location=(-0.037, -0.120, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.030)
            insert_keys(9)
            o.location=(-0.030, 0.070, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.022)
            insert_keys(10)
            o.location=(-0.020, 0.180, 0.040)
            o.rotation_quaternion=(1.000, 0.400, 0.000, -0.015)
            insert_keys(11)
            o.location=(0.000, 0.260, 0.140)
            o.rotation_quaternion=(1.000, 1.000, 0.000, 0.000)
            insert_keys(15)


        for o in Foot_L:
            o.location=(0.000, 0.260, 0.130)
            o.rotation_quaternion=(1.000, 1.000, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.014, 0.220, 0.120)
            o.rotation_quaternion=(1.000, 0.800, 0.000, 0.000)
            insert_keys(3)
            o.location=(0.033, 0.040, 0.080)
            o.rotation_quaternion=(1.000, 0.200, 0.000, 0.022)
            insert_keys(6)
            o.location=(0.040, -0.220, 0.060)
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.055)
            insert_keys(9)
            o.location=(0.036, -0.160, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.060)
            insert_keys(10)
            o.location=(0.027, 0.050, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(11)
            o.location=(0.016, 0.170, 0.028)
            o.rotation_quaternion=(1.000, 0.156, 0.000, 0.014)
            insert_keys(12)
            o.location=(0.007, 0.210, 0.080)
            o.rotation_quaternion=(1.000, 0.500, 0.000, 0.028)
            insert_keys(13)
            o.location=(0.000, 0.260, 0.130)
            o.rotation_quaternion=(1.000, 1.000, 0.000, 0.000)
            insert_keys(15)


        for o in Heel_R:
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, -0.200, 0.000, 0.000)
            insert_keys(8)
            o.rotation_quaternion=(1.000, -0.080, 0.000, 0.000)
            insert_keys(9)
            o.rotation_quaternion=(1.000, 0.300, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(12)
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.000)
            insert_keys(15)


        for o in Heel_L:
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(6)
            o.rotation_quaternion=(1.000, -0.200, 0.000, 0.000)
            insert_keys(8)
            o.rotation_quaternion=(1.000, -0.200, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(1.000, 0.400, 0.000, 0.000)
            insert_keys(11)
            o.rotation_quaternion=(1.000, 0.300, 0.000, 0.000)
            insert_keys(12)
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.000)
            insert_keys(15)


        for o in Toe_R:
            o.rotation_quaternion=(1.000, 0.700, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(9)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(1.000, 0.600, 0.000, 0.000)
            insert_keys(11)
            o.rotation_quaternion=(1.000, 0.700, 0.000, 0.000)
            insert_keys(15)


        for o in Toe_L:
            o.rotation_quaternion=(1.000, 0.700, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(11)
            o.rotation_quaternion=(1.000, 1.200, 0.000, 0.000)
            insert_keys(12)
            o.rotation_quaternion=(1.000, 0.700, 0.000, 0.000)
            insert_keys(15)


        for o in Torso:
            o.location=(0.000, 0.000, 0.010)
            insert_keys(1)
            o.location=(0.000, 0.000, 0.012)
            insert_keys(6)
            o.location=(0.000, 0.000, 0.030)
            insert_keys(11)
            o.location=(0.000, 0.000, 0.010)
            insert_keys(15)


        for o in Hips:
            o.location=(0.000, 0.018, 0.000)
            o.rotation_quaternion=(1.000, 0.078, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, 0.004, 0.070)
            o.rotation_quaternion=(1.000, 0.040, 0.000, 0.000)
            insert_keys(4)
            o.location=(0.000, -0.008, 0.089)
            o.rotation_quaternion=(1.000, -0.010, 0.000, 0.000)
            insert_keys(6)
            o.location=(0.000, -0.010, 0.090)
            o.rotation_quaternion=(1.000, -0.060, 0.000, 0.000)
            insert_keys(7)
            o.location=(0.000, -0.009, 0.083)
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.000)
            insert_keys(8)
            o.location=(0.000, -0.006, 0.065)
            o.rotation_quaternion=(1.000, -0.130, 0.000, 0.000)
            insert_keys(9)
            o.location=(0.000, -0.001, 0.040)
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.000)
            insert_keys(10)
            o.location=(0.000, 0.010, -0.004)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(12)
            o.location=(0.000, 0.014, -0.004)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(13)
            o.location=(0.000, 0.018, 0.000)
            o.rotation_quaternion=(1.000, 0.078, 0.000, 0.000)
            insert_keys(15)


        for o in Chest:
            o.location=(0.000, -0.004, 0.000)
            o.rotation_quaternion=(1.000, -0.060, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, 0.000, -0.005)
            o.rotation_quaternion=(1.000, -0.020, 0.000, 0.000)
            insert_keys(3)
            o.location=(0.000, 0.014, -0.020)
            o.rotation_quaternion=(1.000, 0.050, 0.000, 0.000)
            insert_keys(6)
            o.location=(0.000, 0.018, -0.022)
            o.rotation_quaternion=(1.000, 0.048, 0.000, 0.000)
            insert_keys(7)
            o.location=(0.000, 0.019, -0.019)
            o.rotation_quaternion=(1.000, 0.042, 0.000, 0.000)
            insert_keys(8)
            o.location=(0.000, 0.018, -0.010)
            o.rotation_quaternion=(1.000, 0.031, 0.000, 0.000)
            insert_keys(9)
            o.location=(0.000, 0.005, 0.000)
            o.rotation_quaternion=(1.000, -0.020, 0.000, 0.000)
            insert_keys(12)
            o.location=(0.000, -0.004, 0.000)
            o.rotation_quaternion=(1.000, -0.060, 0.000, 0.000)
            insert_keys(15)


        for o in Neck:
            o.rotation_quaternion=(1.000, 0.150, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(5)
            o.rotation_quaternion=(1.000, 0.300, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(1.000, 0.150, 0.000, 0.000)
            insert_keys(15)


        for o in Head:
            o.rotation_quaternion=(1.000, 0.050, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.020, 0.000, 0.000)
            insert_keys(4)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(1.000, 0.050, 0.000, 0.000)
            insert_keys(15)


        for o in Tail_Master_001:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(8)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(15)


        for o in Spine_FK_001:
            o.location=(0.000, -0.001, 0.028)
            o.rotation_quaternion=(1.000, 0.030, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, -0.001, 0.028)
            o.rotation_quaternion=(1.000, -0.250, 0.000, 0.000)
            insert_keys(8)
            o.location=(0.000, -0.001, 0.028)
            o.rotation_quaternion=(1.000, 0.030, 0.000, 0.000)
            insert_keys(15)


        for o in Spine_FK_003:
            o.rotation_quaternion=(1.000, -0.056, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, -0.056, 0.000, 0.000)
            insert_keys(15)







        # Add Cycles Modifier

        ob = bpy.context.object
        ob_fcurve = ob.animation_data.action.fcurves


        def add_cycle_modifier():
            
               
            for fc in ob_fcurve:
                d_path = ('location', 'rotation_quaternion')
                     
                if fc.data_path.endswith((d_path)):
                    fc.modifiers.new(type='CYCLES')
                
                fc.update()


        add_cycle_modifier()
         

        # Action Name
        ob = bpy.context.object
        ob.animation_data.action.name = ob.name + '_Run' 

         
        # JUMP TO START AND PLAY ANIMATION
        bpy.ops.screen.frame_jump(end=False)
        bpy.ops.screen.animation_play()



        # FRAME SELECTED RANGE IN TIMELINE

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

              

        return {'FINISHED'}



# =====================================================
#      END  - CAT - 14 FRAMES  RUN CYCLE
# =====================================================


 



classes = [
           OBJECT_OT_rigify_zoo_cat_walk_32_ra,
           OBJECT_OT_rigify_zoo_cat_run_14_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()








