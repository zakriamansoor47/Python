"""Text Animation Program Made by Zakria Mansoor"""

import time # import time for text animation
from os import system # import system for clear screen

# Created a Function Name 'textanimation' to get values from user
# Function Need four arguments 1= stringvalue, 2=letters, 3=speed, 4=spaces
# 1=stringvalue is the string value or text on which text animation will applied
# 2=letters. it is the display size of animated text (must be integer)
# 3=speed. it is the speed of moving of text. (less floating value = More the Speed)
# 4=spaces. it is the size of spaces after the text string ends. (must be integer)
def textanimation(stringvalue, letters = 50, speed = 0.12, spaces = 20):
    space = " "*spaces 
    list1 = list(space+stringvalue) # Convert Spaces+User text(string value) into list
    list2 = [] # created a empty list
    # Created 3 integers
    word = 0
    word2 = 0
    word3 = 0
    text = "" # empty string
    # Now we will Count how much letters in User Text
    for dl in list1:
        word3 +=1
    while(True):
        if word < word3:
            list2.append(list1[word])
            word +=1 
            for i in list2: # Counting how much letters in Second List
                word2 +=1
            if word2 >=letters: # check if the letters in Second list is >= 2nd argument of function
                lol = list2[-letters:] # Removeing frist letter from list
                time.sleep(speed) # Speed of moving of text
                for let in lol: # converting list into string and print it
                    text += let
                    print(f"----------------------------------------|{text}|----------------------------------------", end="\r")
                else: # when the letters in list ends we will set the value of text to empty string
                    text =""
            word2 = 0
        elif word >= word3: # Check if the letters of list2 >= letters of User Text
            word =0


user = input("Enter Something\n")
system('cls')
print("\n\n\n")
textanimation(user, 50, 0.12, 35)
