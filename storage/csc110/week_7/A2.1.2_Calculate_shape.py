import math
### Create functions to calculate

def compute_are_square(digit):
    return compute_are_rectangle(digit, digit)

def compute_are_rectangle(length, width):
    return length * width
    

def compute_are_circle(radius_circle):
    return math.pi * radius_circle
    


shape = " "


while shape != "quit":

    print("\nThere's 3 options: \n1._Square \n2._Rectangle \n3._Circle")
    shape = input("\nWhat shape do you have? (Write Quit to finish): ".lower())

    if shape == "1":
        digit = int(input("\nEnter the width: "))
        area = compute_are_square(digit)
        print(f"\n\n\nThe are of the square is {area}")

    elif shape == "2":
        length = int(input("\nplease enter the length: "))
        width = int(input("please enter the width: "))
        area = compute_are_rectangle(length, width)
        print(f"\n\n\nThe are of the rectangle is {area}")

    elif shape == "3":
        radius_circle = int(input("\nPlease enter the radius of the circle "))
        area = compute_are_circle(radius_circle)
        print(f"\n\n\nThe are of the circle is {area}")

quit()