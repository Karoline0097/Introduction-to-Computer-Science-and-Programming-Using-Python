### -------------------------------------------------------------------------------------###
# Write an iterative function iterPower(base, exp) that calculates the exponential
# by simply using successive multiplication
# code must be iterative - use of the ** operator is not allowed.
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    base_mult = base

    if exp == 0:
        return 1
    while exp > 1:
        base_mult = base * base_mult
        exp = exp - 1
    return (base_mult)

print iterPower(2, 4)




### -------------------------------------------------------------------------------------###
# function recurPower(base, exp)
# recursively calling itself to solve a smaller version of the same problem
# and then multiplying the result by base to solve the initial problem
# code must be recursive - use of the ** operator or looping constructs is not allowed
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)

print (recurPower(2, 4))




### -------------------------------------------------------------------------------------###
# Write a program that prints the sum of the prime numbers
# greater than 2 and less than integer user is asked to input
# using lists

import math
list_of_primes = []
list_of_odd_composites = []

# ask for user input
upper = input("Print the sum of the prime numbers greater than 2 and --> choose: less than: ")
upper = int(upper)

# outer loop that iterates over the odd integers between 3 and x
for number in range(3, upper):
    square_root = int(round(math.sqrt(number)) + 1)

    # for div in range(2, square root of number, rounded upwards to next integer)
    # inner for loop that is a primality test nested inside
    for div in range(2, square_root+1):
        rem = number % div

        # if not a prime, number is a composite
        if rem == 0 and div != number:
            # add to list of composites and break inner loop
            list_of_odd_composites.append(number)
            break

    # if not a composite, must be a prime
    if number not in list_of_odd_composites:
        list_of_primes.append(number)

print "All numbers:", list(range(3, 20))
print "Composites:", list_of_odd_composites
print "Primes:", list_of_primes, "--> Sum of all primes: ", sum(list_of_primes)




### -------------------------------------------------------------------------------------###
# Write a program that prints the sum of the prime numbers
# between 3 (inclusive) and 20 (exclusive)
# without lists
primesum = 0

for x in range (3,20):
    compositeflag = None

    if x % 2 == 0:
        compositeflag = True

    else:
        for div in range(3, x, 2):
            rem = x % div
            if rem == 0:
                compositeflag = True
                break

    if compositeflag == None:
        primesum = primesum + x
        print x, "is a prime!"

print "Sum of all primes is:", primesum




### -------------------------------------------------------------------------------------###
# find square root of x
# x can be positive or negative, or no perfect square

x = int(input("Enter positive or negative integer to find square root of: "))
guess = 0
step = 1

while guess**2 < abs(x):
    guess = guess + step

if guess**2 != abs(x):
    print x, "is not a perfect square!"
else:
    if x < 0:
        guess = -guess
    print guess, "is square root of", x




### -------------------------------------------------------------------------------------###
# exhaustive enumeration
# find out if an integer, x, greater than 3 is prime
# divide x by each integer between 2 and, x-1 (using a while loop)
# If the remainder of any of those divisions is 0, x is not prime, otherwise x is prime
# returning the smallest divisor if x is not a prime

x = int(input("Enter integer x > 3 ,to find out whether x is prime or not: "))
div = 2

while div < (x-1):
    rem = x % div
    if rem == 0:
        smallestdiv = div
        break
    div = div + 1

if x % div == 0:
    print x, "is not a prime!"
    print smallestdiv, "is smallest divisor of", x
else:
    print x, "is a prime!"




### -------------------------------------------------------------------------------------###
# exhaustive enumeration
# find out if an integer, x, greater than 3 is prime
# divide x by each integer between 2 and, x-1 (using a for loop)
# If the remainder of any of those divisions is 0, x is not prime, otherwise x is prime
# returning the smallest and greatest divisor if x is not a prime

x = int(input("Enter integer x > 3 ,to find out whether x is prime or not: "))
div = 2

for div in range(2, x):
    rem = x % div
    if rem == 0:
        smallestdiv = div
        break


if x % div == 0:
    print x, "is not a prime!"

    # hint: smallestdivisor * z = x, z is the largest divisor of x
    # z = x / smallestdivisor
    largestdiv = x / smallestdiv
    print smallestdiv, "is smallest divisor of", x
    print largestdiv, "is largest divisor of", x
else:
    print x, "is a prime!"




### -------------------------------------------------------------------------------------###
# Write a function that takes in one agrument, the integer x, and prints two integers, root and pwr,
# such that 1 < pwr < 6 and root**pwr is equal to the integer x
# If no such pair of integers exists, it should print a message to that effect

