import bpy

 
# =====================================================
#                      PANEL INTERFACE
# =====================================================



# =====================================================
#                      Rigify ZOO
# =====================================================

# Rigify ZOO
class PANEL_ANIM_BOX_PT_rigify_anim_box_00(bpy.types.Panel):
    bl_label = "Rigify Zoo"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_00'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        rigify_zoo_bool = addon_prefs.rigify_zoo_bool
        if rigify_zoo_bool:  
            return (True)


    def draw(self, context):
        layout = self.layout

        # Cheetah
        box = layout.box() 
        row = box.row() 
        row.scale_y = 1.2
        row.operator("object.cheetah_rigify_zoo_ra")
        row = box.row()
        row.operator("object.rigify_zoo_cheetah_walk_32_ra")
        row.operator("object.rigify_zoo_cheetah_run_14_ra")


        # Cat
        box = layout.box() 
        row = box.row()
        row.operator("object.cat_rigify_zoo_ra")
        row = box.row()
        row.operator("object.rigify_zoo_cat_walk_32_ra")
        row.operator("object.rigify_zoo_cat_run_14_ra")


        # Horse
        box = layout.box() 
        row = box.row()
        row.operator("object.horse_rigify_zoo_ra")
        row = box.row()
        row.operator("object.rigify_zoo_horse_walk_32_ra")
        row.operator("object.rigify_zoo_horse_run_15_ra")

        # Dog
        box = layout.box() 
        row = box.row()
        row.operator("object.dog_rigify_zoo_ra")
        row = box.row(align=True)
        row.operator("object.rigify_zoo_dog_walk_32_ra")
        row.operator("object.rigify_zoo_dog_trot_24_ra")
        row.operator("object.rigify_zoo_dog_canter_14_ra")

 
# =====================================================
#               End Rigify ZOO
# =====================================================





# =====================================================
#                      Rigify Human
# =====================================================

# Rigify Human
class PANEL_ANIM_BOX_PT_rigify_anim_box_00_1(bpy.types.Panel):
    bl_label = "Rigify Human"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_00_1'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        rigify_human_bool = addon_prefs.rigify_human_bool
        if rigify_human_bool:  
            return (True)

    def draw(self, context):
        layout = self.layout


        row = layout.row(align=True)
        row.label(text="", icon='ARMATURE_DATA')
        row.operator("object.create_test_rig_ra", text='Human Rig')
        row.scale_x = 1.5
        row.operator("object.graph_editor_open_ra",text='', icon='GRAPH')


 
# =====================================================
#               End Rigify Human
# =====================================================



# =====================================================
#              Progressive Walk Run
# =====================================================

