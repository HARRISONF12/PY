from random import *
running = True
adjectives = [ "amazing" , "above-average" ,
"excellent" ]
hobbies = [ "riding a bike" , "programming" , "making a cup of tea" ]
print("Compliment Generator")
print("--------------------")
name = input("What is your name?: ")
print('''
Menu
c = get compliment
a = add hobby to list
d = delete hobby from list
p = print hobbies
q = quit
''')

while running == True:
    menuChoice = input("INPUT LETTER: ").lower()

    if menuChoice == 'c':
        print( "Here is your compliment" , name , ":" )

        print( name , "you are" , choice(adjectives) ,"at" , choice(hobbies) )

        print( "You're welcome!")

    elif menuChoice == 'a':
        itemToAdd = input("Please enter the hobby to add: ")
        if itemToAdd in hobbies:
            print("item already exists")

        hobbies.append(itemToAdd)

    elif menuChoice == 'd':
        itemToDelete = input("Please enter the hobby to remove: ")

        if itemToDelete in hobbies:
            hobbies.remove(itemToDelete)
        else:
            print("Hobby not in list!")

    elif menuChoice == 'p':
        print(hobbies)

    elif menuChoice == 'q':
        running = False
    else:
        print("Hobby not in list!")
