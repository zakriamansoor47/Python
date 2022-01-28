import time
from os import system
print("|-----: Clock :-----|")

try:
    while(True):
        hours = int(input("Enter Hours: "))
        if hours > 12 or hours < 1:
            print("Please Enter Hourse in 12 hours format")
            continue
        else:
            break
except:
    print("Wrong Input! Please Enter an Integer Value")

try:
    while(True):
        mins = int(input("Enter Minutes: "))
        if mins > 60 or mins < 0:
            print("Wrong Input! Please Enter Vaild Minutes")
            continue
        else:
            break
except:
    print("Wrong Input! Please Enter an Integer Value")

try:
    while(True):
        seconds = int(input("Enter Seconds: "))
        if seconds > 60 or seconds < 0:
            print("Wrong Input! Please Enter Vaild Seconds")
            continue
        else:
            break
except:
    print("Wrong Input! Please Enter an Integer Value")

try:
    while(True):
        ampm = input("AM or PM: ")
        if ampm.lower() == "am" or ampm.lower() == "pm":
            break
        else:
            print("Wrong Input! Please Enter AM or PM")
            continue
            
except:
    print("Wrong Input! Please ")

while(True):
    seconds = seconds+1
    if seconds > 59:
        seconds = 0
        mins = mins+1
    if mins > 59:
        mins = 0
        hours = hours+1
    if hours > 12:
        hours = 1
        if ampm.upper() == "AM":
            ampm = "PM"
        elif ampm.upper() == "PM":
            ampm = "AM"
    time.sleep(1)
    system("cls")
    print("         ..:|>>> Clock <<<|:..           ")
    print(f"              {hours:02d}:{mins:02d}:{seconds:02d} {ampm.upper()}                ")
