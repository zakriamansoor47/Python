def getdate():
    import datetime
    return datetime.datetime.now()

def getuser(s):
    if s == 1:
        user = "Usama"
    elif s ==2:
        user = "Umer"
    elif s == 3:
        user = "Talha"
    return user

def Mainmenu():
    print("Welcome to Health Management System")
    print("0 = Exit\n1 = Write Data\n2 = Read Data")
    while(True):
        try:
            input1 =  int(input())
            if input1 == 1 or input1 == 2 or input1 == 0:
                break
            else:
                print("Wrong Input! Please Enter a Vaild Number")
                continue
        except:
            print("Wrong Input! Please Try Again")
            continue
    if input1 == 0:
        return 0
    elif input1 == 1:
        print("|--- Write Data ---|")
    elif input1 == 2:
        print("|--- Read Data ---|")
    print("Please Select a User")
    print("1 = Usama\n2 = Umer\n3 = Talha")
    while(True):
        try:
            input2 =  int(input())
            if input2 == 1 or input2 == 2 or input2 == 3:
                break
            else:
                print("Wrong Input! Please Enter a Vaild Number")
                continue
        except:
            print("Wrong Input! Please Try Again")
            continue
    print("Selected User is:", getuser(input2))
    if input1 == 1:
        print("Please Select what type of Data you want to Write")
    elif input1 == 2:
        print("Please Select what type of Data you want to Read")
    print("1 = Exercise\n2 = Diet")
    while(True):
        try:
            input3 =  int(input())
            if input3 == 1 or input3 == 2:
                break
            else:
                print("Wrong Input! Please Enter a Vaild Number")
                continue
        except:
            print("Wrong Input! Please Try Again")
            continue

    if input1 == 1 and input3 == 1:
        print("|--- Write Exercise Data of", getuser(input2),"---|")
        print("After the Entering Data please type 'exit' to go to main menu")
        filename1 = getuser(input2)+"_Exercise.txt"
        with open (filename1, "a") as u:
            while(True):
                time = getdate()
                data = input()
                file = "["+str(time.strftime("%H:%M | %d/%m/%Y"))+"] "+data+"\n"
                if data == "exit":
                    print("Successfully Entered Data in", filename1)
                    u.close()
                    break
                else:
                    u.write(file)
                    continue
            return Mainmenu()
    if input1 == 1 and input3 == 2:
        print("|--- Write Diet Data of", getuser(input2),"---|")
        print("After the Entering Data please type 'exit' to go to main menu")
        filename2 = getuser(input2)+"_Diet.txt"
        with open (filename2, "a") as u:
            while(True):
                time = getdate()
                data = input()
                file = "["+str(time.strftime("%H:%M | %d/%m/%Y"))+"] "+data+"\n"
                if data == "exit":
                    print("Successfully Entered Data in", filename2)
                    u.close()
                    break
                else:
                    u.write(file) 
                    continue
            return Mainmenu()
    if input1 == 2 and input3 == 1:
        print("|--- Read Exercise Data of", getuser(input2),"---|")
        print("After the Reading Data please type 'exit' to go to main menu")
        filename1 = getuser(input2)+"_Exercise.txt"
        with open (filename1, "r") as u:
            while(True):
                s = u.read()
                print(s)
                data = input()
                if data == "exit":
                    return Mainmenu()
                else:
                    print("Wrong Input! Please Enter 'exit'")
                    continue
    if input1 == 2 and input3 == 2:
        print("|--- Read Diet Data of", getuser(input2),"---|")
        print("After the Reading Data please type 'exit' to go to main menu")
        filename2 = getuser(input2)+"_Diet.txt"
        with open (filename2, "r") as u:
            while(True):
                s = u.read()
                print(s)
                data = input()
                if data == "exit":
                    return Mainmenu()
                else:
                    print("Wrong Input! Please Enter 'exit'")
                    continue

Mainmenu()