cammand = ""
started = False
while True:
    cammand = input(">>>>>")
    if cammand == "start":
        if started == True:
            print("car is already started !!!..............")
        else:
            started = True
            print("car started.......")
    elif cammand == "stop":
        if not started:
            print("car is already stopped !!!!!!!.......")
        else:
            started = False
            print("car stopped..........")
    elif cammand == "quite":
        break
    elif cammand == "help":
        print("""
    start :- to start car
    stop :- to stop car
    quite :- to quite the game """)
    else:
        print("hey ! I didn't understand what you want !!!")
print("game over !!!!")
