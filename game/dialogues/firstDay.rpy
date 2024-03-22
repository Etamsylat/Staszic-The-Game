label fd_intro:
    scene bg_24
    $ position = 24
    "Podchodzi do ciebie Tomek Starczyński, czlonek samorządu naszej wspanalej szkoly"
    show starczynski_t at slide_in_left_fast 
    play audio announcement_sound
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
    somek "Jestesmy wlasnie przed szkolą."
    somek "Na prawo jest wejscie do szkoly, a lewo semgment WF'u."
    scene bg_7
    $ position = 7
    show starczynski_t at slide_in_left_fast
    play audio announcement_sound
    somek "Teraz znajdujemy sie na parterze."
    somek "Znajdziesz tu Biblioteke i Gabinet Higienistki"
    scene bg_12
    $ position = 12
    show starczynski_t at slide_in_left_fast
    play audio announcement_sound
    somek "Weszlismy na Pierwsze Pietro."
    somek "Na lewo jest Pokój Nauczycielski wraz z Sekretariatem."
    scene bg_19
    $ position = 19
    show starczynski_t at slide_in_left_fast
    play audio announcement_sound
    somek "Doszliśmy na Drugie Pietro"
    somek "Jest tu nasza Aula i Golebnik"
    scene bg_2
    $ position = 2
    show starczynski_t at slide_in_left_fast
    play audio announcement_sound
    somek "Na końec zeszlismy na pólpietro"
    somek "To chyba wszystko co mialem Ci do pokazania"
    jump intro_name_class
        
label intro_name_class:
    somek "To Jak masz na imie?"
    $ playerName = renpy.input("Wpisz imię:")
    somek "A, z której jesteś klasy?"
    $ classNumber = renpy.input("Wpisz Klase:")
    jump intro_sksQuest

label intro_sksQuest:
    somek "A, właśnie. Jak byś miał czas dzisiaj po lekcjach, to zapraszam na SKS'y z koszykówki. Możesz zapisać się u dowolnego nauczyciela WFu. Jesteś wysokiego, więc na pewno przydasz się do naszego zespołu. "
    somek "Dobra. Milo Cie bylo poznać, ale ide juz na lekcje."
    somek "Powodzenia"
    hide starczynski_t
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
    show sporon_m at truecenter
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
    call hide_buttons
    "Dzień dobry czy mogłbym prosić klucze do sali 27?"
    ssporon "A z kim masz tam teraz lekcje?"
    "Z Profesorem Mroczkiem"
    ssporon "Dobrze to trzymaj"
    
    "Otrzymano klucz z sali 27"
    python:
        inventory_items.append("key")
        quests.remove("mrokQuest")
        quests.append("mrokQuest2")
    hide ksporon
    call show_buttons
    jump passing
    
label mrocznyBackWithKey:
    show sporon_m at truecenter
    python:
        inventory_items.remove("key")
        quests.remove("mrokQuest2")
        quests.append("mrokQuestDone")
        
    "Mam klucze do sali"
    mroczny "To dobrze"
    mroczny "Zaraz zadzwoni. Wchodźmy do klasy"
    jump passing
    