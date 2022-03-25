# Problem 1 - Paying Debt Off in a Year
# calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required by the credit card company each month.

# test variables:
# balance - the outstanding balance on the credit card
balance = 42
# annualInterestRate - annual interest rate as a decimal
annualInterestRate = 0.2
# monthlyPaymentRate - minimum monthly payment rate as a decimal
monthlyPaymentRate = 0.04
# Result Your Code Should Generate Below:
# Remaining balance: 31.38

# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
def monthly_payment(balance, monthlyPaymentRate):
    """
    :param balance: outstanding balance on the credit card, float
    :param monthlyPaymentRate: annual interest rate as a decimal, float
    :return: amount that is paid monthly, float
    """
    return balance * monthlyPaymentRate

# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
def balance_end_month(balance, monthly_payment):
    """
    :param balance: float
    :param monthly_payment: float
    :return: balance at end of month, float
    """
    return balance - monthly_payment(balance, monthlyPaymentRate)

# Monthly interest rate= (Annual interest rate) / 12.0
def charged_interest(balance_end_month, annualInterestRate):
    """
    :param balance_end_month: balance at end of month, function
    :param annualInterestRate: annual interest rate as a decimal, float
    :return: interest charged on balance remaining at end of month, float
    """
    return balance_end_month(balance, monthly_payment) * (annualInterestRate / 12.0)

month_count = 1
paid_total = 0.00
# for each month in one year, calculate:
for month in range(0, 12):
    # print("---------------")
    # remaining balance
    # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    balance = (balance - monthly_payment(balance, monthlyPaymentRate)) + charged_interest(balance_end_month, annualInterestRate)
    # print("Month:", month_count, "Remaining balance:", round(balance, 2))
    # monthly payment
    monthly_payment(balance, monthlyPaymentRate)
    # print("Month:", month_count, "Monthly Payment:", round(monthly_payment(balance, monthlyPaymentRate),2))
    # keep track of total amount paid
    paid_total = paid_total + monthly_payment(balance, monthlyPaymentRate)
    # print("Month:", month_count, "Total Payment so far:", round(paid_total, 2))
    month_count = month_count + 1


# at the end of 12 months, print out the remaining balance
# print out no more than two decimal digits of accuracy
print ("Remaining balance:", round(balance, 2))

