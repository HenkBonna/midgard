import bpy


# =====================================================
#          RIGIFY ZOO
# =====================================================


# =====================================================
#          HORSE - 15 FRAMES  RUN CYCLE
# =====================================================




# 15 FRAMES RUN CYCLE FOR RIGIFY ZOO - HORSE
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_zoo_horse_run_15_ra(bpy.types.Operator):
    '''15 Frames Run Cycle For Rigify Zoo - Horse.
Rig Name must begin with: 'horse'
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_zoo_horse_run_15_ra"
    bl_label = "Horse Run"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and context.object.name.startswith(('Horse', 'horse', 'HORSE'))
                and context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)
                
                
              

    def execute(self, context):



        # TOTAL RESET



        # TOTAL RESET

        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        bpy.ops.anim.keyframe_clear_v3d() 
        bpy.ops.pose.select_all(action = 'DESELECT')
        bpy.ops.screen.frame_jump(end=False)
            


        pose_bones = bpy.context.object.pose.bones

           
         
        # DEFINING FRAME RANGE

        # START
        bpy.context.scene.frame_start = 1

        # END
        bpy.context.scene.frame_end = 15
         



        # NAMES 

        Head = [pb for pb in pose_bones  if pb.name.startswith('head')]

        Neck = [pb for pb in pose_bones  if pb.name.startswith('neck')]
                    
        Chest = [pb for pb in pose_bones  if pb.name.startswith('chest')]

        Torso = [pb for pb in pose_bones  if pb.name.startswith('torso')]

        Hips  = [pb for pb in pose_bones  if pb.name.startswith('hips')]

        Tail  = [pb for pb in pose_bones  if pb.name.startswith('tail_master.001')]



        # Legs/Feet


        # Front
        Front_Foot_R  = [pb for pb in pose_bones  if pb.name.startswith('forefoot_ik.R')]
        Front_Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('forefoot_heel_ik.R')]
        Front_Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('f_toe_ik.R')]
        Front_Hoof_R  = [pb for pb in pose_bones  if pb.name.startswith('f_hoof.R')]
        


        Front_Foot_L  = [pb for pb in pose_bones  if pb.name.startswith('forefoot_ik.L')]
        Front_Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('forefoot_heel_ik.L')]
        Front_Toe_L  = [pb for pb in pose_bones  if pb.name.startswith('f_toe_ik.L')]
        Front_Hoof_L  = [pb for pb in pose_bones  if pb.name.startswith('f_hoof.L')]
        # Rear

        Foot_R  = [pb for pb in pose_bones  if pb.name.startswith('hind_foot_ik.R')]
        Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('hind_foot_heel_ik.R')]
        Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('r_toe_ik.R')]
        Rear_Hoof_R  = [pb for pb in pose_bones  if pb.name.startswith('r_hoof.R')]


        Foot_L  = [pb for pb in pose_bones  if pb.name.startswith('hind_foot_ik.L')]
        Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('hind_foot_heel_ik.L')]
        Toe_L = [pb for pb in pose_bones  if pb.name.startswith('r_toe_ik.L')]
        Rear_Hoof_L  = [pb for pb in pose_bones  if pb.name.startswith('r_hoof.L')]





        # Insert Keys

        def insert_keys(frame):
            o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
            o.keyframe_insert(data_path = 'location', frame= frame)




        for o in Front_Foot_R:
            o.location=(-0.00, 0.54, 0.07)
            o.rotation_quaternion=(1.00, 0.70, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, 0.60, 0.33)
            o.rotation_quaternion=(1.00, 1.80, 0.00, 0.00)
            insert_keys(2)
            o.location=(0.00, 0.39, 0.42)
            o.rotation_quaternion=(1.00, 3.00, 0.00, 0.00)
            insert_keys(4)
            o.location=(-0.00, -0.01, 0.38)
            o.rotation_quaternion=(1.00, 1.50, 0.00, 0.00)
            insert_keys(6)
            o.location=(-0.00, -0.47, 0.31)
            o.rotation_quaternion=(1.00, 0.50, 0.00, 0.00)
            insert_keys(8)
            o.location=(0.00, -0.70, 0.17)
            o.rotation_quaternion=(1.00, 0.08, 0.00, 0.00)
            insert_keys(10)
            o.location=(0.00, -0.39, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, 0.18, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(14)
            o.location=(-0.00, 0.54, 0.07)
            o.rotation_quaternion=(1.00, 0.70, 0.00, 0.00)
            insert_keys(16)


        for o in Front_Foot_L:
            o.location=(-0.00, 0.32, 0.36)
            o.rotation_quaternion=(1.00, 1.60, 0.00, 0.00)
            insert_keys(1)
            o.location=(-0.00, -0.43, 0.24)
            o.rotation_quaternion=(1.00, 0.70, 0.00, 0.00)
            insert_keys(6)
            o.location=(0.00, -0.54, 0.05)
            o.rotation_quaternion=(1.00, 0.05, 0.00, 0.00)
            insert_keys(8)
            o.location=(0.00, 0.07, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(10)
            o.location=(0.00, 0.37, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(11)
            o.location=(0.00, 0.70, 0.11)
            o.rotation_quaternion=(1.00, 0.90, 0.00, 0.00)
            insert_keys(12)
            o.location=(-0.00, 0.57, 0.27)
            o.rotation_quaternion=(1.00, 2.00, 0.00, 0.00)
            insert_keys(14)
            o.location=(-0.00, 0.32, 0.36)
            o.rotation_quaternion=(1.00, 1.60, 0.00, 0.00)
            insert_keys(16)


        for o in Front_Heel_R:
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, -0.03, 0.00, 0.00)
            insert_keys(2)
            o.rotation_quaternion=(1.00, 0.05, 0.00, 0.00)
            insert_keys(6)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(9)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.04, 0.00, 0.00)
            insert_keys(14)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(16)


        for o in Front_Heel_L:
            o.rotation_quaternion=(1.00, -0.03, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, -0.03, 0.00, 0.00)
            insert_keys(2)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(6)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(9)
            o.rotation_quaternion=(1.00, 0.04, 0.00, 0.00)
            insert_keys(10)
            o.rotation_quaternion=(1.00, 0.04, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, 0.14, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(13)
            o.rotation_quaternion=(1.00, -0.03, 0.00, 0.00)
            insert_keys(16)


        for o in Front_Toe_R:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(9)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(14)
            o.rotation_quaternion=(1.00, -0.18, 0.00, 0.00)
            insert_keys(15)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(16)


        for o in Front_Toe_L:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.12, 0.00, 0.00)
            insert_keys(7)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(10)
            o.rotation_quaternion=(1.00, -0.20, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(13)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(16)


        for o in Foot_R:
            o.location=(0.00, -0.08, 0.22)
            o.rotation_quaternion=(1.00, 0.40, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, -0.55, 0.30)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(3)
            o.location=(-0.00, -0.95, 0.22)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
            insert_keys(6)
            o.location=(-0.00, -0.80, 0.05)
            o.rotation_quaternion=(1.00, -0.01, 0.00, 0.00)
            insert_keys(7)
            o.location=(-0.00, -0.04, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(9)
            o.location=(0.00, 0.30, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(10)
            o.location=(0.00, 0.61, 0.15)
            o.rotation_quaternion=(1.00, 0.70, 0.00, 0.00)
            insert_keys(11)
            o.location=(0.00, 0.76, 0.30)
            o.rotation_quaternion=(1.00, 0.60, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, -0.08, 0.22)
            o.rotation_quaternion=(1.00, 0.40, 0.00, 0.00)
            insert_keys(16)


        for o in Foot_L:
            o.location=(0.00, -0.40, 0.25)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, -0.60, 0.22)
            o.rotation_quaternion=(1.00, 0.15, 0.00, 0.00)
            insert_keys(2)
            o.location=(-0.00, -0.80, 0.15)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(4)
            o.location=(0.00, -0.72, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(5)
            o.location=(0.00, 0.30, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(8)
            o.location=(0.00, 0.73, 0.20)
            o.rotation_quaternion=(1.00, 0.70, 0.00, 0.00)
            insert_keys(10)
            o.location=(0.00, 0.80, 0.30)
            o.rotation_quaternion=(1.00, 0.70, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, -0.40, 0.25)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(16)


        for o in Heel_R:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.02, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(16)


        for o in Heel_L:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, -0.02, 0.00, 0.00)
            insert_keys(4)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(7)
            o.rotation_quaternion=(1.00, -0.02, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(10)
            o.rotation_quaternion=(1.00, -0.14, 0.00, 0.00)
            insert_keys(14)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(16)


        for o in Toe_R:
            o.rotation_quaternion=(1.00, -0.25, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
            insert_keys(6)
            o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(10)
            o.rotation_quaternion=(1.00, -0.20, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(13)
            o.rotation_quaternion=(1.00, -0.25, 0.00, 0.00)
            insert_keys(16)


        for o in Toe_L:
            o.rotation_quaternion=(1.00, -0.28, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, -0.40, 0.00, 0.00)
            insert_keys(4)
            o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
            insert_keys(6)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
            insert_keys(14)
            o.rotation_quaternion=(1.00, -0.28, 0.00, 0.00)
            insert_keys(16)


        for o in Tail:
            o.rotation_quaternion=(1.00, 0.12, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(4)
            o.rotation_quaternion=(1.00, 0.05, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, 0.08, 0.00, 0.00)
            insert_keys(12)
            o.rotation_quaternion=(1.00, 0.12, 0.00, 0.00)
            insert_keys(16)


        for o in Torso:
            o.location=(0.00, 0.00, -0.06)
            insert_keys(1)
            o.location=(0.00, 0.00, -0.10)
            insert_keys(5)
            o.location=(0.00, 0.00, -0.12)
            insert_keys(11)
            o.location=(0.00, 0.00, -0.06)
            insert_keys(16)


        for o in Hips:
            o.location=(0.00, 0.00, 0.00)
            o.rotation_quaternion=(1.00, -0.09, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, -0.02, 0.00)
            o.rotation_quaternion=(1.00, -0.25, 0.00, 0.00)
            insert_keys(5)
            o.location=(0.00, 0.00, 0.00)
            o.rotation_quaternion=(1.00, 0.01, 0.00, 0.00)
            insert_keys(9)
            o.location=(0.00, 0.01, 0.00)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(12)
            o.location=(0.00, 0.00, 0.00)
            o.rotation_quaternion=(1.00, -0.09, 0.00, 0.00)
            insert_keys(16)


        for o in Chest:
            o.location=(0.00, 0.00, -0.03)
            o.rotation_quaternion=(1.00, 0.02, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, 0.00, 0.03)
            o.rotation_quaternion=(1.00, -0.04, 0.00, 0.00)
            insert_keys(6)
            o.location=(0.00, 0.00, 0.00)
            o.rotation_quaternion=(1.00, 0.04, 0.00, 0.00)
            insert_keys(11)
            o.location=(0.00, 0.00, -0.03)
            o.rotation_quaternion=(1.00, 0.02, 0.00, 0.00)
            insert_keys(16)


        for o in Neck:
            o.location=(0.00, 0.00, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.location=(0.00, 0.00, 0.00)
            o.rotation_quaternion=(1.00, 0.14, 0.00, 0.00)
            insert_keys(9)
            o.location=(0.00, 0.00, 0.00)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(16)


        for o in Head:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.07, 0.00, 0.00)
            insert_keys(9)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(16)


        for o in Front_Hoof_R:
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, -0.30, 0.00, 0.00)
            insert_keys(4)
            o.rotation_quaternion=(1.00, -0.05, 0.00, 0.00)
            insert_keys(7)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(9)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(13)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(16)


        for o in Front_Hoof_L:
            o.rotation_quaternion=(1.00, -0.40, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, -0.20, 0.00, 0.00)
            insert_keys(5)
            o.rotation_quaternion=(1.00, 0.10, 0.00, 0.00)
            insert_keys(7)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(9)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(11)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
            insert_keys(13)
            o.rotation_quaternion=(1.00, -0.40, 0.00, 0.00)
            insert_keys(16)


        for o in Rear_Hoof_R:
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(3)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(7)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(10)
            o.rotation_quaternion=(1.00, 0.40, 0.00, 0.00)
            insert_keys(13)
            o.rotation_quaternion=(1.00, 0.20, 0.00, 0.00)
            insert_keys(16)


        for o in Rear_Hoof_L:
            o.rotation_quaternion=(1.00, 0.30, 0.00, 0.00)
            insert_keys(1)
            o.rotation_quaternion=(1.00, -0.10, 0.00, 0.00)
            insert_keys(3)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(5)
            o.rotation_quaternion=(1.00, 0.00, 0.00, 0.00)
            insert_keys(8)
            o.rotation_quaternion=(1.00, 0.30, 0.00, 0.00)
            insert_keys(13)
            o.rotation_quaternion=(1.00, 0.30, 0.00, 0.00)
            insert_keys(16)




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
#      END  - HORSE - 15 FRAMES  RUN CYCLE
# =====================================================








# =====================================================
#          HORSE -  32 FRAMES  WALK CYCLE
# =====================================================




# 32 FRAMES WALK CYCLE FOR RIGIFY ZOO - HORSE
# ORIGINAL BONE NAMES SHOULD REMAIN UNCHANGED !!!
class OBJECT_OT_rigify_zoo_horse_walk_32_ra(bpy.types.Operator):
    '''32 Frames Walk Cycle For Rigify Zoo - Horse.
