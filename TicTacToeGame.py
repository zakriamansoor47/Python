from os import system
import random
import opmodule
import numpy

numberofturns = 0
userscores = 0
cpuscores = 0
firstturn = ""
turn = ""
gamem = ""
winner = ""
user1char = ""
user2char = ""
cpuchar = ""
cpuchoice = ""
characters = ["X", "O"]
address = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " ",]
    ] 

def showboard():
    global board
    print("    A   B   C ")
    print("   -----------")
    print(f"1:  {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("   -----------")
    print(f"2:  {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("   -----------")
    print(f"3:  {board[2][0]} | {board[2][1]} | {board[2][2]} ")




def winningconditions():
    global board,characters,cpuchar,user1char, winner, user2char
    # first check 'X' in every coloumn of any Row
    if "X" in board[0][0] and "X" in board[0][1] and "X" in board[0][2] or "X" in board[1][0] and "X" in board[1][1] and "X" in board[1][2] or "X" in board[2][0] and "X" in board[2][1] and "X" in board[2][2]:
        if cpuchar == "X":
            winner = "cpu"
        elif user2char == "X":
            winner = "user2"
        elif user1char == "X":
            winner = "user"
    # then check 'O' in every coloumn of any Row
    elif "O" in board[0][0] and "O" in board[0][1] and "O" in board[0][2] or "O" in board[1][0] and "O" in board[1][1] and "O" in board[1][2] or "O" in board[2][0] and "O" in board[2][1] and "O" in board[2][2]:
        if cpuchar == "O":
            winner = "cpu"
        elif user2char == "O":
            winner = "user2"
        elif user1char == "O": 
            winner = "user"
    # After that we check 'X' in every row of any Column
    elif "X" in board[0][0] and "X" in board[1][0] and "X" in board[2][0] or "X" in board[0][1] and "X" in board[1][1] and "X" in board[2][1] or "X" in board[0][2] and "X" in board[1][2] and "X" in board[2][2]:
        if cpuchar == "X":
            winner = "cpu"
        elif user2char == "X":
            winner = "user2"
        elif user1char == "X":
            winner = "user"
    # After that we check 'O' in every row of any Column
    elif "O" in board[0][0] and "O" in board[1][0] and "O" in board[2][0] or "O" in board[0][1] and "O" in board[1][1] and "O" in board[2][1] or "O" in board[0][2] and "O" in board[1][2] and "O" in board[2][2]:
        if cpuchar == "O":
            winner = "cpu"
        elif user2char == "O":
            winner = "user2"
        elif user1char == "O":
            winner = "user"
    # board = [                         board = [
    # ["X", " ", " "],                 [" ", " ", "X"],
    # [" ", "X", " "],     or          [" ", "X", " "],
    # [" ", " ", "X",]                 ["X", " ", " ",]
    # ]                                 ]
    # After that we check 'X' in multiply case
    elif "X" in board[0][0] and "X" in board[1][1] and "X" in board[2][2] or "X" in board[2][0] and "X" in board[1][1] and "X" in board[0][2]:
        if cpuchar == "X":
            winner = "cpu"
        elif user2char == "X":
            winner = "user2"
        elif user1char == "X": 
            winner = "user"
    # After that we check 'O' in multiply case
    elif "O" in board[0][0] and "O" in board[1][1] and "O" in board[2][2] or "O" in board[2][0] and "O" in board[1][1] and "O" in board[0][2]:
        if cpuchar == "O":
            winner = "cpu"
        elif user2char == "O":
            winner = "user2"
        elif user1char == "O":
            winner = "user"
    else: return False

def cpuAI():
    global board, user1char,cpuchar, cpuchoice,address
    list1 = numpy.array(board)
    translate = {0: "A",1:  "B",2: "C"}
    translate2 = {0: 1 ,1: 2 ,2: 3}
    word = 0
    word1 = 0
    count = 0
    column = ""
    for i in range(len(board)):
        s = list(list1[:,i])
        l = board[i]
        if " " in l or " " in s:
            for se in l:
                if se == user1char:
                    word = 0
                    break
                elif se == " ":
                    count +=1
                    if count == 2:
                        count = 0
                        word = 0
                        break
                else:
                    word += 1
                    if word == 2:
                        word = 0
                        if " " in l:
                            column = translate[l.index(" ")]
                            cpuchoice = f"{column}{i+1}"
                            break
            for sc in s:
                if sc == user1char:
                    word = 0
                    break
                elif sc == " ":
                    count +=1
                    if count == 2:
                        count = 0
                        word = 0
                        break
                else:
                    word += 1
                    if word == 2:
                        word = 0
                        if " " in s:
                            row = translate2[s.index(" ")]
                            column = translate[i]
                            cpuchoice = f"{column}{row}"
                            print(cpuchoice)
                            break
        if cpuchoice == "":                                     
            for le in l:
                if le == cpuchar:
                     word1 = 0
                     break
                elif le == " ":
                    count +=1
                    if count == 2:
                        count = 0
                        word1 = 0
                        break
                else:
                    word1 += 1
                    if word1 == 2:
                        word1 = 0
                        if " " in l:
                            column = translate[l.index(" ")]
                            cpuchoice = f"{column}{i+1}"
                            break
            for lc in s:
                if lc == cpuchar:
                    word1 = 0
                    break
                elif lc == " ":
                    count +=1
                    if count == 2:
                        count = 0
                        word1 = 0
                        break
                else:
                    word1 += 1
                    if word1 == 2:
                        word1 = 0
                        if " " in s:
                            row = translate2[s.index(" ")]
                            column = translate[i]
                            cpuchoice = f"{column}{row}"
                            break

def get_row_col(value):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = value[0]
    number = value[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)

def DoublePlayer():
    global user1char, user2char,turn, firstturn,cpuchar
    cpuchar = ""
    system("cls")
    print("----------------------\nPlayer '1' Choose Your Character\n----------------------\n1: X\n2: O")
    user1char = opmodule.intvalue(1,2,"P1: ")
    if user1char == 1:
        user1char = "X"
        user2char = "O"
    elif user1char == 2:
        user1char = "O"
        user2char = "X"
    Play()

def SinglePlayer():
    global user1char, cpuchar,turn, firstturn, user2char
    user2char = ""
    system("cls")
    print("----------------------\nChoose Your Character\n----------------------\n1: X\n2: O")
    user1char = opmodule.intvalue(1,2)
    if user1char == 1:
        user1char = "X"
        cpuchar = "O"
    elif user1char == 2:
        user1char = "O"
        cpuchar = "X"
    system("cls")
    Play()

def Play():
    global winner, numberofturns, turn,gamem, user1char, user2char, cpuchar, board, cpuchoice,cpuscores,userscores,firstturn
    numberofturns = 0
    winner = ""
    board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " ",]
    ] 
    firstturn = random.randint(0,1)
    turn = ""
    if firstturn == 1:
        turn = "user"
    else: 
        if gamem == "single": turn = "cpu"
        elif gamem == "double": turn = "user2"
    while(True):
        system("cls")
        showboard()
        if numberofturns == 9 or winner == "cpu" or winner == "user" or winner == "user2":
            if numberofturns == 9 and winner == "": print(f"No One Wins the Game! Draw")
            if gamem == "single": 
                if winner == "cpu": cpuscores +=1
                elif winner =="user": userscores +=1
                print(f"\n{winner.capitalize()} Wins the Game!")
            elif gamem == "double":
                if winner == "user2":
                    winner = "Player '2'"
                    print(f"\n{winner.capitalize()} Wins the Game!")
                elif winner == "user":
                    winner = "Player '1'"
                    print(f"\n{winner.capitalize()} Wins the Game!")
                else: winner = "No One"
            print("\n0: MainMenu\n1: Play Again!")
            user23 = opmodule.intvalue(0,1)
            if user23 == 0:
                mainmenu()
                break
            else: 
                Play()
                break
        if turn == "user":
            while(True):
                if gamem == "single": 
                    turn = "cpu"
                    userchoice = opmodule.stringchecker(address, "User: ").upper()
                elif gamem == "double": 
                    turn = "user2"
                    userchoice = opmodule.stringchecker(address, "P1: ").upper()
                b1 =get_row_col(userchoice)
                if board[b1[0]][b1[1]] == " ":
                    numberofturns +=1
                    board[b1[0]][b1[1]] = user1char
                    winningconditions()
                    break
                else: 
                    system("cls")
                    showboard()
                    print("Your Entered Cell is Already Occupied! Please Enter a Vaild Cell")
        elif turn == "user2":
            while(True):
                userchoice1 = opmodule.stringchecker(address, "P2: ").upper()
                turn = "user"
                b3 =get_row_col(userchoice1)
                if board[b3[0]][b3[1]] == " ":
                    numberofturns +=1
                    board[b3[0]][b3[1]] = user2char
                    winningconditions()
                    break
                else: 
                    system("cls")
                    showboard()
                    print("Your Entered Cell is Already Occupied! Please Enter a Vaild Cell")
        else:
            cpuAI()
            while(True):
                if cpuchoice == "": cpuchoice = random.choice(address)
                if gamem == "single": turn = "user"
                b2 =get_row_col(cpuchoice)
                if board[b2[0]][b2[1]] == " ":
                    numberofturns +=1
                    board[b2[0]][b2[1]] = cpuchar
                    winningconditions()
                    break
                else: 
                    system("cls")
                    cpuchoice = random.choice(address)
                    showboard()
                    continue

