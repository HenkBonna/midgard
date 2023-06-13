import bpy
import math

from bpy.props import (PointerProperty)
from bpy.types import (Panel)



# Progressive Walk Run

#------------------------ Linear Feet Setup ------------------------

class OBJECT_OT_walk_linear_feet_setup_animbox_ra(bpy.types.Operator):
    '''Walk - Linear F-Curve Feet Setup'''
    bl_idname = "object.walk_linear_feet_setup_animbox_ra"
    bl_label = "Feet Setup"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                 context.object.mode == 'POSE'
                 and context.object.animation_data.action is not None)


    def execute(self, context):


        def set_start_frame():

            ob = bpy.context.object
            anim_data = ob.animation_data
            action = anim_data.action
            f_range = action.frame_range

            sc = bpy.context.scene
            fs = sc.frame_start
            fe = sc.frame_end

            sc.frame_end = (int(f_range[1]) - 1)

        set_start_frame()


        def middle_of_timeline():

            #  TIMELINE / 2 (CONDITION)
            sc = bpy.context.scene
            fs = sc.frame_start
            fe = sc.frame_end

            frame = 0

            if fs == 1:
                if fe % 2 == 0:
                    frame = int(fe / 2 + 1)

                if fe % 2 != 0:
                    frame = int(fe / 2 + 1)


            if fs > 1:
                f_num = (fs + fe) - 1
                if f_num % 2 == 0:
                    frame = int(f_num / 2 + 1)

                if f_num % 2 != 0:
                    frame = int(f_num / 2 + 1)


            return frame


        def last_key_last_frame():

            ob = bpy.context.object
            anim_data = ob.animation_data
            action = anim_data.action
            f_range = action.frame_range

            sc = bpy.context.scene
            fs = sc.frame_start
            fe = sc.frame_end

            sc.frame_end = (int(f_range[1]) - 1)

            if anim_data:
                if anim_data.action:
                    fcurve = ob.animation_data.action.fcurves

                    for fc in fcurve:

                        #--------------- Left Foot ------

                        if fc.data_path.endswith(('location')) and 'foot_ik.L' in fc.data_path:
                            if fc.array_index == 1:
                                fcp = fc.keyframe_points

                                for p in fcp:
                                    p_first = p.co[0]
                                    if p_first == f_range[1]:

                                        compare_frame = p_first - fe
                                        if compare_frame == 1:
                                            return True


        #--------------------------------------------------

        def feet_linear_setup(mid_frame, last_frame):

            ob = bpy.context.object
            anim_data = ob.animation_data
            action = anim_data.action

            if anim_data:
                if anim_data.action:

                    fcurve = ob.animation_data.action.fcurves

                    for fc in fcurve:

                        #--------------- Left Foot ------------

                        if fc.data_path.endswith(('location')) and 'foot_ik.L' in fc.data_path:
                            if fc.array_index == 1:
                                fcp = fc.keyframe_points

                                for p in fcp:

                                    p_first = p.co[0]
                                    if p_first > 1 and p_first < mid_frame:
                                        pco = p.co

                                        if fcp[1].co == pco:

                                            fc.keyframe_points.remove(fcp[1])

                                        fc.keyframe_points[0].handle_right_type = 'VECTOR'
                                        fc.keyframe_points[1].handle_left_type = 'VECTOR'

                                        fc.update()


                                    if p_first <= 1 and p_first < mid_frame:

                                        fc.keyframe_points[0].handle_right_type = 'VECTOR'
                                        fc.keyframe_points[0].handle_left_type = 'FREE'
                                        fc.keyframe_points[1].handle_left_type = 'VECTOR'

                                        fc.update()


                        #--------------- Right Foot -------------

                        if fc.data_path.endswith(('location')) and 'foot_ik.R' in fc.data_path:
                            if fc.array_index == 1:
                                fcp = fc.keyframe_points

                                for p in fcp:

                                    p_first = p.co[0]
                                    if p_first < last_frame and p_first > mid_frame:
                                        pco = p.co

                                        if fcp[-2].co == pco:

                                            fc.keyframe_points.remove(fcp[-2])

                                        fc.keyframe_points[-1].handle_left_type = 'VECTOR'
                                        fc.keyframe_points[-2].handle_right_type = 'VECTOR'

                                        fc.update()


                                    if p_first >= last_frame and p_first > mid_frame:

                                        fc.keyframe_points[-1].handle_left_type = 'VECTOR'
                                        fc.keyframe_points[-1].handle_right_type = 'FREE'
                                        fc.keyframe_points[-2].handle_right_type = 'VECTOR'

                                        fc.update()


        #-------------------------------------------------


        sc = bpy.context.scene
        fs = sc.frame_start
        fe = sc.frame_end

        ob = bpy.context.object
        anim_data = ob.animation_data
        action = anim_data.action

        rem_range = (middle_of_timeline() - 1)

        if anim_data:
            if anim_data.action:
                if last_key_last_frame():
                    for i in range(rem_range):
                        feet_linear_setup(middle_of_timeline(), fe)



        return {'FINISHED'}

