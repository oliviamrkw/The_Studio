define n = Character(name=("Nina"), image="nina")

init python:
    inspected_objects = set()
    ALL_OBJECTS = {"knife", "canvas", "letters", "stool", "table", "laptop", "drawer"}

    # Defines all mouse cursors used in the game
    config.mouse = {
        "default": [("images/ui/cursors/cursor.png", 0, 0)],
        "pointer": [("images/ui/cursors/cursor.png", 0, 0)],
        "magnifying": [("images/ui/cursors/default_cursor.png", 0, 0)],
        "hover": [("images/ui/cursors/hover_cursor.png", 0, 0)],
        "dropper": [("images/ui/cursors/dropper.png", 0, 49)],
        "ethanol": [("images/ui/cursors/dropper_filled.png", 0, 49)],
        "reagent": [("images/ui/cursors/dropper_filled.png", 0, 49)],
        "hydrogen": [("images/ui/cursors/dropper_filled.png", 0, 49)],
        "hand": [("images/ui/cursors/default_hand.png", 0, 0)],
        "hand_grab": [("images/ui/cursors/grab_hand.png", 0, 0)]
    }
    
    # Used for tool sensitivity in the toolbox screens defined in custom_screens.rpy
    tools = {
        "uv light": False,
        "magnetic powder": False,
        "scalebar": False,
        "gel lifter": False,
        "tape": False,
        "backing": False,
        "packaging": False,
        "tube": False,
        "bag": False,
        "tamper evident tape": False,
        "swab": False
    }

    # # Used to keep track of player's progress in the game
    # analyzing = {
    #     "handprint": False,
    #     "fingerprint": False,
    #     "splatter": False,
    #     "footprint": False,
    #     "gin": False
    # }

    # # Used to keep track of what evidence has been analyzed
    # analyzed = {
    #     "handprint": False,
    #     "fingerprint": False,
    #     "splatter": False,
    #     "splatter presumptive": False,
    #     "splatter packaged": False,
    #     "footprint": False,
    #     "footprint packaged": False,
    #     "footprint presumptive": False,
    #     "footprint enhanced": False,
    #     "gin": False
    # }

    # Used to keep track of what evidence has been encountered
    # This is used to display the evidence markers and enable respective photos
    # encountered = {
    #     "door": False,
    #     "handprint": False,
    #     "fingerprint": False,
    #     "gin": False,
    #     "splatter": False,
    #     "footprint": False,
    #     "footprint enhanced": False 
    # }

    # Used to ensure that the player is not asked the "How would you like to collect the sample?" question multiple times
    asked = {
        "splatter_swab": False,
        "footprint_swab": False
    }

    # Used to compare against the player's Kastle-Meyer order in the presumptive test scene
    valid_kastle_meyer_orders = [
        ["e", "r", "h"],
        ["e", "r", "r", "h"],
        ["e", "r", "h", "h"],
        ["e", "r", "r", "h", "h"],
        ["e", "e", "r", "h"],
        ["e", "e", "r", "r", "h"],
        ["e", "e", "r", "h", "h"],
        ["e", "e", "r", "r", "h", "h"]
    ]

    player_kastle_meyer_order = []

    # Used to display the evidence description in the casefile
    evidence_desc = ""

    def item_dragging_package(drags):
        """Used to set the mouse cursor to the hand_grab cursor when dragging an item.
        """
        global default_mouse
        default_mouse = "hand_grab"
        return

    def item_dragged_package(drags, drop):
        """Used to set the mouse cursor to the hand_grab cursor when grabbing an item.
        """
        global default_mouse
        default_mouse = "hand_grab"
        
        if not drop:
            default_mouse = "hand"
            return

        store.dragged = drags[0].drag_name
        store.dropped = drop.drag_name

        # Hide all draggable screens
        renpy.hide_screen("sample_to_tube")
        renpy.hide_screen("fingerprint_to_bag")
        renpy.hide_screen("handprint_to_bag")
        renpy.hide_screen("tape_to_bag")
        default_mouse = "default"
        return True
    
    def close_menu():
        """Used to close the casefile menu.
        """
        if renpy.get_screen("casefile_physical"):
            evidence_desc = ""
            renpy.hide_screen("casefile_physical")
        elif renpy.get_screen("casefile_photos"):
            renpy.hide_screen("casefile_photos")
        elif renpy.get_screen("casefile"):
            renpy.hide_screen("casefile")
        else:
            renpy.show_screen("casefile")

label start:
    $ default_mouse = "magnifying"
    scene outside_room
    show nina normal at right

    n "Good evening, investigator."
    show nina talk at right
    n "We received a call earlier regarding the famous painter, Peter Painter, who was found dead in his studio apartment."
    show nina write at right
    n "His neighbours claim to have heard a heated argument at around 6pm with a woman, and went to check up on him later at 10pm, only to find him dead."
    n "There was a knife found in his chest, and his body appeared to have several cuts on the arms, he bled quite a bit."
    show nina think at right
    n "We’re not sure of the motive behind this death, so we need you to be thorough. I’ll give you a fair warning, investigator, there is quite a bit of blood on this scene."
    show nina normal at right
    n "You may enter whenever you’re ready."
    window hide

    show screen outside_room
    $ renpy.pause(hard=True)

label go_to_scene():
    window show
    n "We're at the crime scene now."
    scene room
    show screen crimescene
    return

label investigation_loop:
    if inspected_objects.issuperset(ALL_OBJECTS):
        jump finish_investigation

    call screen crimescene  
    $ result = _return

    if result == "knife":
        call click_knife
    elif result == "canvas":
        call click_canvas
    elif result == "laptop":
        call click_laptop
    elif result == "letters":
        call click_letters
    elif result == "stool_blood":
        call click_stool_blood
    elif result == "table":
        call click_table
    elif result == "drawer_flowers":
        call click_drawer_flowers

    jump investigation_loop