from pygame import mixer
import datetime
import time

timedate = datetime.datetime.now().strftime("%H:%M | %d/%m/%Y")
timeinmins = datetime.datetime.now().strftime("%M")
timeinhours = datetime.datetime.now().strftime("%H")
timeinsec = datetime.datetime.now().strftime("%S")


water = "Water"
eye = "Eye"
physical = "Physical"

def WriteDataInFile(time, message):
    text = f"[{time}] {message}\n"
    with open("HealthyPrgramerLogs.txt","a") as w:
        w.write(text)
        w.close()

def playmusic(filename,  volume = 1.0, loop = 1):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(float(volume))
    mixer.music.play(int(loop))

def stopmusic(exercise_name):
    if exercise_name == "Water":
        ex_name = "drank"
        print(f"After Drinking the Water Please type '{ex_name}' to STOP the MUSIC")
    elif exercise_name == "Eye":
        ex_name = "eydone"
        print(f"After Eye Exercise Please type '{ex_name}' to STOP the MUSIC")
    elif exercise_name == "Physical":
        ex_name = "exdone"
        print(f"After Physical Exercise Please type '{ex_name}' to STOP the MUSIC")
    while(True):
        try:
            value = input()
            if value == "drank" and ex_name == "drank" or value == "eydone" and ex_name == "eydone" or value == "exdone" and ex_name == "exdone":
                mixer.music.stop()
                mixer.music.unload()
                break
            else:
                print(f"Wrong Input! Please Enter '{ex_name}' to STOP Music!")
                continue
        except:
            print(f"Wrong Input! Please Enter '{ex_name}' to STOP Music!")
            continue

def RealTime():
    global timeinmins, timeinsec, timeinhours, seconds, mins, hours
    seconds = int( datetime.datetime.now().strftime("%S"))
    mins = int(datetime.datetime.now().strftime("%M"))
    hours = int(datetime.datetime.now().strftime("%H"))
    hoursminsec = f"{hours:02d}:{mins:02d}:{seconds:02d}"
    return hoursminsec
    
waterliter = 3.5
nextmins =0
time2 = ""
hoursminsec1 = RealTime()
while(hoursminsec1 >= "09:00:00" and hoursminsec1 <= "17:00:00"):
    hoursminsec = RealTime()
    if hoursminsec == "09:00:00":
        nextmins = 35
        nexthours = int(timeinhours)
        time1 = f"{nexthours:02d}:{nextmins:02d}:00"
        time2 = str(time1)
    if nextmins > 60:
        nextmins = nextmins-60
        nexthours = nexthours+1
        time1 = f"{nexthours:02d}:{nextmins:02d}:00"
        time2 = str(time1)
    # Drink Half Liter(0.5 liter) Water after every 1 hour
    if  waterliter != 0.0 and hoursminsec != "09:00:00" and hoursminsec != "09:40:00" and hoursminsec != "17:00:00" and f"{mins:02d}" == "40" and f"{seconds:02d}" == "00":
        print("Go and Drink Half Litre Water Now!")
        playmusic("water.mp3")
        stopmusic(water)
        WriteDataInFile(timedate, "You Drank Water")
        waterliter = waterliter-0.5
        print("Good Job! Get back to work:)")
    # Do Eye Exercise after every 30 Minutes
    if f"{mins:02d}" == "00" and hoursminsec != "09:00:00" and hoursminsec != "17:00:00" or f"{mins:02d}" == "30" and f"{seconds:02d}" == "00":
        print("Go and Do EYE Exercise Now!")
        playmusic("eyes.mp3")
        stopmusic(eye)
        WriteDataInFile(timedate, "You Did Eye Exercise")
        print("Good Job! Get back to work:)") 
    # Do Physical Exercise after every 35 Minutes
    if hoursminsec == time2:
        print("Go and Do Physical Exercise Now!")
        nextmins = nextmins +35
        playmusic("physical.mp3")
        stopmusic(physical)
        WriteDataInFile(timedate, "You Did Physical Exercise")
        print("Good Job! Get back to work:)")