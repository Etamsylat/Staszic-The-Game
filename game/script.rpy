﻿


define monika = Character(name="monia")
define somek = Character(name="Tomek Starczyński")
define popi = Character(name="Małgorzata Popławska")
define ssporon = Character(name="Kazimierz Sporoń")
define mroczny = Character(name="Michał Sporoń")
define nowak = Character(name="Dariusz Nowak")
define klasa = Character(name="Klasa")
define wermin = Character(name="Kuba")




define bg_name = ""

define classNumber="2a"


screen button_right():
    button:
        xalign 1.0
        yalign 0.5
        background Color("#66cc00")
        text "Right"
        action Jump("add")
screen button_left():
    button:
        xalign 0.0
        yalign 0.5
        background Color("#66cc00")
        text "Left"
        action Jump("sub")
screen button_up():
    button:
        xalign 0.5
        yalign 0.0
        background Color("#66cc00")
        text "Up"
        action Jump("up")
screen button_down():
    button:
        xalign 0.5
        yalign 0.7
        background Color("#66cc00")
        text "Down"
        action Jump("down")




transform slide_in_left_fast:
    
    yalign 0.5
    xalign 0.0
    linear .1 xalign 0.5

transform slide_in_left_slow:
    yalign 0.5
    xalign 0.0
    linear 2 xalign 0.5


label passing:
    monika "[position]"
    jump passing


label start:
    
    play music vntrack01 volume 0.2
    jump fd_intro