#================== End Linear Feet Setup ======================






#------------------- Setup - Walk/Run Direct/On Curve -------------

class OBJECT_OT_progressive_walk_run_setup_animbox_ra(bpy.types.Operator):
    '''Progressive Walk-Run Setup'''
    bl_idname = "object.progressive_walk_run_setup_animbox_ra"
    bl_label = "Progressive Walk Run Setup"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE')


    def execute(self, context):
        scene = context.scene

        # Refs
        create_curve = scene.animbox_ra_props.create_setup_walk_run_curve_animbox_ra


        def rename_context_rig():
            ob = bpy.context.object
            on = ob.name.startswith(('pwr', 'PWR', 'Pwr'))

            if not on:
                ob.name = 'pwr_' + ob.name
                ob.data.name = 'pwr_' + ob.name


        rename_context_rig()


        ob = bpy.context.object
        o_split = ob.name.split('.')
        ob.name = o_split[0]
        ob.data.name = o_split[0]


#-------------------------------------------------------

        def add_pre_post_infinity():

            ob = bpy.context.object
            anim_data = ob.animation_data
            pose_bones = ob.pose.bones

            bone_list = ['foot_ik.R', 'foot_ik.L', 'torso',
                         'foot_heel_ik.R', 'foot_heel_ik.L',
                         'upper_arm_fk.L', 'upper_arm_fk.R',]

            for bone in pose_bones:
                if bone.name in bone_list:

                    if anim_data.action is not None:
                        ob_fcurve = ob.animation_data.action.fcurves

                        for fc in ob_fcurve:
                            d_path = ('location', 'rotation_quaternion', 'rotation_euler', 'scale')
                            if fc.data_path.endswith((d_path)) and bone.name in fc.data_path:
                                for m in fc.modifiers:
                                   if (m.type == 'CYCLES'):
                                       fc.modifiers.remove(m)
                                fc.modifiers.new(type='CYCLES')

                            fc.update()


        add_pre_post_infinity()

        #------------------------------------------------


        def remove_curve():
            for o in bpy.data.objects:
                if o.type == 'CURVE' and o.name.startswith('Pwr Curve'):
                    bpy.data.objects.remove(o, do_unlink=True)

        remove_curve()

#------------- Walk Curve -------------------
        def create_walk_curve():

            curveData = bpy.data.curves.new('pwr_curve', type='CURVE')
            curveData.dimensions = '3D'
            curveData.resolution_u = 12

            polyline = curveData.splines.new('BEZIER')
            polyline.bezier_points.add(1)

            polyline.bezier_points[0].co =  ((0.0000, 0.0000, 0.0000))
            polyline.bezier_points[0].handle_left =  ((0.0000, 2, 0.0000))
            polyline.bezier_points[0].handle_right =  ((0.0000, -2, 0.0000))

            polyline.bezier_points[1].co =  ((0.0000, -10.0000, 0.0000))
            polyline.bezier_points[1].handle_left =  ((0.0000, -8, 0.0000))
            polyline.bezier_points[1].handle_right =  ((0.0000, -12, 0.0000))


            curveOB = bpy.data.objects.new('Pwr Curve', curveData)

            scn = bpy.context.scene
            scn.collection.objects.link(curveOB)
            bpy.context.view_layer.objects.active = curveOB
            curveOB.select_set(1)


            for obj in bpy.context.selected_objects:
                if obj.type == 'CURVE':
                    obj.data.bevel_depth = 0.01
                    for s in obj.data.splines:
                        s.use_cyclic_u = False


