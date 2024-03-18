image img1 = "imgages/bg/temp_bg/bg_13.jpg"
scene img1

label fd_intro:
    scene bg_2
    $ position = 2
    "Podchodzi do ciebie Tomek Starczyński, czlonek samorządu naszej wspanalej szkoly"
    show slomek at slide_in_left_fast
    somek "Siema, jesteś nowy?"
    menu:
        "Tak, jestem nowy (Tutorial)":
            somek "Wal sie"
            somek "To chodź. Oprowadze Cie po szkole"
            jump tutorial
        "Nie jestem nowy":
            somek "O, sorry. Nie widzialem Cie wczesniej"
            $ isNew = False

    jump intro_name_class

label tutorial:
        
label intro_name_class:
    somek "To Jak masz na imie?"
    $ playerName = renpy.input("Wpisz imię:")
    somek "A, z której jesteś klasy?"
    $ classNumber = renpy.input("Wpisz Klase:")
    jump intro_sksQuest

label intro_sksQuest:
    somek "A, właśnie. Jak byś miał czas dzisiaj po lekcjach, to zapraszam na SKS'y z koszykówki. Możesz zapisać się u dowolnego nauczyciela WFu. Jesteś wysokiego, więc na pewno przydasz się do naszego zespołu. "
    python:
        quests.append("sksQuest")
    jump intro_end

label intro_end:
    hide slomek
    "Hmm zostało 5 min do lekcji. Przejdę się po szkole"
    call show_buttons
    jump passing

label mrok_quest:
    call hide_buttons
    show mrok at slide_in_left_slow
    mroczny "Ej ty, Ty jesteś z klasy [classNumber]?"
    $ mrokRep = 0
    menu:
        "Tak":
            mroczny "To weź mi podejdź do pokoju nauczycielskiego po klucze do sali 27."
        "Nie":
            $ mrokRep-=2
            mroczny "Nie żartuj sobie. Wiem że jesteś. Zdobadź mi klucze do sali 27"
    python:
        quests.append("mrokQuest")
    hide mrok
    call show_buttons
    jump passing
    

label ssporonEncounter1:
    show ksporon at slide_in_left_slow
    "Dzień dobry czy mogłbym prosić klucze do sali 27?"
    ssporon "A z kim masz tam teraz lekcje?"
    "Z Profesorem Mroczkiem"
    ssporon "Dobrze to trzymaj"
    
    "Otrzymano klucz z sali 27"
    jump passing
    
label mrocznyBackWithKey:
    "Mam klucze do sali"
    "To dobrze"
    jump passing
    