class PANEL_ANIM_BOX_PT_rigify_anim_box_00_2(bpy.types.Panel):
    bl_label = "Progressive Walk-Run"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_00_2'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        progressive_walk_run_bool = addon_prefs.progressive_walk_run_bool
        if progressive_walk_run_bool:  
            return (True)


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        ra_props = scene.animbox_ra_props 

        icon_v = 'SEQUENCE_COLOR_04'
        # Check Blender Version
        blender_version = bpy.app.version[0]

        if blender_version == 2:
            icon_v = 'PLAY'
            icon_curv = 'PLAY'

        if blender_version == 3:
            icon_v = 'SEQUENCE_COLOR_04'
            icon_curv = 'SEQUENCE_COLOR_02'


        text_main_setup = 'Main Setup'
        text_main_curve_setup = 'Main Setup On Curve'

        # Ref 'On Curve'
        curve_opt_on = ra_props.create_setup_walk_run_curve_animbox_ra

        if curve_opt_on == True:
            icon = icon_curv
            text = text_main_curve_setup

        if curve_opt_on == False:
            icon = icon_v
            text = text_main_setup

        #-----------------------------------------------------------

        box = layout.box()
        row = box.row()
        row.scale_x = 0.1
        row.label(text="Walk")
        row.scale_x = 0.4
        row.label(text='', icon='FORWARD')
        row.scale_y = 1.2
        row.scale_x = 2
        row.operator("object.walk_linear_feet_setup_animbox_ra", text='Linear Feet Setup')

        row = box.row(align=True)

        row.scale_y = 1.4
        row.operator("object.progressive_walk_run_setup_animbox_ra", text=text, icon=icon)

        row = box.row()
        row.label(text='', icon='CON_FOLLOWPATH')
        row.scale_x = 1.5
        row.label(text='On Curve  ->')
        row.prop(ra_props, "create_setup_walk_run_curve_animbox_ra")

        #----------------------
        box = layout.box()
        #----------------------

        box = layout.box()
        row = box.row()

        row.label(text="Adjust" , icon='FILE_REFRESH')

        row.scale_x = 0.7
        row.prop(ra_props, "run_curve_speed_animbox_ra", text='<- Run')

        row = box.row(align=True)
        row.scale_y = 1.2
        row.prop(ra_props, "multiply_frame_range_animbox_ra")
        row.scale_x = 2.5
        row.operator("object.walk_run_direct_speed_animbox_ra", text='Direct Speed')


        row = box.row(align=True)
        row.scale_y = 1.2
        row.operator("object.walk_run_curve_speed_animbox_ra", text='Curve Speed')
        row.scale_x = 0.2
        row.operator("object.curve_speed_frame_timeline_animbox_ra", text='FT')


 
# =====================================================
#               End Progressive Walk Run
# =====================================================







# =====================================================
#               RIGIFY WALK / RUN
# =====================================================


