import bpy





# Eyes Setup 
class OBJECT_OT_eye_control_setup_ra(bpy.types.Operator):
    '''Eye Control Setup'''
    bl_idname = "object.eye_control_setup_ra"
    bl_label = "Eye Control Setup"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    def poll(cls, context):
        return (context.object is not None 
        and len(context.selected_objects) != 0
        and context.object.type == 'MESH' 
        and context.object.mode == 'OBJECT')

    def execute(self, context):
        


        # Control Curve rename
        for o in bpy.data.objects:
            if o.type == 'CURVE' and o.name == 'Eye Ctrl':
                o.name = 'Eye Ctrl_new'

        # Control Curve rename
        for o in bpy.data.objects:
            if o.type == 'CURVE' and  o.name == 'Eye Main Ctrl':
                o.name = 'Eye Main Ctrl_new'

 
        
 
        # Rename Existing Armature with name 'Armature' - objects
        for arm in bpy.data.armatures:
            if arm.name.startswith('Armature'):
                arm.name = 'Armature to rename'    
    

        # Rename Existing Armature with name 'Armature' - armatures
        for arm in bpy.data.objects:
            if arm.type == 'ARMATURE' and arm.name.startswith('Armature'):
                arm.name = 'Armature to rename'    
        


        # Rename  Existing Armature with name 'Eyes Setup Armature' - objects
        for arm in bpy.data.objects:
            if arm.type == 'ARMATURE' and arm.name.startswith('Eyes Setup Armature'):  
                arm.name = 'Eyes Setup Armature_new'    
        

        # Rename  Existing Armature with name 'Eyes Setup Armature' - armatures
        for arm in bpy.data.armatures:
            if arm.name == 'Eyes Setup Armature':
                arm.name =  'Eyes Setup Armature_new'

        



        sel_ob = bpy.context.selected_objects
        act_ob = bpy.context.active_object
        cursor_location = bpy.context.scene.cursor.location

        # Get Selected Object Dimension 'y' 
        for o in sel_ob:    
            obj_dimentions_y = o.dimensions.y
            
          

        
#========= Define Name by Cursor Position ============
                   
        def curs_pos_name():
            act_ob = bpy.context.active_object
            if cursor_location.x > 0:
                act_ob.name = 'Eye Left GEO'
            if cursor_location.x < 0:
                act_ob.name = 'Eye Right GEO'
                      
#========= Define Name by Cursor Position ============
        
        
           


#===================================================
#============== Check if Mirror Modifier ===========

        # Check If object has 'Mirror' Modifier
        def obj_has_modifiers():
            for o in sel_ob:
                for n in o.modifiers:            
                    if n.name == 'Mirror':
                        return True
                    
        obj_has_modifiers()


        # If Object has 'Mirror' Modifier
        if obj_has_modifiers():
                   
            # Apply 'Mirror' Modifier
            bpy.ops.object.modifier_apply(modifier='Mirror')

            bpy.ops.mesh.separate(type='LOOSE')                    
                
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
                 
                 
            sel_ob = bpy.context.selected_objects
                 
            # Cursor to Active / func call
            bpy.ops.view3d.snap_cursor_to_active()
            curs_pos_name()


            # Switch active and selected
            sel_obj = bpy.context.selected_objects
            act_obj = bpy.context.view_layer.objects

            if act_obj.active == sel_obj[0]:
                act_obj.active = sel_obj[-1]

            elif act_obj.active == sel_obj[-1]:
                act_obj.active = sel_obj[0]
                
            # Cursor to Active / func call
            bpy.ops.view3d.snap_cursor_to_active()
            curs_pos_name()
        




