# function that performs a primality test
import math
def primality_test(x):
    """
    :param x: int > 1
    :return: True if n is prime
    """
    assert x >= 2
    # 2 is a prime
    if x == 2:
        print (x, "is prime")
        return True
    # if n divisible by 2, it is divisble by any even number -> n is not a prime
    elif x% 2 == 0:
        print (x, "is not a prime")
        return False

    # else, n is an uneven number
    # find all unique divisors of n ranging from 3 to square root of n, looking only at uneven divisors
    else:
        for div in range(3, (int(math.sqrt(x)) + 1), 2):
            # divide n by each unique divisor, look at remainder
            rem = x % div
            # as soon as remainder 0 is found, n is not prime so return False
            if rem == 0:
                print (x, "is not a prime")
                return False
        # if no remainder 0 is found for any div, n is prime so return True
        print (x, "is prime")
        return True


# Write a generator, genPrimes,
# that returns the sequence of prime numbers on successive calls to its next() method:
# 2, 3, 5, 7, 11, ...
def genPrimes():
    """ generator
    :return: sequence of prime numbers on successive calls to its next() method:
    2, 3, 5, 7, 11, ...
    """
    # keep a list of all earlier primes p generated
    primes_list = [2]

    # start with 2, 2 is prime, so yield 2
    yield 2

    # indefinite loop that keeps incrementing x by 1 and performs primality test on each x
    x = 2
    while True:
        # increment x by 1
        x = x + 1
        # assume x is prime
        x_flag = True
        # performs primality test on x to test assumption
        for p in primes_list:
            rem = x % p
            # if any remainder 0 is found, x is not a prime, so x_flag gets set to False
            if rem == 0:
                x_flag = False

        # candidate number x is prime if (x % p) != 0 for all earlier primes p in primes_list
        # append primes_list with x and yield x
        if x_flag == True:
            primes_list.append(x)
            yield x
mygenerator = genPrimes()
print(mygenerator.__next__())
print(mygenerator.__next__())
print(mygenerator.__next__())
print(mygenerator.__next__())










