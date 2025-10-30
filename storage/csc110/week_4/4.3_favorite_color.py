

word = "Commitment"

favorite_letter = input("What is your favorite letter? ")


for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
    print()