#==================================================        
#=============== IF 1 SELECTED OBJECT ===============
   

        if len(sel_ob) == 1:
                
            # Separate Mesh
            bpy.ops.mesh.separate(type='LOOSE')
  
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
                
                
    #========== If 2 selected Object after separation ========= 
        
            sel_ob = bpy.context.selected_objects
            if len(sel_ob) == 2:
                    

                # Cursor to Active / func call
                bpy.ops.view3d.snap_cursor_to_active()
                curs_pos_name()
                

                # Switch active and selected
                sel_obj = bpy.context.selected_objects
                act_obj = bpy.context.view_layer.objects

                if act_obj.active == sel_obj[0]:
                    act_obj.active = sel_obj[-1]

                elif act_obj.active == sel_obj[-1]:
                    act_obj.active = sel_obj[0]
                    
                # Cursor to Active / func call
                bpy.ops.view3d.snap_cursor_to_active()
                curs_pos_name()
                
                
            
    #========== If 1 selected Object after separation ========= 
        
            sel_ob = bpy.context.selected_objects
            if len(sel_ob) == 1:
                

                bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
     
                bpy.context.object.modifiers.new('Mirror', 'MIRROR')

                # Apply 'Mirror' Modifier
                bpy.ops.object.modifier_apply(modifier='Mirror')

                bpy.ops.mesh.separate(type='LOOSE')                    
                    
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
                     
                     
                sel_ob = bpy.context.selected_objects
                     
                # Cursor to Active / func call
                bpy.ops.view3d.snap_cursor_to_active()
                curs_pos_name()


                # Switch active and selected
                sel_obj = bpy.context.selected_objects
                act_obj = bpy.context.view_layer.objects

                if act_obj.active == sel_obj[0]:
                    act_obj.active = sel_obj[-1]

                elif act_obj.active == sel_obj[-1]:
                    act_obj.active = sel_obj[0]
                    
                # Cursor to Active / func call
                bpy.ops.view3d.snap_cursor_to_active()
                curs_pos_name()
            

#===================================================

#=============== IF 2 SELECTED OBJECTS =============== 
        
   
        if len(sel_ob) == 2:
            # Origing to GEO
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
                       
            # Cursor to Active / func call
            bpy.ops.view3d.snap_cursor_to_active()
            curs_pos_name()
            
            
            # Switch active and selected
            sel_obj = bpy.context.selected_objects
            act_obj = bpy.context.view_layer.objects

            if act_obj.active == sel_obj[0]:
                act_obj.active = sel_obj[-1]

            elif act_obj.active == sel_obj[-1]:
                act_obj.active = sel_obj[0]
                
            # Cursor to Active / func call
            bpy.ops.view3d.snap_cursor_to_active()
            curs_pos_name()
        
                            



#=============================================
        def select_eye_left():
            
            eye_L = bpy.data.objects['Eye Left GEO']
            eye_L.select_set(1) 
            bpy.context.view_layer.objects.active = eye_L 
             
            # Cursor to Active   
            bpy.ops.view3d.snap_cursor_to_active()   



#=============================================

#=============================================

#============ EYES ARMATURE ==================







