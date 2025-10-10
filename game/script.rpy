# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define chel = Character('Лёха', color="#7fff00")
define hp = 100
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

screen hp_counter():
    vbox:
        xalign 0.02
        yalign 0.02
        spacing 5
            
        text "сытость: [hp] %":
            size 42
            color "#00ffff"
            bold True
            outlines [ (3, "#000000", 0, 0) ]

label start:

    scene orig
    show screen hp_counter

    play music "audio/goMusic.mp3" loop

    "Лёха решил пешком дойти до школы"
    show loh
    chel "я уже у порога школы"
    hide loh

    "Прошёл урок математики и началась перемена"
    $ hp -= 10
    scene coridor 

    show loh happy
    chel "у меня в кармане есть 20 рублей, куплю себе булочку с сахаром"
    hide loh happy

    show gandon
    chel "Щас пизды перескокову дам"
   
    return