class PANEL_ANIM_BOX_PT_rigify_anim_box(bpy.types.Panel):
    bl_label = "Rigify Walk / Run"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}


    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        rigify_walk_run_bool = addon_prefs.rigify_walk_run_bool
        if rigify_walk_run_bool and context.object is not None and context.object.mode == 'POSE':  
            return (True)


    def draw(self, context):
        scene = context.scene
        ra_props = scene.animbox_ra_props        

        layout = self.layout


        # Check Blender Version
        blender_version = bpy.app.version[0]

        if blender_version == 2:
            icon_red = 'PLAY'
            icon_blue = 'PLAY'
            icon_green = 'PLAY'
            icon_yellow = 'PLAY'
            

        if blender_version == 3:
            icon_red = 'SEQUENCE_COLOR_01' 
            icon_blue = 'SEQUENCE_COLOR_05'
            icon_green = 'SEQUENCE_COLOR_04'   
            icon_yellow = 'SEQUENCE_COLOR_03'     
        
        
        
        # Walk
        text_walk_18 = 'Walk 18'
        text_walk_24 = 'Walk 24'
        text_walk_32 = 'Walk 32'
        
        # Run
        text_run_14 = 'Run 14'
        text_run_18 = 'Run 18'
        text_run_22 = 'Run 22'
        
        
        text_w = ''
        text_r = ''        
        
        icon_w = ''
        icon_r = ''
        
        # Ref
        walk_18_on = ra_props.walk_cycle_18_frames_animbox_ra 
        walk_24_on = ra_props.walk_cycle_24_frames_animbox_ra 
        
        run_14_on = ra_props.run_cycle_14_frames_animbox_ra
        run_18_on = ra_props.run_cycle_18_frames_animbox_ra

        

        if walk_18_on == True:
            icon_w = icon_green
            text_w = text_walk_18

        if walk_24_on == True:
            icon_w = icon_yellow
            text_w = text_walk_24
            
 
        if walk_18_on == False:
            text_w = text_walk_24

        if walk_24_on == False:
            text_w = text_walk_18
            
        if walk_18_on == False and walk_24_on == False:  
            icon_w = icon_red    
            text_w = text_walk_32
        
   
        if run_14_on == True:
            icon_r = icon_green
            text_r = text_run_14       
        
        if run_18_on == True:
            icon_r = icon_yellow
            text_r = text_run_18  
  
        if run_14_on == False:
            text_r = text_run_18      
        
        if run_18_on == False:
            text_r = text_run_14   
            
             
        if run_14_on == False and run_18_on == False:
            icon_r = icon_blue
            text_r = text_run_22


        #-------------------------------------------------------------
        box = layout.box() 
        row = box.row()
        row.scale_y = 0.9
        row.label(text="Disable Arms")
        row.scale_x = 2
        row.prop(ra_props, "exclude_arms_from_anim", icon='CANCEL')
        #-------------------------------------------------------------

        box = layout.box()
        box.scale_y = 0.6
        box.label(icon='DOWNARROW_HLT', text="Unlimited Rig Size")

        box = layout.box()  
        row = box.row(align=True)
        row.scale_y = 1.2
        row.label(text="Walk ->")
        row.prop(ra_props, "walk_cycle_18_frames_animbox_ra") 
        row.prop(ra_props, "walk_cycle_24_frames_animbox_ra") 


        row = box.row(align=True)
        row.scale_y = 1.5
        row.operator("object.walk_adaptive_animbox_ra", text=text_w, icon=icon_w)
        row.operator("object.run_adaptive_animbox_ra", text=text_r, icon=icon_r)


        row = box.row(align=True)
        row.scale_y = 1.2
        row.label(text="Run ->")

        row.prop(ra_props, "run_cycle_14_frames_animbox_ra") 
        row.prop(ra_props, "run_cycle_18_frames_animbox_ra") 



        #-------------------------------------------------------------
 

        box = layout.box() 


        box = layout.box() 
        box.scale_y = 0.6
        box.label(icon='DOWNARROW_HLT', text="Limited Rig Size")

        box = layout.box()
        row = box.row(align=True)
        row.label(text="Walk")
 
        row.scale_y = 1.2
        row.scale_x = 2
        row.operator("OBJECT_OT_rigify_magic_walk_multiple_limbs_18_ra", text="18")
        row.operator("OBJECT_OT_rigify_magic_walk_multiple_limbs_24_ra", text="24")
        row.operator("OBJECT_OT_rigify_magic_walk_multiple_limbs_32_ra", text="32")

    
        box = layout.box() 
        row = box.row(align=True)
        row.label(text="Run")
 
        row.scale_y = 1.2
        row.scale_x = 2
        row.operator("object.rigify_magic_run_multiple_limbs_14_ra", text="14")
        row.operator("object.rigify_magic_run_multiple_limbs_18_ra", text="18")
        row.operator("object.rigify_magic_run_multiple_limbs_22_ra", text="22")

# =====================================================
#             End  RIGIFY WALK / RUN
# =====================================================



# =====================================================
#           RIGBOX
# =====================================================

class PANEL_ANIM_BOX_PT_rigify_anim_box_001(bpy.types.Panel):
    bl_label = "RigBox"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_001'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        rig_box_bool = addon_prefs.rig_box_bool
        if rig_box_bool:  
            return (True)

    def draw(self, context):
        layout = self.layout

        box = layout.box() 

        row = box.row()
        row.operator("object.eye_control_setup_ra", icon='HIDE_OFF')



# =====================================================
#               RIGIFY SAMPLES
# =====================================================


class PANEL_ANIM_BOX_PT_rigify_anim_box_002(bpy.types.Panel):
    bl_label = "Rigify Samples"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_002'
    bl_parent_id = 'PANEL_ANIM_BOX_PT_rigify_anim_box_001'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        box = layout.box() 


        row = box.row() 
        row.scale_y = 1.2
        row.operator("object.human_metarig_no_face_with_hands_ra")

        row = box.row()
        row.operator("object.human_metarig_arms_with_hands_ra")

        row = box.row()
        row.operator("object.human_metarig_simple_spine_ra")

        row = box.row()
        row.operator("object.human_metarig_simple_spine_with_head_ra")

        row = box.row() 
        row.operator("object.human_metarig_legs_ra")

        row = box.row() 
        row.operator("object.human_metarig_legs_with_torso_ra")

        row = box.row() 
        row.operator("object.human_metarig_legs_spine_head_ra")


        # Rigify ZOO Metarigs
        box = layout.box() 

        row = box.row() 
        # row.scale_y = 1.2
        row.scale_y = 0.6
        row.label(text="Rigify ZOO Metarigs", icon='ADD')
        row = box.row(align=True)
        row.operator("object.rigify_zoo_horse_metarig_ra", text='Horse')
        row.operator("object.rigify_zoo_cheetah_metarig_ra", text='Cheetah')
        row = box.row(align=True)
        row.operator("object.rigify_zoo_cat_metarig_ra", text='Cat')
        row.operator("object.rigify_zoo_dog_metarig_ra", text='Dog')




