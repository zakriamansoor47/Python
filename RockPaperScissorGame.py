import random
from os import system
import opmodule
userwins = 0
cpuwins = 0

def checker(user, cpu):
    s = "rock"
    w = "paper"
    g = "scissor"
    system("cls")
    if user == cpu:
        print("|--- Round Draw! Both Choosed Same ---|")
        print(f"Your Choice: {user.capitalize()}     Computer Choice: {cpu.capitalize()}\n")
        global rounds
        global totalroundsplayed
        totalroundsplayed = totalroundsplayed -1
        rounds = rounds-1
    elif user == s and cpu == g or user == g and cpu == w or user == w and cpu == s:
        global userwins
        global userscores
        userwins = userwins+1
        userscores = int(userscores)+1
        print("|--- You win this round ---|")
        print(f"Your Choice: {user.capitalize()}     Computer Choice: {cpu.capitalize()}\n")
    elif user == g and cpu == s or user == w and cpu == g or user == s and cpu == w:
        global cpuwins
        global cpuscores
        cpuwins= cpuwins+1
        cpuscores = int(cpuscores)+1
        print("|--- Computer win this round ---|")
        print(f"Computer Choice: {cpu.capitalize()}     Your Choice: {user.capitalize()}\n")

rounds = 0
totalrounds = 5
totalroundsplayed = 0
winrounds = 3
userscores = 0
cpuscores = 0
characters = ["rock", "paper", "scissor","1","2","3"]

def gamesettings():
    global totalrounds
    global winrounds
    print("|--------: Game Settings :--------|")
    print("Total Rounds:", totalrounds)
    print("Rounds Needs to Win the Game:", winrounds)
    print("-----------------------------------")
    print("1: Set Total Rounds\n2: Set Rounds Need to Win\n0: Back to Main Menu")
    print("-----------------------------------")
    user = intvalue(0,2)
    if user == 1:
        system("cls")
        setrounds = int(input("|--- Enter Total Rounds ---|\n"))
        totalrounds = setrounds
        system("cls")
        gamesettings()
    elif user == 2:
        system("cls")
        setwinrounds = int(input("|--- Enter How Many Rounds Need to Win the Game ---|\n"))
        winrounds = setwinrounds
        system("cls")
        gamesettings()
    elif user == 0:
        system("cls")
        mainmenu()

def Game():
    global rounds, totalrounds, characters, userwins, cpuwins, winrounds, totalroundsplayed, cpuscores, userscores
    print(f"You Need to Win '{winrounds}' Rounds out of '{totalrounds}'")
    while(rounds!=totalrounds):
        cpuchoosed = random.choice(characters)
        if cpuchoosed == "1":
            cpuchoosed = "rock"
        elif cpuchoosed == "2":
            cpuchoosed = "paper"
        elif cpuchoosed == "3":
            cpuchoosed = "scissor"
        print("----------------------")
        print("Choose Your Character\n----------------------\n1: Rock\n2: Paper\n3: Scissor")
        user = opmodule.stringvalue(characters)
        if user.isnumeric():
            if user == "1":
                user = "rock"
            elif user == "2":
                user = "paper"
            elif user == "3":
                user = "scissor"
            checker(user, cpuchoosed)
        else:
            checker(user.lower(), cpuchoosed)
        rounds = rounds +1
        totalroundsplayed = int(totalroundsplayed)+1
        print(f"Total Rounds Played {rounds}/{totalrounds}")
        if rounds == totalrounds or userwins ==  winrounds or cpuwins == winrounds:
            if userwins > cpuwins: 
                winner = "User"
                scores = userwins
                print(f"---------------------------\nGame End and the Winner is '{winner}' with '{scores}' Scores")
            elif cpuwins > userwins:
                winner = "Computer"
                scores = cpuwins
                print(f"---------------------------\nGame End and the Winner is '{winner}' with '{scores}' Scores")
            else:
                print(f"---------------------------\nGame Draw! No one is Winner")
            print(f"Scores are:\nYou = {userwins}       Computer = {cpuwins}\n---------------------------\n")
            break

    writefile()
    print("Enter Any Thing to Goto Main Menu")
    lol = input()
    if lol != "" or lol == "":        
        rounds = 0
        userwins = 0
        cpuwins = 0
        mainmenu()            

def readfile():
    global totalroundsplayed, userscores, cpuscores
    u = open("RockPaperScissorScores.txt", "r")
    list1 = u.read().splitlines()
    u.close()
    totalroundsplayed = int(list1[0])
    userscores = int(list1[1])
    cpuscores = int(list1[2])
    return 0

def writefile():
    global totalroundsplayed, userscores, cpuscores
    w = open("RockPaperScissorScores.txt", "w")
    w.write(f"{totalroundsplayed}\n")
    w.write(f"{userscores}\n")
    w.write(f"{cpuscores}\n")
    w.close()
    return 0

def intvalue(min, max):
    while(True):
        try:
            value = int(input())
            if value < min:
                print("Wrong Input! Please Enter a Vaild Number")
                continue
            elif value > max:
                print("Wrong Input! Please Enter a Vaild Number")
                continue
            else:
                return value
        except:
            print("Wrong Input! Please Enter a Integer Value")
            continue

def winscores():
    system("cls")
    global totalroundsplayed
    global userscores
    global cpuscores
    if userscores > cpuscores:
        winner1 = "User"
    elif cpuscores > userscores:
        winner1 = "Computer"
    else:
        winner1 = "NO ONE"
    print("------------------------------------------------")
    print("|---------->      Scores Sheet      <----------|")
    print("------------------------------------------------")
    print(f"            Total Rounds Played: {int(totalroundsplayed)}")
    print(f"                 Your Wins: {int(userscores)}\n               Computer Wins: {int(cpuscores)}")
    print(f"               Winner: {winner1}")
    print("------------------------------------------------")
    print("\n0: Back\n1: Reset Scores")
    user = intvalue(0, 1)
    if user == 0:
        mainmenu()
    elif user == 1:
        totalroundsplayed = 0
        userscores = 0
        cpuscores = 0
        writefile()
        system("cls")
        winscores()
    return 0

def mainmenu():
    system("cls")
    print("--------------------------------------")
    print("| Welcome to Rock Paper Scissor Game |")
    print("--------------------------------------\n")
    print("1: Play Game\n2: Scores\n3: Settings\n4: Exit")
    readfile()
    user1 = intvalue(1,4)
    if user1 == 1:
        system("cls")
        Game()
    elif user1 == 2:
        winscores()
    elif user1 == 3:
        system("cls")
        gamesettings()
    elif user1 == 4:
        system("cls")
        print("Do you really want to Exit the Game? 1 = Yes, 0 = No")
        user2 = intvalue(0, 1)
        if user2 == 1:
            system("cls")
        elif user2 == 0:
            system("cls")
            mainmenu()

mainmenu()

