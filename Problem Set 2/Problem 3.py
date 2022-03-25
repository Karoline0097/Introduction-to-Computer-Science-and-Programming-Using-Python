# Problem 3 - Using Bisection Search to Make the Program Faster
# calculate a more accurate fixed monthly payment than we did in Problem 2
# without running into the problem of slow code
# using bisection search

# test variables:
# balance - the outstanding balance on the credit card
balance = 320000
# annualInterestRate - annual interest rate as a decimal
annualInterestRate = 0.2
# Result Your Code Should Generate Below:
# Lowest Payment: 29157.09

# store original balance for later comparison
balance_initial = balance

# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
def balance_end_month(balance, payment):
    """
    :param balance: float
    :param payment: float
    :return:
    """
    return balance - payment

# Monthly interest rate= (Annual interest rate) / 12.0
def charged_interest(balance_end_month, annualInterestRate):
    """
    :param balance_end_month: balance at end of month, function
    :param annualInterestRate: annual interest rate as a decimal, float
    :return: interest charged on balance remaining at end of month, float
    """
    return balance_end_month(balance, payment) * (annualInterestRate / 12.0)

# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
def balance_remaining(balance_end_month, annualInterestRate):
    """
    :param balance_end_month: balance at end of month, float
    :param annualInterestRate: annual interest rate as a decimal, float
    :return: total remaining balance at the end of month, after interest was charged
    """
    return balance_end_month(balance, payment) + charged_interest(balance_end_month, annualInterestRate)


# monthly interest rate = (Annual interest rate) / 12.0
monthly_interest_rate = annualInterestRate / 12.0

# starting values for lower and upper bound
# monthly payment lower bound = Balance / 12
monthly_payment_low = balance / 12
# monthly payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0
monthly_payment_high = (balance * (1 + monthly_interest_rate) ** 12) / 12.0
# payment lies between lower bound and upper bound
payment = (monthly_payment_low + monthly_payment_high) / 2


# calculate, with starting value for fixed monthly payment, remaining balance after one year
for month in range(0, 12):
    balance = balance_remaining(balance_end_month, annualInterestRate)
balance = round(balance, 2)

# with smallest possible monthly payment, balance should be 0.00 after one year
# find smallest possible monthly payment by bisection search
while balance != 0:
    # if, with that monthly payment, returned balance at end of one year is lower than 0
    if balance < 0:
        # monthly payment was too high, so set this payment as new higher bound
        # print("Remaining balance too low:", round(balance,2), "Monthly payment was too high:", round(payment,2))
        monthly_payment_high = payment
    # else if, with that monthly payment, returned balance at end of one year is higher than 0
    elif balance > 0:
        # monthly payment was too low, so set this payment as new lower bound
        # print("Remaining balance too high:", round(balance,2), "Monthly payment was too low:", round(payment,2))
        monthly_payment_low = payment
    payment = (monthly_payment_low + monthly_payment_high) / 2

    # reset balance to original balance
    balance = balance_initial
    # calculate, with new value for fixed monthly payment, remaining balance after one year
    for month in range(0, 12):
        balance = balance_remaining(balance_end_month, annualInterestRate)
    balance = round(balance, 2)


# print out lowest payment to pay off credit card balance within 12 months
# monthly payment must be a multiple of $0.01 and is the same for all months
# print out no more than two decimal digits of accuracy
# print ("Monthly payment was neither too high nor too low")
print ("Lowest Payment: ", round(payment, 2))