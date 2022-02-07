#--------------------------------------------
#Radian to Degress
#--------------------------------------------
# def radiantodegree(value):
#     pi = 3.14159265359
#     degree = 180/pi*value
#     return degree

# user = int(input("Enter radian to convert it into degress\n"))
# print(radiantodegree(user))


#--------------------------------------------
# Sort List in ascending and descending order
#--------------------------------------------
# def sortlist(list, string1):
#     if string1 == "asc":
#         return sorted(list)
#     elif string1 == "desc":
#         return sorted(list,reverse=True)
#     elif string1 == "none":
#         return list
#     else:
#         print("Wrong Input! Noob")

# list1 = ["a","c","e","d","b"]
# user = input("Enter asc desc or none\n")
# s = sortlist(list1,user)
# print(s)

#--------------------------------------------
# Count the vowels in a string
#--------------------------------------------
# def contvowels(word):
#     vowels = ["a","e","i","o","u"]
#     lol =  list(word)
#     count = 0
#     for i in vowels:
#         for s in lol:
#             if i == s:
#                 count += 1
#     print(f"There are '{count}' vowels in '{word}'")            
# user = input("Enter a string\n")
# contvowels(user)

#--------------------------------------------
# Hide the credit card number
#--------------------------------------------

# user = input("Enter Credit Card Number\n")
# def hideString(number, showletters = 4, hiddenlettersymbol = "*"):
#     listofnumbers = list(number)
#     digits = ""
#     words = 0
#     newlist2 = []
#     for i in listofnumbers:
#         words += 1
#     if words-showletters >= 0:
#         for s in range(words-showletters,words):
#             newlist2.append(listofnumbers[s])
#         for e in newlist2:
#             digits += e
#     else:
#         print("Second Argument is Invaild!")
#     letters = words-showletters
#     hideletters = hiddenlettersymbol*letters
#     hidden = f"{hideletters}{digits}"
#     return hidden

# s = hideString(user)
# print(s)

#--------------------------------------------
# Give me the discount
#--------------------------------------------
# user = input("Enter Iteam Price\n")
# user2 = input("Enter Discount\n")
# def discount(price, discounted):
#     itemprice = discounted/100*price
#     return int(price-itemprice)

# s = discount(int(user),int(user2))
# print("Total price:",s)

#--------------------------------------------
# Just the numbers
#--------------------------------------------

# lol = ["a", 1,2,"c","b",5,4,"s"]
# def onlynumbers(list1):
#     letter = ""
#     list2 = []
#     for i in list1:
#         letter = str(i)
#         if letter.isnumeric():
#             list2.append(letter)
#     return print(list2)

# onlynumbers(lol)

#--------------------------------------------
# Repeat the characters
#--------------------------------------------

# user = input("Enter a String\n")
# def repeatcharacters(value):
#     list1 = list(value)
#     dobuleletter = ""
#     for i in list1:
#         letter = str(i)
#         dobuleletter += letter*2
#     return print(dobuleletter)

# repeatcharacters(user)

#--------------------------------------------
# Encoder
#--------------------------------------------

# user = input("Enter a String\n")

# list1 = ["a", "e", "i", "o", "u"]
# list2 = ["@", "3", "!", "0", "#"]
# def encoder(message, list1, list2):
#     list0 = list(message)
#     word = ""
#     digit = 0
#     digit2 = 0
#     for s in list1:
#         digit += 1
#     for se in list2:
#         digit2 += 1
#     num = digit-1
#     if digit == digit2:
#         for e in list0:
#             if e in list1:
#                 while(True):
#                     if e == list1[num]:
#                         word += list2[num]
#                     num -=1
#                     if num < 0:
#                         num = digit-1
#                         break
#             else:
#                 word += e
#         return word
#     else:
#         print("Encoding Error: Number of Items of 2nd and 3rd Arguments are not matched")
    
# encoded = encoder(user, list1, list2)
# print(encoded)
# # print(f"encoded: {encoded}")
# # decoded = encoder(encoded, list2, list1)
# # print(f"decoded: {decoded}")


#--------------------------------------------
# Capital Indexes
#--------------------------------------------


# st = "HeLlO"
# def capital_indexes(string1):
#     ls = list(string1)
#     word = 0
#     word2 = []
#     for i in ls:
#         word += 1
#         if i.isupper() == True:
#             word2.append(word-1)
#     return word2
# print(capital_indexes(st))

#--------------------------------------------
# Middle Letter
#--------------------------------------------

# st = "HeLlo"
# def mid(stringvalue):
#     if len(stringvalue)%2 == 0:
#         return ""
#     return stringvalue[len(stringvalue)//2]
# print(mid(st))

#--------------------------------------------
# Online Status
#--------------------------------------------

#status = {"Zakria":"Online","Abdullah":"Online","Usama":"Offline","Usman":"Online","Umer":"Online","Talha":"Offline"}
# def online_count(dictionary):
#     list1 = list(dictionary.values())
#     word = 0
#     for i in list1:
#         if i == "online":
#             word += 1
#     return word

