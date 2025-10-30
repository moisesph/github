lowest_life_expectancy = 999999999999
country_lowest = " "
year_lowest = " "

highest_life_expectancy = 0
country_highest = " "
year_highest = " "

life_expectancy = 0
addition = 0
counts = 0
average = 0

max_average = 0
max_count = 0

min_average = 0
min_count = 0



########################

lowest_life_expectancy_single = 999999999999
country_lowest_single = " "
year_lowest_single = " "

highest_life_expectancy_single = 0
country_highest_single = " "
year_highest_single = " "


global_high_single = 0

life_expectancy_single = 0
addition_single = 0
counts_single = 0
average_single = 0

max_average_single = 0
max_count_single = 0

min_average_single = 0
min_count_single = 0


########################



question_year = int(input("\nEnter the year of interest: "))


with open("life-expectancy.csv") as file:
    next(file)
    for data in file:

        info = data.split(",")
        
        country = info[0]
        code = info[1]
        year = int(info[2])
        life_expectancy = float(info[3])

        counts += 1
        addition += life_expectancy
        average = addition / counts  

        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy   
            country_lowest = country 
            year_lowest = year


        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy 
            country_highest = country 
            year_highest = year

#################

with open("life-expectancy.csv") as file:
    next(file)
    for data in file:
        info = data.split(",")
        year_single = int(info[2])
        if year_single == question_year:



            country_single = info[0]
            code_single = info[1]
            year_single = int(info[2])
            life_expectancy_single = float(info[3])



            if life_expectancy_single < lowest_life_expectancy_single:
                lowest_life_expectancy_single = life_expectancy_single   
                country_lowest_single = country_single 
                year_lowest_single = year_single


            if life_expectancy_single > highest_life_expectancy_single:
                highest_life_expectancy_single = life_expectancy_single 
                country_highest_single = country_single 
                year_highest_single = year_single


      
#We just need the average
                    

print(f"\nThe overall max life expectancy is: {highest_life_expectancy:.2f} from {country_highest} in {year_highest}")
print(f"The overall min life expectancy is: {lowest_life_expectancy:.2f} from {country_lowest} in {year_lowest}\n")

print(f"\nfor the year {question_year}:")
print(f"The average life expectancy accross all countries was {average:.2f}")
print(f"The max life expectancy was in {country_highest_single} with {highest_life_expectancy_single:.2f}")
print(f"The min life expectancy was in {country_lowest_single} with {lowest_life_expectancy_single:.2f}")
