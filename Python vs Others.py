#This is the codes for Counting words in sentence with Python.

#declaring variables.
userchoice = 0


print() # <- get a line break.
print("     WELCOME TO RABIN'S PYTHON VS OTHER LANGUAGES")
print() # <- get a line break.

while userchoice != 2:
    # displays menu.
    print("     Make Your Choice..")
    print("     ==================")
    print() # <- get a line break.
    print("     1. See the differences >>")
    print("     2. End the program <<")
    print() # <- get a line break.
    userchoice = input("     Enter your choice number: ")
    print() # <- get a line break.

    # checks for choice.
    if userchoice == str(1):
        
        print() # <- get a line break.
        print("     Differences between Python and other languages >>")
        print("     =================================================")
        print() # <- get a line break.

        print("     Python is a very different and easier language then other languages like js, c++ and so on.")
        print("     The way of defining function, assigning variables, data structures and other many things are different.")

        print() # <- get a line break.
        print("     Three of their differences are:")
        print("     1. The syntax of inputing and printing is different..")
        print("        print() or input() in Python which is different than cout >> or cin << in c++.")
        print("        The input() always takes in the string but not a number.")

        print() # <- get a line break.
        print("     2. Line spacing is very important to declare what is included inside what..")
        print("        Let's take a simple example of structure of ifelse declaration")
        print() # <- get a line break.
        print("        For Qbasic:")
        print("        IF condition THEN")
        print("            (do this)")
        print("        ELSE IF condition THEN")
        print("            (do this)")
        print("        ELSE")
        print("            (do this)")
        print() # <- get a line break.

        print("        For C++:")
        print("        if(condition){(do this)}")
        print("        else if(condition){(do this)}")
        print("        else{(do this)}")
        print() # <- get a line break.

        print("        For Python:")
        print("        IF condition:")
        print("        <--->(do this)")
        print("        ELIF condition:")
        print("        <--->(do this)")
        print("        ELSE:")
        print("        <--->(do this)")

        print() # <- get a line break.
        print("     3. Declaring for next loop is different..")
        print("        Let's take a simple example")
        print() # <- get a line break.
        print("        For Qbasic:")
        print("        FOR variable = starting value TO end value STEP increment/decrement")
        print("            (do this each time during loop)")
        print("        NEXT variable")
        print() # <- get a line break.

        print("        For C++:")
        print("        for(int variable = starting value; variable <= end value; variable++){(do this each time during loop)}")
        print() # <- get a line break.

        print("        For Python:")
        print("        for variable in range(starting value, end value, increment/decrement):")
        print("        <--->(do this each time during loop)")
        

    elif userchoice == str(2):
        print() # <- get a line break.
        print("     Good Bye!")
        print() # <- get a line break.
        print() # <- get a line break.
        break

    else:
        print() # <- get a line break.
        print("     Invalid Choice..! ")
        print() # <- get a line break.
        break

    print() # <- get a line break.
    continueAuthority = input("     Press 5 to continue..")
    print() # <- get a line break.
    print() # <- get a line break.
    userchoice = int(continueAuthority)

# loop executes until the userchoice is not 2.
                

