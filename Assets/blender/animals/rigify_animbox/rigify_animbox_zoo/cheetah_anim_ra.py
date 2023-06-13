import bpy


# =====================================================
#          RIGIFY ZOO
# =====================================================


# =====================================================
#          CHEETAH - 14 FRAMES  RUN CYCLE
# =====================================================



# 14 FRAMES RUN CYCLE FOR RIGIFY ZOO 
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_zoo_cheetah_run_14_ra(bpy.types.Operator):
    '''14 Frames Run Cycle For Rigify Zoo - Cheetah.
Rig Name must begin with: 'cheetah'
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_zoo_cheetah_run_14_ra"
    bl_label = "Cheetah Run"
    bl_options = {'REGISTER', 'UNDO'}


        
  
    @classmethod
    def poll(cls, context):
        return (context.object is not None and context.object.name.startswith(('Cheetah', 'cheetah', 'CHEETAH'))
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

        Tail  = [pb for pb in pose_bones  if pb.name.startswith('spine_master')]

        # Extra
        Spine_FK_004  = [pb for pb in pose_bones  if pb.name.startswith('spine_fk.004')]
        Spine_FK_007  = [pb for pb in pose_bones  if pb.name.startswith('spine_fk.007')]


        # Legs/Feet


        # Front
        Front_Foot_R  = [pb for pb in pose_bones  if pb.name.startswith('front_foot_ik.R')]
        Front_Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('front_foot_heel_ik.R')]
        Front_Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('front_toe.R')]


        Front_Foot_L  = [pb for pb in pose_bones  if pb.name.startswith('front_foot_ik.L')]
        Front_Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('front_foot_heel_ik.L')]
        Front_Toe_L  = [pb for pb in pose_bones  if pb.name.startswith('front_toe.L')]

        # Rear

        Foot_R  = [pb for pb in pose_bones  if pb.name.startswith('foot_ik.R')]
        Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('foot_heel_ik.R')]
        Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('toe.R')]


        Foot_L  = [pb for pb in pose_bones  if pb.name.startswith('foot_ik.L')]
        Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('foot_heel_ik.L')]
        Toe_L = [pb for pb in pose_bones  if pb.name.startswith('toe.L')]







        # Insert Keys

        def insert_keys(frame):
            o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
            o.keyframe_insert(data_path = 'location', frame= frame)






        for o in Front_Foot_R:
            o.location=(0.00, -0.78, 0.55)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, -0.65, 0.25)
            o.rotation_quaternion=(1.00, 0.06, 0.00, 0.00)
            insert_keys(3)
            o.location=(0.01, -0.55, 0.15)
            o.rotation_quaternion=(1.00, 0.03, 0.00, 0.00)
            insert_keys(4)
            o.location=(0.02, -0.30, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(5)
            o.location=(0.03, 0.35, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(6)
            o.location=(0.05, 0.70, 0.14)
            o.rotation_quaternion=(1.00, 1.75, 0.00, 0.00)
            insert_keys(8)
            o.location=(0.03, -0.05, 0.27)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(10)
            o.location=(0.00, -0.45, 0.50)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, -0.78, 0.55)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(15)


        for o in Front_Foot_L:
            o.location=(0.00, -0.60, 0.35)
            o.rotation_quaternion=(1.00, 0.12, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, -0.21, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(3)
            o.location=(0.00, 0.30, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(5)
            o.location=(-0.05, 0.88, 0.28)
            o.rotation_quaternion=(1.00, 2.50, 0.00, 0.00)
            insert_keys(7)
            o.location=(-0.02, -0.26, 0.25)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(10)
            o.location=(0.00, -0.60, 0.37)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, -0.60, 0.35)
            o.rotation_quaternion=(1.00, 0.12, 0.00, 0.00)
            insert_keys(15)


        for o in Front_Heel_R:
            o.rotation_quaternion=(1.00, 0.15, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(6)
            o.rotation_quaternion=(1.00, -0.15, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
            insert_keys(10)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.15, 0.00, 0.00)
            insert_keys(15)


        for o in Front_Heel_L:
            o.rotation_quaternion=(1.00, 0.05, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(3)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(5)
            o.rotation_quaternion=(1.00, -0.05, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, -0.40, 0.00, 0.00)
            insert_keys(10)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.05, 0.00, 0.00)
            insert_keys(15)


        for o in Front_Toe_R:
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(5)
            o.rotation_quaternion=(1.00, -0.20, 0.00, 0.00)
            insert_keys(7)
            o.rotation_quaternion=(1.00, -1.20, 0.00, 0.00)
            insert_keys(10)
            o.rotation_quaternion=(1.00, -0.60, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(15)


        for o in Front_Toe_L:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(4)
            o.rotation_quaternion=(1.00, -0.59, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, -1.20, 0.00, 0.00)
            insert_keys(10)
            o.rotation_quaternion=(1.00, -0.60, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(15)


        for o in Foot_R:
            o.location=(0.00, 0.78, 0.65)
            o.rotation_quaternion=(1.00, 1.60, 0.00, 0.00)
            insert_keys(1)
            o.location=(-0.04, 0.56, 0.57)
            o.rotation_quaternion=(1.00, 2.00, 0.00, 0.00)
            insert_keys(4)
            o.location=(-0.06, 0.41, 0.45)
            o.rotation_quaternion=(1.00, 2.00, 0.00, -0.02)
            insert_keys(5)
            o.location=(-0.08, -0.12, 0.20)
            o.rotation_quaternion=(1.00, 0.80, 0.00, -0.05)
            insert_keys(6)
            o.location=(-0.095, -0.70, 0.15)
            o.rotation_quaternion=(1.00, 0.10, 0.00, -0.08)
            insert_keys(7)
            o.location=(-0.10, -0.80, 0.05)
            o.rotation_quaternion=(1.00, 0.00, 0.00, -0.10)
            insert_keys(8)
            o.location=(-0.095, -0.30, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, -0.08)
            insert_keys(9)
            o.location=(-0.08, 0.12, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, -0.05)
            insert_keys(10)
            o.location=(-0.06, 0.60, 0.25)
            o.rotation_quaternion=(1.00, 1.50, 0.00, -0.02)
            insert_keys(11)
            o.location=(-0.04, 0.75, 0.54)
            o.rotation_quaternion=(1.00, 1.90, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, 0.78, 0.65)
            o.rotation_quaternion=(1.00, 1.60, 0.00, 0.00)
            insert_keys(15)


        for o in Foot_L:
            o.location=(0.00, 0.75, 0.74)
            o.rotation_quaternion=(1.00, 1.60, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.04, 0.65, 0.65)
            o.rotation_quaternion=(1.00, 2.00, 0.00, 0.00)
            insert_keys(4)
            o.location=(0.06, 0.55, 0.55)
            o.rotation_quaternion=(1.00, 2.20, 0.00, 0.02)
            insert_keys(5)
            o.location=(0.08, 0.21, 0.30)
            o.rotation_quaternion=(1.00, 1.50, 0.00, 0.05)
            insert_keys(6)
            o.location=(0.095, -0.50, 0.20)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.08)
            insert_keys(7)
            o.location=(0.10, -0.90, 0.28)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.10)
            insert_keys(8)
            o.location=(0.095, -0.85, 0.05)
            o.rotation_quaternion=(1.00, -0.05, 0.00, 0.08)
            insert_keys(9)
            o.location=(0.08, -0.50, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.05)
            insert_keys(10)
            o.location=(0.06, 0.19, 0.04)
            o.rotation_quaternion=(1.00, 0.80, 0.00, 0.02)
            insert_keys(11)
            o.location=(0.04, 0.50, 0.30)
            o.rotation_quaternion=(1.00, 1.50, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, 0.75, 0.74)
            o.rotation_quaternion=(1.00, 1.60, 0.00, 0.00)
            insert_keys(15)


        for o in Heel_R:
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(6)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(9)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(15)


        for o in Heel_L:
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(6)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(15)


        for o in Toe_R:
            o.rotation_quaternion=(1.00, 0.50, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(6)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, 0.40, 0.00, 0.00)
            insert_keys(13)
            o.rotation_quaternion=(1.00, 0.50, 0.00, 0.00)
            insert_keys(15)


        for o in Toe_L:
            o.rotation_quaternion=(1.00, 0.50, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(6)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, 0.40, 0.00, 0.00)
            insert_keys(13)
            o.rotation_quaternion=(1.00, 0.50, 0.00, 0.00)
            insert_keys(15)


        for o in Tail:
            o.rotation_quaternion=(1.00, 0.02, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(7)
            o.rotation_quaternion=(1.00, -0.08, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, 0.02, 0.00, 0.00)
            insert_keys(15)


        for o in Torso:
            o.location=(0.00, 0.00, 0.10)
            insert_keys(1)
            o.location=(0.00, 0.00, 0.05)
            insert_keys(3)
            o.location=(0.00, 0.00, -0.02)
            insert_keys(8)
            o.location=(0.00, 0.00, 0.10)
            insert_keys(15)


        for o in Hips:
            o.location=(0.00, 0.06, 0.02)
            o.rotation_quaternion=(1.00, 0.12, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, 0.00, 0.02)
            o.rotation_quaternion=(1.00, 0.25, 0.00, 0.00)
            insert_keys(5)
            o.location=(0.00, -0.02, -0.03)
            o.rotation_quaternion=(1.00, -0.06, 0.00, 0.00)
            insert_keys(9)
            o.location=(0.00, 0.03, 0.01)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, 0.06, 0.02)
            o.rotation_quaternion=(1.00, 0.12, 0.00, 0.00)
            insert_keys(15)


        for o in Chest:
            o.location=(0.00, -0.02, 0.01)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, 0.01, 0.00)
            o.rotation_quaternion=(1.00, 0.05, 0.00, 0.00)
            insert_keys(5)
            o.location=(0.00, 0.04, 0.07)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(8)
            o.location=(0.00, -0.01, 0.10)
            o.rotation_quaternion=(1.00, -0.01, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, -0.02, 0.01)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(15)


        for o in Neck:
            o.location=(0.00, 0.00, -0.05)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, 0.00, -0.05)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
            insert_keys(5)
            o.location=(0.00, 0.00, -0.03)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(9)
            o.location=(0.00, 0.00, -0.04)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, 0.00, -0.05)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
            insert_keys(15)


        for o in Head:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, -0.01, 0.00, 0.00)
            insert_keys(5)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, 0.01, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(15)


        for o in Spine_FK_007:
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.15, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(15)


        for o in Spine_FK_004:
            o.location=(0.00, 0.03, 0.03)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, 0.03, 0.03)
            o.rotation_quaternion=(1.00, -0.12, 0.00, 0.00)
            insert_keys(8)
            o.location=(0.00, 0.03, 0.03)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
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
#      END  - CHEETAH - 14 FRAMES  RUN CYCLE
# =====================================================











# =====================================================
#          CHEETAH - 32 FRAMES  WALK CYCLE
# =====================================================




# 32 FRAMES WALK CYCLE FOR RIGIFY ZOO 
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_zoo_cheetah_walk_32_ra(bpy.types.Operator):
    '''32 Frames Walk Cycle For Rigify Zoo - Cheetah.
