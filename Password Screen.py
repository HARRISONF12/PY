attempts = 0
while attempts <3:
    typepassword = input ("please enter your password")
    if typepassword == "Hello":
        print ("well done you have entered the correct password")
        break
    else:
        print ("wrong password try again")
        attempts += 1
        if (attempts == 3) :
            print ("password locked")
