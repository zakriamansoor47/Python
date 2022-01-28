import random
from re import I
import opmodule
from os import system

guess = 0
minguess = 0
maxguess = 100
totalguess = 5

def gamesettings():
    global guess, minguess, maxguess,totalguess
    print("|--------: Game Settings :--------|")
    print(f"Total Guess: {totalguess}")
    print(f"Minimum Guess Number: {minguess}")
    print(f"Maximum Guess Number: {maxguess}")
    print("-----------------------------------")
    print("1: Set Total Guess\n2: Set Min and Max Guess Number\n0: Back to Main Menu")
    print("-----------------------------------")
    user = opmodule.intvalue(0,2)
    if user == 1:
        system("cls")
        setguess = int(input("|--- Enter Total Guess ---|\n"))
        totalguess = setguess
        system("cls")
        gamesettings()
    elif user == 2:
        system("cls")
        setminguess = int(input("|--- Enter Minimum Guess Number ---|\n"))
        minguess = setminguess
        setmaxguess = int(input("|--- Enter Maximum Guess Number ---|\n"))
        maxguess = setmaxguess
        system("cls")
        gamesettings()
    elif user == 0:
        system("cls")
        mainmenu()


def Game():
    global guess, minguess, maxguess,totalguess
    num = random.randint(minguess,maxguess)
    print("---------------------------------------------------------------------------")
    print("               Welcome to 'Guess a Number' Game               ")
    print(f"   Guess a Number which is Greater then '{minguess}' and less then '{maxguess}'   ")
    print(f"             You have '{totalguess}' Guesses to WIN the Game             ")
    print("---------------------------------------------------------------------------\n")
    while(True):
        try:
            user = int(input("Entre a Number : "))
            guess = guess +1
            if user == num:
                print("---------------------------------------------------------------")
                print(f"|===> Horay! You WIN the Game by Guesseing {guess} times <===|")
                print("---------------------------------------------------------------\n")
                break
            else:
                if guess >= totalguess:
                    print("-----------------------------------------")
                    print("|-----> Game Over! Out of Guesses <-----|")
                    print("-----------------------------------------\n")
                    break
                if user < num:
                    print("Your Entered Number is Less then the Given Guess Number! Please Increase Your Number")
                elif user > num:
                    print("Your Entered Number is Greater then the Given Guess Number! Please Decrease Your Number")
                print("Number of Guesses Left :", totalguess-guess)
                continue
        except:
            print("Wrong Input! Please Enter a Integer Number")
            continue
    print("Enter Any Thing to Goto Main Menu")
    lol = input()
    if lol != "" or lol == "":        
        guess = 0
        mainmenu()     

def mainmenu():
    system("cls")
    print("----------------------------------------------------------------")
    print("|               Welcome to 'Guess a Number' Game               |")
    print("----------------------------------------------------------------\n")
    print("1: Play Game\n2: Settings\n3: Exit")
    user1 = opmodule.intvalue(1,3)
    if user1 == 1:
        system("cls")
        Game()
    elif user1 == 2:
        system("cls")
        gamesettings()
    elif user1 == 3:
        system("cls")
        print("Do you really want to Exit the Game? 1 = Yes, 0 = No")
        user2 = opmodule.intvalue(0, 1)
        if user2 == 1:
            system("cls")
        elif user2 == 0:
            system("cls")
            mainmenu()

mainmenu()