#------------- End Walk Curve ---------------


        pose_bones = bpy.context.object.pose.bones


        for b in pose_bones:
            if b.name.startswith('upper_arm_parent.R'):
                b["IK_FK"] = float(1)
            if b.name.startswith('upper_arm_parent.L'):
                b["IK_FK"] = float(1)

            if b.name.startswith('torso'):
                torso_loc = b.location


        for b in pose_bones:
            walk_child_of_const = [c for c in b.constraints if c.name == "Pwr Child Of"]

            for c in walk_child_of_const:
                b.constraints.remove(c)

        def remove_empty():
            for o in bpy.data.objects:
                if o.type == 'EMPTY' and o.name.startswith('Pwr Empty'):
                    bpy.data.objects.remove(o, do_unlink=True)

        remove_empty()

        def walk_empty():

            o = bpy.data.objects.new( "Pwr Empty", None )
            bpy.context.scene.collection.objects.link( o )

            o.empty_display_size = 0.5
            o.empty_display_type = 'PLAIN_AXES'
            o.scale[2] = 2
            o.location.x = 0.0
            o.location.y = 0.0
            o.location.z = 0.0


        walk_empty()



        def empty_name():
            for o in bpy.data.objects:
                if o.type == 'EMPTY' and o.name == 'Pwr Empty':
                    Empty_Name = o.name

                    return Empty_Name


        bone_list = ('torso', 'foot_ik', 'hand_ik')


        for bone in pose_bones:
            if bone.name.startswith(tuple(b for b in bone_list)):
                bpy.context.object.data.bones.active = bone.bone
                bc = bone.constraints.new(type='CHILD_OF')
                bc.target = bpy.data.objects[empty_name()]
                bc.subtarget = bone.name
                bc.name = "Pwr Child Of"



        if create_curve:
            create_walk_curve()

            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            bpy.ops.object.select_all(action='DESELECT')

            for o in bpy.data.objects:
                if o.type == 'EMPTY' and o.name == 'Pwr Empty':
                    o.select_set(1)
                    bpy.context.view_layer.objects.active = o
                    fp = o.constraints.new(type='FOLLOW_PATH')
                    fp.name = "Follow Path"
                    fp.target = bpy.data.objects['Pwr Curve']
                    fp.forward_axis = 'TRACK_NEGATIVE_Y'
                    fp.use_curve_follow = True

                    bpy.ops.constraint.followpath_path_animate(constraint="Follow Path", owner='OBJECT')



        return {'FINISHED'}

#--------------------------- End Progressive Walk Setup ------------





#---------------------------- Adjust Curve Speed -------------------

class OBJECT_OT_walk_run_curve_speed_animbox_ra(bpy.types.Operator):
    '''Adjust Walk-Run Curve Speed
Run - if "Run Speed" option is ON'''
    bl_idname = "object.walk_run_curve_speed_animbox_ra"
    bl_label = "Adjust Curve Speed"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'OBJECT' and
                  len(context.selected_objects) == 1 and
                  context.object.type == 'CURVE')



    def execute(self, context):
        scene = context.scene

        # Refs
        run_speed_opt = scene.animbox_ra_props.run_curve_speed_animbox_ra


        #-----------------------------------------
        #-----------------------------------------
        
        def get_left_Leg_length():
              
            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):
                    bone = o.pose.bones
             
                    b_1 =  bone['DEF-shin.L'].length
                    b_2 =  bone['DEF-shin.L.001'].length
                    b_3 =  bone['DEF-thigh.L'].length
                    b_4 =  bone['DEF-thigh.L.001'].length
                    
                    length = b_1 + b_2 + b_3 + b_4
                    
                    masterlength = round(length, 2)
                    
                    num = (round(1 - masterlength, 2))
                    
                    return num        
        
        
        #-----------------------------------------
        #-----------------------------------------


        def run_feet_distance():

            sc = bpy.context.scene
            frame_start = sc.frame_start
            frame_end = sc.frame_end
            sc.frame_set(frame_start)

            num = 8

            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):

                    list = []
                    for i in range(frame_start, frame_end):
                        sc.frame_set(i)

                    p_bones = o.pose.bones

                    foot_l = p_bones['foot_ik.L'].location
                    foot_r = p_bones['foot_ik.R'].location

                    h = math.dist(foot_l, foot_r)


                    cft = get_left_Leg_length()

                    round_h = round(h, 2)
                    res = (round_h - (cft * 1.57)) * - num

                    # res = round_h * - num

            list.append(res)
            max_res = max(list)

            return max_res


        #-----------------------------------------


        def walk_feet_distance():

            sc = bpy.context.scene
            frame_start = sc.frame_start
            sc.frame_set(frame_start)

            num = 8

            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):

                    p_bones = o.pose.bones

                    foot_l = p_bones['foot_ik.L'].location
                    foot_r = p_bones['foot_ik.R'].location

                    h = math.dist(foot_l, foot_r)

                    round_h = round(h, 2)
                    res = round_h * - num

                    return res


        #-----------------------------------------

        def rig_name():
            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):
                    return True

        if not rig_name():
            self.report({'INFO'}, 'Rig Name must start with "Pwr"')
            pass


        def check_anim_data():
            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):
                    anim_data = o.animation_data
                    if anim_data:
                        action = anim_data.action
                        if action:
                            return True

        def get_walk_frame_range():
            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):
                    if check_anim_data():
                        anim_frame_range = o.animation_data.action.frame_range
                        return anim_frame_range


        if rig_name():
            if check_anim_data():
                sc = bpy.context.scene
                fe = sc.frame_end
                f_range = get_walk_frame_range()
                sc.frame_end = ((int(f_range[1])-1) * 4)


        if rig_name():
            if check_anim_data():

                sel_ob = bpy.context.selected_objects
                for o in sel_ob:

                    curve_length = o.data.splines.active.calc_length()

                    frame_range = get_walk_frame_range()

                    if not run_speed_opt:
                        dist = walk_feet_distance()
                        
                        fe = bpy.context.scene.frame_end
                        fr = (frame_range[1] * 4) - 1

                        s =  abs((curve_length * fr ) / dist)
                        speed = int(s)
                        o.data.path_duration = speed


                    if run_speed_opt:
                        dist = run_feet_distance()

                        fe = bpy.context.scene.frame_end
                        fr = (frame_range[1] * 4) - 1
                        s =  abs(curve_length + dist  ) * 1.6

                        d = fr / 10
                        speed = int(fe + (s * d))


                    if not run_speed_opt:
                        o.data.path_duration = speed

                    if run_speed_opt:
                        o.data.path_duration = int(speed / 2.5)



        sc = bpy.context.scene
        frame_start = sc.frame_start
        sc.frame_set(frame_start)


        return {'FINISHED'}


