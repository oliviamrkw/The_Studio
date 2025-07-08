# # 
# #This file contains all custom screens used in the game.
# # 

screen ui():
    # This is the case file displayed on the top left corner of the screen when the player is in the corridor.
    zorder 2

    hbox:
        xpos 0.02 ypos 0.12
        imagebutton:
            auto "case_file_%s.png" at Transform(zoom=2.5) mouse "pointer"
            hovered Notify("evidence")
            action Function(close_menu)

# Contents of casefile ---------------------------------------------------------------------------------------
screen casefile():
    # This is screen displayed after the player clicks on the case file.
    # It allows the player to choose between the physical evidence and the photos.
    zorder 1
    modal True
    add "casefile_inventory.png"
    text "Evidence Collected" xpos 0.42 ypos 0.15

    text "Physical Evidence" xpos 0.27 ypos 0.7
    text "Photo Evidence" xpos 0.565 ypos 0.7

    hbox:
        xpos 0.17 ypos 0.1
        imagebutton:
            auto "back_button_%s.png" at Transform(zoom=0.2)
            action Function(close_menu)

    hbox:
        xpos 0.2 ypos 0.23
        imagebutton:
            auto "casefile_evidence_%s.png" at Transform(zoom=0.7) mouse "pointer"
            hovered Notify("collected evidence")
            action [ToggleScreen("casefile"), ToggleScreen("casefile_physical")]
    
    hbox:
        xpos 0.5 ypos 0.27
        imagebutton:
            auto "casefile_photos_%s.png" at Transform(zoom=1.5)
            hovered Notify("photos")
            action [ToggleScreen("casefile"), ToggleScreen("casefile_photos")]
    
    
# screen casefile_physical():
#     # This is the screen displayed when the player clicks on the physical evidence.
#     # It shows all evidence collected. When the player clicks on a piece of evidence,
#     # the description of the evidence is displayed on the bottom of the screen.

#     # NOTE: This screen will not be used in future iterations of the game. This
#     # is a placeholder screen. The inventory that Vivian created will be used instead. 
#     zorder 0
#     modal True
#     add "casefile_inventory.png" at Transform(yzoom=1.1)
#     text "Evidence Collected" xpos 0.42 ypos 0.15

#     hbox:
#         xpos 0.17 ypos 0.1
#         imagebutton:
#             auto "back_button_%s.png" at Transform(zoom=0.2)
#             action [ToggleScreen("casefile_physical"), SetVariable("evidence_desc", ""), ToggleScreen("casefile")]
    
#     showif analyzed["knife fingerprint"]:
#         hbox:
#             # xpos 0.5 ypos 0.24
#             xpos 0.2 ypos 0.24
#             imagebutton:
#                 auto "fingerprint %s.png" at Transform(zoom=0.7)
#                 action SetVariable("evidence_desc", "This is the fingerprint we gathered from the knife on the ground.")

#     showif analyzed["table packaged"]:
#         hbox:
#             xpos 0.5 ypos 0.24
#             imagebutton:
#                 auto "sample footprint %s.png" at Transform(zoom=0.7)
#                 action If(analyzed["table packaged"], SetVariable("evidence_desc", "This is blood gathered from the table."), SetVariable("evidence_desc", "This is the red substance gathered from the table. It is unknown what this substance is at the moment."))

#     showif analyzed["splatter packaged"]:
#         hbox:
#             xpos 0.65 ypos 0.24
#             imagebutton:
#                 auto "sample splatter %s.png" at Transform(zoom=0.7)
#                 action If(analyzed["splatter presumptive"], SetVariable("evidence_desc", "This is blood gathered from the splatter on the floor."), SetVariable("evidence_desc", "This is the red substance gathered from the splatter on the floor. It is unknown what this substance is at the moment."))
    
#     text "[evidence_desc]" xalign 0.5 ypos 0.79 size 30 xsize 900 color "#fff"


# screen casefile_photos():
#     # This is the screen displayed when the player clicks on the photos. It shows
#     # photos of all evidence collected.

#     # NOTE: This screen will not be used in future iterations of the game. This
#     # is a placeholder screen. The inventory that Vivian created will be used instead. 
#     zorder 1
#     modal True
#     add "casefile_inventory.png"
#     text "Evidence Collected" xpos 0.42 ypos 0.15
#     hbox:
#         xpos 0.17 ypos 0.1
#         imagebutton:
#             auto "back_button_%s.png" at Transform(zoom=0.2)
#             action [ToggleScreen("casefile_photos"), ToggleScreen("casefile")]

