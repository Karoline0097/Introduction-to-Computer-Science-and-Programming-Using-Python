# Problem 1
# Assume s is a string of lower case characters.
s = 'string of lower case characters'

# count up the number of vowels contained in the string s
vowels_count = 0
# iterate over characters in string
for char in s:
    # if vowel found, increase count by 1
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowels_count = vowels_count + 1
print ("Number of vowels: ", vowels_count)

# Test Case
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5