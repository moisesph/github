#exceed requirements: I asked him to enter his phone number and if he prefers we to contact him By text message or by whatsapp Is in line 18 and 42


#Exceed requirements above OwO


#Is of the expectancy of the great things that I am going to learn, is like a fantasy, 
# cf    1q5 like entering to a portal of great opportunities, it can be frustrating sometimes, but when I see my code, and I know that everything there came from my head, makes me feel great.


import math
import datetime 

def main():
    """
    Ask for user the information to calculate the volume and prints it, this is incorrect, but also ask him his personal info.
    """
    width = float(input("What is the width in mm? "))
    radio = float(input("What is the aspect radio? "))
    diameter = float(input("What is the diameter in inches? "))
    today = datetime.datetime.now().date().strftime("%Y-%m-%d")


    volume = compute_volume(width, radio, diameter)
    write_text(today, width, radio, diameter, volume)
    print(f"The approximate volume is {volume} liters")
    spam = input("do you want to buy more tires? Yes or No?: ").lower()
    if spam == "yes":
        contact_info()
    else: 
        with open("volumes.txt", "a") as file:
            file.write("" + "\n")
    return today, width, radio, diameter

def compute_volume(width, radio, diameter):
    """
    Computes the volume
    """
    volume = round(math.pi * width ** 2 * radio * (width * radio + 2540 *diameter) / 10000000000,2)
    return(volume)

def write_text(today, width, radio, diameter, volume):
        """
        Open the text volumes and write on it, separating everything by comas
        """
        with open("volumes.txt", "a") as file:
            variables = [today, width, radio, diameter, volume]
            file.write(", ".join(map(str, variables)))

def contact_info():
    """
    Writes his information and ask for it, in the text
    """
    with open("volumes.txt", "a") as file:
        phone_number = input("What is your phone number? ")
        contact_by = input("How is the best way to contact you? \n Whatsapp or by Text message? (W) or (T) ")
        data = [phone_number, contact_by]
        file.write(", ".join(map(str, data)) + "\n")


main()
