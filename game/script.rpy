


define monika = Character(name="monia")
define somek = Character(name="Tomek Starczyński")
define popi = Character(name="Małgorzata Popławska")
define ssporon = Character(name="Kazimierz Sporoń")
define mroczny = Character(name="Dariusz Mroczek")

define quests = []
define classNumber="2a"
init python:
    def goRight():
        # This function will be called when the button is clicked
        # Add your code here
        renpy.show("bg_2")
        
        pass  # Placeholder for your code
    def goLeft():
        # This function will be called when the button is clicked
        # Add your code here
        renpy.show("bg_1")
        
        pass  # Placeholder for your code

screen buttons():
    button:
        xalign 1.0
        yalign 0.5
        background Color("#FFFFFF")
        text "Click Me"
        action Jump("changeBg2")
    button:
        xalign 0.0
        yalign 0.5
        background Color("#FFFFFF")
        text "Click Me"
        action Jump("changeBg")




transform slide_in_left_fast:
    yalign 0.5
    xalign 0.0
    linear .1 xalign 0.5

transform slide_in_left_slow:
    yalign 0.5
    xalign 0.0
    linear 2 xalign 0.5


label changeBg:
    scene bg_1    
    jump passing

label changeBg2:
    scene bg_2  
    jump passing

label passing:
    monika "luj"


label start:
    show screen buttons
    
    jump fd_intro

