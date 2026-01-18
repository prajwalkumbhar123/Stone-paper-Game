import random

def get_move_name(choice):
    if choice == 1: return "Stone"
    if choice == 2: return "Paper"
    if choice == 3: return "Scissors"
    return "Invalid"

print("What is Your choice : \n"
      "1. Stone \n"
      "2. Paper \n"
      "3. Scissors \n")

choice1 = int(input("Enter Your Choice (1, 2, or 3): "))
choice2 = int(input("Enter Your Choice (1, 2, or 3): "))
print(f"{get_move_name(choice1)} vs {get_move_name(choice2)}")

if choice1 == choice2:
    print("It's a Draw!")

elif choice1 == 1 and choice2 == 2:
    print("Paper Wins!")
elif choice1 == 2 and choice2 == 1:
    print("Paper Wins!")

elif choice1 == 1 and choice2 == 3:
    print("Stone Wins!")
elif choice1 == 3 and choice2 == 1:
    print("Stone Wins!")

elif choice1 == 2 and choice2 == 3:
    print("Scissors Wins!")
elif choice1 == 3 and choice2 == 2:
    print("Scissors Wins!")

else:
    print("Invalid Move!")