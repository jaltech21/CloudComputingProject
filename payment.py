def get_input(prompt, input_type=float):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def loan_calculation():
    principal_amount = get_input("Enter the principal amount: ", float)
    annual_interest_rate = get_input("Enter the annual interest rate: ", float)
    loan_term = get_input("Enter the loan term in years: ", int)

    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_number_of_payments = loan_term * 12

    num = principal_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_number_of_payments
    denom = (1 + monthly_interest_rate) ** total_number_of_payments - 1

    monthly_payment = num / denom
    print(f"Monthly Payment: ${monthly_payment:.2f}")

def compound_interest_cal():
    principal_amount = get_input("Enter the principal amount: ", float)
    annual_rate = get_input("Enter the annual rate: ", float)
    years_invested = get_input("Enter the years invested: ", int)
    times_compound = get_input("Enter the times interest was compounded per year: ", int)

    annual_rate_decimal = annual_rate / 100
    future_value = principal_amount * (1 + (annual_rate_decimal / times_compound)) ** (times_compound * years_invested)
    print(f"The Future Value of the Investment: ${future_value:.2f}")

def savings_growth():
    initial_savings = get_input("Enter the initial savings: ", float)
    monthly_contribution = get_input("Enter the monthly contribution: ", float)
    annual_interest_rate = get_input("Enter the annual interest rate: ", float)
    number_of_interests = get_input("Enter the number of times interest is compounded per year: ", int)
    time = get_input("How many years: ", int)

    annual_interest_rate_decimal = annual_interest_rate / 100
    total_months = time * 12

    future_investment_value = initial_savings * (1 + (annual_interest_rate_decimal / number_of_interests)) ** (number_of_interests * time)
    future_savings = future_investment_value + (monthly_contribution * ((1 + (annual_interest_rate_decimal / number_of_interests)) ** total_months - 1) / (annual_interest_rate_decimal / number_of_interests))
    print(f"Future Savings: ${future_savings:.2f}")

def main():
    payment_type = input("What type of payment option do you want to calculate? ").strip().upper()

    if payment_type == "LOANPAYMENT":
        loan_calculation()
    elif payment_type == "COMPOUNDINTEREST":
        compound_interest_cal()
    elif payment_type == "SAVINGSGROWTH":
        savings_growth()
    else:
        print("Please choose between one of the following payment types:\nLOANPAYMENT\nCOMPOUNDINTEREST\nSAVINGSGROWTH")

if __name__ == "__main__":
    main()
