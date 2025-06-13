define n = Character("Nina")

default inspected_objects = set()
define ALL_OBJECTS = {"knife", "canvas", "letters", "stool", "table", "laptop", "drawer"}

label start:

    scene outside_room

    show nina at right

    show screen outside_room

    n "Good evening, investigator."
    
    n "We received a call earlier regarding the famous painter, Peter Painter, who was found dead in his studio apartment."
    
    n "His neighbours claim to have heard a heated argument at around 6pm with a woman, and went to check up on him later at 10pm, only to find him dead."
    n "There was a knife found in his chest, and his body appeared to have several cuts on the arms, he bled quite a bit."
    n "We’re not sure of the motive behind this death, so we need you to be thorough. I’ll give you a fair warning, investigator, there is quite a bit of blood on this scene."
    n "You may enter whenever you’re ready."

    pause