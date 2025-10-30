
import random

keep_playing = "yes"

while keep_playing == "yes":
    secret_number = random.randint(1,100)

    guess_count = 0
    guess = -1


    while guess != secret_number:
        guess= int(input("What is your guess? "))
        guess_count = guess_count + 1

        if guess == secret_number:
            print("You guessed it!")
        elif guess < secret_number:
            print("Higher")
        else:
            print("Lower")

    print(f"It took you {guess_count} guesses")

    keep_playing = input("Would you like to play again (yes/no)? ").lower()






shopping_list = []
item = ""
items = ""

change_item = -1
new_item = ""


while item != "Quit":
    item = input("Please enter the items of the shopping list (type: quit to finish): ").capitalize()
    if item != "Quit":
     shopping_list.append(item)

         
print("The shopping list is:")
for i in range (len(shopping_list)):
    items = shopping_list[i]
    human_count = i + 1
    print(f"{human_count}. {items}")



change_item = int(input("Which item would you like to change? "))
change_item =+ 1
shopping_list.pop(change_item)      

new_item = input("What is the new item? ")
shopping_list.insert(change_item, new_item)  


print("The shopping list is:")
for i in range (len(shopping_list)):
    items = shopping_list[i]
    human_count = i + 1
    print(f"{human_count}. {items}")
