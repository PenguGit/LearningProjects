#ON HOLD

#To-Do: Decrypt needs input of key and how many keys, int.input needs to be errorsafe

import secrets
import string
import os
documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
key_path = os.path.join(documents_path, "Key.txt")
encrypted_path = os.path.join(documents_path, "Encrypt.txt")

def generate_unique_rand_string(length):
  """
  Generates a random string of specified length with no duplicate characters.

  Args:
      length (int): The desired length of the random string.

  Returns:
      str: The generated random string with no duplicates.
  """
  characters = string.ascii_lowercase + string.digits
  random_string = ''.join(secrets.choice(characters) for _ in range(length))

  # Check for duplicates using a set
  while len(set(random_string)) < length:
    random_string = ''.join(secrets.choice(characters) for _ in range(length))

  return random_string

#def generate_rand_string(length):
    # Combine lowercase letters and digits
    #characters = string.ascii_lowercase + string.digits
    # Use secrets.choice to randomly select characters
    #random_string = ''.join(secrets.choice(characters) for _ in range(length))
    #return random_string

def repeat_action(var, depth):
    try:
        # Check if 'var' is a list
        if not isinstance(var, list):
            raise ValueError("The 'var' parameter must be a list.")
        
        # Perform the action 'depth' times
        for _ in range(depth):
            var += generate_unique_rand_string(26)  # Append to the list

        return var

    except ValueError as e:
        print(e)



def encrypt(text):
    """
    Encrypts the input text using a custom set of Lists.

    Args:
        text (str): The input string to be encrypted.
        alpha (str): The lowercase alphabet.
        AlphaList (list): List of shifted alphabets for encryption.
        num (str): The digits 0-9.
        numList (list): List of shifted digits for encryption.
        alphaC (str): Uppercase alphabet.
        AlphaListC (str): List of shifted Uppercase alphabets.

    Returns:
        str: The encrypted text.
    """
    # Get the desired number of repetitions from the user
    try:
        depth = int(input("Enter the number of complexity for encryption: "))
    except ValueError as e:
        print(e)
    
    alphaListC = []
    repeat_action(alphaListC, depth) # Generate the List depth
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"

    with open(key_path, 'w') as outfile:
        for item in alphaListC:
            outfile.write(str(item) + '\n')  # Write each item followed by a newline

    
    encrypted_text = ""
    
    l = 0  # Initialize the shift index

    for i in text:
        if i in alpha:
            j = alpha.index(i)
            k = alphaListC[l][j]  # Substitute letter using the shifted alphabet
            l = (l + 1) % depth  # Cycle through the three shift positions
        else:
            k = i  # Any character that isn't in the lists remain unchanged
        encrypted_text += k
    with open(encrypted_path, 'w') as outfile:
        outfile.write("\nEncrypted Text: \n"+ encrypted_text)

    return encrypted_text

def decrypt(text):
    """
    Decrypts the input text using a custom set of keys.

    Args:
      text (str): The input string to be decrypted.

    Returns:
      str: The decrypted text.
    """
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    try:
        depth = int(input("Please put in how many keys you need to enter: "))
    except ValueError as e:
        print(e)

    # Open the key file for reading
    with open(key_path, 'r') as keyfile:
        alphaListC = keyfile.readlines()  # Read all lines into a list

    # Remove trailing newline characters from each key
    alphaListC = [line.strip() for line in alphaListC]

    # Check if enough keys are present in the file
    if len(alphaListC) < depth:
        print("Error: Not enough keys found in the file. Please generate more keys.")
        return
    print(alphaListC)

    decrypted_text = ""
    l = 0
    for i in text:
        if i in alpha:
            j = alphaListC[l].find(i)
            k = alpha[j]  # Reverse substitution for letters
            l = (l + 1) % depth
        else:
            k = i
        decrypted_text += k

    return decrypted_text.capitalize()


def main():

    while True:
        use = input("Enter 'Encrypt', 'Decrypt', or 'Exit': ").lower()
        if use == "encrypt":
            encr = input("Enter a string to encrypt: ")
            print(encrypt(encr))
            input("Press any button to exit.")
            break
        elif use == "decrypt":
            decr = input("Enter a string to decrypt: ").lower()
            print(decrypt(decr))
            input("Press any button to exit.")
            break
        elif use == "exit":
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
