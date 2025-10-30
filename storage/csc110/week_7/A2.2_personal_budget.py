def prompt_annual_salary():
    salary = float(input("What is your annual salary?" ))
    return salary


def compute_monthly_income(annual_income):
    monthly_income = annual_income / 12
    return monthly_income

def compute_tithing(income):
    tithing = income * 0.1
    return tithing

def compute_monthly_tax(annual_income, monthly_income):
    rate = 0

    if annual_income < 60000:
        rate = 10
    elif annual_income < 150000:
        rate = 20
    else: 
        rate - 30

    tax = monthly_income * rate / 100

    return tax

def compute_spending_money(income, tithing, tax):
    spending_money = income - tithing - tax
    return spending_money


def main():
    print("Welcome to the budget program!")
    annual_salary = prompt_annual_salary()
    monthly_income = compute_monthly_income(annual_salary)
    tithing = compute_tithing(monthly_income)
    tax = compute_monthly_tax(annual_salary, monthly_income)
    spending_money = compute_spending_money(monthly_income, tithing, tax)

    print(f"Your Salary is ${annual_salary:,.2f}")
    print(f"Your monthly income is ${monthly_income:.2f}")
    print(f"Your monthly tithing is ${tithing:.2f}")
    print(f"Your tax for the month is ${tax:.2f}")
    print(f"Your spending money for the month is: ${spending_money:.2f}")

main()