"""
Purpose: Convert fahrenheit to celsius

Author: Moises Pleytez
"""

import math

fahrenheit_amount = float(input("What is the temperature in Fahrenheit? "))
celcius_amount = (fahrenheit_amount - 32) *5/9


print(f"The temperature in Celsius is {celcius_amount:.1f} degrees")
