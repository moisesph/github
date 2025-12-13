
###ATTENTION EXTRA FEATURE: I have a counting days for the next black friday in line 78-79 and 89.

"""
Show a receipt with subtotal, tax and total
"""
import csv
from datetime import datetime


def main():
    pass

    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX_REQUEST = 1

    quantity_total = 0
    price_subtotal = 0
    item_repeated = 0
    final_price_subtotal = 0

    tax = 6 / 100

    try:

        products_dict = read_dictionary('products.csv', PRODUCT_INDEX)

        #print("All Products")
        #print(products_dict)
        #print(f"Requested Items")
        print("Out of Stock Store")

        with open("request.csv") as file:
            first_line = file.readline()

            for line in file:
                line = line.strip()
                line_list = line.split(",")
            
                name_requested = line_list[PRODUCT_INDEX]
                quantity_requested = line_list[QUANTITY_INDEX_REQUEST]

             
                products = products_dict[name_requested]
                item = products[NAME_INDEX]
                price = products[PRICE_INDEX]
                print(f"{item}: {quantity_requested} @ {price}")

                quantity_total += int(quantity_requested)
                price_subtotal += float(price)
                item_repeated += int(quantity_requested)
                final_price_subtotal += float(price) * float(quantity_requested)


    except FileNotFoundError:
        print("Error: missing file")
        print("[Errno 2] No such file or directory: 'products.csv'")
        exit()

    except KeyError: 
        print(f"\nATTENTION! {name_requested} Not found, please contact support\n")
        exit()

    except PermissionError:
        print(f"You don't have permission to access")
        exit()

        
    taxes = final_price_subtotal * tax
    total = final_price_subtotal + taxes   

    now = datetime.now()
    date = now.strftime("%a %b %d %X %Y")    
    black_friday = datetime (year=2026, month=11, day=27)

    today = datetime.now()
    black_friday_difference = black_friday - today      
        
    print(f"Number of Items: {quantity_total}")
    print(f"Subtotal: {final_price_subtotal:.2f} ")
    print(f"Sales Tax: {taxes:.2f}")
    print(f"Total: {total:.2f}")

    print("Thank you for shopping at the Out of Stock Store")

    print(date)
    print(f"Our next black friday is in {black_friday_difference.days} days!")







def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename) as file:
        reader = csv.reader(file)

        header = next(reader)
        
        for row in reader:
            iproduct = row[key_column_index]
            dictionary[iproduct] = row

    return dictionary


if __name__ == "__main__":
    main()