# Collection for Eye Armature

        # Create New Collection for Eye Setup
        def add_new_collection(name):
            # Create New collection
            new_collection = bpy.data.collections.new(name)
            bpy.context.scene.collection.children.link(new_collection)
            # Set Color to Collection
            new_collection.color_tag =  'COLOR_05'

            # Set active 'Scene Collection' to some user Collection
            scene_collection = bpy.context.view_layer.layer_collection.children[name]
            bpy.context.view_layer.active_layer_collection = scene_collection


        add_new_collection('Eye Setup') 
         







        # CONSTRUCT EYES ARMATURE

        def add_eyes_armature():
                  

            # func call - select left eye
            select_eye_left()

            # Cursor  Location
            cursor_location = bpy.context.scene.cursor.location
            bpy.context.scene.cursor.rotation_euler[0] = 1.5708

            # Add Bone (Armature) 
            bpy.ops.object.armature_add(enter_editmode=1, align='CURSOR', location=(cursor_location), scale=(1, 1, 1)) 
            ob = bpy.context.object
            ob.name = 'Armature'
            ob.data.name = 'Armature'

            # Armature Name
            ob = bpy.context.object
 
            for arm in bpy.data.armatures:
                if arm.name == 'Armature':
                    arm.name = 'Eyes Setup Armature'
                    
            if ob.type == 'ARMATURE' and ob.name == 'Armature':
                ob.name = 'Eyes Setup Armature'    
               
       
            bpy.ops.armature.select_all(action='SELECT')

       
            for b in bpy.context.selected_bones:
                b.name = 'eye_L'
                # Set Bone 'size' = dimension 'y' of selected obj  
                b.tail[2] = obj_dimentions_y
                

            cursor_location.y = -obj_dimentions_y * 7
    
            bpy.ops.armature.bone_primitive_add(name='Ctrl_eye_L')
            

            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            
            # Set to "not deform"
            bpy.context.object.data.bones["eye_L"].use_deform = False
            bpy.context.object.data.bones["Ctrl_eye_L"].use_deform = False


            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            
            bpy.ops.armature.select_all(action='SELECT')
                    
            bpy.ops.armature.symmetrize()
            
            bpy.ops.armature.select_all(action='DESELECT')
    
    

            # Create Main Control 
            
            for a in bpy.data.armatures:
                for b in a.edit_bones:
                    if b.name == 'Ctrl_eye_L':
                        b.select_head = 1 
                                             
                    if b.name == 'Ctrl_eye_R':
                        b.select_head = 1             
       
  
            bpy.ops.view3d.snap_cursor_to_selected()
            bpy.ops.armature.bone_primitive_add(name='Main_eye_Ctrl')
            
             
             
            # Create "Head Parent"
                                      
            for a in bpy.data.armatures:
                for b in a.edit_bones:
                    if b.name == 'eye_L':
                        b.select_head = 1 
                                             
                    if b.name == 'eye_R':
                        b.select_head = 1          
                           
       
            bpy.ops.view3d.snap_cursor_to_selected()
                   
    
            # Adjust Cursor Position
            for a in bpy.data.armatures:
                for b in a.edit_bones:
                    if b.name == 'eye_L':
                        Bone_lenght = b.length
                    
            
            bpy.ops.armature.bone_primitive_add(name='Parent_to_Head_eye_Ctrl')
                            
       
            # Set Parent
            arm = bpy.data.armatures['Eyes Setup Armature']
            arm.edit_bones['Ctrl_eye_L'].parent = arm.edit_bones['Main_eye_Ctrl']
            arm.edit_bones['Ctrl_eye_R'].parent = arm.edit_bones['Main_eye_Ctrl']
                             
            arm.edit_bones['Main_eye_Ctrl'].parent = arm.edit_bones['Parent_to_Head_eye_Ctrl']
            arm.edit_bones['eye_L'].parent = arm.edit_bones['Parent_to_Head_eye_Ctrl']
            arm.edit_bones['eye_R'].parent = arm.edit_bones['Parent_to_Head_eye_Ctrl']
            


            # Adjust Bone Lenght  
            for a in bpy.data.armatures:
                for b in a.edit_bones:
                    if b.name == 'eye_L':
                        Bone_lenght = b.length
                        
                    if b.name == 'Ctrl_eye_L':
                        b.length = Bone_lenght - (Bone_lenght / 2)
      
                    if b.name == 'Ctrl_eye_R':
                        b.length = Bone_lenght - (Bone_lenght / 2)     
                        
                    if b.name == 'Main_eye_Ctrl':
                        b.length = Bone_lenght - (Bone_lenght / 4) 
                        
            
                    if b.name == 'Parent_to_Head_eye_Ctrl':
                        b.length = Bone_lenght + (Bone_lenght / 4) 
                        
                        

            # Snap 'Parent to Head' to eye bone
            # Select Eyes bones
            bpy.data.armatures['Eyes Setup Armature'].edit_bones['eye_L'].select_head = 1          
            bpy.data.armatures['Eyes Setup Armature'].edit_bones['eye_R'].select_head = 1          
                                      
            bpy.ops.view3d.snap_cursor_to_selected()
            bpy.context.scene.cursor.location[1] += (Bone_lenght * 1.5)
                  
            
            bpy.ops.armature.select_all(action='DESELECT')
            
            # Select Parent Bone
            bpy.data.armatures['Eyes Setup Armature'].edit_bones['Parent_to_Head_eye_Ctrl'].select = 1          
            bpy.data.armatures['Eyes Setup Armature'].edit_bones['Parent_to_Head_eye_Ctrl'].select_head = 1          
            bpy.data.armatures['Eyes Setup Armature'].edit_bones['Parent_to_Head_eye_Ctrl'].select_tail = 1          
 

            bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
            

            bpy.ops.armature.select_all(action='DESELECT')

            
     
            bpy.ops.view3d.snap_cursor_to_center()
            bpy.context.scene.cursor.rotation_euler[0] = 0
            
            
            bpy.ops.object.posemode_toggle()

            def add_damped_track(b_name, sub_name, const_name):
                pose_bones = bpy.context.object.pose.bones
                
                arm = bpy.data.objects['Eyes Setup Armature']
                p_bone = pose_bones[b_name]
                p_bone.bone.select = 1

                bc = p_bone.constraints.new(type='DAMPED_TRACK')
                
                bc.target = arm
                bc.subtarget = sub_name
                bc.name = const_name
                
             
            add_damped_track('eye_L', 'Ctrl_eye_L', 'eye_track_L') 
            add_damped_track('eye_R', 'Ctrl_eye_R', 'eye_track_R') 

                   

        add_eyes_armature()
        
           
                