def exhaust_find_root_and_power(x):
    """
    :param x: int
    :return: None
    prints two integers, root and pwr, such that 1 < pwr < 6 and root**pwr is equal to the integer x
    """
    step = 1

    for pwr in range(2,6):
        root = 0
        while root ** pwr < abs(x):
            root = root + step

        if root ** pwr != abs(x):
            print  "no pair of integers: ( root to the power", pwr, ") exists so that root **", pwr, "=", x
            continue
        else:
            if x < 0:
                root = -root
            print root, "**", pwr, "=", x
            continue

exhaust_find_root_and_power(8)



### -------------------------------------------------------------------------------------###
# exhaustive enumeration
# finding
# approximation
x = 25
guess = 0
epsilon = 0.1
step = epsilon*2

while (guess**2<= x) and abs(x - (guess**2)) >= epsilon:
    guess = guess + step

if abs(x - (guess**2)) >= epsilon:
    print "Failed on finding square root off", x
else:
    print guess, "is (within +/- 0.1) square root of", x

### -------------------------------------------------------------------------------------###
# bisection search
# finding root
# approximation
x = 25
low = 1
high = x
guess = (low + high) / 2
epsilon = 0.1

while abs(x - (guess**2)) >= epsilon:
    if guess**2 > x:
        high = guess
    elif guess**2 < x:
        low = guess
    guess = (low + high) / 2

print guess, "is (within +/- 0.1) square root of", x




### -------------------------------------------------------------------------------------###
# bisection search
# finding root of both negative and positive numbers
# approximation
x = 25
low = 1
high = abs(x)
guess = (low + high) / 2
epsilon = 0.1

while abs(abs(x) - (guess**2)) >= epsilon:
    if guess**2 > abs(x):
        high = guess
    elif guess**2 < abs(x):
        low = guess
    guess = (low + high) / 2

if x < 0:
    guess = -guess

print guess, "is (within +/- 0.1) square root of", x




### -------------------------------------------------------------------------------------###
# bisection search
# finding log base x
# approximation
x = 1024
low = 0
high = x
guess = (low + high) / 2
epsilon = 0.1

while abs(x - 2**guess) >= epsilon:
    if 2**guess > x:
        high = guess
    elif 2**guess < x:
        low = guess
    guess = (low + high) / 2

print guess, "is (within +/- 0.1) close log base 2 of", x



### -------------------------------------------------------------------------------------###
# bisection search
# x provided by user input, x > 1
# find n root of x

x = float(input("Take root of x>1: "))
approx = float(input("Close enough for you: "))
n = int(input("Take n-th root: "))
low = 0
high = x

guess = (low + high)/2

while abs((guess**n)-x) >= approx:
    if guess**n > x:
        high = guess
        guess = (low + high) / 2
    else:
        low = guess
        guess = (low + high) / 2
print ("Approximate square of " + str(x) + " is " + str(guess))



### -------------------------------------------------------------------------------------###
# bisection search
# guess secret number between 0 (inclusive) and 100(not inclusive)!
low = 0
high = 100
guess = (low + high)//2


print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(guess) + "?")

# ask for user input
print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
user_hint = str(input("--> "))

while user_hint != "c":

    if user_hint == "h":
        high = guess
        guess = (low + high) // 2
        print("Is your secret number " + str(guess) + "?")
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        user_hint = str(input("--> "))

    elif user_hint == "l":
        low = guess
        guess = (low + high) // 2
        print("Is your secret number " + str(guess) + "?")
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        user_hint = str(input("--> "))

    else:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) + "?")
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        user_hint = str(input("--> "))

print ("Game over. Your secret number was: " + str(guess))




### -------------------------------------------------------------------------------------###
# bisection search to determine if a character is in a string
# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr.
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    #base cases
    if aStr == "":
        return False
    elif char == aStr:
        return True
    elif aStr[len(aStr) // 2] == char:
        return True

    #recursive cases
    else:
        return isIn(char,aStr[0:len(aStr) // 2]) or isIn(char,aStr[-1:(len(aStr) // 2):-1])




### -------------------------------------------------------------------------------------###
# Newton-Raphson for square root
# find square root of k, so that x**2==k

k = 9
epsilon = 0.01
guess = k/2

while abs(guess**2 - k) >= epsilon:
    guess = float(guess - (((guess**2) - k)/(2*guess)))

print guess, "is (within +/- 0.1) close to root of", k




### -------------------------------------------------------------------------------------###
# regular polygon has n number of sides. Each side has length s
# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places
# import math library

import math

def polysum (n, s):
    """
    argument: int for n, int or float for s
    return: float
    """

    # calculate area of polygon
    polygonArea = (0.25*n*(s**2))/math.tan(math.pi/n)

    # calculate perimeter of polygon
    polygonPerimeter = n * s

    # return sum the area and square of the perimeter of the regular polygon, rounded to 4 decimal places
    sum = polygonArea + (polygonPerimeter**2)
    return round(sum, 4)