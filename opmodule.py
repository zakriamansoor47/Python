import datetime
from pygame import mixer

timeinmins = datetime.datetime.now().strftime("%M")
timeinhours = datetime.datetime.now().strftime("%H")
timeinsec = datetime.datetime.now().strftime("%S")
def intvalue(min, max):
    """Get a INT value Input and check if entered input is not less then or greater then the min or max value OR entered input is not interger.
    if input valued is interger and greater or less then the min or max value then give a error and ask to enter value again. if the entered
    input is not greater or less then the max or min value then return(int) the input value"""
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

def floatvalue(min, max):
    """Get a FLOAT value Input and check if entered input is not less then or greater then the min or max value OR entered input is not float.
    if input valued is float and greater or less then the min or max value then give a error and ask to enter value again. if the entered
    input is not greater or less then the max or min value then return(float) the input value"""
    while(True):
        try:
            value = float(input())
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

def stringvalue(value):
    """Get the STRING input from user and check the entered input is in 'value' which maybe string or list"""
    while(True):
        try:
            user = input()
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
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(float(volume))
    mixer.music.play(int(loop))

def stopmusic(unload = 0):
    """if unload = 1 then it will stop+unload the music. elif unload = 0 or empty then it will only stop the music .
    
    STOP or STOP+UNLOAD the current playing MUSIC
    syntax: stopmusic() or stopmusic(1)"""
    if int(unload) == 1:
        mixer.music.stop()
        mixer.music.unload()
    elif int(unload) == 0:
        mixer.music.stop()

def realtime():
    """return the current TIME
    
    TIME format is 13:23:52"""
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
    digit = 0
    digit2 = 0
    for s in list1:
        digit += 1
    for se in list2:
        digit2 += 1
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
