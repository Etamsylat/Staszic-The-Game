


define monika = Character(name="monia")
define somek = Character(name="Tomek Starczyński")
define popi = Character(name="Małgorzata Popławska")
define ssporon = Character(name="Kazimierz Sporoń")
define mroczny = Character(name="Dariusz Mroczek")

define quests = []
define classNumber="2a"

transform slide_in_left_fast:
    yalign 0.5
    xalign 0.0
    linear .1 xalign 0.5

transform slide_in_left_slow:
    yalign 0.5
    xalign 0.0
    linear 2 xalign 0.5




label start:
    jump fd_intro