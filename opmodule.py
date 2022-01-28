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

