"""
Track strength of the password
"""

# https://byui-cse.github.io/cse111-ww-course/week02/project.html


#5 Calculaled by, password is a regular word? is known password? the length of the password and complexity of the password.
    #if already is on file, is not secure and strength to 0 "'Password is a dictionary word and is not secure."
    #If it is in the toppasword list should  "Password is a commonly used password and is not secure." go to 0
    #if if length less than 10  "Password is too short and is not secure." go to 1
    #if more than 15, is strong "Password is long, length trumps complexity this is a good password." go to 5

    #4 kinds characters, upper case, lower case, numeric digits, and special symbols, exep, only upper characters, it would be a 1, if it had upper and lower, a 2 etc.
            #this 4 should be calculaed in base of the length + this four


    #Possible for values, should I create a variable where it sums the security from 0 to 1


# TO open: open(filename, "r",encoding="utf-8")
#Remote the new line character at the end of string


LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]



def main():
    """
    Loop
    """

    quit = " "
    while quit != "q":
        quit = input('Enter password to test it (Press "q" and enter to quit) ').lower()

        if quit != "q":
            password = quit
            #print(len(password))
            password_strength(password)
        
        #You need to report result to user


def word_in_file(word,filename,case_sensitive):
    """
     Compare if the name is on file
    """
    #Read each line on file,
    for read in files:
        with open():
            pass
    # if word matches, is true, 
    # other wise is false.

    #if case_sensitive is true, a case sensitive match is performed
    #if false also

    #Case sensitive should false by default.
    #Return boolean
    pass

def word_has_character(word, character_list):
    """
    Goes through each character in the word parameter and check if matches with any on the character_list, if any character are present returns true, if non false
    """
    #Boolean
    pass

def word_complexity(word):
    """
    Check how complex is the word
    """
    # Call word_has_character function, for each 4 kinds characters, 
    # add to complexity ranking
    #range from 0 to 4
    #0 only when no characters
    #int
    pass

def password_strength(password): #min_length, strong_length
    """
    Computes the final strength
    """
    #Checks on dictionary and known passwords
    #call word_complexity
    #Determine strength based user requirementes
    #return strength from 0 to 5
    #the min_length default 10
    #the strong 16
    #int
    pass


if __name__ == "__main__":
    main()


#Add an extra feature, put it above everything