# Problem 2
# Assume s is a string of lower case characters.
s = 'string of lower case characters'

# count up the number of "bob" substring contained in the string s
bob_count = 0
# iterate over characters in string
for char in range(len(s)):
    # find substring "bob" of length 3 found, increase count by 1
    if s[char:char+3] == "bob":
        bob_count= bob_count + 1

print ("Number of times bob occurs is: ", bob_count)

# Test Case
# For example, if s = 'azcbobobegghakl', then your program should print:
# Number of times bob occurs is: 2