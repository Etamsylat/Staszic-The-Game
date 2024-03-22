label intoSks1:
    show monia
    show kucin
    monika "O! Witaj ponownie [playerName]!"
    "Chciałem zapisać się na SKSy z koszykówki"
    monika "O jak dobrze, akurat wypadł nam zawodnik z głównej drużyny, więc znajdzie się miejsce dla ciebie."
    monika "no i świetnie jestes w drużynie"
    python:
        quests.remove("sksQuest")
        quests.append("sksQuestDone")
    hide monia
    hide kucin
    jump passing

