# Problem 4 MIT Midterm #
# Write a function called gcd
# that calculates the greatest common divisor of two positive integers.
# The gcd of two or more integers, when at least one of them is not zero,
# is the largest positive integer that divides the numbers without a remainder.
# 20 min until finished

# One way is recursively,
# where the greatest common denominator of a and b can be calculated as gcd(a, b) = gcd(b, a mod b).
# Hint: remember the mod symbol is % in Python. Do not import anything.
# For example, the greatest common divisor (gcd) between a = 20 and b = 12 is: 4
# gcd(20,12) is the same as gcd(12, 20 mod 12)	= gcd(12,8)
# gcd(12,8) is the same as gcd(8, 12 mod 8)	= gcd(8,4)
# gcd(8,4)	is the same as gcd(4, 8 mod 4) = gcd(4,0)
# The gcd is found (and the gcd is equal to a) when we reach 0 for b.
def gcd (a, b):
    """
    :param a: int
    :param b: int
        at least one of the two integers is not 0
    :return: largest positive integer gcd that divides the numbers a and b without remainder
    """
    # handling of negative integers
    if a < 0 and b < 0:
        a = abs(a)
        b = abs(b)
    elif a < 0 or b < 0:
        return 0


    # a > b, so b is smaller integer of pair
    if a > b:
        # base case, if one of two integers is 0, other non zero integer is greatest common divisor
        if b == 0:
            return a
        # recursive case
        else:
            return gcd(b, a % b)


    # b > a, so a is smaller integer of pair
    elif b > a:
        # base case, if one of two integers is 0, other non zero integer is greatest common divisor
        if a == 0:
            return b
        # recursive case
        else:
            return gcd(a, b % a)

    # b == a
    else:
        return a
print (gcd (20, 12))
print (gcd (12, 20))
print (gcd (0, 20))
print (gcd (-20, -12))
print (gcd (-12, -20))
print (gcd (0, -20))

# Other way is iteratively
def gcd_iter(a, b):
    """
    :param a: int
    :param b: int
        , at least one of the two integers is not 0
    :return: largest positive integer gcd that divides the numbers a and b without remainder
    """
    # handling of negative integers
    if a < 0 and b < 0:
        a = abs(a)
        b = abs(b)
    elif a < 0 or b < 0:
        return 0


    # a > b, so b is smaller integer of pair
    if a > b:
        # base case, if one of two integers is 0, other non zero integer is greatest common divisor
        if b == 0:
            return a
        # else enter loop, divide bigger integer by every gcd from smaller integer to 0
        else:
            for gcd in range(b, -1, -1):
                rem = a % gcd
                if rem == 0 and b % gcd == 0:
                    return gcd

     # b > a, so a is smaller integer of pair
    elif b > a:
        # base case, if one of two integers is 0, other non zero integer is greatest common divisor
        if a == 0:
            return b
        # else enter loop, decreasing smaller of two integers by 1 until bigger % smaller == 0
        else:
            for gcd in range(a, -1, -1):
                rem = b % gcd
                if rem == 0 and a % gcd == 0:
                    return gcd

    # b == a
    else:
        return a



print (gcd_iter (20, 12))
print (gcd_iter (12, 20))
print (gcd_iter (0, 20))

print (gcd_iter (-20, -12))
print (gcd_iter (-12, -20))
print (gcd_iter (0, -20))