image img1 = "imgages/bg/temp_bg/bg_13.jpg"
scene img1

label fd_intro:
    scene placeholder2
    show monia at truecenter

    monika "Siema nowy"
    menu:
        "Jestem nowy (Tutorial)":
            monika "Wal sie"
            $ isNew = True
        "3 lata tu chodze":
            monika "Nie poznałam cie"
            $ isNew = False
    monika "A, z której jesteś klasy?"
    $ classNumber = renpy.input("Wpisz Klase:")
    monika "Dobrze, to idź już do szkoly. Za chwile zaczyna sie lekcja"
    hide monia


        

label fd_wild_somek1:

    "Wild somek appears"
    show slomek at slide_in_left_fast
    $ somekRep = 0
    if isNew:
        jump fd_somek_talk1
    else:
        menu:
            "Podejdź":
                jump fd_somek_talk1
            "Olej":
                jump afterSomek



label fd_somek_talk1:
    $ somekRep+=2
    somek "Siema, jestem Tomek Starczyński, przewodniczący szkoły."
    if isNew:
        somek "Jak się nazywasz?"
        $ playerName = renpy.input("Wpisz imię:")
    else:
        somek "Ciebie kojarzę z widzenia, jak masz na imię?"
        $ playerName = renpy.input("Wpisz imię:")
    
    


label fd_somek_talk2:
    somek "A, właśnie. Jak byś miał czas dzisiaj po lekcjach, to zapraszam na SKS'y z koszykówki. Możesz zapisać się u dowolnego nauczyciela WFu. Jesteś wysokiego, więc na pewno przydasz się do naszego zespołu. "
    python:
        quests.append("sksQuest")



label afterSomek:
    hide slomek
    "Hmm zostało 5 min do lekcji. Przejdę się po szkole"
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
    





label ssporonEncounter1:
    show ksporon at slide_in_left_slow
    "Dzień dobry czy mogłbym prosić klucze do sali 27?"
    ssporon "A z kim masz tam teraz lekcje?"
    "Z Profesorem Mroczkiem"
    ssporon "Dobrze to trzymaj"
    
label mrocznyBackWithKey:
    "Mam klucze do sali"
    "To dobrze"
    
    

    