# print(online_count(status))

#--------------------------------------------
# Random Number(Randomness)
#--------------------------------------------

# import random
# def random_number():
#     return random.randint(1,100)
# print(random_number())

#--------------------------------------------
# Type Check
#--------------------------------------------

# def only_ints(first, second):
#     return type(first) == int and type(second) == int
# print(only_ints(1,2))

#--------------------------------------------
# Double letters
#--------------------------------------------
# user = "hello"
# def double_letters(string):
#     list1 = list(string)
#     word = ""
#     for i in list1:
#         if i == word:
#             return True
#         word = i
#     return False
# print(double_letters(user))

#--------------------------------------------
# Adding and Removing Dots
#--------------------------------------------

# user = "test"
# def add_dots(s):
#     return ".".join(s)

# def remove_dots(s):
#     return s.replace(".", "")
# print(add_dots(user))

#--------------------------------------------
# Counting Syllables
#--------------------------------------------

# def count(string):
#     return len(string.split("-"))
# print(count("ho-tel"))

#--------------------------------------------
# Anagrams
#--------------------------------------------

# Method 1
# def is_anagram(string1, string2):
#     list1 = list(string1)
#     list1.sort()
#     list2 = list(string2)
#     list2.sort()
#     if list1 == list2:
#         return True
#     else: return False

# Method 2
# def is_anagram(string1, string2):
#     list1 = list(string1)
#     list2 = list(string2)
#     for i in list1:
#         if list1.count(i) == list2.count(i):
#             return True
#         else: return False
        
# print(is_anagram("test", "tets"))

#--------------------------------------------
# Flatten a list
#--------------------------------------------

# def flatten(list1):
#     list2 = []
#     for i in list1:
#         for s in i:
#             list2.append(s)
#     return list2
# print(flatten([[1, 2], [3, 4]]))

#--------------------------------------------
# Min-maxing
#--------------------------------------------

# def largest_difference(list1):
#     list1.sort()
#     if list1[-1] <=100 and list1[0] >= -100:
#         return (list1[-1]-list1[0])
# print(largest_difference([1, 2, 3]))

#--------------------------------------------
# Divisible by 3
#--------------------------------------------

# def div_3(intvalue):
#     if intvalue%3 == 0:
#         return True
#     else: return False
#   OR
#     return intvalue%3 == 0
# print(div_3(5))

#-------------------------
# Palindrome
#-------------------------

# def palindrome(string):
#     reversedtext = list(reversed(string))
#     word = ""
#     for i in reversedtext:
#         word += i
#     if string == word:
#         return True
#     else: return False
#OR
# def palindrome(string):
#     return string == string[::-1]
# print(palindrome("abba"))

#-------------------------
# Up and Down
#-------------------------

# def up_down(value):
#     return (value-1, value+1)
# print(up_down(8))

#-------------------------
# Consecutive zeros
#-------------------------

# def consecutive_zeros(value):
#     result = 0
#     streak = 0
#     for letter in value:
#         if letter == "0":
#             streak += 1
#         else:
#             streak = 0
#         result = max(result, streak)
#     return result
# print(consecutive_zeros("1000011010000010000010"))

#-------------------------
# All Equal
#-------------------------

# def all_equal(list1):
#     new = list1[0]
#     for i in list1:
#         if new != i:
#             return False
#     return True
# print(all_equal([1,1,1]))

#-------------------------
# Boolean and
#-------------------------

# def triple_and(param1, param2, param3):
#     return param1 and param2 and param3
# print(triple_and(True,True,True))

#----------------------------------------------------------------------------------------------------
# Writing short code (Converting List 'int' items into 'string' items just in one line)
#----------------------------------------------------------------------------------------------------

# def convert(list1):
#     return [str(i) for i in list1]
# print(convert([1, 2, 3]))

#-------------------------
# Custom zip
#-------------------------

# def zap(list1, list2):
#     word = 0
#     list3 = []
#     while(True):
#         if len(list1) == word:
#             break
#         list3.append((list1[word],list2[word]))
#         word +=1
#     return list3
# OR
# def zap(a, b):
#     return [(a[i], b[i]) for i in range(len(a))]
# print(zap(
#     [0, 1, 2, 3],
#     [5, 6, 7, 8]
# ))

#-------------------------
# Solution validation
#-------------------------

# def validate(code):
#     if "def" not in code:
#         return "missing def"
        
#     if ":" not in code:
#         return "missing :"
#     if "(" not in code or ")" not in code:
#         return "missing paren"
#     if "()" in code:
#         return "missing param"
#     if "    " not in code:
#         return "missing indent"
#     if "validate" not in code:
#         return "wrong name"
#     if "return" not in code:
#         return "missing return"
#     return True
# print(validate('def validate(a):    return'))

#-------------------------
# List xor
#-------------------------

