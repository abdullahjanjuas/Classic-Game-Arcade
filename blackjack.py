import random

def start_game():
    cont = True
    while cont:
        #List of cards for user and computer
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        player = []
        comp = []
        random_elements1 = random.sample(cards,2)
        random_elements2 = random.sample(cards,2)
        for elements in random_elements1:
            player.append(elements)
        for elements in random_elements2:
            comp.append(elements)

        #Display computer's first card 
        print("Computer's first card: ",comp[0])

        #Take user's choice and display the cards
        choice = input("Type \'y\' to get another card or type \'n\' to pass: ").lower()
        if choice == 'y':
            player.append(random.choice(cards))
        
        print(f"Your final hand: {player}")
        print(f"Computer's final hand: {comp}")

        #Calculating scores
        sum_1 = 0
        sum_2 = 0 
        for elements in player:
            sum_1 += elements
        for elements in comp:
            sum_2+= elements

        #Adjusting for aces
        if sum_1+11>21 or sum_2+11>21:
            cards[0] = 1

        #Conditions to check for win or lose
        if sum_1 > 21:
            print("You Lose. Your score exceeds 21")

        elif sum_1<=21:
        
            while sum_2 < 17:
                sum_2 = 0 
                comp.append(random.choice(cards))
                for elements in comp:
                    sum_2 += elements
                print("Computer's score was less than 17 so adding another card...")
                print(f"Computer's final hand now after another card is: {comp}")
        

            if sum_2>21:
                print("You Win. Computer's score exceeds 21")
            if sum_1 == sum_2:
                print("It's a draw")
            elif sum_1 > sum_2:
                print("You win")
            elif sum_1 < sum_2 and sum_2<=21:
                print("You lose")

        #Ask the user for a rematch
        rematch = input("Would you like to play again? Type \'y\' or \'n\': ").lower()
        if rematch == 'y':
            print("Let's play again")
            cont = True
        else:
            print("Thanks for playing.Goodbye :)")
            cont = False
        
    
