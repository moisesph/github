import csv
from PIL import Image
import time

def read_dictionary(filename, key_column_index):
    s_dictionary = {}

    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)

        header = next(reader)

        for row in reader:
            key_value = row[key_column_index]
            s_dictionary[key_value] = row

        return s_dictionary

def main():
    ID_INDEX = 0
    NAME_INDEX = 1

    picture = Image.open('picture.png')
    students = read_dictionary("students.csv", ID_INDEX)

    inumber = input("What is the student's ID Number?: ") #751766201
    inumber = inumber.replace("-","")

    if not inumber.isdigit():
        print("Invalid ID Number")

    elif len(inumber) != 9:
        print("The digits must be 9")

    elif len(inumber) > 9:
        print("You entered too many digits, must be 9")


    else:
        if inumber in students:
            student = students[inumber]
            name = student[NAME_INDEX]

            print(f"That student's name is {name}")
            print("Have a good day")
            time.sleep(1)
            picture.show()

        else: 
            print("No such student!")

if __name__ == "__main__":
    main()