Rig Name must begin with: 'horse'
Original Bone Names Should Remain Unchanged !!!'''
    bl_idname = "object.rigify_zoo_horse_walk_32_ra"
    bl_label = "Horse Walk"
    bl_options = {'REGISTER', 'UNDO'}



    @classmethod
    def poll(cls, context):
        return (context.object is not None and context.object.name.startswith(('Horse', 'horse', 'HORSE'))
                and context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)
                
                
              

    def execute(self, context):



        # TOTAL RESET



        # TOTAL RESET

        bpy.ops.pose.select_all(action = 'SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
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

        Tail  = [pb for pb in pose_bones  if pb.name.startswith('tail_master.001')]



        # Legs/Feet


        # Front
        Front_Foot_R  = [pb for pb in pose_bones  if pb.name.startswith('forefoot_ik.R')]
        Front_Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('forefoot_heel_ik.R')]
        Front_Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('f_toe_ik.R')]
        Front_Hoof_R  = [pb for pb in pose_bones  if pb.name.startswith('f_hoof.R')]
        


        Front_Foot_L  = [pb for pb in pose_bones  if pb.name.startswith('forefoot_ik.L')]
        Front_Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('forefoot_heel_ik.L')]
        Front_Toe_L  = [pb for pb in pose_bones  if pb.name.startswith('f_toe_ik.L')]
        Front_Hoof_L  = [pb for pb in pose_bones  if pb.name.startswith('f_hoof.L')]
        # Rear

        Foot_R  = [pb for pb in pose_bones  if pb.name.startswith('hind_foot_ik.R')]
        Heel_R  = [pb for pb in pose_bones  if pb.name.startswith('hind_foot_heel_ik.R')]
        Toe_R  = [pb for pb in pose_bones  if pb.name.startswith('r_toe_ik.R')]
        Rear_Hoof_R  = [pb for pb in pose_bones  if pb.name.startswith('r_hoof.R')]


        Foot_L  = [pb for pb in pose_bones  if pb.name.startswith('hind_foot_ik.L')]
        Heel_L  = [pb for pb in pose_bones  if pb.name.startswith('hind_foot_heel_ik.L')]
        Toe_L = [pb for pb in pose_bones  if pb.name.startswith('r_toe_ik.L')]
        Rear_Hoof_L  = [pb for pb in pose_bones  if pb.name.startswith('r_hoof.L')]


        # Shoulders
        Shoulder_R  = [pb for pb in pose_bones  if pb.name.startswith('shoulder.R')]
        Shoulder_L  = [pb for pb in pose_bones  if pb.name.startswith('shoulder.L')]


        # Insert Keys

        def insert_keys(frame):
            o.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)
            o.keyframe_insert(data_path = 'location', frame= frame)






        for o in Front_Foot_R:
            o.location=(0.000, 0.450, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, 0.120, 0.100)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(9)
            o.location=(0.000, -0.350, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(14)
            o.location=(0.000, 0.450, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(33)


        for o in Front_Foot_L:
            o.location=(0.000, 0.450, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(17)
            o.location=(0.000, 0.120, 0.100)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(25)
            o.location=(0.000, -0.350, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(30)
            o.location=(0.000, 0.450, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(49)


        for o in Front_Heel_R:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.070, 0.000, 0.000)
            insert_keys(9)
            o.rotation_quaternion=(1.000, -0.120, 0.000, 0.000)
            insert_keys(29)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(33)


        for o in Front_Heel_L:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(17)
            o.rotation_quaternion=(1.000, 0.070, 0.000, 0.000)
            insert_keys(25)
            o.rotation_quaternion=(1.000, -0.120, 0.000, 0.000)
            insert_keys(45)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(49)


        for o in Front_Toe_R:
            o.rotation_quaternion=(1.000, -0.070, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, -0.800, 0.000, 0.000)
            insert_keys(9)
            o.rotation_quaternion=(1.000, 0.100, 0.000, 0.000)
            insert_keys(15)
            o.rotation_quaternion=(1.000, 0.300, 0.000, 0.000)
            insert_keys(22)
            o.rotation_quaternion=(1.000, -0.070, 0.000, 0.000)
            insert_keys(33)


        for o in Front_Toe_L:
            o.rotation_quaternion=(1.000, -0.070, 0.000, -0.000)
            insert_keys(17)
            o.rotation_quaternion=(1.000, -0.800, 0.000, -0.000)
            insert_keys(25)
            o.rotation_quaternion=(1.000, 0.100, 0.000, -0.000)
            insert_keys(31)
            o.rotation_quaternion=(1.000, 0.300, 0.000, -0.000)
            insert_keys(38)
            o.rotation_quaternion=(1.000, -0.070, 0.000, -0.000)
            insert_keys(49)


        for o in Foot_R:
            o.location=(-0.000, 0.250, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(25)
            o.location=(-0.000, -0.200, 0.080)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(35)
            o.location=(-0.000, -0.500, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(39)
            o.location=(-0.000, 0.250, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(57)


        for o in Foot_L:
            o.location=(0.000, 0.250, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(10)
            o.location=(0.000, -0.200, 0.080)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(20)
            o.location=(0.000, -0.500, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(24)
            o.location=(0.000, -0.097, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(34)
            o.location=(0.000, 0.250, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(42)


        for o in Heel_R:
            o.rotation_quaternion=(1.000, -0.050, 0.000, 0.000)
            insert_keys(25)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(49)
            o.rotation_quaternion=(1.000, -0.050, 0.000, 0.000)
            insert_keys(57)


        for o in Heel_L:
            o.rotation_quaternion=(1.000, -0.050, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(34)
            o.rotation_quaternion=(1.000, -0.050, 0.000, 0.000)
            insert_keys(42)


        for o in Toe_R:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(25)
            o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
            insert_keys(33)
            o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
            insert_keys(35)
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.000)
            insert_keys(40)
            o.rotation_quaternion=(1.000, -0.350, 0.000, 0.000)
            insert_keys(46)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(57)


        for o in Toe_L:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
            insert_keys(18)
            o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
            insert_keys(20)
            o.rotation_quaternion=(1.000, -0.100, 0.000, 0.000)
            insert_keys(24)
            o.rotation_quaternion=(1.000, -0.350, 0.000, 0.000)
            insert_keys(30)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(42)


        for o in Tail:
            o.rotation_quaternion=(1.000, 0.005, 0.000, -0.014)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.020)
            insert_keys(5)
            o.rotation_quaternion=(1.000, 0.010, 0.000, 0.000)
            insert_keys(13)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.020)
            insert_keys(21)
            o.rotation_quaternion=(1.000, 0.010, 0.000, 0.000)
            insert_keys(29)
            o.rotation_quaternion=(1.000, 0.005, 0.000, -0.014)
            insert_keys(33)


        for o in Torso:
            o.location=(0.000, 0.000, -0.100)
            insert_keys(1)
            o.location=(0.000, 0.000, -0.100)
            insert_keys(33)


        for o in Hips:
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.000, -0.030, 0.030)
            insert_keys(12)
            o.location=(-0.020, 0.000, 0.020)
            o.rotation_quaternion=(1.000, 0.040, 0.000, 0.000)
            insert_keys(21)
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.030, -0.030)
            insert_keys(28)
            o.location=(0.020, 0.000, 0.020)
            o.rotation_quaternion=(1.000, 0.040, 0.000, 0.000)
            insert_keys(37)
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.000, -0.030, 0.030)
            insert_keys(44)


        for o in Chest:
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.000, -0.010, -0.020)
            insert_keys(3)
            o.location=(0.060, 0.000, 0.040)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(11)
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.000, 0.010, 0.020)
            insert_keys(19)
            o.location=(-0.060, 0.000, 0.040)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(27)
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.000, -0.010, -0.020)
            insert_keys(35)


        for o in Neck:
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.132, 0.000, 0.000)
            insert_keys(1)
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.120, 0.000, 0.000)
            insert_keys(3)
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.180, 0.000, 0.000)
            insert_keys(12)
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.120, 0.000, 0.000)
            insert_keys(19)
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.180, 0.000, 0.000)
            insert_keys(28)
            o.location=(0.000, 0.000, 0.000)
            o.rotation_quaternion=(1.000, 0.132, 0.000, 0.000)
            insert_keys(33)


        for o in Head:
            o.rotation_quaternion=(1.000, 0.101, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, 0.070, 0.000, 0.000)
            insert_keys(4)
            o.rotation_quaternion=(1.000, 0.150, 0.000, 0.000)
            insert_keys(13)
            o.rotation_quaternion=(1.000, 0.070, 0.000, 0.000)
            insert_keys(20)
            o.rotation_quaternion=(1.000, 0.150, 0.000, 0.000)
            insert_keys(29)
            o.rotation_quaternion=(1.000, 0.101, 0.000, 0.000)
            insert_keys(33)


        for o in Front_Hoof_R:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, -1.200, 0.000, 0.000)
            insert_keys(9)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(14)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(33)


        for o in Front_Hoof_L:
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(17)
            o.rotation_quaternion=(1.000, -1.200, 0.000, -0.000)
            insert_keys(25)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(30)
            o.rotation_quaternion=(1.000, 0.000, 0.000, -0.000)
            insert_keys(49)


        for o in Rear_Hoof_R:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(25)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(26)
            o.rotation_quaternion=(1.000, 0.700, 0.000, 0.000)
            insert_keys(32)
            o.rotation_quaternion=(1.000, 0.700, 0.000, 0.000)
            insert_keys(34)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(38)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(57)


        for o in Rear_Hoof_L:
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(10)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(11)
            o.rotation_quaternion=(1.000, 0.700, 0.000, 0.000)
            insert_keys(17)
            o.rotation_quaternion=(1.000, 0.700, 0.000, 0.000)
            insert_keys(19)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(23)
            o.rotation_quaternion=(1.000, 0.000, 0.000, 0.000)
            insert_keys(42)


        for o in Shoulder_R:
            o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
            insert_keys(1)
            o.rotation_quaternion=(1.000, -0.080, 0.000, 0.000)
            insert_keys(17)
            o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
            insert_keys(30)
            o.rotation_quaternion=(1.000, 0.200, 0.000, 0.000)
            insert_keys(33)


        for o in Shoulder_L:
            o.rotation_quaternion=(1.000, 0.200, 0.000, -0.000)
            insert_keys(17)
            o.rotation_quaternion=(1.000, -0.080, 0.000, -0.000)
            insert_keys(33)
            o.rotation_quaternion=(1.000, 0.200, 0.000, -0.000)
            insert_keys(46)
            o.rotation_quaternion=(1.000, 0.200, 0.000, -0.000)
            insert_keys(49)





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
#      END  - HORSE - 32 FRAMES  WALK CYCLE
# =====================================================









classes = [
           OBJECT_OT_rigify_zoo_horse_run_15_ra,
           OBJECT_OT_rigify_zoo_horse_walk_32_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()











 






 