Rig Name must begin with: 'cheetah'
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_zoo_cheetah_walk_32_ra"
    bl_label = "Cheetah Walk"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and context.object.name.startswith(('Cheetah', 'cheetah', 'CHEETAH'))
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

        Tail  = [pb for pb in pose_bones  if pb.name == ('spine') ]

        Tail_001  = [pb for pb in pose_bones  if pb.name.startswith('spine.001') ]

        Tail_003  = [pb for pb in pose_bones  if pb.name.startswith('spine.003') ]
 
        # Legs/Feet


        # Front
        Front_Foot_R  = [pb for pb in pose_bones  if pb.name.startswith('front_foot_ik.R')]
        Front_Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('front_foot_heel_ik.R')]
        Front_Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('front_toe.R')]


        Front_Foot_L  = [pb for pb in pose_bones  if pb.name.startswith('front_foot_ik.L')]
        Front_Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('front_foot_heel_ik.L')]
        Front_Toe_L  = [pb for pb in pose_bones  if pb.name.startswith('front_toe.L')]

        # Rear

        Foot_R  = [pb for pb in pose_bones  if pb.name.startswith('foot_ik.R')]
        Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('foot_heel_ik.R')]
        Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('toe.R')]


        Foot_L  = [pb for pb in pose_bones  if pb.name.startswith('foot_ik.L')]
        Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('foot_heel_ik.L')]
        Toe_L = [pb for pb in pose_bones  if pb.name.startswith('toe.L')]







        # Insert Keys

        def insert_keys(frame):
            o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
            o.keyframe_insert(data_path = 'location', frame= frame)






        for o in Front_Foot_R:
            o.location=(0.00, -0.48, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, 0.31, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(19)
            o.location=(0.00, -0.08, 0.12)
            o.rotation_quaternion=(1.00, 0.50, 0.00, 0.00)
            insert_keys(25)
            o.location=(0.00, -0.50, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(31)
            o.location=(0.00, -0.48, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(33)


        for o in Front_Foot_L:
            o.location=(0.00, 0.28, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, 0.31, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(3)
            o.location=(0.00, -0.08, 0.12)
            o.rotation_quaternion=(1.00, 0.50, 0.00, 0.00)
            insert_keys(9)
            o.location=(0.00, -0.50, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(15)
            o.location=(0.00, 0.28, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(33)


        for o in Front_Heel_R:
            o.rotation_quaternion=(1.00, 0.03, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.15, 0.00, 0.00)
            insert_keys(6)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(14)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(31)
            o.rotation_quaternion=(1.00, 0.03, 0.00, 0.00)
            insert_keys(33)


        for o in Front_Heel_L:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(15)
            o.rotation_quaternion=(1.00, 0.15, 0.00, 0.00)
            insert_keys(23)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(31)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(33)


        for o in Front_Toe_R:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(19)
            o.rotation_quaternion=(1.00, -0.50, 0.00, 0.00)
            insert_keys(24)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(29)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(33)


        for o in Front_Toe_L:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(3)
            o.rotation_quaternion=(1.00, -0.50, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(13)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(33)


        for o in Foot_R:
            o.location=(0.00, -0.22, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, 0.20, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(11)
            o.location=(0.00, -0.22, 0.12)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(17)
            o.location=(0.00, -0.65, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(23)
            o.location=(0.00, -0.22, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(33)


        for o in Foot_L:
            o.location=(0.00, -0.22, 0.12)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, -0.65, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(7)
            o.location=(0.00, 0.20, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(27)
            o.location=(0.00, -0.22, 0.12)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(33)


        for o in Heel_R:
            o.rotation_quaternion=(1.00, 0.02, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(20)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(28)
            o.rotation_quaternion=(1.00, 0.02, 0.00, 0.00)
            insert_keys(33)


        for o in Heel_L:
            o.rotation_quaternion=(1.00, 0.19, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(4)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.19, 0.00, 0.00)
            insert_keys(33)


        for o in Toe_R:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, 0.50, 0.00, 0.00)
            insert_keys(17)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(23)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(33)


        for o in Toe_L:
            o.rotation_quaternion=(1.00, 0.50, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(7)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(27)
            o.rotation_quaternion=(1.00, 0.50, 0.00, 0.00)
            insert_keys(33)


        for o in Torso:
            o.location=(0.00, 0.00, -0.10)
            insert_keys(1)
            o.location=(0.00, 0.00, -0.10)
            insert_keys(33)


        for o in Hips:
            o.location=(-0.03, 0.00, 0.02)
            o.rotation_quaternion=(1.00, 0.00, 0.04, -0.02)
            insert_keys(1)
            o.location=(-0.03, 0.00, 0.02)
            o.rotation_quaternion=(1.00, 0.00, 0.04, -0.03)
            insert_keys(2)
            o.location=(0.00, 0.00, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.04, -0.05)
            insert_keys(7)
            o.location=(0.03, 0.00, -0.02)
            o.rotation_quaternion=(1.00, 0.00, -0.04, -0.03)
            insert_keys(12)
            o.location=(0.04, 0.00, 0.00)
            o.rotation_quaternion=(1.00, 0.00, -0.04, 0.00)
            insert_keys(15)
            o.location=(0.03, 0.00, 0.02)
            o.rotation_quaternion=(1.00, 0.00, -0.04, 0.03)
            insert_keys(18)
            o.location=(0.00, 0.00, 0.00)
            o.rotation_quaternion=(1.00, 0.00, -0.04, 0.05)
            insert_keys(23)
            o.location=(-0.03, 0.00, -0.02)
            o.rotation_quaternion=(1.00, 0.00, 0.04, 0.03)
            insert_keys(28)
            o.location=(-0.03, 0.00, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.04, -0.00)
            insert_keys(31)
            o.location=(-0.03, 0.00, 0.02)
            o.rotation_quaternion=(1.00, 0.00, 0.04, -0.02)
            insert_keys(33)


        for o in Chest:
            o.location=(-0.02, 0.00, -0.00)
            o.rotation_quaternion=(1.00, 0.00, -0.01, 0.06)
            insert_keys(1)
            o.location=(-0.03, 0.00, -0.02)
            o.rotation_quaternion=(1.00, 0.00, 0.05, 0.01)
            insert_keys(5)
            o.location=(0.00, 0.00, 0.01)
            o.rotation_quaternion=(1.00, 0.00, 0.05, -0.07)
            insert_keys(14)
            o.location=(0.03, 0.00, -0.02)
            o.rotation_quaternion=(1.00, 0.00, -0.05, -0.01)
            insert_keys(21)
            o.location=(0.00, 0.00, 0.01)
            o.rotation_quaternion=(1.00, 0.00, -0.05, 0.07)
            insert_keys(30)
            o.location=(-0.02, 0.00, -0.00)
            o.rotation_quaternion=(1.00, 0.00, -0.01, 0.06)
            insert_keys(33)


        for o in Head:
            o.rotation_quaternion=(1.00, -0.02, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.02, 0.00, 0.00)
            insert_keys(9)
            o.rotation_quaternion=(1.00, -0.02, 0.00, 0.00)
            insert_keys(17)
            o.rotation_quaternion=(1.00, 0.02, 0.00, 0.00)
            insert_keys(25)
            o.rotation_quaternion=(1.00, -0.02, 0.00, 0.00)
            insert_keys(33)


        for o in Tail:
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(33)


        for o in Tail_001:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.02)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.02)
            insert_keys(4)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.00, 0.00, -0.02)
            insert_keys(20)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(28)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.02)
            insert_keys(33)


        for o in Tail_003:
            o.rotation_quaternion=(1.00, -0.11, 0.00, 0.02)
            insert_keys(1)
            o.rotation_quaternion=(1.00, -0.12, 0.00, 0.03)
            insert_keys(4)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, -0.12, 0.00, -0.03)
            insert_keys(20)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
            insert_keys(28)
            o.rotation_quaternion=(1.00, -0.11, 0.00, 0.02)
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
#      END  - CHEETAH - 32 FRAMES  WALK CYCLE
# =====================================================

 



classes = [OBJECT_OT_rigify_zoo_cheetah_run_14_ra,
           OBJECT_OT_rigify_zoo_cheetah_walk_32_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()







 