#=================================================
#=================================================
#=================================================
#=================================================


        # PARENT EYES TO BONE       

        def parent_eye_bone(sel_mesh, object, armature, bone, act_bone):
            
            
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
     
            bpy.ops.object.select_all(action='DESELECT')
          
            for o in bpy.context.scene.objects:
                if o.type == 'MESH' and o.name.startswith(sel_mesh):
                    o.select_set(True)
                else:
                    o.select_set(False)


            bpy.ops.object.posemode_toggle()  
            
            bpy.data.objects[object].select_set(True)           
            bpy.data.objects[armature].select_set(True)
            
            
            bpy.ops.pose.select_all(action='DESELECT')
            
            pose_bones = bpy.context.object.pose.bones

            for bone in pose_bones:
                if bone.name == bone:
                    bone.bone.select = 1

            b_name = act_bone 

            bone_act = bpy.data.armatures['Eyes Setup Armature']
              
            bone_act.bones.active = bpy.data.armatures['Eyes Setup Armature'].bones[b_name]

            bpy.ops.object.parent_set(type='BONE')

            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            
            bpy.ops.object.select_all(action='DESELECT')
          

        # Func Call
        parent_eye_bone('Eye Left GEO', 'Eye Left GEO', 'Eyes Setup Armature', 'eye_L', 'eye_L')
                    
        # Func Call
        parent_eye_bone('Eye Right GEO', 'Eye Right GEO', 'Eyes Setup Armature', 'eye_R', 'eye_R')
                              
        

#=================================================
#=================================================





