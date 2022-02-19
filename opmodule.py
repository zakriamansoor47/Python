def intvalue(min = 0, max = 9,text = ""):
    """Get a INT value Input and check if entered input is not less then or greater then the min or max value OR entered input is not interger.
    if input valued is interger and greater or less then the min or max value then give a error and ask to enter value again. if the entered
    input is not greater or less then the max or min value then return(int) the input value"""
    while(True):
        try:
            value = int(input(text))
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
def floatvalue(min =0.0, max = 1.0,text=""):
    """Get a FLOAT value Input and check if entered input is not less then or greater then the min or max value OR entered input is not float.
    if input valued is float and greater or less then the min or max value then give a error and ask to enter value again. if the entered
    input is not greater or less then the max or min value then return(float) the input value"""
    while(True):
        try:
            value = float(input(text))
            if value < min:
                print("Wrong Input! Please Enter a Vaild Number")
                continue
            elif value > max:
                print("Wrong Input! Please Enter a Vaild Number")
                continue
            else:
                return value
        except:
            print("Wrong Input! Please Enter a Float Value")
            continue

def stringchecker(value,text = ""):
    """Get the STRING input from user and check the entered input is in 'value' which maybe string or list"""
    while(True):
        try:
            user = input(text)
            if user == "":
                print("Wrong Input! You Pressed Enter Please Type Any Value")
                continue
            if user.lower() in value or user.upper() in value or user.capitalize() in value or user in value:
                return user
            elif float(user) in value or int(user) in value:
                return user
            else:
                print("Wrong Input! Your Entered Value is NOT Found!")
                continue
        except:
            print("Wrong Input! Your Entered Value is NOT Found!")
            continue
def playmusic(filename, loop = 1, volume = 1.0):
    """playmusic(filename => string, loop => int (default value: 1), volume (default value: 1.0)=> float)
    
    Play Music like this: playmusic("your.mp3", 2, 0.8)"""
    from pygame import mixer
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(float(volume))
    mixer.music.play(int(loop))

def stopmusic(unload = 0):
    """if unload = 1 then it will stop+unload the music. elif unload = 0 or empty then it will only stop the music .
    
    STOP or STOP+UNLOAD the current playing MUSIC
    syntax: stopmusic() or stopmusic(1)"""
    from pygame import mixer
    if int(unload) == 1:
        mixer.music.stop()
        mixer.music.unload()
    elif int(unload) == 0:
        mixer.music.stop()

def realtime():
    """return the current TIME
    
    TIME format is 13:23:52"""
    import datetime
    seconds = int( datetime.datetime.now().strftime("%S"))
    mins = int(datetime.datetime.now().strftime("%M"))
    hours = int(datetime.datetime.now().strftime("%H"))
    hoursminsec = f"{hours:02d}:{mins:02d}:{seconds:02d}"
    return hoursminsec

def hideString(number, showletters = 4, hiddenlettersymbol = "*"):
    """This Function hide the letters of String. it can be use to hide password or credit card number. You can hide all or some letters of string
    depend on you.
    
    Syntax: hideString(number --> String value, showletters --> int value(default = 4), hiddenlettersymbol --> string(Default = "*"))
    To Hide All letters (useful for password) Change the value of second argument 'showletters' to '0'
    To Change the Symbol of Hidden Letters change the value of third argument 'hiddenlettersymbol'"""
    listofnumbers = list(number)
    digits = ""
    words = 0
    newlist2 = []
    for i in listofnumbers:
        words += 1
    if words-showletters >= 0:
        for s in range(words-showletters,words):
            newlist2.append(listofnumbers[s])
        for e in newlist2:
            digits += e
    else:
        print("Second Argument is Invaild!")
    letters = words-showletters
    hideletters = hiddenlettersymbol*letters
    hidden = f"{hideletters}{digits}"
    return hidden

def encoder(message, list1, list2):
    """The Function Encode a String. Change specific letters in string with another specific letters

    s = "aeiou"
            
    l1 = ["a", "e", "i", "o", "u"]

    l2 = ["@", "3", "!", "0", "#"]
                encoded = encoder(s, l1, l2)
                print(encoded)
        Output:  @3!0#
    Synatx: encoder(message --> string, list1 -->list, list2 -->list)"""
    list0 = list(message)
    word = ""
    digit = len(list1)
    digit2 = len(list2)
    num = digit-1
    if digit == digit2:
        for e in list0:
            if e in list1:
                while(True):
                    if e == list1[num]:
                        word += list2[num]
                    num -=1
                    if num < 0:
                        num = digit-1
                        break
            else:
                word += e
        return word
    else:
        print("Encoding Error: Number of Items of 2nd and 3rd Arguments are not matched")

def textanimation(stringvalue, letters = 50, speed = 0.12, spaces = 20):
    """Print Animation of Enetered Text

    1=stringvalue is the string value or text on which text animation will applied

    2=letters. it is the display size of animated text (must be integer)

    3=speed. it is the speed of moving of text. (less floating value = More the Speed) 

    4=spaces. it is the size of spaces after the text string ends. (must be integer)
    Synatx: textanimation(stringvalue --> string, letters -->int, speed -->float, spaces -->int)"""
    import time
    space = " "*spaces 
    list1 = list(space+stringvalue) # Convert Spaces+User text(string value) into list
    list2 = [] # created a empty list
    # Created 3 integers
    word = 0
    word2 = 0
    word3 = len(list1)
    text = "" # empty string
    # Now we will Count how much letters in User Text
    while(True):
        if word < word3:
            list2.append(list1[word])
            word +=1 
            word2 = len(list2) #counting the letters in list2
            if word2 >=letters: # check if the letters in Second list is >= 2nd argument of function
                lol = list2[-letters:] # Removeing frist letter from list
                time.sleep(speed) # Speed of moving of text
                for let in lol: # converting list into string and print it
                    text += let
                    print(f"|{text}|", end="\r")
                else: # when the letters in list ends we will set the value of text to empty string
                    text =""
            word2 = 0
        elif word >= word3: # Check if the letters of list2 >= letters of User Text
            word =0

def design(func):
    def inner(msg):
        print("-" *len(msg))
        func(msg)
        print("-" *len(msg))
    return inner
@design
def dprint(msg):
    print(f"{msg}")

def printinlist(msg,start=1,split=";"):
    """This Function print your string in list with serial Numbers and return the last item number
    
    for example: 
        printinlist("Play Game;Scores;Exit")
    Output: 1: Play Game
            2: Scores
            3: Exit
    1=msg is the string value or text on which the Function Applied

    2=start it is the starting number of the list like if satrt=0 then list will start from 0 then 1,2,3

    3=split it is the symbol which is used to add next item

    Synatx: printinlist(msg --> string,start--> int(default value: 1) ,split --> string(default value: ";"))"""
    s = ""
    word = start
    for i in msg.split(split):
        s += f"{word}: {i}\n"
        word +=1
    print(s)
    return word-1
def design(func):
    def inner(msg):
        print("-" *len(msg))
        func(msg)
        print("-" *len(msg))
    return inner
@design
def dprint(msg):
    print(f"{msg}")

def listintostring(yourlist,end=" "):
    """This Function converts your list into string and return the converted string
    
    for example: 
        listintostring(["Hello","World"]," - ")
    Output: Hello - World
    1=yourlist - it is the list given by you on which the Function Applied
    2=end - it is the ending word written every time when one item of list is printed
    Synatx: listintostring(yourlist --> list,end--> string(default value: ";"))"""
    string1 = ""
    for i in yourlist:
        string1 += f"{i}{end}"
    return string1.rstrip(string1[-len(end)])
