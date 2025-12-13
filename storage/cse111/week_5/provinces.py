
#reads the contents of provinces.txt into a list and then modifies the list. Your program must do the following:

import csv

def main():

    ELEMENT_INDEX = 0
    read = read_document("provinces.txt", ELEMENT_INDEX)

#print in variable



def read_document(filename, index):

    dictionary = {}

    with open (filename, "rt") as csv_file:

        reader = csv.reader(csv_file):

        for first_list in reader:
            if len(first_list) != 0:
                key = first_list [index]


    #Storage

    #print

    return dictionary



def remove_first():
    pass

#remove the first element



def remote_last():
    pass



def replace_ab():
    pass

    #If AB replace it with it

    #make a count

    #print the count

if __name__ == "__main__":
    main()