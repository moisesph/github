"""
Show a receipt with subtotal, tax and total
"""
import csv


def main():
    pass

    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX_request = 1

    products_dict = read_dictionary('products.csv', PRODUCT_INDEX)
    header = list(products_dict.keys())[0]
    del products_dict[header]





    print(products_dict)



    with open('request.csv', 'rt') as file:

        reader = csv.reader(file)
        
        print(f"Requested Items:")
        for row in reader:
            item_requested = row[PRODUCT_INDEX]
            quantity_requested = row[QUANTITY_INDEX_request]


            if item_requested in products_dict:
        #I'm tryingg to select the values in the products dict 
                reader2 = csv.reader(products_dict)

                print(f"{item_requested}: {quantity_requested}")



          





def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename) as file:
        reader = csv.reader(file)
        
        for row in reader:
            iproduct = row[key_column_index]
            dictionary[iproduct] = row
            
    return dictionary





##################################

#read products.csv.


#Read request.csv



#see the items in order in the catalog

#calculate and display the order


#print store name at the top of receipt
#Print list ordered items, the name, quantity, and price per item
#sum and print orders
#compute and print tax, 6% taxes
#print total
#print THanks message
#Get the date and time from the computer

#Except block to handel FileNotFoundError, PermissionError, and KeyError.

if __name__ in "__main__":
    main()