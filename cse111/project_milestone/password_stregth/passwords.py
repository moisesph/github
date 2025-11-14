"""
Track strength of the password
"""

###🎉✨✨✨ Extra features: in line 32 I added a function to ask user to take off the spaces and in line 28 I called the function, this makes the user take off the spaces from the password.

# https://byui-cse.github.io/cse111-ww-course/week02/project.html



LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]



def main():
    """
    Loop
    """
    password = " "

    while password != "q" or quit != "Q":
        password = input('Enter password to test it (Press "q" and enter to quit) ')
        if password == "q" or password == "Q":
            exit()  
        no_space(password)
        password_strength(password)
  
    
def no_space(password):
    password = list(password)
    if " " in password:
        print("Don't enter spaces please")
        main()
    else: pass

def word_in_file(word, filename, case_sensitive=False): 
    """
     Compare if the name is on file
    """
    with  open(filename, "r",encoding="utf-8") as file:
        for line in file:
            line2 = line.strip()

            if not case_sensitive:
                line2 = line2.lower()
                word_lower = word.lower()
            else:
                word_lower = word
            if line2 == word_lower:
                return True
    return False


def word_has_character(word, character_list):   #This everything good
    """
    Goes through each character in the word parameter and check if matches with any on the character_list, if any character are present returns true, if non false
    """
    word = set(word)
    character_list = set(character_list)
    if word & character_list:
        return True
    else: return False

def word_complexity(word):
    """
    Check how complex is the word
    """
    strength = 0

    if word_has_character(word, LOWER): strength += 1
    if word_has_character(word, UPPER): strength += 1
    if word_has_character(word, DIGITS): strength += 1
    if word_has_character(word, SPECIAL): strength += 1


    word = list(word)
    if len(word) == 0:
        strength = 0

    for i in word:
        if i not in LOWER + UPPER + DIGITS + SPECIAL:
            strength = 0
            return strength
    
    #Character to test: á

    return strength  
  
def password_strength(password,min_length=10,strong_length=16):
    """
    Computes the final strength
    """


    if password == "" or password == " ":
        strength = word_complexity(password)

    case_sensitive = word_in_file(password, "wordlist.txt")


    if password == "":
        strength = word_complexity(password)
        print(f"strength: {strength}")
    if password != "":
        if case_sensitive == True:
            print("Password is a dictionary word and is not secure.")
            strength = 0
            return strength

        case_sensitive = word_in_file(password, "toppasswords.txt")
        if case_sensitive == True:
            print("Password is a commonly used password and is not secure.")
            strength = 0
            return strength

        elif case_sensitive != True:
            strength = 1 + word_complexity(password)
            if  len(password) < min_length:
                strength -=  1 #If the password is short this takes off 1

            if strength != 0:
                if len(password) < min_length:
                        print("Password is too short and is not secure.")

                elif len(password) >= strong_length:
                        print("Password is long, length trumps complexity this is a good password.")
                        strength = 5

                elif len(password) >= min_length and len(password) < strong_length:
                        print(f"strength: {strength}")
            if case_sensitive == True: print(f"strength: {strength}")

    return strength

if __name__ == "__main__":
    main()