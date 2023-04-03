# This system is the Transformational Enhanced Shift System (TESS)
# To encrypt, it takes a phrase and a shift value, 

# Contains all the different characters
characterSet = [
    "A", "a", "B", "b", "C", "c", "D", "d",
    "E", "e", "F", "f", "G", "g", "H", "h",
    "I", "i", "J", "j", "K", "k", "L", "l", 
    "M", "m", "N", "n", "O", "o", "P", "p",
    "Q", "q", "R", "r", "S", "s", "T", "t",
    "U", "u", "V", "v", "W", "w", "X", "x",
    "Y", "y", "Z", "z", " ",
    
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "0",
    
    "`", "~", "!", "@", "$", "%", "^", "&",
    "*", "-", "_", "=", "+", "|", ";", ":",
    "\'", "\"", "\\", "<", ".", ">", "/", "?"
]

# Function for encrypt
def encryption(phrase, shift):
    
    # Contains the encrypted phrase
    encryptedPhrase = ""
    
    # Contains the total shift
    numberShift = 0
    
    # Goes through each character in the phrase
    for letter in phrase:
        
        i = 0
        
        # Finds the character in the character set
        while letter != characterSet[i]:
            
            i += 1
        
        # Increases the shift
        numberShift += shift
        
        # Increments the character
        i += numberShift
        
        # Decreases the character to be inside of the character set
        while i >= len(characterSet):
            
            i -= len(characterSet)
        
        # Adds the encrypted character to the encrypted phrase
        encryptedPhrase += characterSet[i]

    # Returns the encrypted phrase
    return encryptedPhrase

# Function for decrypting
def decryption(phrase, shift):
    
    # Contains the decrypted phrase
    decryptedPhrase = ""
    
    # Contains the total shift
    numberShift = 0
    
    # Goes through each character in the phrase
    for letter in phrase:
        
        i = 0
        
        # Finds the character in the character set
        while letter != characterSet[i]:
            
            i += 1

        # Increments the shift
        numberShift += shift

        # Decrements the character
        i -= numberShift
        
        #Increases the character to be inside the character set
        while i < 0:
            
            i += len(characterSet)
                
        # Adds the decrypted character to the to the decrypted phrase
        decryptedPhrase += characterSet[i]
    
    # Returns the decrypted phrase
    return decryptedPhrase

phrase = input("Enter phrase: ")
shift = int(input("Enter shift: ")

# Asks the user to chose encryption or decryption
encryptOrDecrypt = input("\nWhat would you like to do (e/d)? ").lower()

# Option to encrypt
if encryptOrDecrypt == "e":

    encryptedPhrase = encryption(phrase, shift)
    print(encryptedPhrase)

# Option to decrypt
elif encryptOrDecrypt == "e":

    decryptedPhrase = decryption(phrase, shift)
    print(decryptedPhrase)
