# Problem 1 MIT Midterm #
# Implement a function called closest_power that meets the specifications below.
# for example
# closest_power(3,12) returns 2
# closest_power(4,12) returns 2
# closest_power(4,1) returns 0
# 60min until solved

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''

    exp = 0

    # for every base, base**0 == 1
    if 1 == num:
        # exp = 0
        return exp
    # for every base, base**1 == base
    elif base == num:
        # exp = 1
        return exp + 1

    else:
        # number > 1
        if num > 1:
            testnum = 0
            exp = -1
            # increase exponent by 1 until first test number bigger than number is reached
            while testnum <= num:
                exp = exp + 1
                testnum = base ** exp

            # number between A and B
            # B: test number and exponent > number
            testnumB = testnum
            expB = exp
            # A: test number and exponent < number
            expA = expB - 1
            testnumA = base ** expA

            # return one of the exponents so that base**exponent is closest to number
            if abs(testnumB - num) < abs(testnumA - num):
                return expB
            elif abs(testnumB - num) > abs(testnumA - num):
                return expA
            # in case of a tie, return smaller exponent
            else:
                return expA

        # 0 < number < 1
        elif 0 < num < 1:
            testnum = 1
            exp = 1
            # decrease exponent by 1 until first test number smaller than number is reached
            while testnum >= num:
                exp = exp - 1
                testnum = base ** exp

            # A: test number and lower exponent < number
            testnumA = testnum
            expA = exp
            # B: test number and higher exponent > number
            expB = expA + 1
            testnumB = base ** expB

            # return one of the exponents so that base**exponent is closest to number
            if abs(testnumB - num) < abs(testnumA - num):
                return expB
            elif abs(testnumB - num) > abs(testnumA - num):
                return expA
            # in case of a tie, return smaller exponent
            else:
                return expA


print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))



