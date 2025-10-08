# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define chel = Character('Лёха', color="#013220")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene orig


    play music "audio/goMusic.mp3" loop

    "Лёха решил пешком дойти до школы"
    show loh
    chel "я уже у порога школы"
    hide loh

    "Прошёл урок математики и началась перемена"

    scene coridor 

    show loh happy
    chel "у меня в кармане есть 20 рублей, куплю себе булочку с сахаром"
    hide loh happy
   
    return
