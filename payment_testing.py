import math
# 1. Loan Payment Calculator
def loan_pay(principal_rate, anual_rate_t, year_rate):
    month_rate = anual_rate_t / 12 / 100
    number_payment = year_rate * 12
    Monthly_payment_rate = (principal_rate * month_rate * (1 + month_rate)**number_payment) / ((1 + month_rate)**number_payment - 1)
    return Monthly_payment_rate
# 2. Compound Interest Calculator
def compound_interest(principal_rate, anual_rate_t, compounds_per_year, year_rate):
    future_value = principal_rate * (1 + anual_rate_t / compounds_per_year / 100)**(compounds_per_year * year_rate)
    return future_value
# 3. Savings Growth Calculator
def savings_growth(initial_savings, monthly_contribution, anual_rate_t, year_rate):
    month_rate = anual_rate_t / 12 / 100
    num_months = year_rate * 12
    total_savings = initial_savings * (1 + month_rate)**num_months + monthly_contribution * ((1 + month_rate)**num_months - 1)  / month_rate
    return total_savings

def main():
    print("Good Evening Class this is group A Prestinting on cloud computing ")
    print("Tema Members: YUSIFU CONTEH \n OSMAN JALLLOH \n CHERRNOR ")
    print("Financial Calculator")
    print("1. Loan Payment Calculator")
    print("2. Compound Interest Calculator")
    print("3. Savings Growth Calculator")
    choice = input("Select an option (1/2/3): ")

    if choice == "1":
        principal_rate = float(input("Hello Yusifu Enter principal_rate amount: "))
        anual_rate_t = float(input("Hello Yusifu Enter annual interest rate (%): "))
        year_rate = int(input("Hello Yusifu Enter loan term (year_rate): "))
        print(f"Hello Yusifu your Monthly Payment is : {loan_pay(principal_rate, anual_rate_t, year_rate):.2f}")

    elif choice == "2":
        principal_rate = float(input("Hello Osman Enter principal_rate amount: "))
        anual_rate_t = float(input(" Hello Osman Enter annual interest rate (%): "))
        compounds_per_year = int(input("Hello Osman Enter number of times interest is compounded per year: "))
        year_rate = int(input("Hello OsmanEnter time (year_rate): "))
        print(f"Hello Osman your Future Value is : {compound_interest(principal_rate, anual_rate_t, compounds_per_year, year_rate):.2f}")

    elif choice == "3":
        initial_savings = float(input("Hello Darboh Enter initial savings: "))
        monthly_contribution = float(input("Hello Darboh Enter monthly contribution: "))
        anual_rate_t = float(input("Hello Darboh Enter annual interest rate (%): "))
        year_rate = int(input("Hello Darboh Enter time (year_rate): "))
        print(f"Hello Darboh Total Savings: {savings_growth(initial_savings, monthly_contribution, anual_rate_t, year_rate):.2f}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
