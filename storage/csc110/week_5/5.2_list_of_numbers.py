###Addition, min and max numbers; find

numbers = []

user_number = -1

while user_number != 0:
    #ask the user for a number
    user_number= int(input("Please enter a number: "))

    #check for 0
    if user_number != 0:
     #put it into the list
        numbers.append(user_number) 

additions = 0

for number in numbers:
    additions += number

count = len(numbers)
average = additions / count

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

#Check for the smallest positive number
smallest_positive = 9999999999999999

for number in numbers:
    if number > 0 and number < smallest_positive:
        smallest_positive = number

print(f"the sum is {additions}")
print(f"The average is {average}")
print(f"The largest number was {largest}")
print(f"The smallest positive number is {smallest_positive}")