#This is the codes for generating fibonaachi sequence program.

#declaring variables.
userchoice = 0


print() # <- get a line break.
print("     WELCOME TO RABIN'S FIBONAACHI SEQUENCE")
print() # <- get a line break.

while userchoice != 2:
    # displays menu.
    print("     Make Your Choice..")
    print("     ==================")
    print() # <- get a line break.
    print("     1. Start the Fibonaachi Sequence >>")
    print("     2. End the program <<")
    print() # <- get a line break.
    userchoice = input("     Enter your choice number: ")
    print() # <- get a line break.

    # checks for choice.
    if userchoice == str(1):

        def fibonaci(n):
            firstNum, lastNum = 1,1

            for looper in range(n-1):
                firstNum,lastNum = lastNum, firstNum+lastNum
            
            return firstNum
        

        print() # <- get a line break.
        sequenceLen = input("     Enter the number of character for the seqquence: ")
        print() # <- get a line break.

        print() # <- get a line break.
        for looper in range(1,int(sequenceLen)+1):
            print("     Position "+str(looper)+" : "+str(fibonaci(looper)))
        print() # <- get a line break.


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