################# Create Eye Curve Controls ########



        ####### Remove Curves ################

        # Remove "Eye  Ctrl"
        for o in bpy.context.scene.objects:
            if o.type == 'CURVE' and  o.name == 'Eye Ctrl':
                bpy.data.objects.remove(o)



        # Remove "Eye Main Ctrl"
        for o in bpy.context.scene.objects:
            if o.type == 'CURVE' and  o.name == 'Eye Main Ctrl':
                bpy.data.objects.remove(o)

        ####### Remove Curves ################




        current_mode = bpy.context.mode
        if current_mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')




        bpy.ops.object.select_all(action='DESELECT')



        ############# Eye Main Ctrl ################



        # create the Curve Datablock
        curveData = bpy.data.curves.new('eye_main_ctrl', type='CURVE')
        curveData.dimensions = '3D'
        curveData.resolution_u = 12

        # map coords to spline
        polyline = curveData.splines.new('BEZIER')
        polyline.bezier_points.add(7)




        # Points
        polyline.bezier_points[0].co =  ((0.7476, 0.0000, 0.0000))
        polyline.bezier_points[0].handle_left =  ((0.7476, -0.1071, -0.0000))
        polyline.bezier_points[0].handle_right =  ((0.7476, 0.1071, 0.0000))

        polyline.bezier_points[1].co =  ((0.5122, 0.3252, 0.1205))
        polyline.bezier_points[1].handle_left =  ((0.6433, 0.2420, 0.0353))
        polyline.bezier_points[1].handle_right =  ((0.3811, 0.4085, 0.2057))

        polyline.bezier_points[2].co =  ((-0.0000, 0.2589, 0.4000))
        polyline.bezier_points[2].handle_left =  ((0.2748, 0.2589, 0.4000))
        polyline.bezier_points[2].handle_right =  ((-0.2748, 0.2589, 0.4000))

        polyline.bezier_points[3].co =  ((-0.5122, 0.3252, 0.1205))
        polyline.bezier_points[3].handle_left =  ((-0.3811, 0.4085, 0.2057))
        polyline.bezier_points[3].handle_right =  ((-0.6433, 0.2420, 0.0353))

        polyline.bezier_points[4].co =  ((-0.7476, -0.0000, -0.0000))
        polyline.bezier_points[4].handle_left =  ((-0.7476, 0.1071, 0.0000))
        polyline.bezier_points[4].handle_right =  ((-0.7476, -0.1071, -0.0000))

        polyline.bezier_points[5].co =  ((-0.5122, -0.3252, 0.1205))
        polyline.bezier_points[5].handle_left =  ((-0.6433, -0.2420, 0.0353))
        polyline.bezier_points[5].handle_right =  ((-0.3811, -0.4085, 0.2057))

        polyline.bezier_points[6].co =  ((-0.0000, -0.2589, 0.4000))
        polyline.bezier_points[6].handle_left =  ((-0.2748, -0.2589, 0.4000))
        polyline.bezier_points[6].handle_right =  ((0.2748, -0.2589, 0.4000))

        polyline.bezier_points[7].co =  ((0.5122, -0.3252, 0.1205))
        polyline.bezier_points[7].handle_left =  ((0.3811, -0.4085, 0.2057))
        polyline.bezier_points[7].handle_right =  ((0.6433, -0.2420, 0.0353))



        # create Object
        curveOB = bpy.data.objects.new('Eye Main Ctrl', curveData)

        # Set active 'Scene Collection' to 'Eye Setup'
        scene_collection = bpy.context.view_layer.layer_collection.children['Eye Setup']
        bpy.context.view_layer.active_layer_collection = scene_collection


        # attach to scene and validate context
        scene_collection.collection.objects.link(curveOB)
        bpy.context.view_layer.objects.active = curveOB
        curveOB.select_set(1)


        for obj in bpy.context.selected_objects:
            if obj.type == 'CURVE':
                for s in obj.data.splines:
                    s.use_cyclic_u = True






        ############# Eye Ctrl ################



        # create the Curve Datablock
        curveData = bpy.data.curves.new('eye_ctrl', type='CURVE')
        curveData.dimensions = '3D'
        curveData.resolution_u = 12

        # map coords to spline
        polyline = curveData.splines.new('BEZIER')
        polyline.bezier_points.add(1)



        # Points
        polyline.bezier_points[0].co =  ((-0.7445, 0.0000, 0.0000))
        polyline.bezier_points[0].handle_left =  ((-0.2211, -0.5820, 0.0000))
        polyline.bezier_points[0].handle_right =  ((-0.2211, 0.5820, 0.0000))

        polyline.bezier_points[1].co =  ((0.7521, 0.0000, 0.0000))
        polyline.bezier_points[1].handle_left =  ((0.2720, 0.4446, 0.0000))
        polyline.bezier_points[1].handle_right =  ((0.2720, -0.4446, 0.0000))



        # create Object
        curveOB = bpy.data.objects.new('Eye Ctrl', curveData)

        # Set active 'Scene Collection' to 'Eye Setup'
        scene_collection = bpy.context.view_layer.layer_collection.children['Eye Setup']
        bpy.context.view_layer.active_layer_collection = scene_collection


        # attach to scene and validate context
        scene_collection.collection.objects.link(curveOB)
        bpy.context.view_layer.objects.active = curveOB
        curveOB.select_set(1)

        for obj in bpy.context.selected_objects:
            if obj.type == 'CURVE':
                for s in obj.data.splines:
                    s.use_cyclic_u = True





        ########## Add / Remove Modifiers #############
        # ==============================================


        # Remove Modifier
        scene = bpy.context.scene
        for o in scene.objects:
            if o.type == 'CURVE' and o.name == 'Eye Ctrl':
                bpy.context.view_layer.objects.active = o
                bpy.ops.object.modifier_remove(modifier="Triangulate")
                

        # Remove Modifier
        scene = bpy.context.scene
        for o in scene.objects:
            if o.type == 'CURVE' and  o.name == 'Eye Main Ctrl':
                bpy.context.view_layer.objects.active = o
                bpy.ops.object.modifier_remove(modifier="Triangulate")
                

                 
         
        # Add Modifier
        for o in bpy.data.objects:
            if o.name == 'Eye Ctrl':
                modifier = o.modifiers.new(name="Triangulate", type='TRIANGULATE')

                # Hide in viewport
                o.hide_viewport = 1
                


        # Add Modifier
        for o in bpy.data.objects:
            if o.name == 'Eye Main Ctrl':
                modifier = o.modifiers.new(name="Triangulate", type='TRIANGULATE')

                # Hide in viewport
                o.hide_viewport = 1
                


        for o in bpy.data.objects:
            if o.name == "Eyes Setup Armature":
                o.select_set(1)
                bpy.context.view_layer.objects.active = o

 