# =====================================================
#           End  RIGIFY SAMPLES
# =====================================================









# =====================================================
#                   MIRROR / CYCLE
# =====================================================


class PANEL_ANIM_BOX_PT_rigify_anim_box_1(bpy.types.Panel):
    bl_label = "Mirror / Cycle"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_1'
    # bl_parent_id = 'PANEL_ANIM_BOX_PT_rigify_anim_box'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        mirror_cycle_bool = addon_prefs.mirror_cycle_bool
        if mirror_cycle_bool and context.object is not None and context.object.mode == 'POSE':  
            return (True)



    def draw(self, context):
        layout = self.layout

        scene = context.scene
        ra_props = scene.animbox_ra_props 


        # Mirror Pose in place

        box = layout.box()
        row = box.row()

        row.scale_y = 1
        row.operator("object.mirror_pose_in_place_ra", icon='MOD_MIRROR')
        row = box.row()
        row.operator("object.copy_sel_to_opposite_ra", icon='PASTEFLIPDOWN')                


        box = layout.box()
        row = box.row()
        box = layout.box()

 
        row = box.row(align=True)     
        row.operator("object.mirror_pose_after_num_ra", text='Mirror',) 
        
        row.operator("object.copy_pose_after_num_ra", text='Copy', ) 
      

        row = box.row()        
        row.label(text="After", icon='DECORATE_KEYFRAME')       
        row.scale_x = 1.8
        row.prop(ra_props, "frame_int")         

        # Rigify Auto Mirror
        box = layout.box()
        row = box.row()
        row.scale_y = 0.5
        row.label(text="Rigify Auto Mirror", icon='AUTO')  
        row.scale_x = 0.5
        row = box.row(align=True)
        row.operator("object.auto_mirror_rigify_feet_ik_ra")         
        row.operator("object.auto_mirror_rigify_hands_ik_ra")         
        row.operator("object.auto_mirror_rigify_arms_forearms_ra")         

        # Smart Mirror Selected
        box = layout.box()
        row = box.row()
        row.scale_y = 1.2
        row.operator("object.smart_mirror_pose_after_sel_ra", icon='KEYTYPE_BREAKDOWN_VEC') 


        box = layout.box()


        # Smart 3-Pose Creator
        box = layout.box()
        row = box.row(align=True)
        row.scale_y = 1.2
        row.operator("object.smart_three_pose_cycle_auto_ra", icon='KEYTYPE_EXTREME_VEC')


        # Add CYCLES Modifier ( Pre_Post_Infinity ) to Selected
        row.scale_x = 2
        row.operator("object.add_cycles_modifier_to_selected_ra", text='', icon='FCURVE')
       
        # Mirroring Extended Cycle
        box = layout.box()
        row = box.row()

        row.operator("wm.custom_pose_cycle_ra", text="Mirroring Extended Cycle", icon='EVENT_C')    # POSE CYCLE CREATOR
        row = layout.row()


# =====================================================
#             End  MIRROR / CYCLE
# =====================================================




# =====================================================
#               
# =====================================================


# class PANEL_ANIM_BOX_PT_rigify_anim_box_2(bpy.types.Panel):
#     bl_label = ""
#     bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_2'
#     bl_space_type = 'VIEW_3D'
#     bl_region_type = 'UI'
#     bl_category = "RA"
#     bl_options = {'DEFAULT_CLOSED'}

