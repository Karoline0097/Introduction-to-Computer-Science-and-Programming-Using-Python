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
# Newton-Raphson for square root
# find square root of k, so that x**2==k

k = 9
epsilon = 0.01
guess = k/2

while abs(guess**2 - k) >= epsilon:
    guess = float(guess - (((guess**2) - k)/(2*guess)))

print guess, "is (within +/- 0.1) close to root of", k





