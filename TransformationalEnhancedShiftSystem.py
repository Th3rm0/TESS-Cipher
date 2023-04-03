# This system is the Transformational Enhanced Shift System (TESS)
# To encrypt, if takes a phrase and a shift value, 

alphabet = [
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
    "\'", "\"", "<", ".", ">", "/", "?",
]

def save_to_file(item, shift):

    with open("TESS.txt", "a") as f:

        f.write(f"{item} <|> {shift}\n")

def read_from_file():

    with open("TESS.txt", "r") as f:

        for line in f.readlines():

            data = line.rstrip()

            item, shift = data.split(" <|> ")

            print(f"Item: {item}\nShift: {shift}")

def read_and_decrypt(master_password):

    if master_password == decryption("IlGhM1T9V", 3):

        with open("TESS.txt", "r") as f:

            for line in f.readlines():

                data = line.rstrip()

                password, shift = data.split(" <|> ")

                print(decryption(password, shift))
    
    else:

        print("Incorrect password")

def encryption(phrase, shift):
    
    encrypted_phrase = ""
    number_shift = 0
    
    for letter in phrase:
        
        i = 0
        
        while letter != alphabet[i]:
            
            i += 1
        
        number_shift += shift
        
        i += number_shift
        
        while i > len(alphabet) - 1:
            
            i -= len(alphabet)
        
        print(alphabet[i])

        encrypted_phrase += alphabet[i]

    return encrypted_phrase

def decryption(phrase, shift):
    
    decrypted_phrase = ""
    number_shift = 0
    
    for letter in phrase:
        
        i = 0
        
        while letter != alphabet[i]:
            
            i += 1

        number_shift += int(shift)

        i -= number_shift
        
        while i < 0:
            
            i += len(alphabet)
                
        decrypted_phrase += alphabet[i]
    
    return decrypted_phrase

while True:

    choice = input("\nWhat would you like to do (encrypt/decrypt/save/read/q)? ").lower()

    if choice == "q":

        break
    if choice == "encrypt":

        print(encryption(input("Phrase: "), int(input("Shift: "))))
    
    elif choice == "decrypt":

        print(decryption(input("Phrase: "), int(input("Shift: "))))

    elif choice == "save":

        save_to_file(input("Item: "), input("Shift: "))
    
    elif choice == "read":

        read_from_file()

    elif choice == "master decryption":

        read_and_decrypt(input("Password: "))