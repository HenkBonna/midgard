
import bpy

 




# =============================================================
#  LEFT ARM TO -> FK  
# =============================================================
 

class OBJECT_OT_left_arm_to_fk_ra(bpy.types.Operator):
    '''LEFT ARM TO -> FK '''
    bl_idname = "object.left_arm_to_fk_ra"
    bl_label = "FK"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):



        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name

 

        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.data.objects[ob.name].data.bones

        #set the frame
        frame = bpy.context.scene.frame_current

        # Pivot 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'


        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Deselect All
        bpy.ops.pose.select_all(action = 'DESELECT')


        rig = bpy.data.objects[ob.name]

        # Variable for rig_ID
        rig_id = rig.data['rig_id'] 


        # Variables for IK FK switch ops
        arm_ik2fk = eval('bpy.ops.pose.rigify_limb_ik2fk_' + rig_id)
        arm_fk2ik = eval('bpy.ops.pose.rigify_generic_snap_' + rig_id)


        
# =============================================================
#  TOGGLE
# =============================================================



        for bone in pose_bones: 
                                    
            # Arms To FK  
            if bone.name.startswith('upper_arm_parent') and ".L" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L\", \"forearm_fk.L\", \"hand_fk.L\"]", ik_bones="[\"upper_arm_ik.L\", \"MCH-forearm_ik.L\", \"MCH-upper_arm_ik_target.L\"]", ctrl_bones="[\"upper_arm_ik.L\", \"upper_arm_ik_target.L\", \"hand_ik.L\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L\", \"MCH-forearm_ik.L\", \"MCH-upper_arm_ik_target.L\"]", output_bones="[\"upper_arm_fk.L\", \"forearm_fk.L\", \"hand_fk.L\"]", ctrl_bones="[\"upper_arm_ik.L\", \"upper_arm_ik_target.L\", \"hand_ik.L\"]")

         
                                      
                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )

         
        #------------------------------ 001 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.001" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):   
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.001\", \"forearm_fk.L.001\", \"hand_fk.L.001\"]", ik_bones="[\"upper_arm_ik.L.001\", \"MCH-forearm_ik.L.001\", \"MCH-upper_arm_ik_target.L.001\"]", ctrl_bones="[\"upper_arm_ik.L.001\", \"upper_arm_ik_target.L.001\", \"hand_ik.L.001\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.001\", \"MCH-forearm_ik.L.001\", \"MCH-upper_arm_ik_target.L.001\"]", output_bones="[\"upper_arm_fk.L.001\", \"forearm_fk.L.001\", \"hand_fk.L.001\"]", ctrl_bones="[\"upper_arm_ik.L.001\", \"upper_arm_ik_target.L.001\", \"hand_ik.L.001\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 002 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.002" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.002\", \"forearm_fk.L.002\", \"hand_fk.L.002\"]", ik_bones="[\"upper_arm_ik.L.002\", \"MCH-forearm_ik.L.002\", \"MCH-upper_arm_ik_target.L.002\"]", ctrl_bones="[\"upper_arm_ik.L.002\", \"upper_arm_ik_target.L.002\", \"hand_ik.L.002\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.002\", \"MCH-forearm_ik.L.002\", \"MCH-upper_arm_ik_target.L.002\"]", output_bones="[\"upper_arm_fk.L.002\", \"forearm_fk.L.002\", \"hand_fk.L.002\"]", ctrl_bones="[\"upper_arm_ik.L.002\", \"upper_arm_ik_target.L.002\", \"hand_ik.L.002\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 003 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.003" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.003\", \"forearm_fk.L.003\", \"hand_fk.L.003\"]", ik_bones="[\"upper_arm_ik.L.003\", \"MCH-forearm_ik.L.003\", \"MCH-upper_arm_ik_target.L.003\"]", ctrl_bones="[\"upper_arm_ik.L.003\", \"upper_arm_ik_target.L.003\", \"hand_ik.L.003\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.003\", \"MCH-forearm_ik.L.003\", \"MCH-upper_arm_ik_target.L.003\"]", output_bones="[\"upper_arm_fk.L.003\", \"forearm_fk.L.003\", \"hand_fk.L.003\"]", ctrl_bones="[\"upper_arm_ik.L.003\", \"upper_arm_ik_target.L.003\", \"hand_ik.L.003\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 004 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.004" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.004\", \"forearm_fk.L.004\", \"hand_fk.L.004\"]", ik_bones="[\"upper_arm_ik.L.004\", \"MCH-forearm_ik.L.004\", \"MCH-upper_arm_ik_target.L.004\"]", ctrl_bones="[\"upper_arm_ik.L.004\", \"upper_arm_ik_target.L.004\", \"hand_ik.L.004\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.004\", \"MCH-forearm_ik.L.004\", \"MCH-upper_arm_ik_target.L.004\"]", output_bones="[\"upper_arm_fk.L.004\", \"forearm_fk.L.004\", \"hand_fk.L.004\"]", ctrl_bones="[\"upper_arm_ik.L.004\", \"upper_arm_ik_target.L.004\", \"hand_ik.L.004\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )


        #------------------------------ 005 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.005" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.005\", \"forearm_fk.L.005\", \"hand_fk.L.005\"]", ik_bones="[\"upper_arm_ik.L.005\", \"MCH-forearm_ik.L.005\", \"MCH-upper_arm_ik_target.L.005\"]", ctrl_bones="[\"upper_arm_ik.L.005\", \"upper_arm_ik_target.L.005\", \"hand_ik.L.005\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.005\", \"MCH-forearm_ik.L.005\", \"MCH-upper_arm_ik_target.L.005\"]", output_bones="[\"upper_arm_fk.L.005\", \"forearm_fk.L.005\", \"hand_fk.L.005\"]", ctrl_bones="[\"upper_arm_ik.L.005\", \"upper_arm_ik_target.L.005\", \"hand_ik.L.005\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 006 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.006" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.006\", \"forearm_fk.L.006\", \"hand_fk.L.006\"]", ik_bones="[\"upper_arm_ik.L.006\", \"MCH-forearm_ik.L.006\", \"MCH-upper_arm_ik_target.L.006\"]", ctrl_bones="[\"upper_arm_ik.L.006\", \"upper_arm_ik_target.L.006\", \"hand_ik.L.006\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.006\", \"MCH-forearm_ik.L.006\", \"MCH-upper_arm_ik_target.L.006\"]", output_bones="[\"upper_arm_fk.L.006\", \"forearm_fk.L.006\", \"hand_fk.L.006\"]", ctrl_bones="[\"upper_arm_ik.L.006\", \"upper_arm_ik_target.L.006\", \"hand_ik.L.006\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 007 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.007" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.007\", \"forearm_fk.L.007\", \"hand_fk.L.007\"]", ik_bones="[\"upper_arm_ik.L.007\", \"MCH-forearm_ik.L.007\", \"MCH-upper_arm_ik_target.L.007\"]", ctrl_bones="[\"upper_arm_ik.L.007\", \"upper_arm_ik_target.L.007\", \"hand_ik.L.007\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.007\", \"MCH-forearm_ik.L.007\", \"MCH-upper_arm_ik_target.L.007\"]", output_bones="[\"upper_arm_fk.L.007\", \"forearm_fk.L.007\", \"hand_fk.L.007\"]", ctrl_bones="[\"upper_arm_ik.L.007\", \"upper_arm_ik_target.L.007\", \"hand_ik.L.007\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 008 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.008" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.008\", \"forearm_fk.L.008\", \"hand_fk.L.008\"]", ik_bones="[\"upper_arm_ik.L.008\", \"MCH-forearm_ik.L.008\", \"MCH-upper_arm_ik_target.L.008\"]", ctrl_bones="[\"upper_arm_ik.L.008\", \"upper_arm_ik_target.L.008\", \"hand_ik.L.008\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.008\", \"MCH-forearm_ik.L.008\", \"MCH-upper_arm_ik_target.L.008\"]", output_bones="[\"upper_arm_fk.L.008\", \"forearm_fk.L.008\", \"hand_fk.L.008\"]", ctrl_bones="[\"upper_arm_ik.L.008\", \"upper_arm_ik_target.L.008\", \"hand_ik.L.008\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 009 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.009" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.009\", \"forearm_fk.L.009\", \"hand_fk.L.009\"]", ik_bones="[\"upper_arm_ik.L.009\", \"MCH-forearm_ik.L.009\", \"MCH-upper_arm_ik_target.L.009\"]", ctrl_bones="[\"upper_arm_ik.L.009\", \"upper_arm_ik_target.L.009\", \"hand_ik.L.009\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.009\", \"MCH-forearm_ik.L.009\", \"MCH-upper_arm_ik_target.L.009\"]", output_bones="[\"upper_arm_fk.L.009\", \"forearm_fk.L.009\", \"hand_fk.L.009\"]", ctrl_bones="[\"upper_arm_ik.L.009\", \"upper_arm_ik_target.L.009\", \"hand_ik.L.009\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 010 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.010" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.010\", \"forearm_fk.L.010\", \"hand_fk.L.010\"]", ik_bones="[\"upper_arm_ik.L.010\", \"MCH-forearm_ik.L.010\", \"MCH-upper_arm_ik_target.L.010\"]", ctrl_bones="[\"upper_arm_ik.L.010\", \"upper_arm_ik_target.L.010\", \"hand_ik.L.010\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.010\", \"MCH-forearm_ik.L.010\", \"MCH-upper_arm_ik_target.L.010\"]", output_bones="[\"upper_arm_fk.L.010\", \"forearm_fk.L.010\", \"hand_fk.L.010\"]", ctrl_bones="[\"upper_arm_ik.L.010\", \"upper_arm_ik_target.L.010\", \"hand_ik.L.010\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )






        # Select and Insert Keys
        #  Left Arm  

        def insert_keys():
            bone.keyframe_insert(data_path = 'location', frame= frame)
            bone.keyframe_insert(data_path = 'scale', frame= frame)
            bone.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)



        for bone in pose_bones:
            if bone.name.startswith('upper_arm_parent') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('upper_arm_fk') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('upper_arm_ik') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys()
                bone.bone.select = 0

            if bone.name.startswith('forearm_fk') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('hand_ik') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys()
                bone.bone.select = 0

            if bone.name.startswith('hand_fk') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            else:
                pass   
           


        
        # Select Left Arm

 
        for bone in pose_bones:
            if bone.name.startswith('upper_arm_fk') and ".L" in bone.name:    
                bone.bone.select = 1                    

        return {'FINISHED'}

 