#     showif encountered["knife"]:
#         hbox:
#             xpos 0.18 ypos 0.22
#             imagebutton:
#                 idle "footprint" at Transform(zoom=0.2)

#     showif encountered["canvas"]:
#         hbox:
#             xpos 0.4 ypos 0.22
#             imagebutton:
#                 idle "footprint enhanced" at Transform(zoom=0.2)

#     showif encountered["letters"]:
#         hbox:
#             xpos 0.62 ypos 0.22
#             imagebutton:
#                 idle "handprint dusted" at Transform(zoom=0.2)

#     showif encountered["stool"]:
#         hbox:
#             xpos 0.18 ypos 0.5
#             imagebutton:
#                 idle "fingerprint dusted" at Transform(zoom=0.2)

#     showif encountered["table"]:
#         hbox:
#             xpos 0.4 ypos 0.5
#             imagebutton:
#                 idle "splatter" at Transform(zoom=0.2)

#     showif encountered["laptop"]:
#         hbox:
#             xpos 0.62 ypos 0.5
#             imagebutton:
#                 idle "gin" at Transform(zoom=0.2)
    
#     showif encountered["drawer"]:
#         hbox:
#             xpos 0.62 ypos 0.5
#             imagebutton:
#                 idle "gin" at Transform(zoom=0.2)

# Contents of toolbox --------------------------------------------------------------------------------------
screen toolbox_print():
    # This is the toolbox used for the fingerprint.
    zorder 1
    hbox:
        xpos 0.89 ypos 0.084
        imagebutton:
            sensitive tools["uv light"]
            auto "uv_light_%s.png" at Transform(zoom=0.06)
            hovered Notify("flashlight")
            action [SetDict(tools, "uv light", False), Show("dark_overlay_with_mouse")]
    
    hbox:
        xpos 0.88 ypos 0.27
        imagebutton:
            sensitive tools["magnetic powder"]
            auto "magnetic_powder_%s.png" at Transform(zoom=0.06)
            hovered Notify("magnetic powder")
            action [SetDict(tools, "magnetic powder", False), If(analyzing["handprint"], [SetDict(tools, "gel lifter", True), Jump("handprint_dusted")], [SetDict(tools, "scalebar", True), Jump("fingerprint_dusted")])]
    
    hbox:
        xpos 0.885 ypos 0.5
        imagebutton:
            sensitive tools["silver granular powder"]
            auto "silver_granular_powder_%s.png" at Transform(zoom=0.06)
            hovered Notify("silver granular powder")
            action [SetDict(tools, "silver granular powder", False), If(analyzing["knife"], [SetDict(tools, "gel lifter", True), Jump("fingerprint_1_dusted")], [SetDict(tools, "scalebar", True), Jump("fingerprint_1_dusted")])]
        
    hbox:
        xpos 0.88 ypos 0.65
        imagebutton:
            sensitive tools["scalebar"]
            auto "scalebar_%s.png" at Transform(zoom=0.6)
            hovered Notify("scalebar")
            action [SetDict(tools, "scalebar", False), SetDict(tools, "tape", True), If(analyzing["handprint"], Jump("handprint_scalebar"), Jump("fingerprint_scalebar"))]
    
    hbox:
        xpos 0.885 ypos 0.8
        imagebutton:
            sensitive tools["tape"]
            auto "tape_%s.png" at Transform(zoom=1)
            hovered Notify("tape")
            action [SetDict(tools, "tape", False), SetDict(tools, "backing", True), If(analyzing["handprint"], Jump("handprint_taped"), Jump("fingerprint_taped"))]
    
    hbox:
        xpos 0 ypos 0.13
        imagebutton:
            sensitive tools["backing"]
            auto "backing_card_%s.png" at Transform(zoom=0.6)
            hovered Notify("backing card")
            action [SetDict(tools, "backing", False), SetDict(tools, "packaging", True), Jump("fingerprint_backing")]
    
    hbox:
        xpos 0 ypos 0.34
        imagebutton:
            sensitive tools["packaging"]
            auto "casefile_evidence_%s.png" at Transform(zoom=0.3)
            hovered Notify("packaging")
            action [SetDict(tools, "packaging", False), SetDict(tools, "tube", True), Jump("packaging")]

    hbox:
        xpos 0 ypos 0.45
        imagebutton:
            sensitive tools["gel lifter"]
            auto "gel_lifter_%s.png" at Transform(zoom=0.35)
            hovered Notify("gel lifter")
            action [SetDict(tools, "gel lifter", False), SetDict(tools, "packaging", True)]

