### -------------------------------------------------------------------------------------###
aTup = ('I', 'am', 'a', 'test', 'tuple')
def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''

    newTup = ()
    newTup = aTup [0::2]
    return newTup

print oddTuples(aTup)


### -------------------------------------------------------------------------------------###
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# function that returns the sum of the number of values associated with a dictionary
def how_many (aDict):
    """
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    """
    key = aDict.keys()
    val = []
    for key in aDict:
        aDict[key]
        val = val + aDict[key]

    return len(val)
print (how_many (animals))



### -------------------------------------------------------------------------------------###
aDict = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}
# returns the key corresponding to the entry with the largest number of values associated with it
# If there is more than one such entry, return any one of the matching keys
# If there are no values in the dictionary, biggest should return None
def biggest (aDict):
    """
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    """

    key = aDict.keys()
    val = aDict.values()
    valcurrent = []
    valmax = []

    if aDict.values() == []:
        keymax = None

    for key in aDict:
        valcurrent= aDict[key]
        if len(valcurrent) >= len (valmax):
            valmax = valcurrent
            keymax = key
        else:
            valcurrent = []


    return keymax



### -------------------------------------------------------------------------------------###
aTuple= ((1,"one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"))
# function that separates numbers and words into different tuples
# return smallest number, largest number, number of unique words
def getData (tup):
    """
    argument: tuple with tuple of int[0] and string[1] inside
    return: int for smallest int, largest int, number of unique strings
    """
    numbers = ()
    words = ()

    for elem in tup:
        if elem[0] not in numbers and (type(elem[0])==int):
            numbers = numbers + (elem[0],)
        if elem[1] not in words and (type(elem[1])== str):
            words = words + (elem[1],)

    smallestnum = min(numbers)
    largestnum = max(numbers)
    uniquewords = len(words)
    return (smallestnum, largestnum, uniquewords)

(small, large, unique) = getData (aTuple)
print (small, large, unique)



### -------------------------------------------------------------------------------------###
#list
myList = [0, 1, 2, 3, 4, 5]
#function
def myFunct(x):
    x = x*2
    return x

#apply function to each element of list
def applyFtoEachElemList1 (L, f):
    """
    argument: List L and function f
    apply function to each element inside of list
    return new List with function applied to each element of old list
    """
    Lapp = []
    for elem in L:
        elem = myFunct(elem)
        Lapp = Lapp + [elem]
    return Lapp
print applyFtoEachElemList1 (myList, myFunct)

def applyFtoEachElemList2 (L, f):
    """
    argument: List L and function f
    apply function to each element inside of list
    mutates L by replacing each element of L by f(elem)
    return mutated L
    """
    for index in range(len(L)):
        L[index] = f(L[index])
    return L
print applyFtoEachElemList2 (myList, myFunct)


### -------------------------------------------------------------------------------------###
#list
ListofFunct = [abs, int]
#value
elem = -5.0

def applyEachFunctionToElem (L, x):
    """
    argument: List of functions, x
    applies each function in List to x
    """
    for funct in L:
        x = funct(x)
        print x

applyEachFunctionToElem (ListofFunct, elem)




### -------------------------------------------------------------------------------------###
# list of lyrics/every word in song "she loves you"
she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

# create a frequency dictionary, mapping words to number of occurences
def lyrics_to_dictionary(songlyrics):
    """
    argument: List, songlyrics
    returns: dictionary with ->  word in songlyrics(key):numberofoccurences in song(value)
    """
    lyrics_dictionary = {}
    for word in songlyrics:
        if word in lyrics_dictionary:
            lyrics_dictionary[word] = lyrics_dictionary[word] + 1
        else:
            lyrics_dictionary[word] = 1

    return lyrics_dictionary
beatles = lyrics_to_dictionary(she_loves_you)

def most_frequent_word(dictionary):
    frequent_word = []
    valuemax = max(dictionary.values())
    for key in dictionary:
        if (dictionary[key] == valuemax):
            frequent_word.append(key)
    return (frequent_word, valuemax)
print (most_frequent_word(beatles))


def words_often(dictionary, minTimes):
    minimum_occurrence_word = []
    doneflag = False
    while not doneflag:
        temp = most_frequent_word(dictionary)
        if temp[1] >= minTimes:
            minimum_occurrence_word.append(temp)
            for keyword in temp[0]:
                del (dictionary[keyword])
        else:
            doneflag = True
    return minimum_occurrence_word
print (words_often(beatles, 5))


### -------------------------------------------------------------------------------------###
def fib_efficient(n, dictionary):
    """
    argument:
    n-th fibonacci number,
    dictionary storing already calculated n as key for n-th fibonacci numbers as value
    return n-th fibonacci number
    """
    if n in dictionary:
        return dictionary[n]
    else:
        ans = fib_efficient(n-1, dictionary) + fib_efficient(n-2, dictionary)
        dictionary[n] = ans
        return ans

fib_dictionary = {1:1, 2:2}
print(fib_efficient(6, fib_dictionary))


### -------------------------------------------------------------------------------------###
list_even1 = []
for n in range(15):
    if n%2 == 0:
        n = n - 1
        list_even1.append(n)
print (list_even1)

# list comprehension
list_even2 = [(n-1) for n in range(15) if (n % 2 == 0)]
print list_even2


### -------------------------------------------------------------------------------------###
namesDict = {"Nora": 56, "Lulu": 15, "Gino": 31}
list_odd1 = []
for val in namesDict.values():
    if val%2 != 0:
        list_odd1.append(val*10)
print (list_odd1)

# list comprehension with dictionary
list_odd2 = [(val * 10) for val in namesDict.values() if (val % 2 != 0)]
print (list_odd2)



### -------------------------------------------------------------------------------------###
grades = {"Nora": 90, "Lulu": 15, "Gino": 60}

# dict comprehension
grades_doubled2 = {key: value*2 for (key, value) in grades.items() if (value%2 == 0)}
print (grades_doubled2)

#
grades_doubled1 = {}
for key in grades:
    if grades[key]%2 == 0:
        grades[key] = grades[key]*2
        grades_doubled1[key] = grades[key]
print grades_doubled1




### -------------------------------------------------------------------------------------###
grades = {"Nora": 90, "Lulu": 15, "Gino": 60}

def double(value):
    return value * 2

def even(value):
    if value % 2 == 0:
        return True
    else:
        return False

# dict comprehension
grades_doubled2 = {key: double(value) for (key, value) in grades.items() if even(value)}
print (grades_doubled2)

grades_doubled1 = {}
for key in grades:
    if even(grades[key]):
        grades[key] = double(grades[key])
        grades_doubled1[key] = grades[key]
print grades_doubled1




### -------------------------------------------------------------------------------------###
grades = {"Nora": 90, "Lulu": 15, "Gino": 60}
grades.update((key, grades[key]*2) for key in grades)
print grades
