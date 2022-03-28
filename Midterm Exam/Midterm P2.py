# Problem 2 MIT Midterm #
# Write a Python function that returns the sublist of strings in aList
# that contain fewer than 4 characters.
# For example, if aList = ["apple", "cat", "dog", "banana"],
# your function should return: ["cat", "dog"]
# This function takes in a list of strings and returns a list of strings.
# Your function should not modify aList.
# 1o min until solved


def lessThan4(aList):
    """
    :param aList: list of strings
    :return: list of all strings in aList with less than 4 characters
    """
    lessthan4char = []
    for elem in aList:
        if len(elem) < 4:
            lessthan4char.append(elem)
    return lessthan4char


aList = ["apple", "cat", "dog", "banana"]
print (lessThan4(aList))