
import math
import datetime 


def compute_volume(width, radio, diameter):
    volume = round(math.pi * width ** 2 * radio * (width * radio + 2540 *diameter) / 10000000000,2) #Volume in liters 
    return(volume)

def write_text():
        with open("volumes.txt", "a") as file:
            variables = [today, width, radio, diameter, volume]
            file.write(", ".join(map(str, variables)))

width = float(input("What is the width in mm? "))
radio = float(input("What is the aspect radio? "))
diameter = float(input("What is the diameter in inches? "))

today = datetime.datetime.now().date()


volume = compute_volume(width, radio, diameter)
write_text()