define position = 0

label add:
    $ position = position + 1
    jump changeBg

label sub:
    $ position = position - 1
    jump changeBg

label changeBg:
    $ renpy.jump("corridor_" + str(position))

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

label corridor_7:
    scene bg_7

label corridor_8:
    scene bg_8

label corridor_9:
    scene bg_9

label corridor_10:
    scene bg_10

label corridor_11:
    scene bg_11

label corridor_12:
    scene bg_12

label corridor_13:
    scene bg_13

label corridor_14:
    scene bg_14

label corridor_15:
    scene bg_15

label corridor_16:
    scene bg_16

label corridor_17:
    scene bg_17

label corridor_18:
    scene bg_1

label corridor_19:
    scene bg_19

label corridor_20:
    scene bg_20

label corridor_21:
    scene bg_21

label corridor_22:
    scene bg_22

label corridor_23:
    scene bg_23

label corridor_24:
    scene bg_24

label corridor_25:
    scene bg_25

label corridor_26:
    scene bg_26