#     @classmethod
#     def poll(cls, context):    
#         return (context.object is not None  and
#                 context.object.mode == 'POSE' )

#     def draw(self, context):
#         layout = self.layout



# =====================================================
#          
# =====================================================


# =====================================================
#          RIGIFY SELECTOR
# =====================================================

class PANEL_ANIM_BOX_PT_rigify_anim_box_3_1(bpy.types.Panel):
    bl_label = "Select / Key / Reset"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_3_1'
    # bl_parent_id = 'PANELANIM_PT_animhelpers_3'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}


    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        select_key_reset_bool = addon_prefs.select_key_reset_bool
        if select_key_reset_bool and context.object is not None  and context.object.mode == 'POSE':  
            return (True)

 

    def draw(self, context):
        layout = self.layout

        scene = context.scene


        # Insert Key

        row = layout.row()
        row.scale_y = 0.6
        row.label(text="SET KEY/s")

        box = layout.box()

        row = box.row()
        row.operator("object.insert_key_ra", icon='KEYINGSET')  
        row.operator("object.duo_insert_key_ra", icon='KEYINGSET')  
        row.operator("object.insert_key_all_ra", icon='KEYINGSET') 
        row = box.row()
        row.operator("object.insert_pose_keyframe_animbox_ra", icon='KEYINGSET') 
        row = layout.row()


        row.label(text="SELECT")
        box = layout.box()

        row.scale_y = 0.6


        # Mirror Selection 
        row = box.row()
        row.operator("pose.select_mirror", text="Mirror Selection").extend = 0   
        # row = box.row()
        row.operator("pose.select_mirror", text="Select Both Sides").extend = 1    

        box = layout.box()        
        row = box.row()
        row.operator("object.rigify_sel_set_move_rig")
        row.operator("object.rigify_torso_sel")
        row.operator("object.rigify_chest_sel")
        row.operator("object.rigify_head_sel")

        row = box.row()
        row.operator("object.rigify_feet_sel")
        row.operator("object.rigify_hands_sel")

        row = box.row()
        row.operator("object.rigify_right_arm_sel")
        row.operator("object.rigify_left_arm_sel")


        box = layout.box()
        row = box.row(align=True)
        row.operator("object.rigify_sel_fingers_right")
        row.operator("object.rigify_sel_fingers_left")
        row.operator("object.rigify_sel_fingers_both_hands_ra", text="All Fing")
 


        box = layout.box()
        row = box.row(align=True)
        row.label(text="Select")
        row.scale_x = 2
        row.operator("object.rigify_select_related_ra", text='Related')
        row.operator("object.rigify_select_next_ra", text='Next')


        box = layout.box()
        row = box.row()
        row.scale_y = 0.6
        row.label(text="Add Parent Empty to", icon='OUTLINER_OB_EMPTY')

        # Add Parent Empty to "Related"
        row = box.row(align=True)
        row.operator("object.adding_move_empty_to_selected_ra", text='Related')
        
        # Add Parent Empty to any selected Bone/Bones
        row.operator("object.add_parent_empty_to_any_selected_bone_ra" , text='Selected')



        box = layout.box()
        row = box.row()
        row.scale_y = 0.6
        row.label(text="Arm Positions", icon='TRIA_DOWN')
        row = box.row()
        row.operator("object.rigify_arms_down_pos")
        row.operator("object.rigify_arms_in_front_pos")
        row.operator("object.rigify_arms_up_pos")
        row = box.row()
        row.operator("object.rigify_arms_down_pos_selected")
        row.operator("object.rigify_arms_in_front_pos_selected")
        row.operator("object.rigify_arms_up_pos_selected")
 



        box = layout.box()
        row = box.row()
        row.scale_y = 0.6
        row.label(text="Rigify Auto Foot/Feet Down", icon='AUTO')

        row = box.row()
        row.operator("object.rigify_auto_foot_down_left_ra", icon='TRIA_DOWN')
        row.operator("object.rigify_auto_foot_down_right_ra", icon='TRIA_DOWN')
        row.operator("object.rigify_auto_foot_down_both_ra", text="Both", icon='TRIA_DOWN')

        box = layout.box()
        row = box.row()
        row.scale_y = 0.6
        row.label(text="Selected Foot Down", icon='IMPORT')
        row = box.row()
        # Put Foot on Floor (Plant) for Rigify_like Rigs
        row.operator("object.plant_sel_foot_down_rigify_ra", text="Rigify", icon='MOD_DYNAMICPAINT')
        # For not Rigify_like Rigs
        row.operator("object.plant_sel_foot_down_not_rigify_ra", text="NON Rigify", icon='MOD_DYNAMICPAINT')




        # Reset All Transformations

        box = layout.box()
        row = box.row()
        row.scale_y = 0.6
        row.label(text="RESET")
        row = box.row()
        row.operator("object.qpf_total_reset_ra", text="TOTAL Reset", icon='FILE_REFRESH')
        row.operator("object.reset_pose_all_ra", text="Reset Pose", icon='QUIT')
        
        row = box.row()
        row.operator("object.reset_pose_selected_ra", text="Reset Selected", icon='QUIT')
        row.operator("object.duo_reset_pose_selected_ra", text="Mirrored Reset", icon='QUIT')

        row = layout.row()