# =============================================================
#  END LEFT ARM TO -> FK  
# =============================================================



# =============================================================
#  LEFT ARM TO -> IK  
# =============================================================




class OBJECT_OT_left_arm_to_ik_ra(bpy.types.Operator):
    '''LEFT ARM TO -> IK'''
    bl_idname = "object.left_arm_to_ik_ra"
    bl_label = "IK"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):


        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name



        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.data.objects[ob.name].data.bones

        #set the frame
        frame = bpy.context.scene.frame_current

        # Pivot 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'


        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Deselect All
        bpy.ops.pose.select_all(action = 'DESELECT')


        rig = bpy.data.objects[ob.name]

        # Variable for rig_ID
        rig_id = rig.data['rig_id'] 


        # Variables for IK FK switch ops
        arm_ik2fk = eval('bpy.ops.pose.rigify_limb_ik2fk_' + rig_id)
        arm_fk2ik = eval('bpy.ops.pose.rigify_generic_snap_' + rig_id)


        
# =============================================================
#  TOGGLE
# =============================================================


        for bone in pose_bones: 
                                    
            # Arms To FK  
            if bone.name.startswith('upper_arm_parent') and ".L" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                   
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L\", \"forearm_fk.L\", \"hand_fk.L\"]", ik_bones="[\"upper_arm_ik.L\", \"MCH-forearm_ik.L\", \"MCH-upper_arm_ik_target.L\"]", ctrl_bones="[\"upper_arm_ik.L\", \"upper_arm_ik_target.L\", \"hand_ik.L\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L\", \"MCH-forearm_ik.L\", \"MCH-upper_arm_ik_target.L\"]", output_bones="[\"upper_arm_fk.L\", \"forearm_fk.L\", \"hand_fk.L\"]", ctrl_bones="[\"upper_arm_ik.L\", \"upper_arm_ik_target.L\", \"hand_ik.L\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 001 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.001" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.001\", \"forearm_fk.L.001\", \"hand_fk.L.001\"]", ik_bones="[\"upper_arm_ik.L.001\", \"MCH-forearm_ik.L.001\", \"MCH-upper_arm_ik_target.L.001\"]", ctrl_bones="[\"upper_arm_ik.L.001\", \"upper_arm_ik_target.L.001\", \"hand_ik.L.001\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.001\", \"MCH-forearm_ik.L.001\", \"MCH-upper_arm_ik_target.L.001\"]", output_bones="[\"upper_arm_fk.L.001\", \"forearm_fk.L.001\", \"hand_fk.L.001\"]", ctrl_bones="[\"upper_arm_ik.L.001\", \"upper_arm_ik_target.L.001\", \"hand_ik.L.001\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 002 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.002" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.002\", \"forearm_fk.L.002\", \"hand_fk.L.002\"]", ik_bones="[\"upper_arm_ik.L.002\", \"MCH-forearm_ik.L.002\", \"MCH-upper_arm_ik_target.L.002\"]", ctrl_bones="[\"upper_arm_ik.L.002\", \"upper_arm_ik_target.L.002\", \"hand_ik.L.002\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.002\", \"MCH-forearm_ik.L.002\", \"MCH-upper_arm_ik_target.L.002\"]", output_bones="[\"upper_arm_fk.L.002\", \"forearm_fk.L.002\", \"hand_fk.L.002\"]", ctrl_bones="[\"upper_arm_ik.L.002\", \"upper_arm_ik_target.L.002\", \"hand_ik.L.002\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 003 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.003" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.003\", \"forearm_fk.L.003\", \"hand_fk.L.003\"]", ik_bones="[\"upper_arm_ik.L.003\", \"MCH-forearm_ik.L.003\", \"MCH-upper_arm_ik_target.L.003\"]", ctrl_bones="[\"upper_arm_ik.L.003\", \"upper_arm_ik_target.L.003\", \"hand_ik.L.003\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.003\", \"MCH-forearm_ik.L.003\", \"MCH-upper_arm_ik_target.L.003\"]", output_bones="[\"upper_arm_fk.L.003\", \"forearm_fk.L.003\", \"hand_fk.L.003\"]", ctrl_bones="[\"upper_arm_ik.L.003\", \"upper_arm_ik_target.L.003\", \"hand_ik.L.003\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 004 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.004" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.004\", \"forearm_fk.L.004\", \"hand_fk.L.004\"]", ik_bones="[\"upper_arm_ik.L.004\", \"MCH-forearm_ik.L.004\", \"MCH-upper_arm_ik_target.L.004\"]", ctrl_bones="[\"upper_arm_ik.L.004\", \"upper_arm_ik_target.L.004\", \"hand_ik.L.004\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.004\", \"MCH-forearm_ik.L.004\", \"MCH-upper_arm_ik_target.L.004\"]", output_bones="[\"upper_arm_fk.L.004\", \"forearm_fk.L.004\", \"hand_fk.L.004\"]", ctrl_bones="[\"upper_arm_ik.L.004\", \"upper_arm_ik_target.L.004\", \"hand_ik.L.004\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 005 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.005" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.005\", \"forearm_fk.L.005\", \"hand_fk.L.005\"]", ik_bones="[\"upper_arm_ik.L.005\", \"MCH-forearm_ik.L.005\", \"MCH-upper_arm_ik_target.L.005\"]", ctrl_bones="[\"upper_arm_ik.L.005\", \"upper_arm_ik_target.L.005\", \"hand_ik.L.005\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.005\", \"MCH-forearm_ik.L.005\", \"MCH-upper_arm_ik_target.L.005\"]", output_bones="[\"upper_arm_fk.L.005\", \"forearm_fk.L.005\", \"hand_fk.L.005\"]", ctrl_bones="[\"upper_arm_ik.L.005\", \"upper_arm_ik_target.L.005\", \"hand_ik.L.005\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 006 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.006" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.006\", \"forearm_fk.L.006\", \"hand_fk.L.006\"]", ik_bones="[\"upper_arm_ik.L.006\", \"MCH-forearm_ik.L.006\", \"MCH-upper_arm_ik_target.L.006\"]", ctrl_bones="[\"upper_arm_ik.L.006\", \"upper_arm_ik_target.L.006\", \"hand_ik.L.006\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.006\", \"MCH-forearm_ik.L.006\", \"MCH-upper_arm_ik_target.L.006\"]", output_bones="[\"upper_arm_fk.L.006\", \"forearm_fk.L.006\", \"hand_fk.L.006\"]", ctrl_bones="[\"upper_arm_ik.L.006\", \"upper_arm_ik_target.L.006\", \"hand_ik.L.006\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 007 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.007" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.007\", \"forearm_fk.L.007\", \"hand_fk.L.007\"]", ik_bones="[\"upper_arm_ik.L.007\", \"MCH-forearm_ik.L.007\", \"MCH-upper_arm_ik_target.L.007\"]", ctrl_bones="[\"upper_arm_ik.L.007\", \"upper_arm_ik_target.L.007\", \"hand_ik.L.007\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.007\", \"MCH-forearm_ik.L.007\", \"MCH-upper_arm_ik_target.L.007\"]", output_bones="[\"upper_arm_fk.L.007\", \"forearm_fk.L.007\", \"hand_fk.L.007\"]", ctrl_bones="[\"upper_arm_ik.L.007\", \"upper_arm_ik_target.L.007\", \"hand_ik.L.007\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 008 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.008" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.008\", \"forearm_fk.L.008\", \"hand_fk.L.008\"]", ik_bones="[\"upper_arm_ik.L.008\", \"MCH-forearm_ik.L.008\", \"MCH-upper_arm_ik_target.L.008\"]", ctrl_bones="[\"upper_arm_ik.L.008\", \"upper_arm_ik_target.L.008\", \"hand_ik.L.008\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.008\", \"MCH-forearm_ik.L.008\", \"MCH-upper_arm_ik_target.L.008\"]", output_bones="[\"upper_arm_fk.L.008\", \"forearm_fk.L.008\", \"hand_fk.L.008\"]", ctrl_bones="[\"upper_arm_ik.L.008\", \"upper_arm_ik_target.L.008\", \"hand_ik.L.008\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 009 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.009" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.009\", \"forearm_fk.L.009\", \"hand_fk.L.009\"]", ik_bones="[\"upper_arm_ik.L.009\", \"MCH-forearm_ik.L.009\", \"MCH-upper_arm_ik_target.L.009\"]", ctrl_bones="[\"upper_arm_ik.L.009\", \"upper_arm_ik_target.L.009\", \"hand_ik.L.009\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.009\", \"MCH-forearm_ik.L.009\", \"MCH-upper_arm_ik_target.L.009\"]", output_bones="[\"upper_arm_fk.L.009\", \"forearm_fk.L.009\", \"hand_fk.L.009\"]", ctrl_bones="[\"upper_arm_ik.L.009\", \"upper_arm_ik_target.L.009\", \"hand_ik.L.009\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 010 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".L.010" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.L.010\", \"forearm_fk.L.010\", \"hand_fk.L.010\"]", ik_bones="[\"upper_arm_ik.L.010\", \"MCH-forearm_ik.L.010\", \"MCH-upper_arm_ik_target.L.010\"]", ctrl_bones="[\"upper_arm_ik.L.010\", \"upper_arm_ik_target.L.010\", \"hand_ik.L.010\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.L.010\", \"MCH-forearm_ik.L.010\", \"MCH-upper_arm_ik_target.L.010\"]", output_bones="[\"upper_arm_fk.L.010\", \"forearm_fk.L.010\", \"hand_fk.L.010\"]", ctrl_bones="[\"upper_arm_ik.L.010\", \"upper_arm_ik_target.L.010\", \"hand_ik.L.010\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )







        # Select and Insert Keys
        #  Left Arm  

        def insert_keys():
            bone.keyframe_insert(data_path = 'location', frame= frame)
            bone.keyframe_insert(data_path = 'scale', frame= frame)
            bone.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)


        for bone in pose_bones:
            if bone.name.startswith('upper_arm_parent') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('upper_arm_fk') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('upper_arm_ik') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys()
                bone.bone.select = 0

            if bone.name.startswith('forearm_fk') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('hand_ik') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys()
                bone.bone.select = 0

            if bone.name.startswith('hand_fk') and ".L" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            else:
                pass   
           

        
        # Select Left Arm

 
        for bone in pose_bones:
            if bone.name.startswith('hand_ik') and ".L" in bone.name:    
                bone.bone.select = 1                    


        return {'FINISHED'}
    
 
