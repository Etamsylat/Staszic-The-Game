define position = 0


    
label hide_buttons:
    hide screen inventory_display_toggle
    hide screen quests_display_toggle
    return

label show_buttons:
    show screen inventory_display_toggle
    show screen quests_display_toggle
    return 

label corridor_0:
    scene bg_0
    jump passing

label corridor_1:
    scene bg_1
    jump passing

label corridor_2:
    scene bg_2
    "Chcesz wyjść ze szkoly?"
    menu:
        "Tak":
            $ position = 23
            jump changeBg
        "Nie":
            jump passing

label corridor_3:
    scene bg_3
    jump passing

label corridor_4:
    scene bg_4
    jump passing

label corridor_5:
    scene bg_5
    jump passing

label corridor_6:
    scene bg_6
    jump passing

label corridor_7:
    scene bg_7
    jump passing
label corridor_8:
    scene bg_8
    jump passing

label corridor_9:
    scene bg_9
    jump passing

label corridor_10:
    scene bg_10
    jump passing

label corridor_11:
    scene bg_11
    if "mrokQuest" in quests or "mrokQuest2" in quests or "mrokQuestDone" in quests:
        jump passing
    else:
        jump mrok_quest

label corridor_12:
    scene bg_12
    jump passing

label corridor_13:
    scene bg_13
    if "mrokQuest" in quests:
        jump ssporonEncounter1
    else:
        jump passing

label corridor_14:
    scene bg_14
    jump passing

label corridor_15:
    scene bg_15
    if "key" in inventory_items:
        jump mrocznyBackWithKey
    else:
        "czy chcesz wejsc do klasy?"
        menu:
            "tak":
                jump matematyka_start
            "nie":
                jump passing
            
       


label corridor_16:
    scene bg_16
    jump passing

label corridor_17:
    scene bg_17
    jump passing

label corridor_18:
    scene bg_18
    jump passing

label corridor_19:
    scene bg_19
    jump passing

label corridor_20:
    scene bg_20
    "czy chcesz wejsc do klasy?"
    menu:
        "tak":
            jump biola1
        "nie":
            jump passing

label corridor_21:
    scene bg_21
    jump passing

label corridor_22:
    scene bg_22
    jump passing

label corridor_23:
    scene bg_23
    jump passing

label corridor_24:
    scene bg_24
    jump passing

label corridor_25:
    scene bg_25
    jump passing

label corridor_26:
    scene bg_26
    jump passing

label corridor_27:
    scene bg_27
    jump passing

label corridor_28:
    scene bg_28
    if "sksQuest" in quests:
        jump intoSks1
    else:
        jump passing




