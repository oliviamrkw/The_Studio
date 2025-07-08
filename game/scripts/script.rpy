define s = Character(name=("Nina"), image="nina")

init python:
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
        "silver granular powder": False,
        "scalebar": False,
        "gel lifter": False,
        "tape": False,
        "backing": False,
        "packaging": False,
        "tube": False,
        "bag": False,
        "tamper evident tape": False,
        "swab": True
    }

    # Used to keep track of player's progress in the game
    analyzing = {
        "knife": False,
        "knife fingerprint": False,
        "knife fingerprint alt": False,
        "canvas": False,
        "stool": False,
        "table": False,
    }

    # Used to keep track of what evidence has been analyzed
    analyzed = {
        "canvas": False,
        "canvas presumptive": False,
        "canvas packaged": False,
        "splatter": False,
        "splatter presumptive": False,
        "splatter packaged": False,
        "knife fingerprint": False,
        "knife fingerprint alt": False,
        "knife presumptive": False,
        "knife packaged": False,
        "knife fingerprint packaged": False,
        "knife fingerprint alt packaged": False,
        "table presumptive": False,
        "table packaged": False,
    }

    # Used to keep track of what evidence has been encountered
    # This is used to display the evidence markers and enable respective photos
    encountered = {
        "knife": False, 
        "canvas": False,
        "letters": False,
        "stool": False,
        "table": False,
        "laptop": False,
        "drawer": False
    }

    # Used to ensure that the player is not asked the "How would you like to collect the sample?" question multiple times
    asked = {
        "stool_swab": False,
        "canvas_swab": False,
        "table_swab": False,
        "knife_swab": False
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

    #REQUIRED FOR INVENTORY:
    $config.rollback_enabled = False # disables rollback
    $quick_menu = False # removes quick menu (at bottom of screen) - might put this back since inventory bar moved to right side

    # environment:
    $environment_SM = SpriteManager(event = environmentEvents) # sprite manager that manages environment items; triggers function environmentEvents() when event happens with sprites (e.g. button click)
    $environment_sprites = [] # holds all environment sprite objects
    $environment_items = [] # holds environment items
    $environment_item_names = [] # holds environment item names

    # inventory
    $inventory_SM = SpriteManager(update = inventoryUpdate, event = inventoryEvents) # sprite manager that manages evidence items; triggers function inventoryUpdate 
    $inventory_sprites = [] # holds all evidence sprite objects
    $inventory_items = [] # holds evidence items
    $inventory_item_names = ["Tape on acetate", "Tapeglo in bag", "Tape photo", "Duct tape tapeglo", "Distilled water", "Tape in tweezers", "Duct tape", "Tapeglo", 
    "Fingerprint on card", "Backing card","Scalebar", "Lifting tape", "Jar photo", "Lid in tweezers", "Camel brush", "Lid with soot", "Lid", "Camphor smoke", "Lighter", 
    "Tweezers", "Gloves box", "Evidence bag", "Jar in bag", "Tape in bag", "Pvs in bag"] # holds names for inspect pop-up text 
    $inventory_db_enabled = False # determines whether up arrow on evidence hotbar is enabled or not
    $inventory_ub_enabled = False # determines whether down arrow on evidence hotbar is enabled or not
    $inventory_slot_size = (int(215 / 2), int(196 / 2)) # sets slot size for evidence bar
    $inventory_slot_padding = 120 / 2 # sets padding size between evidence slots
    $inventory_first_slot_x = 110 # sets x coordinate for first evidence slot
    $inventory_first_slot_y = 175 # sets y coordinate for first evidence slot
    $inventory_drag = False # by default, item isn't draggable

    # toolbox:
    $toolbox_SM = SpriteManager(update = toolboxUpdate, event = toolboxEvents) # sprite manager that manages toolbox items; triggers function toolboxUpdate 
    $toolbox_sprites = [] # holds all toolbox sprite objects
    $toolbox_items = [] # holds toolbox items
    # $toolbox_item_names = ["Tape", "Ziploc bag", "Jar in bag", "Tape in bag", "Gun all", "Empty gun", "Cartridges", "Gun with cartridges", "Tip", "Pvs in bag"] # holds names for inspect pop-up text 
    $toolbox_db_enabled = False # determines whether up arrow on toolbox hotbar is enabled or not
    $toolbox_ub_enabled = False # determines whether down arrow on toolbox hotbar is enabled or not
    # $toolbox_slot_size = (int(215 / 2), int(196 / 2)) # sets slot size for toolbox bar
    $toolbox_slot_size = (100, 100)
    # $toolbox_slot_padding = 125 / 2 # sets padding size between toolbox slots
    $toolbox_slot_padding = 69
    $toolbox_first_slot_x = 110 # sets x coordinate for first toolbox slot
    $toolbox_first_slot_y = 175 # sets y coordinate for first toolbox slot
    $toolbox_drag = False # by default, item isn't draggable

    # toolbox popup:
    $toolboxpop_SM = SpriteManager(update = toolboxPopUpdate, event = toolboxPopupEvents) # sprite manager that manages toolbox pop-up items; triggers function toolboxPopUpdate
    $toolboxpop_sprites = [] # holds all toolbox pop-up sprite objects
    $toolboxpop_items = [] # holds toolbox pop-up items
    # $toolboxpop_item_names = ["Tape", "Ziploc bag", "Jar in bag", "Tape in bag", "Gun all", "Empty gun", "Cartridges", "Gun with cartridges", "Tip", "Pvs in bag"] # holds names for inspect pop-up text 
    $toolboxpop_db_enabled = False # determines whether up arrow on toolbox pop-up hotbar is enabled or not
    $toolboxpop_ub_enabled = False # determines whether down arrow on toolbox pop-up hotbar is enabled or not
    $toolboxpop_slot_size = (100, 100) # sets slot size for toolbox pop-up bar
    $toolboxpop_slot_padding = 69 # sets padding size between toolbox pop-up slots
    $toolboxpop_first_slot_x = 406 # sets x coordinate for first toolbox pop-up slot
    $toolboxpop_first_slot_y = 445 # sets y coordinate for first toolbox pop-up slot
    $toolboxpop_drag = False # by default, item isn't draggable

    $current_scene = "scene1" # keeps track of current scene

    $dialogue = {} # set that holds name of character saying dialogue and dialogue message
    $item_dragged = "" # keeps track of current item being dragged
    $mousepos = (0.0, 0.0) # keeps track of current mouse position
    $i_overlap = False # checks if 2 inventory items are overlapping/combined
    $ie_overlap = False # checks if an inventory item is overlapping with an environment item

    $all_pieces = 0

    show screen full_inventory
    jump begin

label begin:
    scene outside_room
    # show nina normal at right
    # s "Good evening, investigator."
    # show nina talk at right
    # s "We received a call earlier regarding the famous painter, Peter Painter, who was found dead in his studio apartment."
    # show nina write at right
    # s "His neighbours claim to have heard a heated argument at around 6pm with a woman, Emily Exgirlfriend, and went to check up on him later at 10pm, only to find him dead."
    # s "There was a knife found in his chest, and his body appeared to have several cuts on the arms, he bled quite a bit."
    # show nina think at right
    # s "We’re not sure of the motive behind this death, so we need you to be thorough. I’ll give you a fair warning, investigator, there is quite a bit of blood on this scene."
    show nina normal at right
    s "You may enter whenever you’re ready."
    # window hide

    call screen outside_room
    # $ renpy.pause(hard=True)

label toolbox_init:
    python:
        addToInventory(["swab_pack"])
        addToInventory(["ethanol"])
        addToInventory(["reagent"])
        addToInventory(["hydrogen"])
        addToInventory(["uv light"])
        addToInventory(["magnetic powder"])
        addToInventory(["silver granular powder"])
        addToInventory(["scalebar"])
        addToInventory(["gel lifter"])
        addToInventory(["tape"])
        addToInventory(["backing"])
        addToInventory(["packaging"])
        addToInventory(["tube"])
        addToInventory(["bag"])
        addToInventory(["tamper evident tape"])

label crimescene:
    scene room
    $ default_mouse = "magnifying"
    call screen crimescene
    # jump investigation_loop

# label investigation_loop:
#     if all(analyzed.values()):
#         jump finish_investigation

    # call screen crimescene
    # $ result = _return

    # if result == "knife":
    #     call click_knife
    # elif result == "canvas":
    #     call click_canvas
    # elif result == "laptop":
    #     call click_laptop
    # elif result == "letters":
    #     call click_letters
    # elif result == "stool":
    #     call click_stool
    # elif result == "table":
    #     call click_table
    # elif result == "drawer":
    #     call click_drawer

    # call investigation_loop


# label investigation_loop:
#     # $ crimescene_result = None
#     show screen crimescene_overlay

#     # while crimescene_result is None:
#     #     $ renpy.pause(0.1)

#     $ result = crimescene_result
#     # hide screen crimescene_overlay

#     if result == "knife":
#         call click_knife
#     elif result == "canvas":
#         call click_canvas
#     elif result == "laptop":
#         call click_laptop
#     elif result == "letters":
#         call click_letters
#     elif result == "stool":
#         call click_stool
#     elif result == "table":
#         call click_table
#     elif result == "drawer":
#         call click_drawer

#     jump investigation_loop

label go_to_scene():
    # s "We're at the crime scene now."
    jump crimescene
    # return

label finish_investigation:
    $ hide_all_inventory()
    scene black
    show nina talk at right
    s "Good work, investigator!\nYou've collected all the evidence."
    return

label click_laptop:
    $ default_mouse = "default"
    hide screen casefile_physical
    hide screen casefile_photos
    call screen inspect_laptop

    # s "It seems his laptop has been left open, let's take a look at the messages. (click)"

    # window hide
    # $ renpy.pause(hard=True)

label click_letters:
    $ default_mouse = "default"
    hide screen casefile_physical
    hide screen casefile_photos
    call screen inspect_letters
    
    # s "Letters from someone named 'Emily'? I wonder why he has them on his wall."
    
    # window hide
    # $ renpy.pause(hard=True)

label click_drawer:
    $ default_mouse = "default"
    hide screen casefile_physical
    hide screen casefile_photos
    call screen inspect_drawer

    # s "A drawer, it looks like there's a shrine of someone, and some dead roses?"

    # window hide
    # $ renpy.pause(hard=True)


transform half_size:
    zoom 0.5