import random
import os
inventory = []
def main():
    Starting_money = 1000  # how much u money start with





    def plinko(start_money): #one of the games to be played in the casino

        Values = [0.5, 1, 2, 3, 4, 5, 6]

        print(f"welcome to plinko\nHere you can bet however much money you want and the stakes are:")
        for i in Values:
            print(f"{i}x")  # gives the stakes in times(x)

        plinko_amt = int(input("\nenter how much you want to bet: "))

        if start_money < 0:
            print("You have no money.")
        elif plinko_amt >= start_money:
            print("not enough money")
        else:

            Values = random.choice(Values)
            print(f"\nRandom value landed on {Values}x")
            lost_or_gained = Values * plinko_amt
            if lost_or_gained < plinko_amt:
                print(f"you lost ${lost_or_gained}")

            else:
                print(f"you gained ${lost_or_gained}")
                final_plinko = lost_or_gained + start_money
                print(f"you have a total of ${final_plinko}")

            strt_cash_plinko = start_money - plinko_amt


    games_at_VegasCasino = ["plinko", "rock paper siccor"]

    debt = random.randrange(-20001, -10000) #the amount of debt
    Has_money = True
    name = input("Whats your name: ")
    os.system("cls") #clears screen




    print("---------------\n\n")

    print(f"     with each passing day, the weight of {name} debts pressed down upon him,\n \
    threatening to suffocate him in a sea of despair. he had exhausted every avenue,\n \
    every possibility of escape of escape. But as teh walls closed in around him, one\n \
    last glimmer of hope beckoned from the shadows - the promise of quick riches through letting\n \
    the ods favor his life steadfast, otherwise known as gambling\n\n")

    print(f"Starting money: ${Starting_money}")
    print(f"Your debt: ${debt}")



    print("\n---------------")  # intro
    print("Press H to go home or C to start gambling\n")





    def show_money():
        print(f"You have ${Starting_money} in your account") #shows the person the amount of money in acocunt

    start = True
    while start == True:
        choice = input(f"\nWhat would you like to do {name}?").lower()
        if choice == "m":
            show_money()
        elif choice == "h":
            print("you saved your life by being a good person but died becuase of the stress from the amount of debt")
            break
        elif choice == "c":
            print("These are the games available: ")
            for i in games_at_VegasCasino:
                print(i)
            game_choice = input("What would you like to play? Press P for plinko or R for rock paper siccor ").lower()
            if game_choice == "p":
                plinko(Starting_money)
























main()