screen toolbox_blood():
    # This is the toolbox used for the bloody footprint and the splatter.
    # It contains the swab and the hungarian red reagent.
    zorder 1
    hbox:
        xpos 0.13 ypos 0.03
        imagebutton:
            auto "back_button_%s.png" at Transform(zoom=0.2)
            action [If(analyzing["splatter"], SetDict(analyzing, "splatter", False)), Jump("crimescene")]
    hbox:
        xpos 0.77 ypos 0.11
        imagebutton:
            sensitive tools["swab"]
            hovered Notify("swab")
            auto "swab_pack_%s.png" at Transform(zoom=0.8)
            action [SetDict(tools, "swab", False), If(analyzing["table"], Jump("table_swab")),
                If(analyzing["splatter"], Jump("splatter_swab")),
                If(analyzing["knife"] and not (analyzing["knife fingerprint"] or analyzing["knife fingerprint alt"]), Jump("knife_swab")),
                If(analyzing["canvas"], Jump("canvas_swab"))]

screen toolbox_presumptive():
    # This is the toolbox used for the presumptive test.
    zorder 1
    hbox:
        xpos 0.88 ypos 0.02
        imagebutton:
            auto "ethanol_%s.png"
            hovered Notify("ethanol")
            action [SetVariable("default_mouse", "ethanol"), ToggleScreen("toolbox_presumptive")] mouse "dropper"
    
    hbox:
        xpos 0.885 ypos 0.26
        imagebutton:
            auto "reagent_%s.png"
            hovered Notify("reagent")
            action [SetVariable("default_mouse", "reagent"), ToggleScreen("toolbox_presumptive")] mouse "dropper"

    hbox:
        xpos 0.885 ypos 0.5
        imagebutton:
            auto "hydrogen_peroxide_%s.png"
            hovered Notify("hydrogen peroxide")
            action [SetVariable("default_mouse", "hydrogen"), ToggleScreen("toolbox_presumptive")] mouse "dropper"

    hbox:
        xpos 0.898 ypos 0.75
        imagebutton:
            auto "trash_%s"
            hovered Notify("trash")

            action Jump("trash")

    # showif analyzing["canvas"]:
    #     hbox:
    #         xpos 0.895 ypos 0.26
    #         imagebutton:
    #             hovered Notify("hungarian red")
    #             auto "hungarian_red_%s.png"
    #             action Jump("enhancement")

screen toolbox_packaging():
    # This is the toolbox used for packaging the evidence.
    zorder 1
    hbox:
        xpos 0.89 ypos 0.13
        imagebutton:
            sensitive tools["tube"]
            hovered Notify("tube")
            auto "tube_%s" at Transform(zoom=0.8)
            action [SetDict(tools, "tube", False), SetDict(tools, "bag", True), If(analyzing["stool"] or analyzing["knife"], Jump("splatter_packaging_0"))]
    hbox:
        xpos 0.885 ypos 0.32
        imagebutton:
            sensitive tools["bag"]
            auto "evidence_bag_%s" at Transform(zoom=0.9)
            hovered Notify("evidence bag")
            action [SetDict(tools, "tube", False), SetDict(tools, "bag", False), SetDict(tools, "tamper evident tape", True), If(analyzing["knife"], Jump("packaging_1")), If((analyzing["knife"] or analyzing["canvas"] or analyzing["stool"] or analyzing["table"]), Jump("splatter_packaging_1"))]
    
    hbox:
        xpos 0.885 ypos 0.51
        imagebutton:
            sensitive tools["tamper evident tape"]
            hovered Notify("tamper evident tape")
            auto "tamper_evident_tape_%s.png" at Transform(zoom=0.9)
            action [SetDict(tools, "tamper evident tape", False), If((analyzing["knife fingerprint"] or analyzing["knife fingerprint alt"]), Jump("packaging_2")), If((analyzing["knife"] or analyzing["canvas"] or analyzing["stool"] or analyzing["table"]), Jump("splatter_packaging_2"))]

