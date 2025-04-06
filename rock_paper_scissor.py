import random

def start_game():
    user = int(input("Enter your choice, 0 for Rock, 1 for paper and 2 for scissor:"))
    computer = [0,1,2]
    comp_choice = random.choice(computer)
    print(f"Your choice:{user} \nComputer's choice:{comp_choice}")

    #When user selects 0
    if user == 0 and comp_choice == 0:
        print("It's a Draw.")
    elif user == 0 and comp_choice == 1:
        print("You lose:(")
    elif user == 0 and comp_choice == 2:
        print("You Win!")
        
    #When user selects 1
    if user == 1 and comp_choice == 0:
        print("You Win!")
    elif user == 1 and comp_choice == 1:
        print("It's a Draw.")
    elif user == 1 and comp_choice == 2:
        print("You Lose:(")

    #When user selects 2
    if user == 2 and comp_choice == 0:
        print("You Lose:(")
    elif user == 2 and comp_choice == 1:
        print("Yo Win!")
    elif user == 2 and comp_choice == 2:
        print("It's a Draw.")