#--------------------- End Curve Speed ----------------
#======================================================






#---------------------------- Frame Timeline ----------
#======================================================


class OBJECT_OT_curve_speed_frame_timeline_animbox_ra(bpy.types.Operator):
    '''Frame Timeline while using PWR Curve'''
    bl_idname = "object.curve_speed_frame_timeline_animbox_ra"
    bl_label = "Frame Timeline"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.mode == 'OBJECT')


    def execute(self, context):


        bpy.ops.object.select_all(action='DESELECT')
        
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

#--------------------- End Frame Timeline -------------
#======================================================





#--------------------- Direct Speed -------------------
#======================================================



class OBJECT_OT_walk_run_direct_speed_animbox_ra(bpy.types.Operator):
    '''Adjust Walk - Run Direct Speed
Run - if "Run Speed" option is ON'''
    bl_idname = "object.walk_run_direct_speed_animbox_ra"
    bl_label = "Adjust Direct Speed"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'OBJECT' and
                  len(context.selected_objects) == 1 and
                  context.object.type == 'EMPTY')



    def execute(self, context):
        scene = context.scene

        # Refs
        run_speed_opt = scene.animbox_ra_props.run_curve_speed_animbox_ra


        mult_frame_range = scene.animbox_ra_props.multiply_frame_range_animbox_ra

        #-----------------------------------------

        def run_feet_distance():

            sc = bpy.context.scene
            frame_start = sc.frame_start
            frame_end = sc.frame_end
            sc.frame_set(frame_start)

            num = mult_frame_range * 2

            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):

                    list = []
                    for i in range(frame_start, frame_end):
                        sc.frame_set(i)

                    p_bones = o.pose.bones

                    foot_l = p_bones['foot_ik.L'].location
                    foot_r = p_bones['foot_ik.R'].location


                    h = math.dist(foot_l, foot_r)

                    round_h = round(h, 2)
                    res = round_h * - num

            list.append(res)
            max_res = max(list) * 1.57

            return max_res


        #-----------------------------------------

        def walk_feet_distance(times):

            sc = bpy.context.scene
            frame_start = sc.frame_start
            sc.frame_set(frame_start)

            num = times * 2

            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):

                    p_bones = o.pose.bones

                    foot_l = p_bones['foot_ik.L'].location
                    foot_r = p_bones['foot_ik.R'].location


                    h = math.dist(foot_l, foot_r)

                    round_h = round(h, 2)
                    res = round_h * - num

                    return res


        #-----------------------------------------

        def rig_name():
            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):
                    return True

        if not rig_name():
            self.report({'INFO'}, 'Rig Name must start with "Pwr"')
            pass


        def check_anim_data():
            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):
                    anim_data = o.animation_data
                    if anim_data:
                        action = anim_data.action
                        if action:
                            return True


        def get_walk_frame_range():

            for o in bpy.data.objects:
                if o.type == 'ARMATURE' and o.name.startswith(('Pwr', 'pwr', 'PWR')):
                    if check_anim_data():

                        anim_frame_range = o.animation_data.action.frame_range
                        return anim_frame_range



        def linear_keyframes(f_1, f_2, val_1, val_2):


            ob = bpy.context.object
            ob.animation_data_create()
            ob.animation_data.action = bpy.data.actions.new(name="Direct Walk_Run")

            fcu_y = ob.animation_data.action.fcurves.new(data_path="location", index=1)
            fcu_y.keyframe_points.add(2)

            fcu_y.keyframe_points[0].co = f_1, val_1
            fcu_y.keyframe_points[1].co = f_2, val_2

            fcu_y.keyframe_points[0].handle_left_type = 'FREE'
            fcu_y.keyframe_points[0].handle_right_type = 'VECTOR'

            fcu_y.keyframe_points[1].handle_left_type = 'VECTOR'
            fcu_y.keyframe_points[1].handle_right_type = 'FREE'

            action = ob.animation_data.action
            fcurve = action.fcurves.find('location', index=1)
            fcurve.update()




        if rig_name():
            if check_anim_data():

                sc = bpy.context.scene
                fe = sc.frame_end
                frame_start = sc.frame_start
                f_range = get_walk_frame_range()
                sc.frame_end = int(f_range[1]-1) * mult_frame_range
                sfe = sc.frame_end


                if not run_speed_opt:
                    w_dist = walk_feet_distance(mult_frame_range)
                    linear_keyframes(frame_start, sfe, 0.0, w_dist)

                if run_speed_opt:
                    r_dist = run_feet_distance()
                    linear_keyframes(frame_start, sfe, 0.0, r_dist)


        sc = bpy.context.scene
        frame_start = sc.frame_start
        sc.frame_set(frame_start)



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


