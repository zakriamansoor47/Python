#-------------------------------------------------------------
# Importing Modules
#-------------------------------------------------------------

import os
import opmodule

#-------------------------------------------------------------
# Global Veriables
#-------------------------------------------------------------

avoidfilepath = "D:\Zakria Work\Python\\avoidfiles.txt"
#avoidextspath = "No Path Given"
avoidextspath = "D:\Zakria Work\Python\\avoidexts.txt"

#-------------------------------------------------------------
# File Reading Function
#-------------------------------------------------------------

def filereader(path):
    w = open(path, "r")
    list1 = w.read().splitlines()
    w.close()
    return list1

#-------------------------------------------------------------
# Entered Extension Check
#-------------------------------------------------------------

def extschecker(text):
    while True:
        try:
            text1 = input(text)
            if text1.islower() == True and "." not in text1:
                return text1
        except:continue


#-------------------------------------------------------------
# Confirming Message Function
#-------------------------------------------------------------

def doYou(name):
    os.system("cls")
    opmodule.dprint(f"Do you really want to {name}? 1 = Yes, 0 = No")
    user = opmodule.intvalue(0,1)
    return user

#-------------------------------------------------------------
# Capitalize Files Name Function
#-------------------------------------------------------------
def capitalize():
    global avoidfilepath,avoidextspath
    userinput = doYou("Capitalize Files Name")
    if userinput == 0: Prettifyer()
    else: 
        Fileslist = filereader(avoidfilepath)
        Extslist = filereader(avoidextspath)
        for s in os.walk(os.getcwd()):
            for l in sorted(s[2],key=len):
                fort = l.split(".")
                if l not in Fileslist and fort[-1] not in Extslist:
                    os.rename(l,f"{l[0].capitalize()+l[1:]}")
        else:
            os.system("cls") 
            opmodule.dprint("All Files Name are now Capitalized!")
        user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
        if user1 == 0: Prettifyer()

#-------------------------------------------------------------
# Change Files Name to UpperCase Function
#-------------------------------------------------------------

def UpperCase():
    global avoidfilepath,avoidextspath
    userinput = doYou("Upper Case Files Name")
    if userinput == 0: Prettifyer()
    else: 
        Fileslist = filereader(avoidfilepath)
        Extslist = filereader(avoidextspath)
        for s in os.walk(os.getcwd()):
            for l in sorted(s[2],key=len):
                fort = l.split(".")
                word =""
                for i in fort[:-1]:
                    word +=i
                if l not in Fileslist and fort[-1] not in Extslist:
                    os.rename(l,f"{word.upper()+'.'+fort[-1]}")
        else:
            os.system("cls") 
            opmodule.dprint("All Files Name are now UPPER Case!")
        user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
        if user1 == 0: Prettifyer()

#-------------------------------------------------------------
# Change Files Name to LowerCase Funtion
#-------------------------------------------------------------

def LowerCase():
    userinput = doYou("Lower Case Files Name")
    if userinput == 0: Prettifyer()
    else: 
        global avoidfilepath,avoidextspath
        Fileslist = filereader(avoidfilepath)
        Extslist = filereader(avoidextspath)
        for s in os.walk(os.getcwd()):
            for l in sorted(s[2],key=len):
                fort = l.split(".")
                if l not in Fileslist and fort[-1] not in Extslist:
                    os.rename(l,l.lower())
        else:
            os.system("cls") 
            opmodule.dprint("All Files Name are now Lower Case!")
        user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
        if user1 == 0: Prettifyer()

#-------------------------------------------------------------
# Change File Extensions Function
#-------------------------------------------------------------

def ChangeFileExts():
    userinput = doYou("Change Files Extensions")
    if userinput == 0: Prettifyer()
    else: 
        global avoidfilepath
        Fileslist = filereader(avoidfilepath)
        os.system("cls")
        opmodule.dprint("|---> Change Files Extensions <---|")

        exts1= extschecker("Enter the name of Extension (without dot'.') which you want to Change:\n")
        exts2 = extschecker("Enter the name of Extension (without dot'.') which you want to Apply:\n")
        for s in os.walk(os.getcwd()):
            for l in sorted(s[2],key=len):
                fort = l.split(".")
                if l not in Fileslist and fort[-1] == exts1:
                    word =""
                    for i in fort[:-1]:
                        word +=i+'.'
                    os.rename(l,f"{word.rstrip(word[-1])+'.'+exts2}")
        else:
            os.system("cls") 
            opmodule.dprint(f"All Files of this ({exts1}) Extension are Changed to this ({exts2}) Extension!")
        user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
        if user1 == 0: Prettifyer()

