# PSET 2.1 #############################################################################################################
# program to calculate the credit card balance still due after one year
# if a person only pays the minimum monthly payment required by the credit card company each month
# variables
# balance - the outstanding balance on the credit card
balance = 5000.00
# annualInterestRate - annual interest rate as a decimal
annualInterestRate = 0.18
# monthlyPaymentRate - minimum monthly payment rate as a decimal
monthlyPaymentRate = 0.02
# For this example, after a year
# you will have paid $1165.63 and yet you will still owe $4691.11 on what was originally a $5000.00 debt

def monthlyPayment(balance, monthlyPaymentRate):
    """
    argument: float
    return: float
    """
    monthlyPay = balance * monthlyPaymentRate
    return monthlyPay

def eBalance(balance, monthlyPayment):
    """
    argument: float
    return: float
    """
    endofmonthBalance = balance - monthlyPayment(balance, monthlyPaymentRate)
    return endofmonthBalance

def chargedInterest(eBalance, annualInterestRate):
    """
    argument: float
    return: float
    """
    InterestendofmonthBalance = eBalance(balance, monthlyPayment) * (annualInterestRate / 12.0)
    return InterestendofmonthBalance


paidTotal = 0.00
# for each month, calculate statements on the monthly payment and remaining balance
# keep track of total amount paid
for month in range(0, 12):
    p = monthlyPayment(balance, monthlyPaymentRate)
    i = chargedInterest(eBalance, annualInterestRate)
    balance = (balance - p) + i
    paidTotal = paidTotal + p
    print ("Month: " + str(month))
    print ("Paid: " + str(p))
    print ("Interest: " + str(i))
    print ("Remaning balance: " + str(balance))
    print ("Paid total until this month: " + str(paidTotal))

# at the end of 12 months, print out the remaining balance and total amount paid
# print out no more than two decimal digits of accuracy
print ("Remaining balance after 12 years: " + str(round(balance, 2)))
print ("Paid Total in 12 months: " + str(round(paidTotal, 2)))





# PSET 2.2 #############################################################################################################
# program to calculate the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months
# variables
# balance - the outstanding balance on the credit card
# possible for the balance to become negative using this payment scheme, which is okay
balance = 3329
# annualInterestRate - annual interest rate as a decimal
annualInterestRate = 0.2
# For this example, Result Your Code Should Generate: Lowest Payment: 310

#functions needed
def monthlyPaymentfixed(monthlyPayment):
    """
    argument: int>=0 for monthlyPayment
    return: float
    """
    monthlyPay = monthlyPayment * 10
    return monthlyPay

def eBalance(balance, monthlyPayment):
    """
    argument: float
    return: float
    """
    endofmonthBalance = balance - monthlyPaymentfixed(monthlyPayment)
    return endofmonthBalance

def chargedInterest(eBalance, annualInterestRate):
    """
    argument: float
    return: float
    """
    InterestendofmonthBalance = eBalance(balance, monthlyPayment) * (annualInterestRate / 12.0)
    return InterestendofmonthBalance

def remainingBalance(eBalance, annualInterestRate):
    remBalance = eBalance(balance, monthlyPayment) + chargedInterest(eBalance, annualInterestRate)
    return remBalance

# start value for monthlyPayment
monthlyPayment = 1
# reset value for balance in while loop
balanceInitial = balance

while balance > 0:
    # calculate, with fixed monthly payment, remaining balance after one year
    for month in range(0,12):
        balance = remainingBalance(eBalance, annualInterestRate)
    # if no or negative remaining balance, fixed monthly payment was sufficient to pay off debt in a year
    if balance <= 0:
        break
    else:
        # balance remaining at the end of the year, so payment is not yet high enough
        # reset the balance to the initial balance
        # increase the payment by $10
        # try again
        balance = balanceInitial
        monthlyPayment = monthlyPayment + 1

# print out lowest payment to pay off credit card balance within 12 months
# monthly payment must be a multiple of $10 and is the same for all months
# print out no more than two decimal digits of accuracy
print ("Lowest Payment: " + str(monthlyPayment*10))




# PSET 2.3 #############################################################################################################
# bisection search for faster running program
# searching for the smallest monthly payment to the cent such that we can pay off the entire balance within a year
# variables given
# balance - the outstanding balance on the credit card
balance = 999999
# annualInterestRate - annual interest rate as a decimal
annualInterestRate = 0.18
# For this example, Result Your Code Should Generate: Lowest Payment: 90325.03


# store original balance for later comparison
balanceOriginal = balance

#functions needed
def eBalance(balance, payment):
    """
    argument: float
    return: float
    """
    endofmonthBalance = balance - payment
    return endofmonthBalance

def chargedInterest(eBalance, annualInterestRate):
    """
    argument: float
    return: float
    """
    InterestendofmonthBalance = eBalance(balance, payment) * (annualInterestRate / 12.0)
    return InterestendofmonthBalance

def remainingBalance(eBalance, annualInterestRate):
    remBalance = eBalance(balance, payment) + chargedInterest(eBalance, annualInterestRate)
    return remBalance

# monthly interest rate = (Annual interest rate) / 12.0
monthlyInterestRate = annualInterestRate / 12.0
# starting values for lower and upper bound
# monthly payment lower bound = Balance / 12
# monthly payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0
# payment lies between lower bound and upper bound
paymentLow = balance / 12
paymentHigh = (balance * (1 + monthlyInterestRate)**12) / 12.0
payment = (paymentLow + paymentHigh)/2


# calculate, with starting value for fixed monthly payment, remaining balance after one year
for month in range(0, 12):
    balance = remainingBalance(eBalance, annualInterestRate)
balance = round(balance, 2)


# with smallest possible monthly payment, balance should be 0.00 after one year
# find smallest possible monthly payment by bisection search
while balance != 0:
    # if, with that payment, returned balance at end of one year is lower than 0
    if balance < 0:
        # payment was too high, so set this payment as new higher bound
        paymentHigh = payment
    # else if, with that payment, returned balance at end of one year is higher than 0
    elif balance > 0:
        # payment was too low, so set this payment as new lower bound
        paymentLow = payment
    payment = (paymentLow + paymentHigh) / 2

    # reset balance to original balance
    balance = balanceOriginal
    # calculate, with new value for fixed monthly payment, remaining balance after one year
    for month in range(0, 12):
        balance = remainingBalance(eBalance, annualInterestRate)
    balance = round(balance, 2)


# print out lowest payment to pay off credit card balance within 12 months
# monthly payment must be a multiple of $0.01 and is the same for all months
# print out no more than two decimal digits of accuracy
# print ("Lowest Payment: + str(round(payment?,2))" )
print ("Lowest Payment: " + str(round(payment, 2)))

