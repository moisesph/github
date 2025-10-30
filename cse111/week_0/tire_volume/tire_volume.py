import math
import datetime 


def compute_volume(width, radio, diameter):
    volume = round(math.pi * width ** 2 * radio * (width * radio + 2540 *diameter) / 10000000000,2) #Volume in liters 
    return(volume)
   

width = float(input("What is the width in mm? "))
radio = float(input("What is the aspect radio? "))
diameter = float(input("What is the diameter in inches? "))


volume = compute_volume(width, radio, diameter)


today = datetime.datetime.now().date()
print(today)


with open("volumes.txt", "a") as file:
    file.write(str(today) + "," + str(width) + "," + str(radio) + "," + str(diameter) + "," + str(volume))