# =====================================================
#          End RIGIFY SELECTOR
# =====================================================




# =====================================================
#          RIGIFY  <IK FK> SWITCH
# =====================================================


class PANEL_ANIM_BOX_PT_rigify_anim_box_3_2(bpy.types.Panel):
    bl_label = "Rigify - FK <> IK"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_3_2'
    # bl_parent_id = 'PANEL_ANIM_BOX_PT_rigify_anim_box_3_1'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        rigify_fk_ik_bool = addon_prefs.rigify_fk_ik_bool
        if rigify_fk_ik_bool and context.object is not None  and context.object.mode == 'POSE':  
            return (True)

 
    def draw(self, context):
        layout = self.layout

        scene = context.scene

      
        use_align = True
        row = layout.row(align=use_align)
        

        # ARMS ARMS ARMS
        row.scale_y = 0.8
        box1 = row.box()
        box1.label(text="Right Arm", icon = "KEYTYPE_MOVING_HOLD_VEC")
        box1.operator("object.right_arm_to_fk_ra", icon = "FORWARD")
        box1.operator("object.right_arm_to_ik_ra", icon = "LOOP_BACK")
        box1.operator("object.select_right_arm_fk_ik_ctrls_ra", text="Sel R.Arm", icon = "SELECT_SET")

        box2 = row.box()
        box2.label(text="Left Arm", icon = "KEYTYPE_BREAKDOWN_VEC")
        box2.operator("object.left_arm_to_fk_ra", icon = "FORWARD")
        box2.operator("object.left_arm_to_ik_ra", icon = "LOOP_BACK")
        box2.operator("object.select_left_arm_fk_ik_ctrls_ra", text="Sel L.Arm", icon = "SELECT_SET")



# =====================================================
#       End  RIGIFY  <IK FK> SWITCH
# =====================================================



# =====================================================
#                 RIGIFY JUMPER
# =====================================================