# Drag and drop screens -------------------------------------------------------------------------------

screen sample_to_tube():
    draggroup:
        drag:
            drag_name "sample"
            child "red swab cropped"
            xpos 0.28 ypos 0.3
            draggable True
            droppable True
            dragging item_dragging_package
            dragged item_dragged_package

        drag:
            drag_name "tube"
            child "tube"
            xpos 0.59 ypos 0.29
            draggable True
            droppable True
            dragging item_dragging_package
            dragged item_dragged_package


screen tube_to_bag():
    draggroup:
        drag:
            drag_name "sample test tube"
            child "sample test tube"
            xpos 0.23 ypos 0.2
            draggable True
            droppable True
            dragging item_dragging_package
            dragged item_dragged_package

        drag:
            drag_name "bag"
            child "evidence bag large"
            xpos 0.54 ypos 0.19
            draggable True
            droppable True
            dragging item_dragging_package
            dragged item_dragged_package

screen fingerprint_to_bag():
    draggroup:
        drag:
            drag_name "fingerprint"
            child "backing fingerprint"
            xpos 0.25 ypos 0.3
            draggable True
            droppable True
            dragging item_dragging_package
            dragged item_dragged_package

        drag:
            drag_name "bag"
            child "evidence bag large"
            xpos 0.55 ypos 0.2
            draggable True
            droppable True
            dragging item_dragging_package
            dragged item_dragged_package

screen tape_to_bag():
    draggroup:
        drag:
            drag_name "tape"
            child "tamper evident tape"
            xpos 0.25 ypos 0.3
            draggable True
            droppable True
            dragging item_dragging_package
            dragged item_dragged_package
        
        drag:
            drag_name "bag"
            child "evidence bag large"
            xpos 0.55 ypos 0.2
            draggable True
            droppable True
            dragging item_dragging_package
            dragged item_dragged_package

# Backgrounds -------------------------------------------------------------------------------------------
screen crimescene():
    zorder 0
    # modal True

    add "backgrounds/room.png"

    imagebutton:
        idle "images/objects/knife.png"
        hover "images/objects/hover/knife.png"
        xpos 200
        ypos 900
        action Jump("click_knife")
    
    imagebutton:
        idle "images/objects/canvas.png"
        hover "images/objects/hover/canvas.png"
        xpos 200
        ypos 200
        action Jump("click_canvas")

    imagebutton:
        idle "images/objects/letters.png"
        hover "images/objects/hover/letters.png"
        xpos 1050
        ypos 250
        action Jump("click_letters")

    imagebutton:
        idle "images/objects/stool.png"
        hover "images/objects/hover/stool.png"
        xpos 300
        ypos 700
        action Jump("click_stool")

    imagebutton:
        idle "images/objects/table.png"
        hover "images/objects/hover/table.png"
        xpos 1130
        ypos 575
        action Jump("click_table")

    imagebutton:
        idle "images/objects/laptop.png"
        hover "images/objects/hover/laptop.png"
        xpos 1215
        ypos 390
        action Jump("click_laptop")

    imagebutton:
        idle "images/objects/drawer.png"
        hover "images/objects/hover/drawer.png"
        xpos 915
        ypos 415
        action Jump("click_drawer")

    showif encountered["canvas"]:
        add "marker 1" at Transform(xpos=0.06, ypos=0.76, zoom= 0.32)
    
    showif encountered["knife"]:
        add "marker 2" at Transform(xpos=0.16, ypos=0.87, zoom=0.3)
    
    showif encountered["stool"]:
        add "marker 3" at Transform(xpos=0.55, ypos=0.83, zoom=0.33)

    showif encountered["table"]:
        add "marker 4" at Transform(xpos=0.81, ypos=0.88, zoom=0.33)

screen bloody_swab():
    # This is the screen used to allow the player to add drops of chemicals
    # to the swab during the presumptive test.
    imagebutton:
        idle "red swab" at Transform(xpos=0.4, ypos=0.3)
        action Jump("presumptive")