#-------------------------------------------------------------
# Sort Files by Numbers Function
#-------------------------------------------------------------
def number():
    userinput = doYou("Sort Files by Numbers")
    if userinput == 0: Prettifyer()
    else: 
        global avoidfilepath
        Fileslist = filereader(avoidfilepath)
        os.system("cls")
        opmodule.dprint("|--->  Sort Files by Numbers  <---|")
        exts1= extschecker("Enter the name of Extension (without dot'.') which you want to Sort by Numbers:\n")
        word = 1
        word2 = 1
        while True: # Check is there any files are sorted with number 
            if os.path.exists(f"{word}.{exts1}") == True: word +=1 # if sorted files exists count them
            else: break # End the loop after counting all sorted files
        for s in os.walk(os.getcwd()):
            for l in sorted(s[2],key=len):
                fort = l.split(".")
                if l not in Fileslist and fort[-1] == exts1:
                    word2 +=1
                    if word2 <= word:
                        continue # Skip the File
                    try:
                        os.rename(l, f"{word}.{exts1}")
                    finally: word +=1
        else:
            os.system("cls") 
            opmodule.dprint(f"All Files of ({exts1}) Extension are now Sorted by Numbers!")
            user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
            if user1 == 0: Prettifyer()

#-------------------------------------------------------------
# Add Text in Files Name Function
#-------------------------------------------------------------

def AddText():
    userinput = doYou("Add Text in Files Name")
    if userinput == 0: Prettifyer()
    else: 
        global avoidfilepath
        Fileslist = filereader(avoidfilepath)
        os.system("cls")
        opmodule.dprint("|---> Add Text in Files Name <---|")
        exts1 = extschecker("Enter the name of Files Extension (without dot'.') in which you want to add Text:\n")
        text = input("Enter the Text which You want to Add in the Files Name:\n")
        print("What will be the Text Position?\n")
        position1 = opmodule.intvalue(1,opmodule.printinlist("In Start;In End"))
        for s in os.walk(os.getcwd()):
            for l in sorted(s[2],key=len):
                fort = l.split(".")
                if l not in Fileslist and fort[-1] == exts1:
                    word =""
                    for i in fort[:-1]:
                        word +=i+'.'
                    if position1 == 1: os.rename(l, f"{text}{word.rstrip(word[-1])}.{exts1}")
                    if position1 == 2: os.rename(l, f"{word.rstrip(word[-1])}{text}.{exts1}")
        else:
            os.system("cls") 
            opmodule.dprint(f"Your Entered Text is Added in All Files Name of this ({exts1}) Extension")
            user1 =  opmodule.intvalue(0,opmodule.printinlist("Back",0))
            if user1 == 0: Prettifyer()

#-------------------------------------------------------------
# Folder Prettifying Functions Menu
#-------------------------------------------------------------
def Prettifyer():
    os.system("cls")
    opmodule.dprint("|----->  Select Function  <-----|")
    print(f"Note: Your Current Working Folder is: {os.getcwd()}")
    print("All These Funcitons are Applied only in this Folder!\n")
    user = opmodule.intvalue(0, opmodule.printinlist("Back;Capitalize Files Name;Upper Case Files Name;lower Case Files Name;"
    "Change Files Extension;Sort Files by Numbers;Add Text in File Name",0))
    if user == 0: mainmenu()
    elif user ==1: capitalize()
    elif user == 2: UpperCase()
    elif user == 3: LowerCase()
    elif user == 4: ChangeFileExts()
    elif user ==5: number()
    elif user == 6: AddText()

#-------------------------------------------------------------
# Change Working Folder Function
#-------------------------------------------------------------

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

#-------------------------------------------------------------
# Change 'Avoid Files List' File Path Funciton
#-------------------------------------------------------------

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

#-------------------------------------------------------------
# Change 'Avoid Extensions List' File Path Funciton
#-------------------------------------------------------------

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

#-------------------------------------------------------------
# Settings Menu
#-------------------------------------------------------------

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


#-------------------------------------------------------------
# Main Menu
#-------------------------------------------------------------
def mainmenu():
    os.system("cls")
    opmodule.dprint("|---> Folder Prettifyer by Zakria <---|")
    user = opmodule.intvalue(1, opmodule.printinlist("Start Prettifying;Settings;Exit"))
    if user == 1:
        Prettifyer()
    elif user == 2:
        settings()
    elif user == 3:
        os.system("cls")
        opmodule.dprint("Do you really want to Exit the Program? 1= Yes, 0= No")
        user1 =  opmodule.intvalue(0,1)
        if user1 == 0:
            mainmenu()
        else: pass

mainmenu()