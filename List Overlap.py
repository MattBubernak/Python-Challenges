#This is the codes for list overlap with Python.

#declaring variables.
userchoice = 0


print() # <- get a line break.
print("     WELCOME TO RABIN'S LIST OVERLAP 5.1")
print() # <- get a line break.

while userchoice != 2:
    # displays menu.
    print("     Make Your Choice..")
    print("     ==================")
    print() # <- get a line break.
    print("     1. Start the List Overlap >>")
    print("     2. End the program <<")
    print() # <- get a line break.
    userchoice = input("     Enter your choice number: ")
    print() # <- get a line break.

    # checks for choice.
    if userchoice == str(1):
        
        print() # <- get a line break.
        print("     Let's create the 2 different lists..")
        print() # <- get a line break.
        print("     List 1")
        print() # <- get a line break.

        print("     Let's enter the numbers..")
        print("     =========================")
        print() # <- get a line break.
        print("     1. Enter the numbers..")
        print("     2. Generate random numbers..")
        print() # <- get a line break.
        inputChoice = input("     Enter your choice number: ")
        print() # <- get a line break.

        # checks for inout choice.
        if inputChoice == str(1):
            firstList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            for looper in range(0,10):
                firstList[looper] = int(input("     Enter the number for position " + str(looper+1) + " : "))

            print("     Data were successfully added..")


            print() # <- get a line break.
            print("     Your entered elements are..")
            print() # <- get a line break.
                
            position = 1
            for looper in range(0,10):
                print("     Position: " + str(position) + " --> " + str(firstList[looper]))
                position = position+1

                
        elif inputChoice == str(2):
            firstList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            for looper in  range(0,10):
                import random
                firstList[looper] = random.randint(0,100)

            print("     Datae were successfully added..")


            print() # <- get a line break.
            print("     Your generated elements are..")
            print() # <- get a line break.

            position = 1
            for looper in range(0,10):
                print("     Position: " + str(position) + " --> " + str(firstList[looper]))
                position = position+1



        print() # <- get a line break.
        print() # <- get a line break.
        print("     List 2")
        print() # <- get a line break.

        print("     Let's enter the numbers..")
        print("     =========================")
        print() # <- get a line break.
        print("     1. Enter the numbers..")
        print("     2. Generate random numbers..")
        print() # <- get a line break.
        inputChoice = input("     Enter your choice number: ")
        print() # <- get a line break.

        # checks for inout choice.
        if inputChoice == str(1):
            secondList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            for looper in range(0,15):
                secondList[looper] = int(input("     Enter the number for position " + str(looper+1) + " : "))

            print("     Data were successfully added..")


            print() # <- get a line break.
            print("     Your entered elements are..")
            print() # <- get a line break.
                
            position = 1
            for looper in range(0,15):
                print("     Position: " + str(position) + " --> " + str(secondList[looper]))
                position = position+1

                
        elif inputChoice == str(2):
            secondList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            for looper in  range(0,15):
                import random
                secondList[looper] = random.randint(0,100)

            print("     Datae were successfully added..")


            print() # <- get a line break.
            print("     Your generated elements are..")
            print() # <- get a line break.

            position = 1
            for looper in range(0,15):
                print("     Position: " + str(position) + " --> " + str(secondList[looper]))
                position = position+1


        # comparision goes here.
        print() # <- get a line break.
        print() # <- get a line break.
        continueAuthority = input("     Press any number to continue..")
        print() # <- get a line break.
        print() # <- get a line break.
        
        for a in range(0,len(firstList)):
            for z in range(0,len(secondList)):
                if firstList[a] == secondList[z]:
                    print("     Common elements : " + str(firstList[a]))
        

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
    continueAuthority = input("     Press 5 to continue.. ")
    print() # <- get a line break.
    print() # <- get a line break.
    userchoice = int(continueAuthority)

# loop executes until the userchoice is not 2.
                

