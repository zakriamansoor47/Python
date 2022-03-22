import os
import opmodule

avoidfilepath = "D:\Zakria Work\Python\zakria.txt"
#avoidextspath = "No Path Given"
avoidextspath = "D:\Zakria Work\Python\exts.txt"

def filereader(path):
    w = open(path, "r")
    list1 = w.read().splitlines()
    w.close()
    return list1

def solider(path, file, foramt):
    with open(file, "r") as w:
        list1 = w.read().splitlines()
        w.close()
    if os.path.exists(path) == True:
        os.chdir(path)
        word = 1
        word1 = 1
        for s in os.walk(os.getcwd()):
            for l in s[2]:
                fort = l.split(".")
                if l in list1: # if file exists in files list
                    continue # Do nothing with that file
                elif fort[-1] == foramt:
                    try:
                        if os.path.exists(f"{word}.{foramt}") == True:
                            word1=1
                            while(word1 != word):
                                try:
                                    os.rename(l, f"{word}.{foramt}")
                                except: word1 +=1
                            print(f"file exists: {word}.{foramt}")
                        else: 
                            print("i am here")
                            os.rename(l, f"{word}.{foramt}")
                    finally: word +=1
                else:
                    os.rename(l, l.capitalize())
    else: print("Your Entered Path is not Exists")
    
def capitalize():
    global avoidfilepath,avoidextspath
    Fileslist = filereader(avoidfilepath)
    Extslist = filereader(avoidextspath)
    for s in os.walk(os.getcwd()):
            for l in s[2]:
                fort = l.split(".")
                if l not in Fileslist and fort[-1] not in Extslist:
                    os.rename(l,f"{l[0].capitalize()+l[1:]}")
    else:
        os.system("cls") 
        opmodule.dprint("All Files Name are now Capitalized!")
    user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
    if user1 == 0: Prettifyer()
    
def UpperCase():
    global avoidfilepath,avoidextspath
    Fileslist = filereader(avoidfilepath)
    Extslist = filereader(avoidextspath)
    for s in os.walk(os.getcwd()):
            for l in s[2]:
                fort = l.split(".")
                if l not in Fileslist and fort[-1] not in Extslist:
                    os.rename(l,l.upper())
    else:
        os.system("cls") 
        opmodule.dprint("All Files Name are now UPPER Case!")
    user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
    if user1 == 0: Prettifyer()

def LowerCase():
    global avoidfilepath,avoidextspath
    Fileslist = filereader(avoidfilepath)
    Extslist = filereader(avoidextspath)
    for s in os.walk(os.getcwd()):
            for l in s[2]:
                fort = l.split(".")
                if l not in Fileslist and fort[-1] not in Extslist:
                    os.rename(l,l.lower())
    else:
        os.system("cls") 
        opmodule.dprint("All Files Name are now Lower Case!")
    user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
    if user1 == 0: Prettifyer()

def ChangeFileExts():
    global avoidfilepath,avoidextspath
    Fileslist = filereader(avoidfilepath)
    Extslist = filereader(avoidextspath)
    os.system("cls")
    opmodule.dprint("|---> Change Files Extensions <---|")
    user2 =  opmodule.intvalue(0,opmodule.printinlist("Back;Change File Extension",0))
    if user2 == 0: Prettifyer()
    else:
        exts1= input("Enter the name of Extension (without dot'.') which you want to Change:\n")
        exts2 = input("Enter the name of Extension (without dot'.') which you want to Apply:\n")
        for s in os.walk(os.getcwd()):
                for l in s[2]:
                    fort = l.split(".")
                    word =""
                    for i in fort[:-1]:
                        word +=i+'.'
                    if l not in Fileslist and fort[-1] == exts1:
                        os.rename(l,f"{word.rstrip(word[-1])+'.'+exts2}")
        else:
            os.system("cls") 
            opmodule.dprint("Extensions of All Files are Now Changed!")
        user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
        if user1 == 0: Prettifyer()

def number():
    global avoidfilepath,avoidextspath
    pass

def Prettifyer():
    os.system("cls")
    opmodule.dprint("|----->  Select Mode  <-----|")
    user = opmodule.intvalue(0, opmodule.printinlist("Back;Capitalize File Name;Upper Case File Name;lower Case File Name;Change Files Extension;Number",0))
    if user == 0: mainmenu()
    elif user ==1: capitalize()
    elif user == 2: UpperCase()
    elif user == 3: LowerCase()
    elif user == 4: ChangeFileExts()
    elif user ==5: number()