# =============================================================
#  END LEFT ARM TO -> IK  
# =============================================================



#==============================================================
#==============================================================
#==============================================================


# =============================================================
#  RIGHT ARM    RIGHT ARM    RIGHT ARM    RIGHT ARM
# =============================================================
  




# =============================================================
#  RIGHT ARM TO -> FK 
# =============================================================
 

class OBJECT_OT_right_arm_to_fk_ra(bpy.types.Operator):
    '''RIGHT ARM TO -> FK'''
    bl_idname = "object.right_arm_to_fk_ra"
    bl_label = "FK"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):



        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name



        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.data.objects[ob.name].data.bones

        #set the frame
        frame = bpy.context.scene.frame_current

        # Pivot 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'


        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Deselect All
        bpy.ops.pose.select_all(action = 'DESELECT')


        rig = bpy.data.objects[ob.name]

        # Variable for rig_ID
        rig_id = rig.data['rig_id'] 


        # Variables for IK FK switch ops
        arm_ik2fk = eval('bpy.ops.pose.rigify_limb_ik2fk_' + rig_id)
        arm_fk2ik = eval('bpy.ops.pose.rigify_generic_snap_' + rig_id)


        
# =============================================================
#  TOGGLE
# =============================================================



        for bone in pose_bones: 
                                    
            # Arms To FK  
            if bone.name.startswith('upper_arm_parent') and ".R" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R\", \"forearm_fk.R\", \"hand_fk.R\"]", ik_bones="[\"upper_arm_ik.R\", \"MCH-forearm_ik.R\", \"MCH-upper_arm_ik_target.R\"]", ctrl_bones="[\"upper_arm_ik.R\", \"upper_arm_ik_target.R\", \"hand_ik.R\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R\", \"MCH-forearm_ik.R\", \"MCH-upper_arm_ik_target.R\"]", output_bones="[\"upper_arm_fk.R\", \"forearm_fk.R\", \"hand_fk.R\"]", ctrl_bones="[\"upper_arm_ik.R\", \"upper_arm_ik_target.R\", \"hand_ik.R\"]")

         
                                      
                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )

         
        #------------------------------ 001 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.001" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):   
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.001\", \"forearm_fk.R.001\", \"hand_fk.R.001\"]", ik_bones="[\"upper_arm_ik.R.001\", \"MCH-forearm_ik.R.001\", \"MCH-upper_arm_ik_target.R.001\"]", ctrl_bones="[\"upper_arm_ik.R.001\", \"upper_arm_ik_target.R.001\", \"hand_ik.R.001\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.001\", \"MCH-forearm_ik.R.001\", \"MCH-upper_arm_ik_target.R.001\"]", output_bones="[\"upper_arm_fk.R.001\", \"forearm_fk.R.001\", \"hand_fk.R.001\"]", ctrl_bones="[\"upper_arm_ik.R.001\", \"upper_arm_ik_target.R.001\", \"hand_ik.R.001\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 002 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.002" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.002\", \"forearm_fk.R.002\", \"hand_fk.R.002\"]", ik_bones="[\"upper_arm_ik.R.002\", \"MCH-forearm_ik.R.002\", \"MCH-upper_arm_ik_target.R.002\"]", ctrl_bones="[\"upper_arm_ik.R.002\", \"upper_arm_ik_target.R.002\", \"hand_ik.R.002\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.002\", \"MCH-forearm_ik.R.002\", \"MCH-upper_arm_ik_target.R.002\"]", output_bones="[\"upper_arm_fk.R.002\", \"forearm_fk.R.002\", \"hand_fk.R.002\"]", ctrl_bones="[\"upper_arm_ik.R.002\", \"upper_arm_ik_target.R.002\", \"hand_ik.R.002\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 003 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.003" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.003\", \"forearm_fk.R.003\", \"hand_fk.R.003\"]", ik_bones="[\"upper_arm_ik.R.003\", \"MCH-forearm_ik.R.003\", \"MCH-upper_arm_ik_target.R.003\"]", ctrl_bones="[\"upper_arm_ik.R.003\", \"upper_arm_ik_target.R.003\", \"hand_ik.R.003\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.003\", \"MCH-forearm_ik.R.003\", \"MCH-upper_arm_ik_target.R.003\"]", output_bones="[\"upper_arm_fk.R.003\", \"forearm_fk.R.003\", \"hand_fk.R.003\"]", ctrl_bones="[\"upper_arm_ik.R.003\", \"upper_arm_ik_target.R.003\", \"hand_ik.R.003\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 004 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.004" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.004\", \"forearm_fk.R.004\", \"hand_fk.R.004\"]", ik_bones="[\"upper_arm_ik.R.004\", \"MCH-forearm_ik.R.004\", \"MCH-upper_arm_ik_target.R.004\"]", ctrl_bones="[\"upper_arm_ik.R.004\", \"upper_arm_ik_target.R.004\", \"hand_ik.R.004\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.004\", \"MCH-forearm_ik.R.004\", \"MCH-upper_arm_ik_target.R.004\"]", output_bones="[\"upper_arm_fk.R.004\", \"forearm_fk.R.004\", \"hand_fk.R.004\"]", ctrl_bones="[\"upper_arm_ik.R.004\", \"upper_arm_ik_target.R.004\", \"hand_ik.R.004\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )


        #------------------------------ 005 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.005" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.005\", \"forearm_fk.R.005\", \"hand_fk.R.005\"]", ik_bones="[\"upper_arm_ik.R.005\", \"MCH-forearm_ik.R.005\", \"MCH-upper_arm_ik_target.R.005\"]", ctrl_bones="[\"upper_arm_ik.R.005\", \"upper_arm_ik_target.R.005\", \"hand_ik.R.005\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.005\", \"MCH-forearm_ik.R.005\", \"MCH-upper_arm_ik_target.R.005\"]", output_bones="[\"upper_arm_fk.R.005\", \"forearm_fk.R.005\", \"hand_fk.R.005\"]", ctrl_bones="[\"upper_arm_ik.R.005\", \"upper_arm_ik_target.R.005\", \"hand_ik.R.005\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 006 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.006" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.006\", \"forearm_fk.R.006\", \"hand_fk.R.006\"]", ik_bones="[\"upper_arm_ik.R.006\", \"MCH-forearm_ik.R.006\", \"MCH-upper_arm_ik_target.R.006\"]", ctrl_bones="[\"upper_arm_ik.R.006\", \"upper_arm_ik_target.R.006\", \"hand_ik.R.006\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.006\", \"MCH-forearm_ik.R.006\", \"MCH-upper_arm_ik_target.R.006\"]", output_bones="[\"upper_arm_fk.R.006\", \"forearm_fk.R.006\", \"hand_fk.R.006\"]", ctrl_bones="[\"upper_arm_ik.R.006\", \"upper_arm_ik_target.R.006\", \"hand_ik.R.006\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 007 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.007" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.007\", \"forearm_fk.R.007\", \"hand_fk.R.007\"]", ik_bones="[\"upper_arm_ik.R.007\", \"MCH-forearm_ik.R.007\", \"MCH-upper_arm_ik_target.R.007\"]", ctrl_bones="[\"upper_arm_ik.R.007\", \"upper_arm_ik_target.R.007\", \"hand_ik.R.007\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.007\", \"MCH-forearm_ik.R.007\", \"MCH-upper_arm_ik_target.R.007\"]", output_bones="[\"upper_arm_fk.R.007\", \"forearm_fk.R.007\", \"hand_fk.R.007\"]", ctrl_bones="[\"upper_arm_ik.R.007\", \"upper_arm_ik_target.R.007\", \"hand_ik.R.007\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 008 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.008" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.008\", \"forearm_fk.R.008\", \"hand_fk.R.008\"]", ik_bones="[\"upper_arm_ik.R.008\", \"MCH-forearm_ik.R.008\", \"MCH-upper_arm_ik_target.R.008\"]", ctrl_bones="[\"upper_arm_ik.R.008\", \"upper_arm_ik_target.R.008\", \"hand_ik.R.008\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.008\", \"MCH-forearm_ik.R.008\", \"MCH-upper_arm_ik_target.R.008\"]", output_bones="[\"upper_arm_fk.R.008\", \"forearm_fk.R.008\", \"hand_fk.R.008\"]", ctrl_bones="[\"upper_arm_ik.R.008\", \"upper_arm_ik_target.R.008\", \"hand_ik.R.008\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 009 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.009" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.009\", \"forearm_fk.R.009\", \"hand_fk.R.009\"]", ik_bones="[\"upper_arm_ik.R.009\", \"MCH-forearm_ik.R.009\", \"MCH-upper_arm_ik_target.R.009\"]", ctrl_bones="[\"upper_arm_ik.R.009\", \"upper_arm_ik_target.R.009\", \"hand_ik.R.009\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.009\", \"MCH-forearm_ik.R.009\", \"MCH-upper_arm_ik_target.R.009\"]", output_bones="[\"upper_arm_fk.R.009\", \"forearm_fk.R.009\", \"hand_fk.R.009\"]", ctrl_bones="[\"upper_arm_ik.R.009\", \"upper_arm_ik_target.R.009\", \"hand_ik.R.009\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 010 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.010" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.010\", \"forearm_fk.R.010\", \"hand_fk.R.010\"]", ik_bones="[\"upper_arm_ik.R.010\", \"MCH-forearm_ik.R.010\", \"MCH-upper_arm_ik_target.R.010\"]", ctrl_bones="[\"upper_arm_ik.R.010\", \"upper_arm_ik_target.R.010\", \"hand_ik.R.010\"]", extra_ctrls="[]")

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.010\", \"MCH-forearm_ik.R.010\", \"MCH-upper_arm_ik_target.R.010\"]", output_bones="[\"upper_arm_fk.R.010\", \"forearm_fk.R.010\", \"hand_fk.R.010\"]", ctrl_bones="[\"upper_arm_ik.R.010\", \"upper_arm_ik_target.R.010\", \"hand_ik.R.010\"]")


                bone["IK_FK"] = float(1)  
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )





        # Select and Insert Keys
        # Right Arm  

        def insert_keys():
            bone.keyframe_insert(data_path = 'location', frame= frame)
            bone.keyframe_insert(data_path = 'scale', frame= frame)
            bone.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)


        for bone in pose_bones:
            if bone.name.startswith('upper_arm_parent') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('upper_arm_fk') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('upper_arm_ik') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys()
                bone.bone.select = 0

            if bone.name.startswith('forearm_fk') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('hand_ik') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys()
                bone.bone.select = 0

            if bone.name.startswith('hand_fk') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            else:
                pass   
           
        
        # Select Right Arm

 
        for bone in pose_bones:
            if bone.name.startswith('upper_arm_fk') and ".R" in bone.name:    
                bone.bone.select = 1                    



        return {'FINISHED'}

 


