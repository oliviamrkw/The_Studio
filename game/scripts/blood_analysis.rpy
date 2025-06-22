"""
This file contains all labels and functions related to the blood analysis
"""

label splatter:
    $ default_mouse = "default"
    hide screen casefile_physical
    hide screen casefile_photos
    scene splatter

    if analyzed["splatter"] and analyzed["splatter presumptive"] and analyzed["splatter packaged"]:
        $ analyzing["splatter"] = False
        s normal3 "You've finished analyzing the splatter."
        jump corridor

    if encountered["splatter"] == False:
        $ encountered["splatter"] = True
        "New photo added to evidence."

    $ analyzing["splatter"] = True

    $ addToToolbox(["swab_pack"])
    call screen toolbox
    call screen toolbox_blood

label footprint:
    $ default_mouse = "default"
    hide screen casefile_physical
    hide screen casefile_photos

    if analyzed["footprint"]:
        $ analyzing["footprint"] = False
        scene footprint enhanced
        s normal2 "You've already enhanced the footprint."
        s normal2 "There's nothing more you can do now."
        jump corridor

    $ analyzing["footprint"] = True
    scene footprint

    if encountered["footprint"] == False:
        $ encountered["footprint"] = True
        "New photo added to evidence."

    if "swab_pack" not in toolbox_items and "hungarian_red" not in toolbox_items:
        $ addToToolbox(["swab_pack", "hungarian_red"])

    call screen toolbox
    call screen toolbox_blood



label footprint_swab:
    scene footprint dark
    if asked["footprint_swab"]:
        show red swab at Transform(xpos=0.4, ypos=0.3)
        "Sample successfully collected."
        jump sample
    
    show clean swab at Transform(xpos=0.4, ypos=0.3)
    menu:
        "How would you like to collect the sample?"
        "Using a wet swab":
            hide clean swab
            show red swab at Transform(xpos=0.4, ypos=0.3)
            "Sample successfully collected."
            $ asked["footprint_swab"] = True
            jump sample
        "Using a dry swab":
            "Remember, we can't collect dry samples using dry swabs."
            jump footprint

label splatter_swab:
    scene splatter dark
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

label enhancement:
    $ encountered["footprint enhanced"] = True
    scene footprint enhanced
    "The flooring with the print will be taken back to the lab for further examination."
    $ analyzing["footprint"] = False
    $ analyzed["footprint"] = True
    jump corridor

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