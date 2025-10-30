
friends_names = []
new_friend = ""

while new_friend != "end":
    new_friend = input("Type the name of a friend: ").lower()
    if new_friend != "end":
     friends_names.append(new_friend)

print(f"Your friends are:")
for quantity_friends in friends_names:
    print(f"{quantity_friends}")