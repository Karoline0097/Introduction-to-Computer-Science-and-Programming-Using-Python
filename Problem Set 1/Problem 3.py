# Problem 3
# Assume s is a string of lower case characters.
s = 'string of lower case characters'

lengthstring = len(s)

alphcurrent = ""
alphlongest = ""
indexpos = 0


# iterate over every character in string
for char in s:

    # if last character
    if indexpos + 1 == len(s):
        if s[indexpos-1] < s[indexpos]:
            alphcurrent = alphcurrent + s[indexpos]
            if len(alphcurrent) > len(alphlongest):
                alphlongest = alphcurrent
        break

    # if character following current character is same or higher in lexicographical order
    elif s[indexpos] <= s[indexpos+1]:
        # add this character to current string
        alphcurrent = alphcurrent + s[indexpos]
        # and if length of current string is then higher than of longest string so far
        # current string becomes new longest string
        if len(alphcurrent) > len(alphlongest):
            alphlongest = alphcurrent
        # string to be continued

    # if character following current character is lower in lexicographical order
    # and character before current character is lower in lexicographical order and part of current string
    elif (s[indexpos] > s[indexpos+1]) and (s[indexpos-1] < s[indexpos]) and (s[indexpos-1]==alphcurrent[-1]):
        alphcurrent = alphcurrent + s[indexpos]
        if len(alphcurrent) > len(alphlongest):
            alphlongest = alphcurrent
        # end of current string
        alphcurrent = ""

    else:
        alphcurrent = ""

    # update index position for every character
    indexpos = indexpos + 1
# print the longest substring of s in which the letters occur in alphabetical order
print ("Longest substring in alphabetical order is:", alphlongest)


# Test Case
# For example, if s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh