command = ""
started = False
while True: #this is an infinite loop, it will keep running until we break out of it, we replace the condition with True, so it will always be true, and we will use the break statement to exit the loop when the user wants to quit the game.
    command= input (">").lower() #this is called dry code, it stands for don't repeat yourself, it is a good practice to avoid repeating code
    if command == "start":
        if started:
            print("car is already started...    ")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("car is already stopped...    ")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game
             """ )
    elif command == "quit":
        print("Quitting the game...")
        break   
    else:
        print("I don't understand that...")