# =============================================================
#  RIGHT ARM  TO -> IK  
# =============================================================




class OBJECT_OT_right_arm_to_ik_ra(bpy.types.Operator):
    '''RIGHT ARM  TO -> IK'''
    bl_idname = "object.right_arm_to_ik_ra"
    bl_label = "IK"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):



        # Active object
        ob = bpy.context.object

        # Rig Name Variable
        if ob.type == 'ARMATURE':
            ob.name = ob.name



        pose_bones = bpy.context.object.pose.bones

        sel_bones = bpy.data.objects[ob.name].data.bones

        #set the frame
        frame = bpy.context.scene.frame_current

        # Pivot 
        bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'


        # To Auto Keys
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True

        # Deselect All
        bpy.ops.pose.select_all(action = 'DESELECT')


        rig = bpy.data.objects[ob.name]

        # Variable for rig_ID
        rig_id = rig.data['rig_id'] 


        # Variables for IK FK switch ops
        arm_ik2fk = eval('bpy.ops.pose.rigify_limb_ik2fk_' + rig_id)
        arm_fk2ik = eval('bpy.ops.pose.rigify_generic_snap_' + rig_id)


        
# =============================================================
#  TOGGLE
# =============================================================



        for bone in pose_bones: 
                                    
            # Arms To FK  
            if bone.name.startswith('upper_arm_parent') and ".R" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                   
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R\", \"forearm_fk.R\", \"hand_fk.R\"]", ik_bones="[\"upper_arm_ik.R\", \"MCH-forearm_ik.R\", \"MCH-upper_arm_ik_target.R\"]", ctrl_bones="[\"upper_arm_ik.R\", \"upper_arm_ik_target.R\", \"hand_ik.R\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R\", \"MCH-forearm_ik.R\", \"MCH-upper_arm_ik_target.R\"]", output_bones="[\"upper_arm_fk.R\", \"forearm_fk.R\", \"hand_fk.R\"]", ctrl_bones="[\"upper_arm_ik.R\", \"upper_arm_ik_target.R\", \"hand_ik.R\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 001 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.001" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.001\", \"forearm_fk.R.001\", \"hand_fk.R.001\"]", ik_bones="[\"upper_arm_ik.R.001\", \"MCH-forearm_ik.R.001\", \"MCH-upper_arm_ik_target.R.001\"]", ctrl_bones="[\"upper_arm_ik.R.001\", \"upper_arm_ik_target.R.001\", \"hand_ik.R.001\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.001\", \"MCH-forearm_ik.R.001\", \"MCH-upper_arm_ik_target.R.001\"]", output_bones="[\"upper_arm_fk.R.001\", \"forearm_fk.R.001\", \"hand_fk.R.001\"]", ctrl_bones="[\"upper_arm_ik.R.001\", \"upper_arm_ik_target.R.001\", \"hand_ik.R.001\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 002 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.002" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.002\", \"forearm_fk.R.002\", \"hand_fk.R.002\"]", ik_bones="[\"upper_arm_ik.R.002\", \"MCH-forearm_ik.R.002\", \"MCH-upper_arm_ik_target.R.002\"]", ctrl_bones="[\"upper_arm_ik.R.002\", \"upper_arm_ik_target.R.002\", \"hand_ik.R.002\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.002\", \"MCH-forearm_ik.R.002\", \"MCH-upper_arm_ik_target.R.002\"]", output_bones="[\"upper_arm_fk.R.002\", \"forearm_fk.R.002\", \"hand_fk.R.002\"]", ctrl_bones="[\"upper_arm_ik.R.002\", \"upper_arm_ik_target.R.002\", \"hand_ik.R.002\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 003 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.003" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.003\", \"forearm_fk.R.003\", \"hand_fk.R.003\"]", ik_bones="[\"upper_arm_ik.R.003\", \"MCH-forearm_ik.R.003\", \"MCH-upper_arm_ik_target.R.003\"]", ctrl_bones="[\"upper_arm_ik.R.003\", \"upper_arm_ik_target.R.003\", \"hand_ik.R.003\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.003\", \"MCH-forearm_ik.R.003\", \"MCH-upper_arm_ik_target.R.003\"]", output_bones="[\"upper_arm_fk.R.003\", \"forearm_fk.R.003\", \"hand_fk.R.003\"]", ctrl_bones="[\"upper_arm_ik.R.003\", \"upper_arm_ik_target.R.003\", \"hand_ik.R.003\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 004 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.004" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.004\", \"forearm_fk.R.004\", \"hand_fk.R.004\"]", ik_bones="[\"upper_arm_ik.R.004\", \"MCH-forearm_ik.R.004\", \"MCH-upper_arm_ik_target.R.004\"]", ctrl_bones="[\"upper_arm_ik.R.004\", \"upper_arm_ik_target.R.004\", \"hand_ik.R.004\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.004\", \"MCH-forearm_ik.R.004\", \"MCH-upper_arm_ik_target.R.004\"]", output_bones="[\"upper_arm_fk.R.004\", \"forearm_fk.R.004\", \"hand_fk.R.004\"]", ctrl_bones="[\"upper_arm_ik.R.004\", \"upper_arm_ik_target.R.004\", \"hand_ik.R.004\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 005 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.005" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.005\", \"forearm_fk.R.005\", \"hand_fk.R.005\"]", ik_bones="[\"upper_arm_ik.R.005\", \"MCH-forearm_ik.R.005\", \"MCH-upper_arm_ik_target.R.005\"]", ctrl_bones="[\"upper_arm_ik.R.005\", \"upper_arm_ik_target.R.005\", \"hand_ik.R.005\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.005\", \"MCH-forearm_ik.R.005\", \"MCH-upper_arm_ik_target.R.005\"]", output_bones="[\"upper_arm_fk.R.005\", \"forearm_fk.R.005\", \"hand_fk.R.005\"]", ctrl_bones="[\"upper_arm_ik.R.005\", \"upper_arm_ik_target.R.005\", \"hand_ik.R.005\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 006 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.006" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.006\", \"forearm_fk.R.006\", \"hand_fk.R.006\"]", ik_bones="[\"upper_arm_ik.R.006\", \"MCH-forearm_ik.R.006\", \"MCH-upper_arm_ik_target.R.006\"]", ctrl_bones="[\"upper_arm_ik.R.006\", \"upper_arm_ik_target.R.006\", \"hand_ik.R.006\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.006\", \"MCH-forearm_ik.R.006\", \"MCH-upper_arm_ik_target.R.006\"]", output_bones="[\"upper_arm_fk.R.006\", \"forearm_fk.R.006\", \"hand_fk.R.006\"]", ctrl_bones="[\"upper_arm_ik.R.006\", \"upper_arm_ik_target.R.006\", \"hand_ik.R.006\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 007 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.007" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.007\", \"forearm_fk.R.007\", \"hand_fk.R.007\"]", ik_bones="[\"upper_arm_ik.R.007\", \"MCH-forearm_ik.R.007\", \"MCH-upper_arm_ik_target.R.007\"]", ctrl_bones="[\"upper_arm_ik.R.007\", \"upper_arm_ik_target.R.007\", \"hand_ik.R.007\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.007\", \"MCH-forearm_ik.R.007\", \"MCH-upper_arm_ik_target.R.007\"]", output_bones="[\"upper_arm_fk.R.007\", \"forearm_fk.R.007\", \"hand_fk.R.007\"]", ctrl_bones="[\"upper_arm_ik.R.007\", \"upper_arm_ik_target.R.007\", \"hand_ik.R.007\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 008 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.008" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.008\", \"forearm_fk.R.008\", \"hand_fk.R.008\"]", ik_bones="[\"upper_arm_ik.R.008\", \"MCH-forearm_ik.R.008\", \"MCH-upper_arm_ik_target.R.008\"]", ctrl_bones="[\"upper_arm_ik.R.008\", \"upper_arm_ik_target.R.008\", \"hand_ik.R.008\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.008\", \"MCH-forearm_ik.R.008\", \"MCH-upper_arm_ik_target.R.008\"]", output_bones="[\"upper_arm_fk.R.008\", \"forearm_fk.R.008\", \"hand_fk.R.008\"]", ctrl_bones="[\"upper_arm_ik.R.008\", \"upper_arm_ik_target.R.008\", \"hand_ik.R.008\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 009 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.009" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.009\", \"forearm_fk.R.009\", \"hand_fk.R.009\"]", ik_bones="[\"upper_arm_ik.R.009\", \"MCH-forearm_ik.R.009\", \"MCH-upper_arm_ik_target.R.009\"]", ctrl_bones="[\"upper_arm_ik.R.009\", \"upper_arm_ik_target.R.009\", \"hand_ik.R.009\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.009\", \"MCH-forearm_ik.R.009\", \"MCH-upper_arm_ik_target.R.009\"]", output_bones="[\"upper_arm_fk.R.009\", \"forearm_fk.R.009\", \"hand_fk.R.009\"]", ctrl_bones="[\"upper_arm_ik.R.009\", \"upper_arm_ik_target.R.009\", \"hand_ik.R.009\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



        #------------------------------ 010 -----------------------
                                           
            if bone.name.startswith('upper_arm_parent') and ".R.010" in bone.name:
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )
                
                if bone["IK_FK"] == float(1):
                    arm_ik2fk(prop_bone=bone.name, fk_bones="[\"upper_arm_fk.R.010\", \"forearm_fk.R.010\", \"hand_fk.R.010\"]", ik_bones="[\"upper_arm_ik.R.010\", \"MCH-forearm_ik.R.010\", \"MCH-upper_arm_ik_target.R.010\"]", ctrl_bones="[\"upper_arm_ik.R.010\", \"upper_arm_ik_target.R.010\", \"hand_ik.R.010\"]", extra_ctrls="[]")
                    

                if bone["IK_FK"] == float(0):
                    arm_fk2ik(input_bones="[\"upper_arm_ik.R.010\", \"MCH-forearm_ik.R.010\", \"MCH-upper_arm_ik_target.R.010\"]", output_bones="[\"upper_arm_fk.R.010\", \"forearm_fk.R.010\", \"hand_fk.R.010\"]", ctrl_bones="[\"upper_arm_ik.R.010\", \"upper_arm_ik_target.R.010\", \"hand_ik.R.010\"]")


                bone["IK_FK"] = float(0)
                bone.keyframe_insert(data_path= '["IK_FK"]' , frame= frame )



         


        # Select and Insert Keys
        # Right Arm  

        def insert_keys():
            bone.keyframe_insert(data_path = 'location', frame= frame)
            bone.keyframe_insert(data_path = 'scale', frame= frame)
            bone.keyframe_insert(data_path = 'rotation_quaternion', frame= frame)


        for bone in pose_bones:
            if bone.name.startswith('upper_arm_parent') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('upper_arm_fk') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('upper_arm_ik') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys()
                bone.bone.select = 0

            if bone.name.startswith('forearm_fk') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            if bone.name.startswith('hand_ik') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys()
                bone.bone.select = 0

            if bone.name.startswith('hand_fk') and ".R" in bone.name: 
                bone.bone.select = 1
                insert_keys() 
                bone.bone.select = 0

            else:
                pass   
           

        # Select Right Arm

 
        for bone in pose_bones:
            if bone.name.startswith('hand_ik') and ".R" in bone.name:    
                bone.bone.select = 1                    


        return {'FINISHED'}
    
 
 





