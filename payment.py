listOfPaymentType = ["Loan Payment", "Compound Interest", "Savings Growth"]

print(f"Welcome, Please choose from the option below the type of calculation you want to perform \n")
for i in listOfPaymentType:
    print(f"{i}\n")

paymentType = input("What type of payment option do you want to calculate? ")

#Loan Payment
def loanCalculation():
    principalAmount = int(input("Enter the principal amount: "))
    annualInterestRate = int(input("Enter the annual interest rate: "))
    monthlyInterestRate = annualInterestRate / 12 / 100
    loanTerm = int(input("Enter the loan term in years: "))
    totalNumberOfPayments = loanTerm * 12

    num = principalAmount * monthlyInterestRate * (1 + monthlyInterestRate)**totalNumberOfPayments
    denom = (1 + monthlyInterestRate)**totalNumberOfPayments - 1

    MonthlyPayment = num / denom

    print(f"Monthly Payment: SLE{round(MonthlyPayment, 2)}")

#Compund Interest Function
def compoundInterestCal():
    PrincipalAmount = int(input("Enter the principal amount: "))
    AnnualRate = int(input("Enter the Annual Rate: "))
    YearsInvested = int(input("Enter the Years Invested: "))
    TimesCompound = int(input("Enter the Times Interest was compounded in years: "))
    Annual_Rate_Decimal = AnnualRate / 100
    FutureValue = PrincipalAmount * (1 + (Annual_Rate_Decimal/TimesCompound))**(TimesCompound * YearsInvested)

    print(f"The Future Value of the Investment: SLE{round(FutureValue, 2)}")

#Savings growth
def SavingsGrowth():
    InitialSavings = int(input("Enter the initial savings: "))
    MonthlyContribution = int(input("Enter the monthly income: "))
    AnnualInterestRate = int(input("Enter the annual interest rate: "))
    AnnualInterestRateDecimal = AnnualInterestRate / 100
    NumberOfInterests = int(input("Enter the Number of Times Interest is compounded per year: "))
    Time = int(input("How many years: "))
    TotalMonths = Time * 12
    FutureInvestmentValue = InitialSavings * (1 +(AnnualInterestRateDecimal/NumberOfInterests)**(NumberOfInterests*Time))

    FutureSavings = FutureInvestmentValue + (MonthlyContribution * ((1 + (AnnualInterestRateDecimal/NumberOfInterests))**TotalMonths-1)/(AnnualInterestRateDecimal/NumberOfInterests))

    print(f"Future Savings: SLE{round(FutureSavings)}")

if paymentType == "LOANPAYMENT":
    loanCalculation()

elif paymentType == "COMPOUNDINTEREST":
    compoundInterestCal()

elif paymentType == "SAVINGSGROWTH":
    SavingsGrowth()

else:
    print(f"Please choose between one of the following payment types:\nLOANPAYMENT\nCOMPOUNDINTEREST\nSAVINGSGROWTH")