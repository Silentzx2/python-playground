# This is the first project of python
import random
"""
1 for snake
-1 for water
0 for gun

"""

computer = random.choice([-1, 0, 1])
user = input("Enter s for snake, w for water and g for gun: ").lower()
user_dict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "snake", -1: "water", 0: "gun"}
if user not in user_dict:
    print("Invalid input!")
    exit()
younum = user_dict[user]
print(f"You chose {reverse_dict[younum]} and computer chose {reverse_dict[computer]}")
if computer == younum:
    print("It's a tie!")    

else:                 
    if (computer == -1 and younum == 1):
        print("You win")    
    elif (computer == 1 and younum == -1):
        print("Computer wins")
    elif (computer == 0 and younum == 1):
            print("Computer wins")
    elif (computer == 1 and younum == 0):
        print("You win")
    elif (computer == 0 and younum == -1):
        print("You win")
    elif (computer == -1 and younum == 0):
        print("Computer wins")