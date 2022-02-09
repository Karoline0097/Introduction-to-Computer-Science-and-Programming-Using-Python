# PSET 1.1 #############################################################################################################
# program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# s is a string of lower case characters

s = "azcbobobegghakl"
numvow = 0

# iterate over every character in string
for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        numvow = numvow + 1
print ("Number of vowels: " + str(numvow))





# PSET 1.2 #############################################################################################################
# program that prints the number of times the string 'bob' occurs in s
# s is a string of lower case characters

s = "azcbobobegghakl"
numbob = 0
indexpos = 0

for char in s:
    if char == "b":
        if s[indexpos:indexpos+3] == "bob":
            numbob = numbob + 1
    indexpos = indexpos + 1
print("Number of times bob occurs is: " + str(numbob))





# PSET 1.3 #############################################################################################################
# program that prints the longest substring of s in which the letters occur in alphabetical order
# s is a string of lower case characters

s = 'abcbcd'
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

print ("Longest substring in alphabetical order is: " + alphlongest)