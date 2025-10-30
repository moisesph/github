###Make a shooping list

shopping_list = []
item = ""
items = ""

change_item = -1
new_item = ""


while item != "Quit":
    item = input("Please enter the items of the shopping list (type: quit to finish): ").capitalize()
    if item != "Quit":
     shopping_list.append(item)

         
print("\nThe shopping list is:")
for i in range (len(shopping_list)):
    items = shopping_list[i]
    human_count = i + 1
    print(f"{human_count}. {items}")



change_item = int(input("\nWhich item would you like to change? "))
change_item = change_item - 1
shopping_list.pop(change_item)      

new_item = input("What is the new item? ")
shopping_list.insert(change_item, new_item)  


print("\nThe shopping list is:")
for i in range (len(shopping_list)):
    items = shopping_list[i]
    human_count = i + 1
    print(f"{human_count}. {items}")
