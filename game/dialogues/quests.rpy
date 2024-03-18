screen quests_display_toggle:
    zorder 92
    frame:
        background "#9F99"
        xalign 0.05
        yalign 0.2

        textbutton "Quests":

            action Jump("hideScreenInv")
            

define questScreen = True   
   

label hideScreenInv:
    if questScreen == True:
        $ questScreen = False
        
        hide screen quest_description
    else:
        $ questScreen = True
        $ inventoryScreen = False
        show screen quest_description
        
    
    hide screen inventory_item_description
    jump passing



default quest_descriptions = {"mrokQuest" : "Bardzo mroczne zadanie","mrokQuest2":"Jeszcze mroczniejsze zadanie","sksQuest":"Bardzo"}
default quests = []
default quest_description = ""

style inv_button is frame:
    xsize 200
    ysize 100

style inv_button_text:
    xalign 0.5
    yalign 0.5

screen quest_description:
    
        
    # use this based on your preference
    # modal True
    window:
        background "#AAA9"
        xsize 600
        ysize 150
        xalign 0.5
        yalign 0.1
        text quest_description:
            xfill True
            yfill True

    window:
        background "#99F9"
        xsize 1290
        ysize 600
        xalign 0.5
        yalign 0.7
        hbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 20
            yoffset 20
            style_prefix "inv"
            for item in quests:
                textbutton item:
                    action SetVariable("quest_description", quest_descriptions.get(item))
                    selected False


    on "hide" action SetVariable("quest_description", "")