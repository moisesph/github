"""A word Puzzle"""

import random

words = ["destructor","mundo","alma","monos", "reir"] # 
secret_word = random.choice(words)


def main():
    right_position = ""
    tries = 0
    guess = ""

    hint = make_underscore(secret_word)
    print("Bienvenidos al Quiebra Manos\n")
    print(f"Tu pista es: {hint}\n")
    guess = asking_guess()
    

    while right_position != secret_word:

        tries += 1
        while len(guess) != len(secret_word):
            if len(guess) != len(secret_word):
                print("Lo siento, no tiene la misma cantidad de letras, intenta denuevo")
            guess = asking_guess()
            guess = guess.replace(" ", "")


        right_position = make_upper(guess, secret_word)



        final_answer = right_position.lower()

        if final_answer == secret_word:
            if tries == 1:
                print(f"WoW!! Le atinaste a la primera!\nSolo te tomo {tries} intento.\nEso o hiciste trampa jeje")
                break
            else:   
                print(f"Felicidades! Le atinaste!\nTe tomo {tries} intentos.")
                break
        else:
            separated = separate(right_position)
            print(f"Tu pista es {separated}")
            guess = asking_guess()

def make_underscore(the_word):
    underscored = "_ " * len(the_word)
    underscored = underscored.strip()
    return underscored


def make_upper(the_guess, the_word):
    together = ""
    for l1, l2 in zip(the_guess, the_word):
        if l1 == l2:
            together += l1.upper()
        elif l1 in the_word:
            together += l1.lower()
        else:
            together += "_"
    together = together.strip()
    return together

def separate(the_word):
    result = " ".join(the_word)
    return result  

def asking_guess():
    answer = input("Cual es la palabra? ")
    answer = answer.lower()
    return answer

#Make display

#Make to show a picture of ahorcado

if __name__ == "__main__":
    main()