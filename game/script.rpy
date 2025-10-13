# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define chel = Character('Лёха', color="#7fff00")
define hp = 100
define score = 0

init python:
    import random
    import time

screen hp_counter():
    vbox:
        xalign 0.02
        yalign 0.02
        spacing 5
            
        text "Энергия: [hp] %":
            size 42
            color "#00ffff"
            bold True
            outlines [ (3, "#000000", 0, 0) ]

label start:

    scene orig
    show screen hp_counter

    play music "audio/goMusic.mp3" loop

    "Лёха решил пешком дойти до школы"
    show poker
    chel "я уже у порога школы"
    hide poker

    show smile
    chel "Хорошо погоняли на физкультуре в футбол"
    $ hp -= 10
    chel "Правда, немного устал"
    scene coridor 

    hide smile
    show poker
    chel "Что ж, сейчас будет пятиминутка по математике"
    chel "Со свнининой михайловной"
    hide poker

    show angry

    jump start_game
    return

screen variant(num1, num2):
    timer 5.0 action Return("0") 
    default user_input = ""

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 100  # отступы внутри фрейма
        ypadding 30
        vbox:
            spacing 20
            text "[num1] + [num2]" size 34
            input:
                value ScreenVariableInputValue("user_input")
                allow "0123456789"
            textbutton "Готово": 
                action Return(user_input)
                sensitive user_input != ""

label start_game:
    $ i = 0
    $ answer = ""

    while i < 5:
        $ num1 = random.randint(1, 10)
        $ num2 = random.randint(1, 10)
        $ sum = num1 + num2

        $ answer = renpy.call_screen("variant", num1=num1, num2=num2)
        i += 1
        $ res = int(answer)
        if answer == '0':
            hide smile
            show angry
            chel "Не успел"
        elif res == sum:
            hide angry
            show smile
            chel "Ура, правильный ответ"
        else:
            hide smile
            show angry
            chel "Бля, ошибся"
    jump after_math


# здесь идет после математики
label after_math:


    chel "Так, математика закончилась"


