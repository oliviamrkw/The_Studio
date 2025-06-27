"""
This file has all labels and functions related to the fingerprint and handprint analysis.
It also contains labels related to packaging the fingerprint, handprint, and gin bottle.
"""

label knife:
    $ default_mouse = "default"
    hide screen casefile_physical
    hide screen casefile_photos
    scene inspect_knife
    $ addToToolbox(["uv_light", "magnetic_powder", "scalebar", "tape", "backing_card", "gel_lifter", "evidence_bag"])
    call screen toolbox

label fingerprint:
    if analyzed["knife fingerprint"]:
        $ tools["magnetic powder"] = False
        scene inspect_knife
        s normal2 "You've already analyzed this print."
        jump crimescene
    $ analyzing["knife fingerprint"] = True
    scene inspect_knife
    call screen toolbox

label fingerprint_dusted:
    $ encountered["knife fingerprint"] = True
    scene inspect_knife
    "New photo added to evidence."
    call screen toolbox

label fingerprint_scalebar:
    scene fingerprint scalebar
    call screen toolbox
    
label fingerprint_taped:
    scene fingerprint taped
    call screen toolbox

label fingerprint_backing:
    scene fingerprint backing
    call screen toolbox

label packaging:
    scene door dark
    $ tools["bag"] = True
    if analyzing["knife fingerprint"]:
        show backing fingerprint at Transform(xpos=0.3, ypos=0.2, zoom=1.6)
    
    python:
        removal_list = ["uv_light", "magnetic_powder", "scalebar", "tape", "backing_card", "gel_lifter"]
        for item in removal_list:
            if item in toolbox_items:
                removeToolboxItem(toolbox_sprites[toolbox_items.index(item)])

    $ addToToolbox(["tube", "tamper_evident_tape"])
    call screen toolbox

label packaging_1:
    hide backing fingerprint
    hide backing handprint
    if analyzing["knife fingerprint"]:
        call screen fingerprint_to_bag
    $ tools["bag"] = False
    show evidence bag large at Transform(xpos=0.4, ypos=0.15)
    "Sample successfully placed in bag."
    call screen toolbox

label packaging_2:
    hide evidence bag large
    call screen tape_to_bag

label packaging_3:
    show casefile_evidence_idle at Transform(xpos=0.3, ypos=0.24)
    "The fingerprint has been added to your evidence."
    $ analyzing["knife fingerprint"] = False
    $ analyzed["knife fingerprint"] = True
    $ addToInventory(["fingerprint"])

    hide casefile_evidence_idle

    python:
        removal_list = ["evidence_bag", "tube", "tamper_evident_tape"]
        for item in removal_list:
            if item in toolbox_items:
                removeToolboxItem(toolbox_sprites[toolbox_items.index(item)])

    jump crimescene