# =============================================================
#  SELECT  ARMS   -FK IK- CONTROLS  
# =============================================================
 


# Select ALL FK/IK Controls of Left Arm to Adjust Keys Timeline Position
class OBJECT_OT_select_left_arm_fk_ik_ctrls_ra(bpy.types.Operator):
    '''SELECT LEFT ARM IK_FK Controls '''
    bl_idname = "object.select_left_arm_fk_ik_ctrls_ra"
    bl_label = "Sel LA"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):


        pose_bones = bpy.context.object.pose.bones


        #  Left Arm Bones List
  
        for bone in pose_bones:
            if bone.name.startswith('upper_arm_parent') and ".L" in bone.name: 
                bone.bone.select = 1

            if bone.name.startswith('upper_arm_fk') and ".L" in bone.name: 
                bone.bone.select = 1

            if bone.name.startswith('upper_arm_ik') and ".L" in bone.name: 
                bone.bone.select = 1

            if bone.name.startswith('forearm_fk') and ".L" in bone.name: 
                bone.bone.select = 1

            if bone.name.startswith('hand_ik') and ".L" in bone.name: 
                bone.bone.select = 1

            if bone.name.startswith('hand_fk') and ".L" in bone.name: 
                bone.bone.select = 1

            else:
                pass   
   


        return {'FINISHED'}

 




