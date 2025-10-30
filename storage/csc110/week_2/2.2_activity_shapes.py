import math

#square
#ask info.
side = float(input("What is the length of a side of the square? "))

#calculate
area = side * side

#display
print(f"The are of a square is {area:.4f}")

#Rectangle

length = float(input("What is the length of the rectangle? "))
width = float(input("What is the Width of the rectangle? "))

area_rectangle = length * width 

print(f"The are of the rectangle is {area_rectangle:.4f}")

#Circle

radius_circle = float(input("What is the radius of the circle? "))

radius_circle = math.pi * radius_circle 

print(f"The are of the circle is {radius_circle:.4f}")




###The second exercise###




#square
#ask info.
side = float(input("What is the length of a side of the square (in cm)? "))

#calculate
area = side * side
area_meters = area /10000

#display
print(f"The are of a square is {area:.4f}cm or {area_meters} in meters.")



#Rectangle

length = float(input("What is the length of the rectangle? "))
width = float(input("What is the Width of the rectangle? "))

area_rectangle = length * width 

print(f"The are of the rectangle is {area_rectangle:.4f}")

#Circle

radius_circle = float(input("What is the radius of the circle? "))

radius_circle = math.pi * radius_circle 

print(f"The are of the circle is {radius_circle:.4f}")
