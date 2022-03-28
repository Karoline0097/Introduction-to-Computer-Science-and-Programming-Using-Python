# Problem 5 MIT Midterm #
# Write a Python function called satisfiesF that has the specification below.
# Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:
# 15min until finished

def satisfiesF(L):
    """
    :param L: a list of strings
    Assume function f is already defined for you:
        f maps a string to a Boolean
    satisfiesF(L):
        mutates L such that it contains all of the strings s, originally in L
        such that f(s) returns True, and no other elements
    :return: length of L after mutation
    """
    # your function implementation here
    # do not mutate list while iterating over it
    for elem in L.copy():
        # if f(elem) returns True, leave element in list L and do nothing
        # if f(elem) returns False, remove element from list L
        if f(elem) == False:
            L.remove(elem)
    return len(L)


# For your own testing of satisfiesF, for example, the following test function f and test code:
# list of strings
L = ['a', 'b', 'a']
# function f
def f(s):
    # maps a string to a boolean
    # returns (True or False)
    return 'a' in s


# test case
print (satisfiesF(L))
print (L)
# Should print:
# 2
# ['a', 'a']
# Paste your entire function satisfiesF, including the definition,
# in the box below. After you define your function, make a function call to run_satisfiesF(L, satisfiesF).
# Do not define f or run_satisfiesF. Do not leave any debugging print statements.
# For this question, you will not be able to see the test cases we run.
# This problem will test your ability to come up with your own test cases
