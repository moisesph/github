def compute_wind_chill(temperature, wind_speed): 
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32
    
def loop_wind_speeds(wind_speed):
    wind_speed += 5
    return wind_speed


def main():
    wind_speed = 0
    temperature = float(input("What is the temperature? "))
    temperature_type = input("Fahrenheit or Celsius (F/C)? ").upper()

    if temperature_type == "C":
        temperature = convert_celsius_to_fahrenheit(temperature)

    while wind_speed != 60:
        wind_speed = loop_wind_speeds(wind_speed)
        wind_chill = compute_wind_chill(temperature, wind_speed)
        
        print(f"At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F") 

main()