#--------------------- End Direct Speed ---------------
#======================================================




#======================================================
#==================== Walk - Feet Cleanup =============
#======================================================



class OBJECT_OT_walk_feet_cleanup_animbox_ra(bpy.types.Operator):
    '''Selected Foot -
Duplicate Current Keyframe within number of "Staple Frames"
Repeat process selected number of times -
with an interval of Walk Frame Range'''
    bl_idname = "object.walk_feet_cleanup_animbox_ra"
    bl_label = "Foot Staple Gun"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                context.object.mode == 'POSE' and len(context.selected_pose_bones) != 0)


    def execute(self, context):

        scene = context.scene
     

        sel_bones = bpy.context.selected_pose_bones

        feet_list = ['foot_ik.L', 'foot_ik.R']

 
        for b in sel_bones:
            if b.name not in feet_list:
 
                self.report({'INFO'}, 'Select Left or Right Foot')
                pass


        # Refs
        walk_frame_range_opt = scene.animbox_ra_props.walk_cycle_frame_range_animbox_ra
        skip_frames = scene.animbox_ra_props.staple_frames_animbox_ra
        repeat_times = scene.animbox_ra_props.staple_repeat_times_animbox_ra


        def clone_frame_forward():

            sc = bpy.context.scene

            bpy.ops.pose.copy()
            sc.frame_current += 1


            for key in bpy.data.scenes["Scene"].keying_sets_all:
                if key.bl_label == 'Location, Rotation & Scale':
                    bpy.data.scenes["Scene"].keying_sets.active = key


            for d in range(skip_frames):
                bpy.ops.anim.keyframe_delete()
                sc.frame_current += 1


            bpy.ops.pose.paste(flipped=False)
            bpy.ops.anim.keyframe_insert(type='Location')
            bpy.ops.anim.keyframe_insert(type='Rotation')


            for d in range(skip_frames+1):
                sc.frame_current -= 1


        def next_frame():
            sc = bpy.context.scene

            walk_cycle_range = walk_frame_range_opt
            fc = bpy.context.scene.frame_current

            next_fr = fc + walk_cycle_range
            sc.frame_set(next_fr)



        sel_bones = bpy.context.selected_pose_bones

        feet_list = ['foot_ik.L', 'foot_ik.R']

        for b in sel_bones:
            if b.name in feet_list:
                for _ in range(repeat_times):
                    clone_frame_forward()
                    next_frame()


        return {'FINISHED'}