# Select ALL FK/IK Controls of Right Arm to Adjust Keys Timeline Position
class OBJECT_OT_select_right_arm_fk_ik_ctrls_ra(bpy.types.Operator):
    '''SELECT RIGHT ARM IK_FK Controls '''
    bl_idname = "object.select_right_arm_fk_ik_ctrls_ra"
    bl_label = "Sel RA"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None and
                  context.object.mode == 'POSE')


    def execute(self, context):


        pose_bones = bpy.context.object.pose.bones

  
        for bone in pose_bones:
            if bone.name.startswith('upper_arm_parent') and ".R" in bone.name: 
                bone.bone.select = 1

            if bone.name.startswith('upper_arm_fk') and ".R" in bone.name: 
                bone.bone.select = 1

            if bone.name.startswith('upper_arm_ik') and ".R" in bone.name: 
                bone.bone.select = 1

            if bone.name.startswith('forearm_fk') and ".R" in bone.name: 
                bone.bone.select = 1

            if bone.name.startswith('hand_ik') and ".R" in bone.name: 
                bone.bone.select = 1

            if bone.name.startswith('hand_fk') and ".R" in bone.name: 
                bone.bone.select = 1

            else:
                pass   
 

        return {'FINISHED'}


# =============================================================
# END  SELECT  ARMS   -FK IK- CONTROLS  
# =============================================================





classes = [
            OBJECT_OT_left_arm_to_fk_ra, OBJECT_OT_left_arm_to_ik_ra,
            OBJECT_OT_right_arm_to_fk_ra, OBJECT_OT_right_arm_to_ik_ra,
            OBJECT_OT_select_left_arm_fk_ik_ctrls_ra, OBJECT_OT_select_right_arm_fk_ik_ctrls_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()





 