def chagnepath():
    os.system("cls")
    opmodule.dprint(f"Your Current Working Path is: {os.getcwd()}")
    user2 =  opmodule.intvalue(0,opmodule.printinlist("Back;Change Path",0))
    if user2 == 0: settings()
    else:
        print("Enter the Path of Folder where you want to works with Folder Prettifyer: ")
        path = input()
        os.system("cls")
        if os.path.exists(path) == True:
            os.chdir(path)
            opmodule.dprint("You have Successfully Changed your Folder Path!")
        else: opmodule.dprint("Your Entered Path is not Exits!")
        user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
        if user1 == 0: chagnepath()

def avoidfiles():
    global avoidfilepath
    os.system("cls")
    opmodule.dprint("..:|----->  Avoid These Files  <-----|:..")
    print("Name of the Files on which you don't want\nto Apply Any Folder Prettifyer Funciton!\n")
    user = opmodule.intvalue(0,opmodule.printinlist("Back;Check Current 'Avoid Files List';Change path of 'Avoid Files List' File",0))
    if user == 0: settings()
    elif user == 1:
        os.system("cls")
        opmodule.dprint("|----->  Avoid Files List  <-----|")
        if avoidfilepath != "No Path Given":
            opmodule.printinlist(opmodule.listintostring(filereader(avoidfilepath),";"))
            print("")
        user1 = opmodule.intvalue(0,opmodule.printinlist("Back",0))
        if user1 == 0: avoidfiles()
    elif user ==2: 
        os.system("cls")
        opmodule.dprint(f"Your Current 'Avoid Files List' File Path is: {avoidfilepath}")
        user2 =  opmodule.intvalue(0,opmodule.printinlist("Back;Change File Path",0))
        if user2 == 0: avoidfiles()
        else:
            print("Enter the Path of File where's 'Avoid Files List' is written: ")
            path = input()
            os.system("cls")
            if os.path.exists(path) == True:
                avoidfilepath = path
                opmodule.dprint("You have Successfully Changed your 'Avoid Files List' File Path!")
            else: opmodule.dprint("Your Entered Path is not Exits!")
            user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
            if user1 == 0: avoidfiles()

def avoidextensions():
    global avoidextspath
    os.system("cls")
    opmodule.dprint("..:|----->  Avoid These Extensions  <-----|:..")
    print("Name of the Extensions on which you don't want\nto Apply Any Folder Prettifyer Funciton!\n")
    user = opmodule.intvalue(0,opmodule.printinlist("Back;Check Current 'Avoid Extensions List';Change path of 'Avoid Extensions List' File",0))
    if user == 0: settings()
    elif user == 1:
        os.system("cls")
        opmodule.dprint("|----->  Avoid Extensions List  <-----|")
        if avoidextspath != "No Path Given":
            opmodule.printinlist(opmodule.listintostring(filereader(avoidextspath),";"))
            print("")
        user1 = opmodule.intvalue(0,opmodule.printinlist("Back",0))
        if user1 == 0: avoidextensions()
    elif user ==2: 
        os.system("cls")
        opmodule.dprint(f"Your Current 'Avoid Extensions List' File Path is: {avoidextspath}")
        user2 =  opmodule.intvalue(0,opmodule.printinlist("Back;Change File Path",0))
        if user2 == 0: avoidextensions()
        else:
            print("Enter the Path of File where's 'Avoid Extensions List' is written: ")
            path = input()
            os.system("cls")
            if os.path.exists(path) == True:
                avoidextspath = path
                opmodule.dprint("You have Successfully Changed your 'Avoid Extensions List' File Path!")
            else: opmodule.dprint("Your Entered Path is not Exits!")
            user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
            if user1 == 0: avoidextensions()

def settings():
    os.system("cls")
    opmodule.dprint("|----->  Settigns  <-----|")
    user = opmodule.intvalue(0,opmodule.printinlist("Back;Change Folder Path;Avoid These Files;Avoid these Extensions",0))
    if user == 0:
        mainmenu()
    elif user == 1:
        chagnepath()
    elif user ==2:
        avoidfiles()
    elif user ==3:
        avoidextensions()   
        

def Help():
    os.system("cls")
    opmodule.dprint("|-----> Help <-----|")
    user4 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
    if user4 == 0: mainmenu()

def mainmenu():
    os.system("cls")
    opmodule.dprint("|---> Folder Prettifyer by Zakria <---|")
    user = opmodule.intvalue(1, opmodule.printinlist("Start Prettifying;Settings;Help;Exit"))
    if user == 1:
        Prettifyer()
    elif user == 2:
        settings()
    elif user == 3:
        Help()
    elif user == 4:
        os.system("cls")
        opmodule.dprint("Do you really want to Exit the Program? 1= Yes, 0= No")
        user1 =  opmodule.intvalue(0,1)
        if user1 == 0:
            mainmenu()
        else: pass

mainmenu()