class PANEL_ANIM_BOX_PT_rigify_anim_box_3_3(bpy.types.Panel):
    bl_label = "Rigify - Jumps / Turns"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_3_3'
    # bl_parent_id = 'PANELANIM_PT_animhelpers_3'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        rigify_jumps_turns_bool = addon_prefs.rigify_jumps_turns_bool
        if rigify_jumps_turns_bool and context.object is not None  and context.object.mode == 'POSE':  
            return (True)

    def draw(self, context):
        layout = self.layout

        scene = context.scene


        row = layout.row()
        row.scale_y = 1

        box = layout.box()
        row = box.row()
        row.scale_y = 0.6
        row.label(text="Jump Setup", icon="ONIONSKIN_OFF")
        row = box.row()
        row.operator("object.rigify_jumper_start")
        row.operator("object.rigify_jumper_put_down")
        row = box.row()
        row.operator("object.rigify_jumper", text="Jump to Cursor", icon="CURSOR")
        row = box.row()
        row.operator("object.rigify_jumper_length_cursor", text="Define Jump Length", icon="CURSOR")
        row = box.row()
        row.operator("object.rigify_animbox_jump_simple_ra", text="Simple Jump")
        box = layout.box()
        row = box.row()
        row.scale_y = 0.6
        row.label(text="Turns", icon="ONIONSKIN_OFF")
        row = box.row()
        row.operator("object.rigify_create_turn_cor", icon="FORCE_MAGNETIC")
        row = box.row()
        row.scale_y = 0.6
        row.label(text="Front / Back Flip", icon="ONIONSKIN_OFF")
        row = box.row()
        row.operator("object.front_back_flip_ready", icon="ORIENTATION_GIMBAL")

# =====================================================
#             End    RIGIFY JUMPER
# =====================================================





# =====================================================
#                   MOTION PATH
# =====================================================

class PANEL_ANIM_BOX_PT_rigify_anim_box_3_4(bpy.types.Panel):
    bl_label = "Motion Path"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_3_4'
    # bl_parent_id = 'PANEL_ANIM_BOX_PT_rigify_anim_box'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}


    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        motion_path_bool = addon_prefs.motion_path_bool
        if motion_path_bool and context.object is not None:  
            return (True)


    def draw(self, context):
        layout = self.layout

        scene = context.scene

 

        box = layout.box()
        row = box.row()
        row.operator("object.motion_path_cfpr_objects_bones_ra", icon="TRACKING" )

 
        
          
# =====================================================
#                End   MOTION PATH
# =====================================================


# =====================================================
#   
# =====================================================

# class PANEL_ANIM_BOX_PT_rigify_anim_box_3_5(bpy.types.Panel):
#     bl_label = ""
#     bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_3_5'
#     # bl_parent_id = 'PANEL_ANIM_BOX_PT_rigify_anim_box'    
#     bl_space_type = 'VIEW_3D'
#     bl_region_type = 'UI'
#     bl_category = "RA"
#     bl_options = {'DEFAULT_CLOSED'}

#     def draw(self, context):
#         layout = self.layout





             
# =====================================================
#                OBJECT TO BONE
# =====================================================

