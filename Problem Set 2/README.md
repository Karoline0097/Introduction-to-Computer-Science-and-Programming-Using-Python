# Problem Set 2

## Problem 1 - Paying Debt off in a Year
* Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

* The following variables contain values as described below:
   - `balance` - the outstanding balance on the credit card
   - `annualInterestRate` - annual interest rate as a decimal
   - `monthlyPaymentRate` - minimum monthly payment rate as a decimal

* For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy.
* Required Math:
   - Monthly interest rate= (Annual interest rate) / 12.0
   - Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
   - Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
   - Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

* Test Case:
```
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
```
Result Your Code Should Generate Below:
```
Remaining balance: 31.38
```
To make sure you are doing calculation correctly, this is the 
remaining balance you should be getting at each month for this example:
```
Month 1 Remaining balance: 40.99
Month 2 Remaining balance: 40.01
Month 3 Remaining balance: 39.05
Month 4 Remaining balance: 38.11
Month 5 Remaining balance: 37.2
Month 6 Remaining balance: 36.3
Month 7 Remaining balance: 35.43
Month 8 Remaining balance: 34.58
Month 9 Remaining balance: 33.75
Month 10 Remaining balance: 32.94
Month 11 Remaining balance: 32.15
Month 12 Remaining balance: 31.38
```


## Problem 2 - Paying Debt off in a Year
* Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
* In this problem, we will not be dealing with a minimum monthly payment rate.

* The following variables contain values as described below:
   - `balance` - the outstanding balance on the credit card
   - `annualInterestRate` - annual interest rate as a decimal

* The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year

* Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. 

* Required Math:
   - Monthly interest rate = (Annual interest rate) / 12.0
   - Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
   - Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
   
* Test Case:
```
balance = 3329
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
```
Result Your Code Should Generate Below:
```
 Lowest Payment: 310
```