# def list_xor(n,list1,list2):
#     if n in list1 and n not in list2 or n in list2 and n not in list1:
#         return True
#     if n in list1 or n in list2:
#         return False
#     else: return False
#OR
# def list_xor(n, list1, list2):
#     return (n in list1) ^ (n in list2)
# print(list_xor(1,[0, 0, 0], [4, 5, 6]))

#-------------------------
# Counting Parameters
#-------------------------

# def param_count(*args):
#     return len(args)
# print(param_count(1,2,3))

#-------------------------
# Thousands separator
#-------------------------

# def format_number(value):
#     word = 0
#     text = ""
#     for i in list(str(value))[::-1]:
#         if word == 3:
#             text += ","
#             word = 0
#         word += 1
#         text += i
#     return text[::-1]
# print(format_number(1000000))

#--------------------------------------------
# Tic tac toe input
#--------------------------------------------
# board = [
#     [" ", " ", " "],
#     [" ", " ", " "],
#     [" ", " ", " ",]
#     ]
# def get_row_col(value):
#     column = 0
#     row = 0
#     for i in value:
#         if i == "A":
#             column = 0
#         if i == "B":
#             column = 1
#         if i == "C":
#             column = 2
#         else: row = i
#     return (int(row)-1, column)
# print(get_row_col("B1"))

#--------------------------------------------
# Computer AI for Tic Tac Toe Game
#--------------------------------------------
# import random
# import numpy
# user1char = "X"
# cpuchar = "O"
# cpuchoice = ""
# address = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
# board = [
#     ["O", "O", " "],
#     ["O", " ", "X"],
#     [" ", " ", "X",]
# ]
# def showboard():
#     global board
#     print("    A   B   C ")
#     print("   -----------")
#     print(f"1:  {board[0][0]} | {board[0][1]} | {board[0][2]} ")
#     print("   -----------")
#     print(f"2:  {board[1][0]} | {board[1][1]} | {board[1][2]} ")
#     print("   -----------")
#     print(f"3:  {board[2][0]} | {board[2][1]} | {board[2][2]} ")

# def get_row_col(value):
#     translate = {"A": 0, "B": 1, "C": 2}
#     letter = value[0]
#     number = value[1]
#     row = int(number) - 1
#     column = translate[letter]
#     return (row, column)

# def cpuAI():
#     global board, user1char,cpuchar, cpuchoice,address
#     list1 = numpy.array(board)
#     translate = {0: "A",1:  "B",2: "C"}
#     translate2 = {0: 1 ,1: 2 ,2: 3}
#     word = 0
#     word1 = 0
#     count = 0
#     column = ""
#     for i in range(len(board)):
#         s = list(list1[:,i])
#         l = board[i]
#         if " " in l or " " in s:
#             for se in l:#Rows
#                 if se == user1char:
#                     word = 0
#                     break
#                 elif se == " ":
#                     count +=1
#                     if count == 2:
#                         count = 0
#                         word = 0
#                         break
#                 else:
#                     word += 1
#                     if word == 2:
#                         word = 0
#                         if " " in l:
#                             column = translate[l.index(" ")]
#                             cpuchoice = f"{column}{i+1}"
#                             break
#             for sc in s: # column
#                 if sc == user1char:
#                     word = 0
#                     break
#                 elif sc == " ":
#                     count +=1
#                     if count == 2:
#                         count = 0
#                         word = 0
#                         break
#                 else:
#                     word += 1
#                     if word == 2:
#                         word = 0
#                         if " " in s:
#                             row = translate2[s.index(" ")]
#                             column = translate[i]
#                             cpuchoice = f"{column}{row}"
#                             break
#         if cpuchoice == "":                                     
#             for le in l:
#                 if le == cpuchar:
#                      word1 = 0
#                      break
#                 elif le == " ":
#                     count +=1
#                     if count == 2:
#                         count = 0
#                         word1 = 0
#                         break
#                 else:
#                     word1 += 1
#                     if word1 == 2:
#                         word1 = 0
#                         if " " in l:
#                             column = translate[l.index(" ")]
#                             cpuchoice = f"{column}{i+1}"
#                             break
#             for lc in s:
#                 if lc == cpuchar:
#                     word1 = 0
#                     break
#                 elif lc == " ":
#                     count +=1
#                     if count == 2:
#                         count = 0
#                         word1 = 0
#                         break
#                 else:
#                     word1 += 1
#                     if word1 == 2:
#                         word1 = 0
#                         if " " in s:
#                             row = translate2[s.index(" ")]
#                             column = translate[i]
#                             cpuchoice = f"{column}{row}"
#                             break

# cpuAI()
# print(cpuchoice)
# while(True):
#     if cpuchoice == "": cpuchoice = random.choice(address)
#     #print(cpuchoice)
#     b2 =get_row_col(cpuchoice)
#     if board[b2[0]][b2[1]] == " ":
#         board[b2[0]][b2[1]] = cpuchar
#         showboard()
#         break
#     else:
#         cpuchoice = random.choice(address)
#         continue