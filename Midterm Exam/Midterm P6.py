# Problem 6 MIT Midterm #
# The function isMyNumber is used to hide a secret number (integer).
# It takes an integer guess as a parameter and compares it to the secret number.
# It returns:
# -1 if the parameter x is less than the secret number
# 0 if the parameter x is correct
# 1 if the parameter x is greater than the secret number

def isMyNumber(guess):
    """
    Procedure that hides a secret number.
    :param guess: integer number
    :return:
    -1 if guess is less than the secret number
    0 if guess is equal to the secret number
    1 if guess is greater than the secret number
    """
    secretnum = 5

    if guess == secretnum:
        return 0
    elif guess < secretnum:
        return -1
    else:
        return 1


# The following function, jumpAndBackPedal, attempts to guess a secret number.
# The only way it can interact with the secret number is through the isMyNumber function explained above
# Unfortunately, the implementation given does not correctly return the secret number.
# Please fix the errors in the code such that jumpAndBackpedal correctly returns the secret number.

def jumpAndBackpedal(isMyNumber):
    """
    :param isMyNumber: function that hides a secret number
    :return: secret number
    """
    # start guess
    guess = 0

    # if isMyNumber returns 0, guess is secretnumber
    if isMyNumber(guess) == 0:
        return guess

    # if isMyNumber does not return 0, guess is not yet correct
    else:
        # keep guessing until right guess
        foundNumber = False
        while not foundNumber:
            # if guess is too high, isMyNumber returns 1
            # so guess needs to be decreased
            if isMyNumber(guess) == 1:
                guess = guess - 1
            # else if guess is too low, isMyNumber returns -1
            # so guess needs to be increased
            elif isMyNumber(guess) == -1:
                guess = guess + 1
            # else if finally guess is secret number, isMyNumber returns 0
            else:
                # break loop with flag
                foundNumber = True
        return guess

# print secret number, retuned
print (jumpAndBackpedal(isMyNumber))