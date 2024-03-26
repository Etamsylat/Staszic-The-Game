label matematyka_start:
    show nowak_book at top
    nowak "Dzień dobry wszystkim"
    klasa "Dzień dobry"
    nowak 'To zapiszczie sobie lekcje i temat "Powtórzenie wiadomości z rozdzialu 2"'
    nowak "To sprawdźmy sobie obecność"
    pause 3
    nowak "Dobrze, Kuba wylosuj kośćmi dyżurnych" 
    wermin "to dyżurnymi bedą nr 4 i 7"
    nowak "No i dobrze to teraz wylosuj ochotnika do tablicy" 
    wermin "nr 756"
    "No nie, to moj numer"
    nowak "O dawno nie byleś przy tablicy"
    nowak "Wybierz sobie podpunkt"
    menu:
        "a)":
            jump zadanie_a
        "b)":
            jump zadanie_b
        "c)":
            jump zadanie_c
        "d)":
            jump zadanie_d
        "e)":
            jump zadanie_e
        "f)":
            jump zadanie_f
        "x)":
            jump zadanie_x
            



label zadanie_a:
    $ answer1 = renpy.input("X =")
    if answer1 == "3":
        nowak "Wszystko jest dobrze"
        nowak "zasłużyłeś na pochwałę słowną"
    else:
        nowak "Nie tak to trzeba zrobić"
        nowak "Od odejmujemy 7 od obu stron równania, aby pozbyć się stałej dodawanej do 3x"
        nowak "Następnie dzielimy obie strony równania przez 3, aby znaleźć wartość x"
        nowak "Więc rozwiązaniem równania 3x + 7 = 16 jest x = 3"
        nowak "zostały 3 minuty więc ja dokończe to zadanie"
    jump matematyka_end
label zadanie_b:
    $ answer1 = renpy.input("X =")
    $ answer2 = renpy.input("Y =")
    if answer1 == "2" and answer2 == "1":
        nowak "Wszystko jest dobrze"
        nowak "zasłużyłeś na pochwałę słowną"
    else:
        nowak "Nie tak to trzeba zrobić"
        nowak "zostały 3 minuty więc ja dokończe to zadanie"
    jump matematyka_end
label zadanie_c:
    $ answer1 = renpy.input("f(2) =")
    if answer1 == "-1":
        nowak "Wszystko jest dobrze"
        nowak "zasłużyłeś na pochwałę słowną"
    else:
        nowak "Nie tak to trzeba zrobić"
        nowak "zostały 3 minuty więc ja dokończe to zadanie"
    jump matematyka_end
label zadanie_d:
    $ answer1 = renpy.input("k =")
    if answer1 == "8":
        nowak "Wszystko jest dobrze"
        nowak "zasłużyłeś na pochwałę słowną"
    else:
        nowak "Nie tak to trzeba zrobić"
        nowak "zostały 3 minuty więc ja dokończe to zadanie"
    jump matematyka_end
label zadanie_e:
    $ answer1 = renpy.input("X =")
    if answer1 == "30":
        nowak "Wszystko jest dobrze"
        nowak "zasłużyłeś na pochwałę słowną"
    else:
        nowak "Nie tak to trzeba zrobić"
        nowak "zostały 3 minuty więc ja dokończe to zadanie"
    jump matematyka_end
label zadanie_f:
    $ answer1 = renpy.input("X =")
    $ answer2 = renpy.input("Y =")
    if answer1 == "20" and answer2 == "20":
        nowak "Wszystko jest dobrze"
        nowak "zasłużyłeś na pochwałę słowną"
        nowak "Nie spodziewalem sie że sobie poradzisz"
    else:
        nowak "Nie tak to trzeba zrobić"
        nowak "zostały 3 minuty więc ja dokończe to zadanie"
    jump matematyka_end
label zadanie_x:
    $ answer1 = renpy.input("Odp =")
    if answer1 == "1415":
        nowak "Bardzo dobrze"
        nowak "A jaka bitwa miala miejsce w tym roku?"
        $ answer2 = renpy.input("A jaka bitwa miala miejsce w tym roku?").lower()
        if answer2 == "azincourt" or answer2 == "bitwa pod azincourt" or answer2 == "bitwa azincourt":
            nowak "Bardzo dobrze Dawid"
        else:
            nowak "Jak to nie wiesz?"
            nowak "Czego wy sie uczycie na historii"
            nowak "Przecież wiadomo że to Bitwa pod Azincourt" 
    else:
        "zastala niezreczna cisza"
        nowak "idź usiąść do lawki"
        nowak "zostały 3 minuty więc ja dokończe to zadanie"
    jump matematyka_end

    label matematyka_end:
       
        nowak "Dobrze zostalo nam 87,42 sekund lekcji wiec możecie sie spakowac"