define position = 0

label sub:
    if position == 26:
        $ position = 28
    elif position != 4 and position != 9 and position != 15 and position != 21:
        $ position = position + 1
    jump changeBg

label add:
    if position == 23:
        $ position = 2
    elif position == 28:
        $ position = 26
    elif position != 0 and position != 5 and position != 10 and position != 16:
        $ position = position - 1
    jump changeBg

label up:
    if position == 2:
        $ position = 7
    elif position == 7:
        $ position = 12
    elif position == 12:
        $ position = 18
    elif position == 26:
        $ position = 27
    jump changeBg

label down:
    if position == 7:
        $ position = 2
    elif position == 12:
        $ position = 7
    elif position == 18:
        $ position = 12
    elif position == 27:
        $ position = 26
    jump changeBg

label changeBg:
    call show_buttons
    $ renpy.jump("corridor_" + str(position))
    
label hide_buttons:
    hide screen button_right
    hide screen button_left
    hide screen button_up
    hide screen button_down
    hide screen inventory_display_toggle
    hide screen quests_display_toggle
    return

label show_buttons:
    if position != 4 and position != 9 and position != 15 and position != 21 and position != 27 and position != 28:
        show screen button_left
    else:
        hide screen button_left
    if position != 0 and position != 5 and position != 10 and position != 16 and position != 27:
        show screen button_right
    else:
        hide screen button_right
    if position == 2 or position == 7 or position == 12 or position == 26:
        show screen button_up
    else:
        hide screen button_up
    if position == 18 or position == 7 or position == 12 or position == 27:
        show screen button_down
    else:
        hide screen button_down

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
    jump passing




