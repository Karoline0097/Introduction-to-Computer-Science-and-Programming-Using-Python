# Problem 3 MIT Midterm #
# Write a Python function that returns a list of keys in aDict that map to integer values that are unique
# (i.e. values appear exactly once in aDict).
# The list of keys you return should be sorted in increasing order.
# (If aDict does not contain any unique values, you should return an empty list.)
# This function takes in a dictionary and returns a list.
# For example:
# If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
# If aDict = {1: 1, 2: 1, 3: 1} then your function should return []
# 40 min until finished


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # if aDict is empty, return empty list
    if aDict == {}:
        return []

    # else if aDict is not empty
    else:
        # make list of all values in aDict
        values_list = []
        for val in aDict.values():
            values_list.append(val)

        # create a new dictionary mapping each value : number of occurrences in list of all values
        values_ocur_dict = {}
        for val in values_list:
            # if value is not yet key in histogram dictionary
            if val not in values_ocur_dict:
                values_ocur_dict[val] = 1
            else:
                values_ocur_dict[val] = values_ocur_dict[val] + 1

        # create a new list with all unique values (that map to number of occurrences 1)
        values_uniq_list = []
        for key in values_ocur_dict:
            if values_ocur_dict[key] == 1:
                values_uniq_list.append(key)

        # create a new list with all keys from aDict that associate with those unique values
        keys_uniq_list = []
        for key in aDict:
            if aDict[key] in values_uniq_list:
                keys_uniq_list.append(key)

        # return should be sorted in increasing order
        keys_uniq_list.sort()
        return keys_uniq_list




aDict = {1: 1, 2: 1, 3: 1}
print (uniqueValues(aDict))

aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print (uniqueValues(aDict))

aDict = {}
print (uniqueValues(aDict))