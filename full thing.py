# Name : Marc Fernando, Syed, and "Abram 2.0"
# Date: 3/8/2024
# Code of a story, gambling addiction gone wrong.


import random

#
Inventory = []
Money = []
Debt = []
Name = []

DIAMOND_CASINO_KEY_CHECK = []
casino1 = "Diamond_Casino"
casino2 = "Regular_Casino"
Home = "Home"


def main():  # INTRO
    Starting_money = 1000
    Money.append(Starting_money)
    debt = random.randrange(-20001, -10000)  # the amount of debt
    Debt.append(debt)
    x = input("What is your name? ")
    Name.append(x)  # APPENDS THE NAME TO THE GLOBAL LIST
    # INTRO HERE:
    print("\n\n---------------\n\n")
    print(f"""     With each passing day, the weight of {x} debts pressed down upon him,\n \
    threatening to suffocate him in a sea of despair. he had exhausted every avenue,\n \
    every possibility of escape of escape. But as teh walls closed in around him, one\n \
    last glimmer of hope beckoned from the shadows - the promise of quick riches through letting\n \
    the ods favor his life steadfast, otherwise known as gambling\n\n""")
    print(f"Starting money ${Starting_money}")
    print(f"Your debt $-{debt}")
    print("\n\n---------------""")

    def INVENTORY_OF_PLAYER():  # CHECKS INVENTORY OF PLAYER
        if len(Inventory) == 0:
            print("Your inventory is empty.")
            main_GUI(Starting_money)
        elif Money >= int(Debt) // 2:  # CODE DOES NOT WORKKKKKKK
            DIAMOND_CASINO_KEY_CHECK.append("TRUE")
            Inventory.append("DIAMOND_CASINO_KEY")
            main_GUI(Starting_money)

        else:
            print("You have the following items: ")
            for item in Inventory:
                print(item)
            main_GUI(Starting_money)

    def Number_Guesser():  # GAME OF GESSING A NUMBER GIVEN
        list_size = []

        # REWARD THE USER INPUTS
        reward_value = []

        cash_gambled = int(input("How much cash do you wanna wager? OR Q TO QUIT."))
        if cash_gambled == "Q" or "q":
            main_GUI(Starting_money)
        number_inlist = int(input(f"Hello! From 2-5 How Low Or High Do You Want Your Odds?\n "
                                  f"Note, higher number means higher payout!"))
        # APPENDS TO LIST (I think code can be simplified lmao)
        if number_inlist not in range(2, 6):
            print("Number not found.")
        elif number_inlist == 2:
            list_size.append(1)
            list_size.append(2)
            reward = 1.1
            reward_value.append(reward)
        elif number_inlist == 3:
            list_size.append(1)
            list_size.append(2)
            list_size.append(3)
            reward = 1.2
            reward_value.append(reward)
        elif number_inlist == 4:
            list_size.append(1)
            list_size.append(2)
            list_size.append(3)
            list_size.append(4)
            reward = 1.4
            reward_value.append(reward)
        elif number_inlist == 5:
            list_size.append(1)
            list_size.append(2)
            list_size.append(3)
            list_size.append(4)
            list_size.append(5)
            reward = 1.5
            reward_value.append(reward)
            # ERROR CHECKER?
        else:
            print("Enter a value given.")

        # AI CHOOSES FROM RANDINT OF (INCLUDED,NOT INCLUDED)
        AI_CHOOSES = random.randint(1, number_inlist)

        PLAYER_CHOOSES = int(input(f"Your odds are a 1 in {number_inlist} chance. What Number Do You Choose?"))
        if PLAYER_CHOOSES == AI_CHOOSES:
            print("Yippee!")
            # ADD FUNCTION OF WIN + ADD MONEY HERE
            cash_gambled * reward_value
            Money.append(cash_gambled)

        else:
            print("Lose. :(")
            # ADD FUNCTION OF LOSE + SUBTRACT MONEY HERE
            Money[0] -= cash_gambled
        Number_Guesser()

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
                PlayerInput = input(f"CHOOSE HERE - Rock, Paper, Scissors, or Q to QUIT: ")
                if PlayerInput in list:
                    return PlayerInput
                elif PlayerInput == "Q" or "q":
                    main_GUI(Starting_money)
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
                    # ADD MONEY WON HERE
                    return ("Player wins!")
                elif player_choice == 'Scissors' and computer_choice == 'Rock':
                    return ("Computer wins!")
                elif player_choice == 'Rock' and computer_choice == 'Scissors':
                    # ADD MONEY WON HERE
                    return ("Player wins!")

                elif player_choice == 'Paper' and computer_choice == 'Scissors':
                    return ("Computer wins!")
                elif player_choice == 'Scissors' and computer_choice == 'Paper':
                    # ADD MONEY WON HERE
                    return ("Player wins!")
                elif player_choice == 'Rock' and computer_choice == 'Paper':
                    # ADD MONEY WON HERE
                    return ("Player wins!")
                elif player_choice == 'Scissors' and computer_choice == 'Rock':
                    return ("Computer wins!")

                elif player_choice == 'Scissors' and computer_choice == 'Rock':
                    return ("Computer wins!")
                elif player_choice == 'Rock' and computer_choice == 'Scissors':
                    # ADD MONEY WON HERE
                    return ("Player wins!")
                elif player_choice == 'Scissors' and computer_choice == 'Paper':
                    # ADD MONEY WON HERE
                    return ("Player wins!")
                elif player_choice == 'Paper' and computer_choice == 'Scissors':
                    return ("Computer wins!")

            print(determine_winner(player_choice, computer_choice))
            main_GUI(Starting_money)

        rockpaperscissor()

    def plinko(start_money):  # one of the games to be played in the casino

        Values = [0.5, 1, 2, 3, 4, 5, 6]

        print(f"welcome to plinko\nHere you can bet however much money you want and the stakes are:\n")
        for i in Values:
            print(f"{i}x")  # gives the stakes in times(x)

        plinko_amt = int(input("\nenter how much you want to bet: "))
        strt_cash_plinko = start_money - plinko_amt

        if start_money <= 0:
            print("You have no money.")
        elif plinko_amt > start_money:
            print("not enough money")
        else:

            Values = random.choice(Values)
            print(f"\nRandom value landed on {Values}x")
            lost_or_gained = Values * plinko_amt

            if lost_or_gained < plinko_amt:  # if you lose something this is used to subtract money to your acocunt
                final_plinko_lost = strt_cash_plinko + lost_or_gained
                print(f"you lost ${lost_or_gained}")
                print(f"you now have ${final_plinko_lost}")
                return final_plinko_lost
            else:
                print(f"you gained ${lost_or_gained}")  # if you win something this is used to add money to your acocunt
                final_plinko = lost_or_gained + start_money
                print(f"you have a total of ${final_plinko}")
                return final_plinko




    def gameOVer():
        print("GAME OVER: INSERT GAME OVER STORYLINE TEXT HERE")

    def show_money():
        print(f"You have ${Starting_money:.2f} in your account")  # shows the person the amount of money in acocunt




    def main_GUI(Money):
        if str(Money) >= str(Debt):
            gameOVer()
        else:
            print(f"\n--------------------------")
            print("ACTIONS: G for Main Menu GUI")
            print("ACTIONS: I for Inventory (HINT: LOOK THROUGH IT OFTEN, IF YOU HAVE A KEY!?)")
            print("ACTIONS: Q to Quit (WILL END ALL PROGRESS)")
            print("ACTIONS: M to money in account")
            print("ACTIONS: D to Travel")
            print("--------------------------")
            print("ACTIONS: N for Number Guesser")
            print("ACTIONS: R for Rock Paper Scissors")
            print("ACTIONS: P for Plinko")

            ACTION_LIST = ["I", "Q", "D", "N", "R", "P", "G", "M"]
            Player_GUI_Choice = input("\nWhat do you wanna do? ").upper()

            if Player_GUI_Choice not in ACTION_LIST:
                print("ACTION NOT FOUND.")
                return main_GUI(Starting_money)
            elif Player_GUI_Choice == "I":
                INVENTORY_OF_PLAYER()

            elif Player_GUI_Choice == "G":
                print("---------------")
                for i in Name:
                    print(f"Name: {i}")
                print(f"Starting money ${Starting_money}")
                for i in Debt:
                    print(f"Your debt ${i}")

                x = input("Hit Y to Exit:")
                if x == "Y" or x == "y":
                    main_GUI(Starting_money)
                else:
                    print("Nah, get returned anyways.")
                    main_GUI(Starting_money)
                return
            elif Player_GUI_Choice == "Q":
                QUIT = input("WARNING! PROGRESS WONT BE SAVED. CONTINUE? (Y / N)")
                if QUIT == "Y":
                    return
                elif QUIT == "N":
                    main_GUI(Starting_money)
            elif Player_GUI_Choice == "D":
                intro_to_background()
            elif Player_GUI_Choice == "M":
                show_money()
            elif Player_GUI_Choice == "N":
                Number_Guesser()
            elif Player_GUI_Choice == "R":
                rockpaperscissors()
            elif Player_GUI_Choice == "P":
                plinko(Starting_money)
                Money = plinko(Money)
            else:
                print("Error.")

            main_GUI(Money)


    def intro_to_background():
        print("D for Diamond Casino.\nR for Regular Casino.\nH for Home.\n")

        casino1 = "Diamond_Casino"
        casino2 = "Regular_Casino"
        Home = "Home"

        PLACES_LIST_SELECTION = ["D", "R", "H"]
        PLACESS = input(f"Where do you wanna go?").upper()
        if PLACESS not in PLACES_LIST_SELECTION:
            print("ERROR, INPUT NOT IN OPTIONS.")
            intro_to_background()

        elif PLACESS == "D" and "DIAMOND_CASINO_KEY" in Inventory:
            # IF Money >= debt //2:
            print("INSERT CASINO1 INTRO")
            DIAMOND_CASINO_KEY_CHECK.append("TRUE")
            main_GUI(Starting_money)

        elif PLACESS == "R":
            print("INSERT CASINO2 INTRO")
            main_GUI(Starting_money)
        elif PLACESS == "H":
            print("INSERT home outro / game over")
            return
        else:
            print("ERROR. NOT IN SELECTION LIST, or you just dont have the key lmao.")
            intro_to_background()

    intro_to_background()


main()