##################################################
#            Add Eye Control Group / Color


        def bone_group_color(arm, act_bone, bone, bone_group, num, color):
            
            current_mode = bpy.context.mode
            
            if current_mode != 'POSE':
                bpy.ops.object.posemode_toggle()    
            
            bpy.ops.pose.select_all(action='DESELECT')

            pose_bones = bpy.context.object.pose.bones    
            
            for b in pose_bones:
                if b.name == bone:
                    b.bone.select = 1
                    bpy.context.object.data.bones.active = b.bone
                 

            bpy.ops.pose.group_add()

            bpy.ops.pose.group_assign(type=num)

            bpy.data.objects[arm].pose.bones[bone].bone_group.name = bone_group

            bpy.data.objects[arm].pose.bones[bone].bone_group.color_set  = color




        bone_group_color('Eyes Setup Armature', 

                        'Ctrl_eye_L', 'Ctrl_eye_L', 
                        
                        'Ctrl_eye_L_Gr',
                        
                        1,
                        
                        'THEME04')

        bone_group_color('Eyes Setup Armature', 

                        'Ctrl_eye_R', 'Ctrl_eye_R', 
                        
                        'Ctrl_eye_R_Gr',
                        
                        2,
                        
                        'THEME03')




        bone_group_color('Eyes Setup Armature', 

                        'Main_eye_Ctrl', 'Main_eye_Ctrl', 
                        
                        'MainEyeCtrl_Gr',
                        
                        3,
                        
                        'THEME02')



################## Custom Shape ####################

        def custom_bone_shape( bone, shape, num):


            bpy.context.object.pose.bones[bone].custom_shape = bpy.data.objects[shape]
            bpy.context.object.pose.bones[bone].use_custom_shape_bone_size = False
            
            b_length = bpy.context.object.pose.bones[bone].bone.length

            # Check Blender Version
            blender_version = bpy.app.version[0]
            if blender_version == 2:
                bpy.context.object.pose.bones[bone].custom_shape_scale = b_length * num

            if blender_version == 3:

                bpy.context.object.pose.bones[bone].custom_shape_scale_xyz.x = b_length * num
                bpy.context.object.pose.bones[bone].custom_shape_scale_xyz.y = b_length * num
                bpy.context.object.pose.bones[bone].custom_shape_scale_xyz.z = b_length * num

            
        custom_bone_shape( 'Main_eye_Ctrl', 'Eye Main Ctrl', 3)    
        custom_bone_shape( 'Ctrl_eye_L', 'Eye Ctrl', 1.2)    
        custom_bone_shape( 'Ctrl_eye_R', 'Eye Ctrl', 1.2)    

 

################ Change Bone Layer #####################
 
        # Change bone layer for Eye Bone
        def bone_layer(bone):
            
            p_bone = bpy.context.object.data.bones[bone]

            p_bone.layers = [False, True,  False,  False,  
                             False, False, False, False, 
                             False, False, False, False, 
                             False, False, False, False, 
                             False, False, False, False, 
                             False, False, False, False, 
                             False, False, False, False, 
                             False, False, False, False]        

        bone_layer('eye_L')
        bone_layer('eye_R')
 


  
        # Change bone layer for 'Parent_to_Head_eye_Ctrl' ( Layer 2 )
        def bone_layer(bone):
            
            p_bone = bpy.context.object.data.bones[bone]

            p_bone.layers = [False, False,  True,  False,  
                             False, False, False, False, 
                             False, False, False, False, 
                             False, False, False, False, 
                             False, False, False, False, 
                             False, False, False, False, 
                             False, False, False, False, 
                             False, False, False, False]   
            
            # Select layer with bone
            bpy.context.object.data.layers[2] = True

        bone_layer('Parent_to_Head_eye_Ctrl')

 
 
 
################################################
        # Remove 'Eye Setup Collection'
        def remove_collection(name):

            for c in bpy.data.collections:

                len_name = len(name)

                if c.name.startswith(name) and len(c.name) > len_name:
                    collection = bpy.data.collections.get(c.name)
                    bpy.data.collections.remove(collection)

        remove_collection('Eye Setup')
         
         
 
################################################
################# Rename Eye GEO ###############
        for o in bpy.data.objects:
            if o.type == 'MESH' and o.name == 'Eye Left GEO':
                o.name = 'Rig_Name Eye Left GEO'



        for o in bpy.data.objects:
            if o.type == 'MESH' and o.name == 'Eye Right GEO':
                o.name = 'Rig_Name Eye Right GEO'




        return {'FINISHED'}









classes = [ OBJECT_OT_eye_control_setup_ra,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()


















