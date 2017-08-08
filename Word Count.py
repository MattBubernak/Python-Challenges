#This is the codes for Counting words in sentence with Python.

#declaring variables.
userchoice = 0


print() # <- get a line break.
print("     WELCOME TO RABIN'S WORD COUNTER PROGRAM 2.0")
print() # <- get a line break.

while userchoice != 2:
    # displays menu.
    print("     Make Your Choice..")
    print("     ==================")
    print() # <- get a line break.
    print("     1. Start the Word Count >>")
    print("     2. End the program <<")
    print() # <- get a line break.
    userchoice = input("     Enter your choice number: ")
    print() # <- get a line break.

    # checks for choice.
    if userchoice == str(1):
        
        print() # <- get a line break.
        inputSentence = input("     Enter any sentence of which you want to count words: ")
        print() # <- get a line break.

        # count for the space in the sentence.
        spaceCount = 0

        # checks for each characters in sentence.
        for character in inputSentence:
            if character == " ":
                spaceCount = spaceCount+1


        # declaring the number of words.
        numWord = spaceCount+1

        print() # <- get a line break.
        print("     There are " + str(numWord) + " words: ")
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
                

