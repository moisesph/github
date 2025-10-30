import random

word_list = ["apple", "temple", "mosiah", "nephi", "helaman", "moroni"]

secret_word = random.choice(word_list)
guess_count = 0
guess = ""

print("Here's your hint: ", end="")
for _ in range(len(secret_word)):
    print("_", end=" ")
print("\n")

while guess != secret_word:
    guess = input("What is your guess?: ").lower()
    guess_count += 1

    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.\n")
    elif guess == secret_word:
        print("Correct! You win!")
        print(f"It took you {guess_count} guesses.")
    else:
        hints = []
        for i in range(len(secret_word)):
            j = guess[i]
            if j == secret_word[i]:
                hints.append(j.upper())
            elif j in secret_word:
                hints.append(j.lower())
            else:
                hints.append("_")

        print("Your hint is:", " ".join(hints) + " \n")
