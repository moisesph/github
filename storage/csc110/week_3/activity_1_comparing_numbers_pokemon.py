"""
Author: Moises Pleytez

Purpose: Compare numbers

"""

pokemon_one = input("What is the level of your Pokemon? ")
pokemon_two = input("What is the level of the rival Pokemon? ")


if pokemon_one > pokemon_two:
    print("Your pokemon wins!")


elif pokemon_one == pokemon_two:
    print("No way, is a draw!!")

elif pokemon_one < pokemon_two:
    print("You loose :(")

else:
    print("What have you entered?")

my_favorite = "mudkip"

your_favorite = input("What is your favorite Pokemon? ").lower()


if my_favorite == your_favorite:
    print("That's my favorite Pokemon too!")


else:
    print("That one is not my favorite")