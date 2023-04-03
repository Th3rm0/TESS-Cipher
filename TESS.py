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
    ",", "<", ".", ">", "/", "?",
]

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
        
        print(i)
        
        encrypted_phrase += alphabet[i]

    return encrypted_phrase

def decryption(phrase, shift):
    
    decrypted_phrase = ""
    number_shift = 0
    
    for letter in phrase:
        
        i = 0
        
        while letter != alphabet[i]:
            
            i += 1

        number_shift += shift

        i -= number_shift
        
        while i < 0:
            
            i += len(alphabet)
        
        print(i)
        
        decrypted_phrase += alphabet[i]
    
    return decrypted_phrase