class PANEL_ANIM_BOX_PT_rigify_anim_box_3_6(bpy.types.Panel):
    bl_label = "Object Tools"
    bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_3_6'
    # bl_parent_id = 'PANEL_ANIM_BOX_PT_rigify_anim_box'    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "RA"
    bl_options = {'DEFAULT_CLOSED'}


    @classmethod
    def poll(cls, context): 
        preferences = context.preferences
        addon_prefs = preferences.addons['rigify_animbox'].preferences
        object_tools_bool = addon_prefs.object_tools_bool
        if object_tools_bool:  
            return (True)


    def draw(self, context):
        layout = self.layout

    
        # Parent Unparent
        box = layout.box()        
        row = box.row()
        row.operator("object.selected_parent_unparent_obj_bone_ra", icon="COMMUNITY")


        # Multiple Objects to Bone
        box = layout.box() 
        row = box.row() 
        row.scale_y = 0.6
        row.label(text="OBJ TO BONE", icon="DISCLOSURE_TRI_DOWN")
        row = box.row() 
        row.scale_x = 0.4              
        row.operator("object.send_sel_obj_to_bone_ra", icon='LAYER_USED')  
        row.scale_x = 0.6
        row.operator("object.sel_obj_to_bone_keep_offset_ra", text="Keep Offset", icon='OUTLINER_DATA_POINTCLOUD') 
          
        box = layout.box() 
        row = box.row() 
        row.scale_y = 0.6
        row.label(text="OBJ TO BONE + PARENT", icon="DISCLOSURE_TRI_DOWN")
        row = box.row()               
        row.operator("object.send_sel_obj_to_sel_bone_parent_ra", icon="LAYER_ACTIVE")
        row = box.row()  
        row.operator("object.sel_obj_to_bone_keep_offset_parent_ra",  text="Keep Offset + Parent", icon="OUTLINER_OB_POINTCLOUD")  
        row = box.row()
        

        # One Obj to Bone with "Child Of" Constraint
        box = layout.box()        
        box = layout.box()        
        row = box.row()
        row.operator("object.sel_obj_to_sel_bone_child_of_ra", text='O2B "Child Of" Constraint', icon='CON_CHILDOF')        

  
        # Send Objects to Selected by Name Bone (Rigify)
        box = layout.box() 
        row = box.row()
               
        row.scale_y = 0.6
        row.label(text="Select Bone by Name (Rigify)")   
          
        row = box.row()
        row.operator("object.call_rigify_object_to_bone_menu_ra", icon="DOWNARROW_HLT")        
        row = box.row()      
        row.operator("object.call_rigify_object_to_bone_child_of_menu_ra", text="Child Of - Constraint", icon="DOWNARROW_HLT") 
        
        
        box = layout.box() 

        box.scale_y = 0.8
        box.label(text="OBJECT - BAKE ", icon= "OBJECT_DATAMODE")

        row = layout.row()
        row.operator("object.bake_clear_parent_constraint_object_ra", text="BAKE Parent / Constraint", icon="OBJECT_DATAMODE")    
             
 
        row = layout.row()
        row.operator("object.selected_object_offset_keyframes_ra", text="Offset Keyframes", icon="SORTSIZE")    
             
 

# =====================================================
#             End   OBJECT TO BONE
# =====================================================






# =====================================================
#               
# =====================================================

# class PANEL_ANIM_BOX_PT_rigify_anim_box_4(bpy.types.Panel):
#     bl_label = ""
#     bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_4'
#     bl_space_type = 'VIEW_3D'
#     bl_region_type = 'UI'
#     bl_category = "RA"
#     bl_options = {'DEFAULT_CLOSED'}
    

#     def draw(self, context):
#         layout = self.layout


# =====================================================
#        
# =====================================================





# =====================================================
#                     
# =====================================================

# class PANEL_ANIM_BOX_PT_rigify_anim_box_5(bpy.types.Panel):
#     bl_label = ""
#     bl_idname = 'PANEL_ANIM_BOX_PT_rigify_anim_box_5'
#     bl_space_type = 'VIEW_3D'
#     bl_region_type = 'UI'
#     bl_category = "RA"
#     bl_options = {'DEFAULT_CLOSED'}

#     def draw(self, context):
#         layout = self.layout










classes = [
            # Panels
            PANEL_ANIM_BOX_PT_rigify_anim_box_00,
            PANEL_ANIM_BOX_PT_rigify_anim_box_00_1,
            PANEL_ANIM_BOX_PT_rigify_anim_box_00_2,
            PANEL_ANIM_BOX_PT_rigify_anim_box,
            PANEL_ANIM_BOX_PT_rigify_anim_box_001,
            PANEL_ANIM_BOX_PT_rigify_anim_box_002,

            PANEL_ANIM_BOX_PT_rigify_anim_box_1,
            # PANEL_ANIM_BOX_PT_rigify_anim_box_2, 
            PANEL_ANIM_BOX_PT_rigify_anim_box_3_1,
            PANEL_ANIM_BOX_PT_rigify_anim_box_3_2, PANEL_ANIM_BOX_PT_rigify_anim_box_3_3,
            PANEL_ANIM_BOX_PT_rigify_anim_box_3_4,
            PANEL_ANIM_BOX_PT_rigify_anim_box_3_6,

            # PANEL_ANIM_BOX_PT_rigify_anim_box_5,
          ]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)




if __name__ == "__main__":
    register()









