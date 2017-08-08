#This is the codes for Bubble Sort with Python.

#declaring variables.
userchoice = 0


print() # <- get a line break.
print("     WELCOME TO RABIN'S BUBBLE SORT")
print() # <- get a line break.

while userchoice != 2:
    # displays menu.
    print("     Make Your Choice..")
    print("     ==================")
    print() # <- get a line break.
    print("     1. Start Bubble Sort >>")
    print("     2. End the program <<")
    print() # <- get a line break.
    userchoice = input("     Enter your choice number: ")
    print() # <- get a line break.

    # checks for choice.
    if userchoice == str(1):
        print("     10 numbers are required to be sorted..")
        print("     ======================================")
        print() # <- get a line break.
        print("     1. Enter the numbers..")
        print("     2. Generate random numbers..")
        print() # <- get a line break.
        inputChoice = input("     Enter your choice number: ")
        print() # <- get a line break.

        # checks for inout choice.
        if inputChoice == str(1):
            Array = [1,2,3,4,5,6,7,8,9,10]
            for ArrayContents in  range(0,10):
                Number = input("     Enter the number for position " + str(ArrayContents) + " : ")
                Array[ArrayContents] = int(Number)

            print("     Data were successfully added..")


            print() # <- get a line break.
            print("     Your entered elements are..")
            print() # <- get a line break.
            position = 1
            for ArrayContents in Array:
                print("     Position: "+ str(position) + " --> " + str(ArrayContents))
                position = position+1

                
        elif inputChoice == str(2):
            Array = [1,2,3,4,5,6,7,8,9,10]
            for ArrayContents in  range(0,10):
                import random
                Array[ArrayContents] = random.randint(0,100)

            print("     Datae were successfully added..")


            print() # <- get a line break.
            print("     Your generated elements are..")
            print() # <- get a line break.
            position = 1
            for ArrayContents in Array:
                print("     Position: "+ str(position) + " --> " + str(ArrayContents))
                position = position+1


        else:
            print() # <- get a line break.
            print("     Invalid Choice..! ")
            print() # <- get a line break.
            break


        # asks for the type of sort.
        print() # <- get a line break.
        print("     Enter your sorting order..")
        print("     ==========================")
        print() # <- get a line break.
        print("     1. Increasing ++")
        print("     2. Decreasing --")
        print() # <- get a line break.
        sortingChoice = input("     Enter your sorting choice number: ")

        if sortingChoice == str(1):
        # works for the incerasing bubble sort.
            for i in range(0,10):
                for j in range(0,9):
                    if Array[j] > Array[j+1]:
                        tmpholder = Array[j]
                        Array[j] = Array[j+1]
                        Array[j+1] = tmpholder

        elif sortingChoice == str(2):
            for i in range(0,10):
                for j in range(9,0,-1):
                    if Array[j] > Array[j-1]:
                        tmpholder = Array[j]
                        Array[j] = Array[j-1]
                        Array[j-1] = tmpholder

        else:
            print() # <- get a line break.
            print("     Invalid Choice..! ")
            print() # <- get a line break.
            break


        # displays the sorted elements.
        print() # <- get a line break.
        print("     Your sorted elements are..")
        print() # <- get a line break.
        position = 1
        for ArrayContents in Array:
            print("     Position: "+ str(position) + " --> " + str(ArrayContents))
            position = position+1


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
                

