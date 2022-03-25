# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
# Do not assume that there are always 7 letters in a hand!
# The parameter n is the number of letters required for a bonus score
# (the maximum number of letters in the hand). Our goal is to keep the code modular.
HAND_SIZE = 7
n = HAND_SIZE

# dictionary that maps each lowercase letter to its Scrabble letter value
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------


## Problem 1 - Word Scores
# calculate the score for a single word
# Test: test_getWordScore()
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # MY IMPLEMENTATION
    # initial score
    score = 0

    # assume input word is always either string of lowercase letters or empty string ""
    # word is empty string, so score is 0
    if word == "":
        return score
    # word is not an empty string
    else:
        # get value associated with every letter in word from SCRABBLE_LETTER_VALUES dictionary
        # add this value to score
        # multiply result by length of word
        # add bonus score 50 if length of word is equal to HAND_SIZE n
        for letter in word:
            score = score + SCRABBLE_LETTER_VALUES[letter]
        score = score * len(word)
        if len(word) == n:
            score = score + 50
        return score



## Problem 2 - Dealing with Hands
# a hand is the set of letters held by a player during the game
# read and understand already imlemented functions: displayHand(hand), dealHand(n)

# Displays a hand in a user-friendly way
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string, letter -> int, number of times that letter is represented in the input string )
    """
    # for every key in hand dictionary
    for letter in hand.keys():
        # print letter as often as integer value associated with that letter
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line
    # returns None

# Generates a random hand
# a hand is set of letters held by a player during the game
# player is initially dealt a set of random letters
# hand will be represented as a dictionary, using getFrequencyDict
# mapping keys: (lowercase) letters to values: number of times the particular letter is repeated in that hand
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    # empty dictionary
    hand={}
    # at least n/3 letters in hand should be vowels
    numVowels = n // 3

    # choose vowel of VOWELS string above at random
    # randrange(start,stop) method returns a randomly selected element from the specified range
    # create / update hand dictionary entry, using vowel letter as key
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    # choose consonant of CONSONANTS string above at random
    # for the rest of the letters in hand
    # randrange(start,stop) method returns a randomly selected element from the specified range
    # create / update hand dictionary entry, using consonant letter as key
    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    # return dictionary
    return hand

# Update a hand by removing letters
# player starts with a hand, a set of letters.
# As the player spells out words, letters from this set are used up.
# Test: test_updateHand()
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # MY IMPLEMENTATION
    # make sure this function has no side effects
    # make copy of hand in order not to mutate the hand passed in
    handcop = hand.copy()

    # for every letter in word,
    # change value associated with that letter in handcop dictionary by -1
    for letter in word:
        handcop[letter] = handcop[letter] - 1
    return handcop


## Problem 3 - Valid Words
# verify that a word given by a player obeys the rules of the game
# valid word is in the word list
# and it is composed entirely of letters from the current hand
# Test: test_isValidWord
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # MY IMPLEMENTATION
    # make copy of hand, so hand is not mutated
    handcop = hand.copy()

    # return True if both are True (AND)
    # short circuit evaluation

    # first condition: valid word is in the word list
    if word in wordList:

        # second condition: word is entirely composed of letters in the hand
        # for every letter in word
        for letter in word:
            # check whether it is key in hand dictionary and its value is still bigger than 0
            if (letter in handcop) and (handcop[letter] > 0):
                # if so, change value associated with that letter in handcop dictionary by -1
                handcop[letter] = handcop[letter] - 1
            # if either key is not in hand dictionary or its value is still equal or smaller than 0, return Flase
            elif (letter not in handcop) or (handcop[letter] <= 0):
                return False
        # loop has checked that all letters of valid word are in hand, so both conditions evaluated to True
        return True

    # elif word is not in the word list, return False
    elif word not in wordList:
        return False



# Problem 4 - Hand Length
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # MY IMPLEMENTATION
    # for every key in hand dictionary
    handlist = []
    for letter in hand.keys():
        # add letter to list as often as integer value associated with that letter
        for j in range(hand[letter]):
            handlist.append(letter)
    # return length of hand
    return len(handlist)



# Problem 5 - Playing a Hand
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # MY IMPLEMENTATION
    # Keep track of the total score
    totalscore = 0

    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print ("Current Hand:", end=" " )
        displayHand(hand)
        
        # Ask user for input
        word = input('Enter word, or a "." to indicate that you are finished: ')

        # If the input is a single period:
        if word == ".":
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not a single period):
        else:

            # If the word is not valid:
            # Reject invalid word (print a message followed by a blank line)
            if isValidWord(word, hand, wordList) is False:
                print ("Invalid word, please try again.")
                print ("")


            # Otherwise (the word is valid):
            elif isValidWord(word, hand, wordList) is True:
                # Tell the user how many points the word earned, and the updated total score,
                # in one line followed by a blank line
                totalscore = totalscore + getWordScore(word, n)
                print('"'+ word + '"', "earned", getWordScore(word, n), "points. Total:", totalscore, "points")
                print("")

                # Update the hand
                hand = updateHand(hand, word)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if word == ".":
        print("Goodbye! Total score:", totalscore, "points.")
        print("")
    else:
        print("Run out of letters. Total score:", totalscore,  "points.")



# Problem 6 - Playing a Game
# game consists of playing multiple hands
# Testing: Try out this implementation as if you were playing the game.
# Try out different values for HAND_SIZE
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # MY IMPLEMENTATION
    # game start
    # HAND_SIZE constant to determine the number of cards in a hand
    n = HAND_SIZE
    playmode = None

    # while user has not yet played or does not exit game
    # keep repeating the UNITS
    while (playmode == None) or (playmode != "e"):

        # get user input
        playmode = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        # handle inappropriate user input
        while ((playmode != "n") and (playmode != "r") and (playmode != "e")):
            print("Invalid command.")
            playmode = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        # let the user play a new (random) hand
        if playmode == "n":
            # call to functions
            hand = dealHand(n)
            playHand(hand, wordList, n)

        # r: let the user replay the last hand again
        elif playmode == "r":
            try:
                # hand must already exist from previous round
                playHand(hand, wordList, n)
            except:
                # if hand does not yet exist, print message and ask again for input
                print("You have not played a hand yet. Please play a new hand first!")
                print("")
                continue

    # e: exit game -> exit



# Build data structures used for entire session and play game
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
