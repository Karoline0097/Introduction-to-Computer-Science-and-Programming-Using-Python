# Problem 2 - Paying Debt Off in a Year
# calculate the minimum fixed monthly payment
# needed in order pay off a credit card balance within 12 months.

# By a fixed monthly payment, we mean a single number which does not change each month,
# but instead is a constant amount that will be paid each month.

# test variables:
# balance - the outstanding balance on the credit card
balance = 3329
# annualInterestRate - annual interest rate as a decimal
annualInterestRate = 0.2
# Result Your Code Should Generate Below:
# Lowest Payment: 310

# monthly payment must be a multiple of $10 and is the same for all months
def fixed_monthly_payment(monthly_payment):
    """
    :param monthly_payment: int>=0
    :return: fixed monthly payment, which is multiple of 10
    """
    return monthly_payment * 10


# Assume that the interest is compounded monthly according to the balance at the end of the month
# (after the payment for that month is made)
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
def balance_end_month(balance, monthly_payment):
    """
    :param balance: outstanding balance on the credit card, float
    :param monthly_payment: monthly payment, float
    :return: balance at end of month, float
    """
    return balance - fixed_monthly_payment(monthly_payment)

# Monthly interest rate= (Annual interest rate) / 12.0
def charged_interest(balance_end_month, annualInterestRate):
    """
    :param balance_end_month: balance at end of month, function
    :param annualInterestRate: annual interest rate as a decimal, float
    :return: interest charged on balance remaining at end of month, float
    """
    return balance_end_month(balance, monthly_payment) * (annualInterestRate / 12.0)

# possible for the balance to become negative using this payment scheme, which is okay.
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
def balance_remaining(balance_end_month, annualInterestRate):
    """
    :param balance_end_month: balance at end of month, float
    :param annualInterestRate: annual interest rate as a decimal, float
    :return: total remaining balance at the end of month, after interest was charged
    """
    return balance_end_month(balance, monthly_payment) + charged_interest(balance_end_month, annualInterestRate)


# start value for monthly payment
monthly_payment = 1
# reset value for balance in while loop
balance_initial = balance

while balance > 0:
    # for each choosen fixed monthly payment, calculate remaining balance after one year
    for month in range(0,12):
        balance = balance_remaining(balance_end_month, annualInterestRate)
    # if no or negative remaining balance, fixed monthly payment was sufficient to pay off debt in a year
    # break out of loop
    if balance <= 0:
        break

    # else if balance remains at the end of the year, fixed monthly payment rate is insufficient
    else:
        # print("Fixed monthly payment rate:", monthly_payment, "Remaining balance:", round(balance,2))
        # reset the balance to the initial balance
        # increase the payment by $10
        balance = balance_initial
        monthly_payment = monthly_payment + 1
        # try again through the loop


# print out minimum fixed monthly payment to pay off credit card balance within 12 months
# monthly payment must be a multiple of $10 and is the same for all months
# print out no more than two decimal digits of accuracy
print ("Lowest Payment: ", monthly_payment * 10)