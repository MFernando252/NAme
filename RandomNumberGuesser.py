#Code that determines a number that the user guesses

import random
def Number_Guesser():

    #SIZE OF THELIST GIVEN FROM USER INPUT.
    list_size = []

    number_inlist = int(input("Hello! From 2-5 How Low Or High Do You Want Your Odds? "))

    #APPENDS TO LIST (I think code can be simplified lmao)
    if number_inlist == 2:
        list_size.append(1)
        list_size.append(2)
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
    #ERROR CHECKER?
    else:
        print("Enter a value given.")

    #AI CHOOSES FROM RANDINT OF (INCLUDED,NOT INCLUDED)
    AI_CHOOSES = random.randint(1,number_inlist)
    PLAYER_CHOOSES = int(input(f"Your odds are a 1 in {number_inlist} chance. What Number Do You Choose?"))
    if PLAYER_CHOOSES == AI_CHOOSES:
        print("Yippee!")
        #ADD FUNCTION OF WIN + ADD MONEY HERE
    else:
        print("Lose. :(")
        #ADD FUNCTION OF LOSE + SUBTRACT MONEY HERE

Number_Guesser()
