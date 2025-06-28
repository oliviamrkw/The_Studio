"""
This file contains all labels and functions related to the blood analysis
"""

label click_canvas:
    $ default_mouse = "default"
    hide screen casefile_physical
    hide screen casefile_photos

    scene inspect_canvas

    if analyzed["canvas"]:
        $ analyzing["canvas"] = False
        s normal "You've already inspected the canvas."
        jump crimescene
    
    s "Could this have been painted with blood?"

    $ analyzing["canvas"] = True

    if encountered["canvas"] == False:
        $ encountered["canvas"] = True
        "New photo added to evidence."

    $ addToToolbox(["swab_pack"])
    # $ asked["canvas_swab"] = True
    call screen toolbox
    # call screen toolbox_presumptive

label click_stool:
    $ default_mouse = "default"
    hide screen casefile_physical
    hide screen casefile_photos
    
    scene inspect_stool

    if analyzed["splatter"] and analyzed["splatter presumptive"] and analyzed["splatter packaged"]:
        $ analyzing["splatter"] = False
        s normal3 "You've finished analyzing the splatter."
        jump crimescene

    s "A broken stool and a pool of red liquid."

    if encountered["splatter"] == False:
        $ encountered["splatter"] = True
        "New photo added to evidence."

    $ analyzing["splatter"] = True

    $ addToToolbox(["swab_pack"])
    call screen toolbox
    call screen toolbox_blood

label click_knife:
    $ default_mouse = "default"
    hide screen casefile_physical
    hide screen casefile_photos

    s "A bloody knife."

    if analyzed["knife presumptive"] and analyzed["knife packaged"] and analyzed["knife fingerprint"]:
        $ analyzing["knife"] = False
        scene inspect_knife
        s normal2 "You've already inspected the knife"
        jump crimescene

    $ analyzing["knife blood"] = True
    scene inspect_knife

    if encountered["knife"] == False:
        $ encountered["knife"] = True
        "New photo added to evidence."

    $ addToToolbox(["swab_pack"])
    call screen toolbox
    call screen toolbox_blood

label canvas_swab:
    scene inspect_canvas
    if asked["canvas_swab"]:
        show red swab at Transform(xpos=0.4, ypos=0.3)
        "Sample successfully collected."
        jump sample
    
    show clean swab at Transform(xpos=0.4, ypos=0.3)
    menu:
        "How would you like to collect the sample?"
        "Using a wet swab":
            $ asked["canvas_swab"] = True
            hide clean swab
            show red swab at Transform(xpos=0.4, ypos=0.3)
            "Sample successfully collected."
            jump sample
        "Using a dry swab":
            $ asked["canvas_swab"] = True
            hide clean swab
            show red swab at Transform(xpos=0.4, ypos=0.3)
            "Sample successfully collected."
            jump sample

label knife_swab:
    scene inspect_knife
    if asked["knife_swab"]:
        show red swab at Transform(xpos=0.4, ypos=0.3)
        "Sample successfully collected."
        jump sample
    
    show clean swab at Transform(xpos=0.4, ypos=0.3)
    menu:
        "How would you like to collect the sample?"
        "Using a wet swab":
            $ asked["knife_swab"] = True
            hide clean swab
            show red swab at Transform(xpos=0.4, ypos=0.3)
            "Sample successfully collected."
            jump sample
        "Using a dry swab":
            $ asked["knife_swab"] = True
            hide clean swab
            show red swab at Transform(xpos=0.4, ypos=0.3)
            "Sample successfully collected."
            jump sample

label splatter_swab:
    scene inspect_stool dark
    if asked["splatter_swab"]:
        show red swab at Transform(xpos=0.4, ypos=0.3)
        "Sample successfully collected."
        jump sample
    
    show clean swab at Transform(xpos=0.4, ypos=0.3)
    menu:
        "How would you like to collect the sample?"
        "Using a wet swab":
            $ asked["splatter_swab"] = True
            hide clean swab
            show red swab at Transform(xpos=0.4, ypos=0.3)
            "Sample successfully collected."
            jump sample
        "Using a dry swab":
            $ asked["splatter_swab"] = True
            hide clean swab
            show red swab at Transform(xpos=0.4, ypos=0.3)
            "Sample successfully collected."
            jump sample

label sample:
    menu:
        "How would you like to proceed?"
        "Package the sample":
            jump splatter_alt
        "Run a presumptive test":
            hide red swab
            show screen bloody_swab
            python: 
                removal_list = ["swab_pack", "hungarian_red"]
                for item in removal_list:
                    if item in toolbox_items:
                        removeToolboxItem(toolbox_sprites[toolbox_items.index(item)])
                addToToolbox(["ethanol", "reagent", "hydrogen_peroxide"])
            call screen toolbox

