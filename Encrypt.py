l = 0
num = "0123456789"
numList = ["3456789012", "9012345678", "5678901234"]
alpha = "abcdefghijklmnopqrstuvwxyz"
AlphaList = ["cdefghijklmnopqrstuvwxyzab", "jklmnopqrstuvwxyzabcdefghi", "uvwxyzabcdefghijklmnopqrst"] # Add more items to list to change the level of encryption
use = input("Type 'Decrypt or 'Encrypt' to choose which function to use:\n")
use = use.lower()

while True:     # Loop so program doesn't close after a wrong input has been done
    if use == "encrypt": # This is executed if user wants to encrypt
        encr = input("Put in a string to encrypt!\n")
        encr = encr.lower()
        for i in encr:
            if i in alpha:
                j = alpha.index(i) # Checks place in alphabet of the first letter that was put in
                k = AlphaList[l][j] # Sets k to the corresponding letter in the current Alphabet that is chosen in the list
                l = l + 1   # Switches to the next Alphabet in the list
                if l > 2:   # Change this number to number of items in the List AlphaList
                    l = 0   # This prevents that l goes further than the amount of items in AlphaList
            elif i in num:
                j = num.index(i) # Checks place in num of the first number that was put in
                k = numList[l][j] # Sets k to the corresponding number in the current Numberset that is chosen
                l = l + 1   # Switches to the next Numberset in the list
                if l > 2:   # Change this number to number of items in the List numList
                    l = 0   # This prevents that l goes further than the amount of items in numList
            else:
                k = i
            print(k, end = '') # Could enhance this to also capitalize the output
        print()
        input("Press any button to exit.")
        break
    # The following is reversing the process that is used above, so variable j and k are swapped in the way the acquire the Letters
    elif use == "decrypt": # This is executed if user wants to decrypt
        decr = '' # Variable put as empty so strings can be added later on, no need if you don't want to capitalize
        encr = input("Put in a string to decrypt!\n")
        encr = encr.lower()
        for i in encr:
            if i in alpha:
                j = AlphaList[l].index(i)
                k = alpha[j]
                l = l + 1
                if l > 2:   # Change this number to number of items in the List AlphaList
                    l = 0
            elif i in num:
                j = numList[l].index(i)
                k = num[j]
                l = l + 1
                if l > 2:   # Change this number to number of items in the List numList
                    l = 0
            else:
                k = i
            decr = decr + k
        decr = decr.capitalize() # optional but I like it
        print(decr)
        input("Press any button to exit.")
        break
    elif use == "exit": # Gives a manual exit to the program in case user doesn't want to encrypt or decrypt
        break
    else: # execute this until user leaves or puts in a valid string
      use = input("Put in either 'Decrypt' or 'Encrypt' or 'Exit'\n") 
      use = use.lower()

