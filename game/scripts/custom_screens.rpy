# # 
# #This file contains all custom screens used in the game.
# # 

screen crimescene():
    zorder 1
    # modal True

    add "backgrounds/room.png"

    imagebutton:
        idle "images/objects/knife.png"
        hover "images/objects/hover/knife.png"
        xpos 100
        ypos 900
        action Return("knife")
    
    imagebutton:
        idle "images/objects/canvas.png"
        hover "images/objects/hover/canvas.png"
        xpos 150
        ypos 200
        action Return("canvas")

    imagebutton:
        idle "images/objects/letters.png"
        hover "images/objects/hover/letters.png"
        xpos 1050
        ypos 250
        action Return("letters")

    imagebutton:
        idle "images/objects/stool_blood.png"
        hover "images/objects/hover/stool_blood.png"
        xpos 300
        ypos 700
        action Return("stool_blood")

    imagebutton:
        idle "images/objects/table.png"
        hover "images/objects/hover/table.png"
        xpos 1125
        ypos 575
        action Return("table")

    imagebutton:
        idle "images/objects/laptop.png"
        hover "images/objects/hover/laptop.png"
        xpos 1215
        ypos 390
        action Return("laptop")

    imagebutton:
        idle "images/objects/drawer_flowers.png"
        hover "images/objects/hover/drawer_flowers.png"
        xpos 915
        ypos 415
        action Return("drawer_flowers")

label click_canvas:
    $ inspected_objects.add("canvas")
    show screen inspect_canvas

    n "Could this have been painted with blood?"

    menu:
        n "Do you want to perform a presumptive blood test?"

        "Yes":
            n "The test confirms the substance on the canvas is blood."
        "No":
            n "Let's keep investigating."
    
    hide screen inspect_canvas

    return

label click_knife:
    $ inspected_objects.add("knife")
    show screen inspect_knife

    n "A bloody knife."

    menu:
        n "Collect fingerprints?"

        "Yes":
            n "You collect two different fingerprints."
        "No":
            n "Let's keep investigating."
    
    menu: 
        n "Do you want to perform a presumptive blood test?"

        "Yes":
            n "The test confirms the substance on the knife is blood."
        "No":
            n "Let's keep investigating."
    
    hide screen inspect_knife

    return

label click_laptop:
    $ inspected_objects.add("laptop")
    show screen inspect_laptop

    n "It seems his laptop has been left open, let's take a look at the messages."

    window hide
    pause

    hide screen inspect_laptop
    return

label click_letters:
    $ inspected_objects.add("letters")
    show screen inspect_letters
    
    n "Letters from someone named 'Emily'? I wonder why he has them on his wall."
    
    return

label click_stool_blood:
    $ inspected_objects.add("stool")
    show screen inspect_stool_blood

    n "A broken stool and a pool of red liquid."

    menu: 
        n "Do you want to perform a presumptive blood test?"

        "Yes":
            n "The test confirms the substance on the floor is blood."
        "No":
            n "Let's keep investigating."

    return

label click_table:
    $ inspected_objects.add("table")
    show screen inspect_table

    n "Painting supplies, and red liquid."

    menu: 
        n "Do you want to perform a presumptive blood test?"

        "Yes":
            n "The test confirms the substance on the knife is blood."
        "No":
            n "Let's keep investigating."

    return

label click_drawer_flowers:
    $ inspected_objects.add("drawer")
    show screen inspect_drawer

    n "A diagnosis."

    return

screen outside_room():
    zorder 0

    imagebutton:
            idle "images/objects/door.png"
            hover "images/objects/hover/door.png"
            xpos 750
            ypos 125
            action [Hide("outside_room"), Jump("investigation_loop")]

screen inspect_canvas():
    imagemap:
        ground "images/backgrounds/inspect.png"

    add "images/objects/inspect/canvas.png" xpos 700 ypos 50

screen inspect_knife():
    imagemap:
        ground "images/backgrounds/inspect.png"

    add "images/objects/inspect/knife.png" xpos 600 ypos 200

screen inspect_laptop():
    imagemap:
        ground "images/backgrounds/inspect.png"

    add "images/objects/inspect/laptop.png"

screen inspect_table():
    imagemap:
        ground "images/backgrounds/inspect.png"

    add "images/objects/inspect/table.png" xpos 600 ypos 200

screen inspect_letters():
    imagemap:
        ground "images/backgrounds/inspect.png"

    add "images/objects/inspect/letters.png" xpos 600 ypos 100

screen inspect_drawer():
    imagemap:
        ground "images/backgrounds/inspect.png"

    add "images/objects/inspect/drawer.png" xpos 600 ypos 200

screen inspect_stool_blood():
    imagemap:
        ground "images/backgrounds/inspect.png"

    add "images/objects/stool_blood.png" xpos 600 ypos 500

label finish_investigation:
    scene black
    show nina at right
    n "Good work, investigator!\nYou've collected all the evidence."
    jump end

label end:
    return