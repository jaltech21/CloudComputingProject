import math

# 1. Loan Payment Calculator
def payment_lone(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    number_of_payments = years * 12
    monthly_payment = (principal * monthly_rate * (1 + monthly_rate) ** number_of_payments) / ((1 + monthly_rate) ** number_of_payments - 1)
    return monthly_payment

# 2. Compound Interest Calculator
def coumpound_intrest_rate(principal, annual_rate, compounds_per_year, years):
    future_value = principal * (1 + annual_rate / compounds_per_year / 100) ** (compounds_per_year * years)
    return future_value

# 3. Savings Growth Calculator
def Savings_growth(initial_savings, monthly_contribution, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    num_months = years * 12
    total_savings = initial_savings * (1 + monthly_rate) ** num_months + monthly_contribution * ((1 + monthly_rate) ** num_months - 1) / monthly_rate
    return total_savings

def main():
    print("Good Evening Class, this is Group A presenting on Cloud Computing.")
    print("Team Members: Yusifu Conteh, Osman Jalloh, Cherrnor")
    print("\nFinancial Calculator")
    print("1. Loan Payment Calculator")
    print("2. Compound Interest Calculator")
    print("3. Savings Growth Calculator")
    
    choice = input("Select an option (1/2/3): ")
    
    if choice == "1":
        principal = float(input("Hello Yusifu, enter the loan amount: "))
        annual_rate = float(input("Hello Yusifu, enter the annual interest rate (%): "))
        years = int(input("Hello Yusifu, enter the loan term (years): "))
        print(f"Hello Yusifu, your monthly payment is: {payment_lone(principal, annual_rate, years):.2f}")
    
    elif choice == "2":
        principal = float(input("Hello Osman, enter the principal amount: "))
        annual_rate = float(input("Hello Osman, enter the annual interest rate (%): "))
        compounds_per_year = int(input("Hello Osman, enter the number of times interest is compounded per year: "))
        years = int(input("Hello Osman, enter the time (years): "))
        print(f"Hello Osman, your future value is: {coumpound_intrest_rate(principal, annual_rate, compounds_per_year, years):.2f}")
    
    elif choice == "3":
        initial_savings = float(input("Hello Darboh, enter initial savings: "))
        monthly_contribution = float(input("Hello Darboh, enter monthly contribution: "))
        annual_rate = float(input("Hello Darboh, enter annual interest rate (%): "))
        years = int(input("Hello Darboh, enter time (years): "))
        print(f"Hello Darboh, total savings: {Savings_growth(initial_savings, monthly_contribution, annual_rate, years):.2f}")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
