### Menu/shopping cart





items = []
item = ""
prices = []
price = ""

human_count = -1
remove_item = ""
total = 0
additions = 0
menu = "Please Select one of the following: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute \n5. Quit"
answer = ""

while answer == "":
    print("\nWelcome to the Shopping Cart Program!\n")

    print(menu)
    answer = int(input("\nPlease enter an action "))

while answer != "5":
    
    item = ""
    if answer == 1:
        while item != "Quit":
            item = input("What item would you like to add? (write 'quit' to stop): ").capitalize()
            if item != "Quit":
                price = float(input(f"What is the price of '{item}'?: $"))
                items.append(item)
                prices.append(price)
                print(f"'{item}' has been added to the cart.\n")
        print(menu)
        answer = int(input("\nPlease enter an action "))

    if answer == 2:
        print("\nThe contents of the shopping cart are:")
        for i in range(len(items)):
            human_count = i + 1
            print(f"{human_count}. {items[i]} - ${prices[i]:.2f}")
        print("")
        print(menu)
        answer = int(input("\nPlease enter an action "))

    if answer == 3:
        for i in range(len(items)):
            human_count = i + 1
            print(f"{human_count}. {items[i]} - ${prices[i]:.2f}")

    
        remove_item = int(input("\nWhich item would you like to remove? (number): "))

        if remove_item > len(items) or remove_item < 1:
            print("Sorry, that is not a valid item number\n")
        else:
            remove_index = remove_item - 1 
            removed_item = items.pop(remove_index)
            removed_price = prices.pop(remove_index)
            print(f"'{removed_item}' removed from the cart.\n")

        print(menu)
        answer = int(input("\nPlease enter an action "))

    if answer == 4:
     for summary in prices:
        total += summary
     print(f"\nThe total price of the items in the shopping cart is ${total:.2f}\n")
    total = 0
    print(menu)
    answer = int(input("\nPlease enter an action "))


    if answer == 5:
     exit()