screen dark_overlay_with_mouse():
    # This is the screen used after pressing the flashlight when analyzing
    # the door.
    modal True

    default mouse = (0, 0)

    # Timer to repeatedly update the mouse position
    timer 0.02 repeat True action SetScreenVariable("mouse", renpy.get_mouse_pos())

    imagemap:
        idle "images/backgrounds/inspect_knife_fingerprint.png"
        # hover "images/backgrounds/inspect_knife_fingerprint.png"
        # fingerprint 1
        hotspot (1091, 627, 87, 84) action [SetDict(tools, "uv light", False), SetDict(tools, "silver granular powder", True), SetDict(analyzing, "knife fingerprint", True), ToggleScreen("dark_overlay_with_mouse"), Jump("knife_fingerprint_1")]
        
        # fingerprint 2
        hotspot (1268, 650, 69, 77) action [SetDict(tools, "uv light", False), SetDict(tools, "silver granular powder", True), SetDict(analyzing, "knife fingerprint alt", True), ToggleScreen("dark_overlay_with_mouse"), Jump("knife_fingerprint_2")]

    # Adding the darkness overlay with the current mouse position
    add "darkness" pos mouse anchor (0.5, 0.5)

screen outside_room():
    zorder 0

    imagebutton:
        idle "images/objects/door.png"
        hover "images/objects/hover/door.png"
        xpos 750
        ypos 125
        action [Hide("outside_room"), Jump("crimescene")]

screen inspect_canvas():
    add "images/backgrounds/inspect_canvas.png" xpos 700 ypos 50

    textbutton "Back" xpos 1800 ypos 1000 action Jump("crimescene")#Hide("inspect_canvas")

screen inspect_knife():
    add "images/backgrounds/inspect_knife.png" xpos 600 ypos 200

    textbutton "Back" xpos 1800 ypos 1000 action Jump("crimescene")#Hide("inspect_knife")

screen inspect_table():
    add "images/backgrounds/inspect_table.png" xpos 600 ypos 200

    textbutton "Back" xpos 1800 ypos 1000 action Jump("crimescene")#Hide("inspect_table")

screen inspect_letters():
    add "images/backgrounds/inspect_letters.png" xpos 10 ypos 10

    textbutton "Back" xpos 1800 ypos 1000 action Jump("crimescene")#Hide("inspect_letters")

screen inspect_stool():
    add "images/backgrounds/inspect_stool.png" xpos 600 ypos 500

    textbutton "Back" xpos 1800 ypos 1000 action Jump("crimescene")#Hide("inspect_stool")

# Interactibles  -------------------------------------------------------------------------------------------

default current_tab = "emily"

screen inspect_laptop():
    $ default_mouse = "cursor"

    add "images/backgrounds/inspect_laptop.png" 

    if current_tab == "emily":
        add "images/backgrounds/laptop_emily.png"
    elif current_tab == "fred":
        add "images/backgrounds/laptop_fred.png"
    elif current_tab == "mom":
        add "images/backgrounds/laptop_mom.png"

    imagebutton:
        idle Solid("#a0a0a010")
        hover Solid("#ffffff1e")
        xpos 336 ypos 247 xsize 230 ysize 130
        action SetVariable("current_tab", "emily")

    imagebutton:
        idle Solid("#a0a0a010")
        hover Solid("#ffffff1e")
        xpos 336 ypos 387 xsize 230 ysize 130
        action SetVariable("current_tab", "fred")

    imagebutton:
        idle Solid("#a0a0a010")
        hover Solid("#ffffff1e")
        xpos 336 ypos 539 xsize 230 ysize 130
        action SetVariable("current_tab", "mom")

    textbutton "Back" xpos 1800 ypos 1000 action Jump("crimescene")#Hide("inspect_laptop")

default drawer_open = False

screen inspect_drawer():
    $ default_mouse = "cursor"

    if drawer_open:
        add "images/backgrounds/inspect_drawer_open.png"
        textbutton "Back" xpos 1800 ypos 1000 action [SetVariable("drawer_open", False)]
    else:
        add "images/backgrounds/inspect_drawer.png"
        imagebutton:
            idle Solid("#352f2d1c")
            hover Solid("#ffffff1e")
            xpos 790 ypos 603 xsize 335 ysize 134
            action SetVariable("drawer_open", True)
        textbutton "Back" xpos 1800 ypos 1000 action Jump("crimescene")#Hide("inspect_drawer")