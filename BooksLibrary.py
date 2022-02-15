from os import system
import opmodule
class Library():
    def __init__(self, library_name, listofbooks):
        self.library_name = library_name
        self.listofbooks = listofbooks
    def display_books(self):
        system("cls")
        print(f"There are '{len(self.listofbooks)}' books in our Library! There Name was:")
        for i,s in enumerate(self.listofbooks,start=1):
            print(f"{i}: {s}")
    def lend_book(self):
        global lendedbooks, usernames
        system("cls")
        print(f"There are '{len(self.listofbooks)}' books in our Library! There Name was:")
        for i,s in enumerate(self.listofbooks,start=1):
            if s in list(lendedbooks.keys()):
                print(f"{i}: {s} - already taken by '{lendedbooks[s]}'")
            else:
                print(f"{i}: {s}")
        print("\n0: Back\n")
        print("Please Select te Book Which you want to Lend!")
        while(True):
            userbook = opmodule.intvalue(0,i)
            if userbook == 0: 
                mainmenu()
                break
            else:
                if self.listofbooks[userbook-1] in lendedbooks.keys():
                    print(f"This Book is already taken! Please Choose any other book")
                else: 
                    print(f"Please Enter Your Name to lend '{self.listofbooks[userbook-1]}' Book!")
                    username = input()
                    if username in usernames:
                        print("You have already taken 1 Book! Please return it first then take another book")
                        Back()
                        break
                    else:
                        lendedbooks.update({self.listofbooks[userbook-1]:username})
                        usernames.append(username)
                        print(f"You have Successfully taken '{self.listofbooks[userbook-1]}' Book!")
                        Back()
                        break
    def return_book(self):
        system("cls")
        global lendedbooks,usernames
        word = 0
        if len(list(lendedbooks.keys())) != 0:
            print("Which Book you want to Return?")
        else: print("No Book is Taken from us")
        for s in list(lendedbooks.keys()):
            word +=1
            print(f"{word}: {s}")
        print("\n0: Back\n")
        while(True):
            userbook = opmodule.intvalue(0,word)
            if userbook == 0: 
                mainmenu()
                break
            else:
                print(f"Please Enter Your Name to return '{list(lendedbooks.keys())[userbook-1]}' Book!")
                username = input()
                if username in usernames and username == lendedbooks[list(lendedbooks.keys())[userbook-1]]:
                    usernames.remove(username)
                    del lendedbooks[list(lendedbooks.keys())[userbook-1]]
                    print(f"You have Successfully returned the Book!")
                    Back()
                    break
                else:
                    print("How you can Return a Book which you don't have taken?")
                    Back()
                    break
    def add_book(self):
        system("cls")
        print("Please Enter the Name of Book Which you want to Add!")
        user = input()
        self.listofbooks.append(user.capitalize())
        print(f"Your Book '{user}' is Added Successfully!")
        print(self.listofbooks)
        print("\n0: Back\n1: Add a New Book")
        user1 = opmodule.intvalue(0,1)
        if user1 == 0:
            mainmenu()
        elif user1 == 1:
            self.add_book()

def Back():
    print("\n0: Back")
    user = opmodule.intvalue(0,0)
    if user == 0:
        system("cls")
        mainmenu()
    
lib_name = "Zakira's Library"
books = ["Math","Chemistry","Biology","Physics"]
lendedbooks = {}
usernames = []
def mainmenu():
    global lib_name, books
    zakiralibrary = Library(lib_name, books)
    system("cls")
    print("---------------------------------------")
    print(f"|     Welcome to {lib_name}     |")
    print("---------------------------------------\n")
    print("Please Enter your Choice:")
    print("1: Add Book\n2: Display Books\n3: Lend Book\n4: Return Book\n5: Exit Program")
    user1 = opmodule.intvalue(1,5)
    if user1 == 1:
        zakiralibrary.add_book()
    elif user1 == 2:
        zakiralibrary.display_books()
        Back()
    elif user1 == 3:
        system("cls")
        zakiralibrary.lend_book()
    elif user1 == 4:
        system("cls")
        zakiralibrary.return_book()
    elif user1 == 5:
        system("cls")
        print("--------------------------------------------------------")
        print("Do you really want to Exit the Program? 1 = Yes, 0 = No")
        print("--------------------------------------------------------")
        user2 = opmodule.intvalue(0, 1)
        if user2 == 1:
            system("cls")
        elif user2 == 0:
            system("cls")
            mainmenu()

mainmenu()