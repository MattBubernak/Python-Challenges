#This is the codes for Password Encryption program.

#declaring variables.
userchoice = 0


print() # <- get a line break.
print("     WELCOME TO RABIN'S PASSWORD ENCRYPTION")
print() # <- get a line break.

while userchoice != 2:
    # displays menu.
    print("     Make Your Choice..")
    print("     ==================")
    print() # <- get a line break.
    print("     1. Start the Password Encryption >>")
    print("     2. End the program <<")
    print() # <- get a line break.
    userchoice = input("     Enter your choice number: ")
    print() # <- get a line break.

    # checks for choice.
    if userchoice == str(1):

        passwordValue={"a":"abc", "b":"def", "c":"ghi", "d":"jkl", "e":"mno", "f":"pqr","g":"stu","h":"vwx", "i":"yzy","j":"12a"}

        print() # <- get a line break.
        password = input("     Enter the Password you want to save (Use character from a-j): ")
        print() # <- get a line break.

        encryptedPassword = ""

        for looper in range(0,len(password)):
            character = password[looper]
            encryptedPassword = encryptedPassword + str(passwordValue[character])

        print() # <- get a line break.
        print("     Password is encrypted!")
        print() # <- get a line break.


        print() # <- get a line break.
        print("     Do you want to match passwords..")
        print("     ================================")
        print() # <- get a line break.
        print("     1. Yes")
        print("     2. No")
        print() # <- get a line break.
        inputChoice = input("     Enter your choice number.. : ")
        print() # <- get a line break.

        if inputChoice == str(1):
            print() # <- get a line break.
            newPassword = input("     Enter the password you wanna match.. ")
            print() # <- get a line break.

            encryptedPasswordNew = ""
            for looper in range(0,len(newPassword)):
                characterNew = newPassword[looper]
                encryptedPasswordNew = encryptedPasswordNew + str(passwordValue[characterNew])

            if encryptedPasswordNew == encryptedPassword:
                print() # <- get a line break.
                print("     Password matches!")
                print() # <- get a line break.

            else:
                print() # <- get a line break.
                print("     Password doesn't matches!")
                print() # <- get a line break.
                
        elif inputChoice == str(2):
            break

        else:
            print() # <- get a line break.
            print("     Invalid Choice..!")

        print() # <- get a line break.
        print("     Do you want to see Encrypted password..")
        print("     =======================================")
        print() # <- get a line break.
        print("     1. Yes")
        print("     2. No")
        print() # <- get a line break.
        inputChoice = input("     Enter your choice number.. : ")
        print() # <- get a line break.

        if inputChoice == str(1):
            print() # <- get a line break.
            print("     The Encrypted Passwoed is : " + str(encryptedPassword))
            print() # <- get a line break.

        elif inputChoice == str(2):
            break

        else:
            print() # <- get a line break.
            print("     Invalid Choice..!")


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