#======================================================
#                    End Walk - Cleanup Feet
#======================================================




# =====================================================
#                    Bake Walk / Run
# =====================================================


class OBJECT_OT_bake_progressive_walk_run_animbox_ra(bpy.types.Operator):
    '''Bake Progressive Walk / Run -

1) Before Current Frame (current Playhead Position)

2) Preview Range'''
    bl_idname = "object.bake_progressive_walk_run_animbox_ra"
    bl_label = "Bake"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):

        return (context.object is not None and
                 context.object.mode == 'POSE'
                 and context.object.animation_data.action is not None)


    def execute(self, context):


        def bone_to_bake():

            ob = bpy.context.object
            anim_data = ob.animation_data
            action = anim_data.action

            pose_bones = bpy.context.object.pose.bones

            for t in pose_bones:
                if t.name.startswith('torso'):
                    t.bone.select = 1

            for b in pose_bones:
                bone_name = b.name

                if anim_data:
                    if anim_data.action:
                        fcurve = ob.animation_data.action.fcurves

                        for fc in fcurve:
                            if bone_name in fc.data_path:
                                b.bone.select = 1


        #-------------------------------------
        def bake_walk_run():

            sc = bpy.context.scene
            fs = sc.frame_start
            fe = sc.frame_end
            fc = sc.frame_current

            f_prev_start = sc.frame_preview_start
            f_prev_end = sc.frame_preview_end


            if f_prev_start:

                bpy.ops.nla.bake(frame_start=f_prev_start,
                                 frame_end=f_prev_end,
                                 only_selected=True,
                                 visual_keying=True,
                                 clear_constraints=True,
                                 bake_types={'POSE'})

            if not f_prev_start:

                bpy.ops.nla.bake(frame_start=1,
                                 frame_end=fc,
                                 only_selected=True,
                                 visual_keying=True,
                                 clear_constraints=True,
                                 bake_types={'POSE'})

        #-------------------------------------

        bone_to_bake()
        bake_walk_run()



        return {'FINISHED'}



# =======================================================
#                     End Bake Walk / Run
# =======================================================





# =====================================================
#              PANEL
# =====================================================

# Bake / Cleanup

class PANEL_PT_walk_feet_cleanup_animbox_ra(bpy.types.Panel):
    bl_label = "Bake / Cleanup"
    bl_idname = 'PANEL_PT_walk_feet_cleanup_animbox_ra'
    bl_parent_id = 'PANEL_ANIM_BOX_PT_rigify_anim_box_00_2'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Walk Curve"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        ra_props = scene.animbox_ra_props 



        # --------------------- Bake ---------------------------
        box = layout.box()
        row = box.row()

        row.label(text="", icon='KEYFRAME_HLT')

        row.scale_y = 1.2
        row.scale_x = 1
        row.operator("object.bake_progressive_walk_run_animbox_ra")


        # --------------------- Cleanup ------------------------

        box = layout.box()
        row = box.row()
        row.alignment = 'CENTER'
        row.scale_y = 0.8
        row.label(text="Walk - Feet Cleanup", icon='NOCURVE')
        row = box.row()

        row.label(text="Frame Range")
        row.prop(ra_props, "walk_cycle_frame_range_animbox_ra")

        row = box.row()
        row.label(text="Staple Frames")
        row.prop(ra_props, "staple_frames_animbox_ra")

        row = box.row()
        row.label(text="Repeat")
        row.prop(ra_props, "staple_repeat_times_animbox_ra")
        row = box.row()

        row.scale_y = 1.2
        row.operator("object.walk_feet_cleanup_animbox_ra", icon='PLAY')


#--------------------------------------------------------------------------



classes = [ OBJECT_OT_walk_linear_feet_setup_animbox_ra,
            OBJECT_OT_progressive_walk_run_setup_animbox_ra,
            OBJECT_OT_walk_run_curve_speed_animbox_ra,
            OBJECT_OT_curve_speed_frame_timeline_animbox_ra,
            OBJECT_OT_walk_run_direct_speed_animbox_ra,
            OBJECT_OT_walk_feet_cleanup_animbox_ra,
            OBJECT_OT_bake_progressive_walk_run_animbox_ra,
            PANEL_PT_walk_feet_cleanup_animbox_ra,

          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)




def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()
