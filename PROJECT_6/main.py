# Number guessing game

import random
import datetime
print("Welcome to Number guessing game \n     You only have 5 life \n    So ready for the Fight!")
date_pl = datetime.datetime.now()
DATE = date_pl.strftime("%y-%m-%d %H:%M")
chances = 1
while chances < 6:
        USER = int(input("Enter your guess between (1 to 10): "))
        COMPUTER = random.randint(1, 10)

        if USER in range (1,11):
            if USER > COMPUTER:
                print("Wrong answer! Try Lower Number")
                with open("/home/david/Documents/dev/python-playground/PROJECT_6/game.logs", "a") as Log:
                    Log.write(f"[{DATE}] User Entered {USER}\n")
                    Log.write(f"[{DATE}] Computer Entered {COMPUTER}\n")
                    Log.write(f"[{DATE}] rong answer! Try Lower Number \n")
            elif USER < COMPUTER:
                print("Wrong answer! Try Hgher Number ")
                with open("/home/david/Documents/dev/python-playground/PROJECT_6/game.logs", "a") as Log:
                    Log.write(f"[{DATE}] User Entered {USER}\n")
                    Log.write(f"[{DATE}] Computer Entered {COMPUTER}\n")
                    Log.write(f"[{DATE}] rong answer! Try Higer Number \n")
            elif USER == COMPUTER:
                print("You won")
                with open("/home/david/Documents/dev/python-playground/PROJECT_6/game.logs", "a") as Log:
                    Log.write(f"[{DATE}] User Entered {USER}\n")
                    Log.write(f"[{DATE}] Computer Entered {COMPUTER} \n")
                    Log.write(f"[{DATE}] ongratulation You Won \n")
                break

        else:
            print("Invalid Number")
            with open("/home/david/Documents/dev/python-playground/PROJECT_6/game.logs", "a") as Log:
                Log.write(f"[{DATE}] User Entered which is invalid {USER}\n")
        chances +=1
