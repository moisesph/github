"""
Track strength of the password
"""

###🎉✨✨✨ Extra features: in line 39 I added a function to ask user to take off the spaces and in line 98 I called the function

# https://byui-cse.github.io/cse111-ww-course/week02/project.html



LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]



def main():
    """
    Loop
    """
    global case_sensitive
    global password
    case_sensitive = False
    password = 0
    word = " "


    while word != "q" or quit != "Q":
        word = input('Enter password to test it (Press "q" and enter to quit) ')
        print("Password / Strength / Additional Message")
        if word == "q" or word =="Q":
            return   
        password_strength(word)

        return word, password
    
    
def no_space(word):
    word = list(word)
    if " " in word :
        print("Don't enter spaces please\n")
        main()
    else: pass

def word_in_file(word, filename): 
    """
     Compare if the name is on file
    """
    with open(filename, "r",encoding="utf-8") as file:
        global case_sensitive
        for line in file:
            line2 = line.strip()
            if word in line2:
                case_sensitive = True
                break
            else: 
                case_sensitive = False
    return case_sensitive 

def word_has_character(word, character_list):
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
    global password

    if word_has_character(word, LOWER) == True:
        password += 1
    if word_has_character(word, UPPER) == True:
        password += 1
    if word_has_character(word, DIGITS) == True:
        password += 1
    if word_has_character(word, SPECIAL) == True:
        password += 1

    return password  
  
def password_strength(word):
    """
    Computes the final strength
    """
    min_length = 10
    strong_length = 16
    global password
    global case_sensitive
    password = 0
   
    no_space(word)
    
    word_in_file(word, "wordlist.txt")
    if case_sensitive == True:
        print(f"{word} / {password} / Password is a dictionary word and is not secure.")
        if case_sensitive == True:
            main()
        
    word_in_file(word, "toppasswords.txt")
    if case_sensitive == True:
        print(f"{word} / {password} / Password is a commonly used password and is not secure.")
        if case_sensitive == True:
            main()

    word_complexity(word)
 


    if len(word) >= strong_length and case_sensitive != True:
        password = 5
        print(f"{word} / {password} / Password is long, length trumps complexity this is a good password")
        if case_sensitive != True:
            main()


    elif len(word) >= min_length and len(word) < strong_length and case_sensitive != True:
        password += 1
        print(f"{word} / {password} /")
        main()
    

    elif password  >= 2 and password < 6 and case_sensitive != True:
        print(f"{word} / {password} /")
        if case_sensitive != True:
            main()


    elif len(word) <= min_length and case_sensitive != True: 
        print(f"{word} / {password} / Password is too short and is not secure.")
        if case_sensitive != True:
            main()
    
    elif password == 1 and case_sensitive != True:
        print(f"{word} / {password} / Password is too short and is not secure.")
        if case_sensitive != True:
            main()
    

if __name__ == "__main__":
    main()