label trash:
    $ default_mouse = "default"
    hide screen toolbox_presumptive
    menu:
        "Should I get rid of this swab?"
        "Yes":
            hide screen bloody_swab
            hide red swab
            $ player_kastle_meyer_order = []
            hide screen toolbox_presumptive
            if analyzing["footprint"]:
                jump footprint
            elif analyzing["splatter"]:
                jump splatter
        "No":
            show screen bloody_swab
            call screen toolbox

label presumptive:
    if default_mouse == "ethanol":
        $ player_kastle_meyer_order.append("e")
        $ default_mouse = "default"
        "A drop of ethanol has been added to the sample."
    elif default_mouse == "reagent":
        $ player_kastle_meyer_order.append("r")
        $ default_mouse = "default"
        "A drop of phenolpthalin has been added to the sample."
    elif default_mouse == "hydrogen":
        $ player_kastle_meyer_order.append("h")
        $ default_mouse = "default"
        "A drop of hydrogen peroxide has been added to the sample."

    if len(player_kastle_meyer_order) > 5:
        $ default_mouse = "default"
        s sweat "I think you put in too many drops... you should try again."
        hide screen bloody_swab
        hide red swab
        $ player_kastle_meyer_order = []
        
        python:
            removal_list = ["ethanol", "reagent", "hydrogen_peroxide"]
            for item in removal_list:
                if item in toolbox_items:
                    removeToolboxItem(toolbox_sprites[toolbox_items.index(item)])

        hide screen toolbox_presumptive
        if analyzing["footprint"]:
            jump footprint
        elif analyzing["splatter"]:
            jump splatter

    if player_kastle_meyer_order in valid_kastle_meyer_orders:
        hide screen toolbox_presumptive
        hide screen bloody_swab
        hide red swab
        show pink swab at Transform(xpos=0.4, ypos=0.3)
        "The results of this test show that this substance is indeed blood."
        $ player_kastle_meyer_order = []

        python:
            removal_list = ["ethanol", "reagent", "hydrogen_peroxide"]
            for item in removal_list:
                if item in toolbox_items:
                    removeToolboxItem(toolbox_sprites[toolbox_items.index(item)])

        if analyzing["footprint"]:
            $ analyzed["footprint presumptive"] = True
            jump footprint
        elif analyzing["splatter"]:
            $ analyzed["splatter presumptive"] = True
            jump splatter
    else:
        show screen bloody_swab
        call screen toolbox

# Splatter packaging
label splatter_alt:
    python:
        removal_list = ["swab_pack", "hungarian_red"]
        for item in removal_list:
            if item in toolbox_items:
                removeToolboxItem(toolbox_sprites[toolbox_items.index(item)])
        
        addToToolbox(["evidence_bag", "tube", "tamper_evident_tape"])
    if analyzing["splatter"]:
        scene splatter dark
    else:
        scene footprint dark
    show red swab at Transform(xpos=0.4, ypos=0.3)
    $ tools["tube"] = True
    call screen toolbox

label splatter_packaging_0:
    hide red swab
    call screen sample_to_tube
    show sample test tube at Transform(xpos=0.4, ypos=0.2)
    "Sample successfully placed in tube."
    call screen toolbox

label splatter_packaging_1:
    hide sample test tube
    call screen tube_to_bag
    show evidence bag large at Transform(xpos=0.4, ypos=0.15)
    "Sample successfully placed in bag."
    call screen toolbox

label splatter_packaging_2:
    hide evidence bag large
    call screen tape_to_bag

label splatter_packaging_3:
    python:
        removal_list = ["evidence_bag", "tube", "tamper_evident_tape"]
        for item in removal_list:
            if item in toolbox_items:
                removeToolboxItem(toolbox_sprites[toolbox_items.index(item)])

    show casefile_evidence_idle at Transform(xpos=0.3, ypos=0.24)
    if analyzing["footprint"]:
        "The footprint sample has been added to your evidence."
        $ analyzed["footprint packaged"] = True
        hide casefile_evidence_idle
        jump footprint
    else:
        "The splatter sample has been added to your evidence."
        $ analyzing["splatter"] = False
        $ analyzed["splatter"] = True
        $ analyzed["splatter packaged"] = True
        $ addToInventory(["splatter"])
        hide casefile_evidence_idle
        jump splatter

label enhancement:
    $ encountered["fingerprint enhanced"] = True
    scene inspect_knife
    "The flooring with the print will be taken back to the lab for further examination."
    $ analyzing["knife fingerprint"] = False
    $ analyzed["knife fingerprint"] = True
    jump crimescene
