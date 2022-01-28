import math
from os import system
def clear():
    _ = system('cls')
def resetscreen():
    print("Type Anything to go to the Main Menu")
    reset = input()
    display1()
    return Wrong()

def display1():
    clear()
    print("------------------------------------------------------------")
    print("|                                                          |")
    print("|          ..:|>>> Calculator By Zakria,<|:..              |")          
    print("|                                                          |")
    print("------------------------------------------------------------")
    print("Entre the Function Number that you want to perform.\n")
    print("1:Addition          ||    2:Subtraction")
    print("3:Multiplication    ||    4:Division")
    print("5:Power of Number   ||    6:Square Root")
    print("7:Remainder         ||    8:cos0")
    print("9:sin0              ||    10:tan0")
    print("11:log              ||    12:Area of circle")
          
def Wrong():
    select = input()
    if select == "1":
        clear()
        print("..:|>>> Addition,<|:..")
        print("Entre First Number :")
        ax = int(input())
        print("Entre Secound Number :")
        bx = int(input())
        print("Sum of your two numbers is :", ax + bx)
        
        return  resetscreen()
    elif select == "2":
        print("..:|>>> Subtraction,<|:..")
        print("Entre First Number :")
        ax = int(input())
        print("Entre Secound Number :")
        bx = int(input())
        print("Subraction of your two numbers is :", ax - bx)
        
        return  resetscreen()
    elif select == "3":
        print("..:|>>> Multiplication,<|:..")
        print("Entre First Number :")
        ax = int(input())
        print("Entre Secound Number :")
        bx = int(input())
        print("Multiplication of your two numbers is :", ax * bx)
        
        return  resetscreen()
    elif select == "4":
        print("..:|>>> Division,<|:..")
        print("Entre First Number :")
        ax = int(input())
        print("Entre Secound Number :")
        bx = int(input())
        print("Division of your two numbers is :", ax / bx)
        
        return  resetscreen()
    elif select == "5":
        print("..:|>>> Power of Number,<|:..")
        ax = int(input("Entre Number :\n"))
        print("Entre Power of Number :")
        bx = int(input())
        print("The Answer is :", ax**bx)
        
        return  resetscreen()    
    elif select == "6":
        print("..:|>>> Square Root,<|:..")
        ax = int(input("Entre Number :\n"))
        print("The Answer is :",math.sqrt(ax))
        
        return  resetscreen()
    elif select == "7":
        print("..:|>>> Remainder,<|:..")
        print("Entre First Number :")
        ax = int(input())
        print("Entre Second Number :")
        bx = int(input())
        print("The Answer is :",math.remainder(ax,bx))
        
        return  resetscreen()    
    elif select == "8":
        print("..:|>>> cos0,<|:..")
        ax = int(input("Entre Number :\n"))
        print("The cos0 is :",math.cos(ax))
        
        return  resetscreen()    
    elif select == "9":
        print("..:|>>> sin0,<|:..")
        ax = int(input("Entre Number :\n"))
        print("The sin0 is :",math.sin(ax))
        
        return  resetscreen()    
    elif select == "10":
        print("..:|>>> tan0,<|:..")
        ax = int(input("Entre Number :\n"))
        print("The tan0 is :",math.tan(ax))
        
        return  resetscreen()    
    elif select == "11":
        print("..:|>>> log,<|:..")
        ax = int(input("Entre Number :\n"))
        print("The log is :",math.log(ax))
        
        return  resetscreen()      
    elif select == "12":
        print("..:|>>> Area of Circle,<|:..")
        ax = int(input("Entre Radius of Circle :\n"))
        print("The Area of Circle is :", 3.14*ax*ax)
        
        return  resetscreen()      
    else:
        display1()
        print("ERROR :Wrong Input")
        return Wrong()

display1()
Wrong()