### -------------------------------------------------------------------------------------###
# rewrite the FancyDivide function to use a helper function.
# This code raises a ZeroDivisionError exception for the following call:
# fancy_divide([0, 2, 4], 0)
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]

# define the simple_divide function
# so that the call does not raise an exception.
# When dividing by 0, fancy_divide should return a list with all 0 elements.
# Any other error cases should still raise exceptions.
def simple_divide(item, denom):
   """
   :param item: element of list of numbers
   :param denom: integer, element at specific index of list of numbers
   :return: float
   """
   try:
      return item / denom
   # only handle the ZeroDivisionError.
   except ZeroDivisionError:
      return 0




### -------------------------------------------------------------------------------------###
# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
# put out an appropriate message and ignore the number.
largest = None
smallest = None

while True:
    # get user input
    num = input("Enter a number: ")
    if num == "done":
        break
    # handling of inadequate user input
    else:
        try:
            num = int(num)
        except:
            print("Invalid input")
            continue

    if (largest is None) and (smallest is None):
        largest = num
        smallest = num
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num

# when done is entered,print out the largest and smallest of the numbers
print("Maximum is " + str(largest))
print("Minimum is " + str(smallest))


### -------------------------------------------------------------------------------------###
