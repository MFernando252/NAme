import random

Inventory = []
Money = []
Debt = []

casino1 = "Diamond_Casino"
casino2 = "Regular_Casino"
Home = "Home"

if len(Inventory) == 0:
    print("Your inventory is empty.")
elif "DIAMOND_CASINO_KEY" in Inventory:
    casino1()
else:
    print("You have the following items: ")
    for item in Inventory:
        print(item)

def main():
    Starting_money = 1000
    Money.append(Starting_money)
    debt = random.randint(10000, 20000)
    Debt.append(debt)
    Has_money = True
    x = input("What is your name?  ")
    print("---------------")
    print(f"Name: {x}")
    print(f"Starting money ${Starting_money}")
    print(f"Your debt $-{debt}")

    print("")
    print("---------------")


    def intro_to_background():
        print("Where do you wanna go?")
        casino1 = "Diamond_Casino"
        casino2 = "Regular_Casino"
        Home = "Home"
        input(f"PLACES TO GO TO: {casino1},{casino2},{Home}")
        if casino1 and "DIAMOND_CASINO_KEY" in Inventory:
            #IF Money >= debt //2:
           print("INSERT CASINO1 INTRO")

        elif casino2:
            print("INSERT CASINO2 INTRO")
        elif Home:
            print("INSERT home INTRO")


    def Casino_Key_Check():
        if Money >= Debt //2:
            Inventory.append("DIAMOND_CASINO_KEY")
            return
        else:
            return

    def Number_Guesser():
        # SIZE OF THELIST GIVEN FROM USER INPUT.
        list_size = []

        number_inlist = int(input("Hello! From 2-5 How Low Or High Do You Want Your Odds? "))

        # APPENDS TO LIST (I think code can be simplified lmao)
        if number_inlist not in range(2,6):
            print("Number not found.")
        elif number_inlist == 2:
            list_size.append(1)
            list_size.append(2)
            reward = 30
            print(list_size)
        elif number_inlist == 3:
            list_size.append(1)
            list_size.append(2)
            list_size.append(3)
            print(list_size)
        elif number_inlist == 4:
            list_size.append(1)
            list_size.append(2)
            list_size.append(3)
            list_size.append(4)
            print(list_size)
        elif number_inlist == 5:
            list_size.append(1)
            list_size.append(2)
            list_size.append(3)
            list_size.append(4)
            list_size.append(5)
            print(list_size)
        # ERROR CHECKER?
        else:
            print("Enter a value given.")

        # AI CHOOSES FROM RANDINT OF (INCLUDED,NOT INCLUDED)
        AI_CHOOSES = random.randint(1, number_inlist)
        PLAYER_CHOOSES = int(input(f"Your odds are a 1 in {number_inlist} chance. What Number Do You Choose?"))
        if PLAYER_CHOOSES == AI_CHOOSES:
            print("Yippee!")
            # ADD FUNCTION OF WIN + ADD MONEY HERE

        else:
            print("Lose. :(")
            # ADD FUNCTION OF LOSE + SUBTRACT MONEY HERE


    def rockpaperscissors():
        def rockpaperscissor():
            list = ["Rock", "Paper", "Scissors"]

            def print_game_rules():
                print(f"The rules are simple!")
                print("--------------------------")
                print("Rock Beats Scissors")
                print("Rock Loses to Paper ")
                print("Paper Beats Rock")
                print("Paper Loses to Scissors ")
                print("Scissors Beats Paper")
                print("Scissors Loses to Rock ")
                print("....Anything else ties!")
                print("--------------------------")

            print_game_rules()

            def get_player_choice():
                # Ask the user for their choice (rock, paper, scissors)
                PlayerInput = input(f"CHOOSE HERE - Rock, Paper, Scissors: ")
                if PlayerInput in list:
                    return PlayerInput
                else:
                    print("Choose something in the list. Mind the Caps.")
                    get_player_choice()

            player_choice = get_player_choice()

            def get_AI_choice():
                return random.choice(list)

            computer_choice = get_AI_choice()

            def determine_winner(player_choice, computer_choice):

                if player_choice == computer_choice:
                    return ("Tie!")
                elif player_choice == 'Rock' and computer_choice == 'Paper':
                    return ("Computer wins!")
                elif player_choice == 'Paper' and computer_choice == 'Rock':
                    return ("Player wins!")
                elif player_choice == 'Scissors' and computer_choice == 'Rock':
                    return ("Computer wins!")
                elif player_choice == 'Rock' and computer_choice == 'Scissors':
                    return ("Player wins!")

                elif player_choice == 'Paper' and computer_choice == 'Scissors':
                    return ("Computer wins!")
                elif player_choice == 'Scissors' and computer_choice == 'Paper':
                    return ("Player wins!")
                elif player_choice == 'Rock' and computer_choice == 'Paper':
                    return ("Player wins!")
                elif player_choice == 'Scissors' and computer_choice == 'Rock':
                    return ("Computer wins!")

                elif player_choice == 'Scissors' and computer_choice == 'Rock':
                    return ("Computer wins!")
                elif player_choice == 'Rock' and computer_choice == 'Scissors':
                    return ("Player wins!")
                elif player_choice == 'Scissors' and computer_choice == 'Paper':
                    return ("Player wins!")
                elif player_choice == 'Paper' and computer_choice == 'Scissors':
                    return ("Computer wins!")

            print(determine_winner(player_choice, computer_choice))


        rockpaperscissor()

    rockpaperscissors()




    #def plinko():




    #def gameOVer():



main()
