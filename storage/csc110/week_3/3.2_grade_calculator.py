grade = float(input("What is your grade?"))

letter = ""

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

last_digit = grade % 10


if last_digit >= 7:
    sign = "+"
elif last_digit <= 3:
    sign = "-"
else:
    sign = ""


if grade >= 95:
    sign = ""
if grade < 60:
    sign = ""
    

if grade >= 70:
    print(f"You passed the course with an {letter}{sign}")
else: print(f"You didn't passed the course, you have an {letter}{sign} take it again please.")