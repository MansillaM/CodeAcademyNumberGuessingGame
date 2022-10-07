"""number_guessing module."""
import random

def check_answer_for_very_easy():
    """Function to check answer for the VERY EASY input()"""
    if int(VEASY) == int(randomNum):
        print("You got it on very easy, not impressive.")
    elif int(VEASY) > int(randomNum):
        print("Lower")
    elif int(VEASY) < int(randomNum):
        print("Higher")
    else:
        print("Heeeeu What?")

def check_answer_for_easy():
    """Function to check answer for the EASY input"""
    if int(EASY) == int(randomNum2):
        print("Easy mode, try a more challenging option.")
    elif int(EASY) > int(randomNum2):
        print("Lower")
    elif int(EASY) < int(randomNum2):
        print("Higher")
    else:
        print("Heeeeu What?")

def check_answer_for_medium():
    """"Function to check answer for the MEDIUM input"""
    if int(MEDIUM) == int(randomNum3):
        print("Good job! Now try a harder difficulty.")
    elif int(MEDIUM) > int(randomNum3):
        print("Lower")
    elif int(MEDIUM) < int(randomNum3):
        print("Higher")
    else:
        print("Heeeeu What?")

def check_answer_for_hard():
    """Function to check answer for the HARD input"""
    if int(HARD) == int(randomNum4):
        print("Wow you got it!")
    elif int(HARD) > int(randomNum4):
        print("Lower")
    elif int(HARD) < int(randomNum4):
        print("Higher")
    else:
        print("Heeeeu What?")

def check_answer_for_very_hard():
    """Function to check answer for the VERY HARD input"""
    if int(VERYHARD) == int(randomNum5):
        print("Incredible! You're a CHAMPION!")
    elif int(VERYHARD) > int(randomNum5):
        print("Lower")
    elif int(VERYHARD) < int(randomNum5):
        print("Higher")
    else:
        print("Heeeeu What?")

greet = input("Please choose a difficulty => Very Easy , Easy, Medium, Hard or Very Hard: ")

if greet == "Very Easy":
    print("You have chosen Very Easy, bahaha!")
    randomNum = random.randint(1,10)
    VEASY = int(0)
    while int(VEASY) != int(randomNum):
        VEASY = input("Choose a number between 1 and 10: ")
        check_answer_for_very_easy()
elif greet == "Easy":
    print("You have chosen Easy, what a rookie!")
    randomNum2 = random.randint(1, 10)
    EASY = int(0)
    for x in range(5):
        while int(EASY) != int(randomNum2):
            EASY = input("Choose a number between 1 and 10: ")
            check_answer_for_easy()
            break
        if x == 4 and int(EASY) != int(randomNum2):
            print("It's not that hard! Try again.")
elif greet =="Medium":
    print("You have chosen Medium, good luck!")
    randomNum3 = random.randint(1, 100)
    MEDIUM = int(0)
    for x in range(5):
        while int(MEDIUM) != int(randomNum3):
            MEDIUM = input("Choose a number between 1 and 100: ")
            check_answer_for_medium()
            break
        if x == 4 and int(MEDIUM) != int(randomNum3):
            print("It's okay keep trying!")
elif greet == "Hard":
    print("You have chosen Hard, I see you're up for a challenge!")
    randomNum4 = random.randint(1, 500)
    HARD = int(0)
    for x in range(8):
        while int(HARD) != int(randomNum4):
            HARD = input("Choose a number between 1 and 500: ")
            check_answer_for_hard()
            break
        if x == 7 and int(HARD) != int(randomNum4):
            print("Don't give up! You can do it.")
elif greet == "Very Hard":
    print("You have chosen Very Hard, what is wrong with you?")
    randomNum5 = random.randint(1, 1000)
    VERYHARD = int(0)
    for x in range(9):
        while int(VERYHARD) != int(randomNum5):
            VERYHARD = input("Choose a number between 1 and 1000: ")
            check_answer_for_very_hard()
            break
        if x == 8 and int(VERYHARD) != int(randomNum5):
            print("This is where the real ones are built! TRY AGAIN!")
else:
    print("Please type correctly! Relaunch the game")
