define position = 0

label add:
    if position != 4 and position != 9 and position != 15 and position != 21:
        $ position = position + 1
    jump changeBg

label sub:
    if position != 0 and position != 5 and position != 10 and position != 16:
        $ position = position - 1
    jump changeBg

label up:
    if position == 2:
        $ position = 7
    elif position == 7:
        $ position = 12
    elif position == 12:
        $ position = 18
    jump changeBg

label down:
    if position == 7:
        $ position = 2
    elif position == 12:
        $ position = 7
    elif position == 18:
        $ position = 12
    jump changeBg

label changeBg:
    $ renpy.jump("corridor_" + str(position))

label corridor_0:
    scene bg_0
    jump passing

label corridor_1:
    scene bg_1
    jump passing

label corridor_2:
    scene bg_2
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
    jump passing

label corridor_12:
    scene bg_12
    jump passing

label corridor_13:
    scene bg_13
    jump passing

label corridor_14:
    scene bg_14
    jump passing

label corridor_15:
    scene bg_15
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