def winscores():
    system("cls")
    global userscores, cpuscores
    if userscores > cpuscores:
        winner1 = "User"
    elif cpuscores > userscores:
        winner1 = "Computer"
    else:
        winner1 = "NO ONE"
    print("------------------------------------------------")
    print("|---------->      Scores Sheet      <----------|")
    print("------------------------------------------------")
    print(f"                  Your Wins: {int(userscores)}\n                 Computer Wins: {int(cpuscores)}")
    print(f"                 Winner: {winner1}")
    print("------------------------------------------------")
    print("\n0: Back\n1: Reset Scores")
    user = opmodule.intvalue(0, 1)
    if user == 0:
        mainmenu()
    elif user == 1:
        userscores = 0
        cpuscores = 0
        system("cls")
        winscores()
    return 0

def Game():
    global gamem
    print("--------------------\n| Choose Game Mode |\n--------------------\n\n1: Single Player\n2: Double Player\n\n0: Back")
    gamemode = opmodule.intvalue(0,2)
    if gamemode == 2:
        gamem = "double"
        DoublePlayer()
    elif gamemode == 1:
        gamem = "single"
        SinglePlayer()
    else: mainmenu()
        

def help():
    system("cls")
    print("----------------------------------------")
    print("|---------->      Help      <----------|")
    print("----------------------------------------\n")
    print("There are 3 Columns and 3 Rows in Game.\nColumns are A, B, C\nRows are 1, 2, 3\n")
    print("You Need to put Input Like this 'A2'")
    print("Where 'A' is Column and '2' is Row")
    print("It is the Address where you want to mark your character")
    print("\n0: Back")
    opmodule.intvalue(0,0)
    mainmenu()

def mainmenu():
    system("cls")
    print("---------------------------------------")
    print("|     Welcome to Tic Tac Toe Game     |")
    print("---------------------------------------\n")
    print("1: Play Game\n2: Scores\n3: How to Play Game\n4: Exit")
    user1 = opmodule.intvalue(1,4)
    if user1 == 1:
        system("cls")
        Game()
    elif user1 == 2:
        winscores()
    elif user1 == 3:
        system("cls")
        help()
    elif user1 == 4:
        system("cls")
        print("------------------------------------------------------")
        print("Do you really want to Exit the Game? 1 = Yes, 0 = No")
        print("------------------------------------------------------")
        user2 = opmodule.intvalue(0, 1)
        if user2 == 1:
            system("cls")
        elif user2 == 0:
            system("cls")
            mainmenu()
        
mainmenu()


