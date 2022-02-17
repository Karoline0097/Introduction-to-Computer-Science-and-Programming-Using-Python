# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()



def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    all the letters in secretWord and lettersGuessed are lowercase
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    """
    # convert string secret word into list of letters
    l_secretWord = list(secretWord)
    # Check if list of guessed letters contains all elements of list of secret word using all()
    # return true if all letters of secret word are contained in guessed letters
    if all(elem in lettersGuessed for elem in l_secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    # convert string secret word into list of letters
    l_secretWord = list(secretWord)

    # underscores, to indicate how many unguessed letters are left in the string
    # displays as many _ as letters contained in secret word
    n_underscore = len(secretWord)
    alreadyGuessed = n_underscore * "_"
    l_alreadyGuessed = list(alreadyGuessed)

    # for every underscore at index i, evaluate if
    index = 0
    for underscore in l_alreadyGuessed:
        # letter at index i in secret word exists in list of guessed letters
        # if letter exists, change underscore at index i to this letter
        if l_secretWord[index] in lettersGuessed:
            l_alreadyGuessed[index] = l_secretWord[index]
        # if it does not exist, do nothing with this underscore and move on to next underscore
        index = index + 1

    # add spacing between underscores for usability
    return " ".join(l_alreadyGuessed)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    # available alphabet
    import string
    # string
    alphabet = string.ascii_lowercase
    # list
    l_alphabet = list(alphabet)

    # for every letter in list of guessed letters
    for letter in lettersGuessed:
        # evaluate if letter is (still) in list of available alphabet
        if letter in l_alphabet:
            # if so, delete that letter from list of available alphabet
            l_alphabet.remove(letter)
        # else, do nothing and move on to next letter in list of guessed letters
    # return string of available alphabet that has not yet been guessed
    return "".join(l_alphabet)

def sketch_hangman(guessnum):
    # progress sketch of hangman with every numguess (8) that is lost
    sketchStep = [  # game over, numguess (0): head, body, both arms, both legs
        """
           --------
           |      |
           | *** (0) ***
           |   >--W--<
           |      M
           |    _/ \_
           -
        """,
        # numguess (1): head, body, both arms, one leg
        """
           --------
           |      |
           |      0
           |   >--W--<
           |      M
           |    _/ 
           -
        """,
        # numguess (2): head, body, both arms
        """
           --------
           |      |
           |      0
           |   >--W--<
           |      M
           |      
           -
        """,
        # numguess (3): head, body, one arm
        """
           --------
           |      |
           |      0
           |   >--W
           |      M
           |     
           -
        """,
        # numguess (4): head and torso
        """
           --------
           |      |
           |      0
           |      W
           |      M
           |     
           -
        """,
        # numguess (5): head
        """
           --------
           |      |
           |      0
           |    
           |      
           |     
           -
        """,
        # numguess (6): gallows rope
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """,
        # numguess (7) initial empty state
        """
           --------
           |      
           |      
           |    
           |      
           |     
           -
        """,
        # numguess (8): man alive
        """


              0     
           >--W--<
              M    
            _/ \_
           
        """,

    ]
    return sketchStep[guessnum]

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print ("Welcome to the game Hangman!")
    # start of the game, let the user know how many letters the computer's word contains
    print ("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")

    # let user guess letters, create list containing guessed letters
    # (initial: no guessed letters)
    lettersGuessed = []

    # user is allowed 8 guesses
    guessnum = 8

    # user can play as many rounds as number of guesses left
    # play while guesses are left
    while guessnum > 0:
        print ("-------------")
        print (sketch_hangman(guessnum))
        print ("You have " + str(guessnum) + " guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))

        # ask user to supply one guess (letter) per round
        # convert user input to lower case
        player_letter = str(input("Please guess a letter: "))
        player_letter = player_letter.lower()

        # The user should receive feedback immediately after each guess
        # about whether their guess appears in the computers word.

        # user guess not correct
        if player_letter not in secretWord:
            # user guess is not correct and already appeared
            if player_letter in lettersGuessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            else:
                # user loses a guess only when s/he guesses incorrectly for first time
                # add guessed letter to list containing guessed letters
                lettersGuessed.append(player_letter)
                guessnum = guessnum - 1
                print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))

        # user guess already appeared
        elif player_letter in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            # add guessed letter to list containing guessed letters
            lettersGuessed.append(player_letter)

        # user guess correct
        elif player_letter in secretWord:
            # add guessed letter to list containing guessed letters
            lettersGuessed.append(player_letter)
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            # winning game:
            # user has not yet run out of guesses, so is still in loop
            # if, immediately after last guess, secret word is completed:
            # True: list of guessed letters contains all elements of list of secret word
            if isWordGuessed(secretWord, lettersGuessed):
                # break out of loop, to prevent infinite loop
                # directly print out winning message
                break

    # game should end when ...
    print ("------------")

    # winning game:
    # player has constructed full word
    # True: list of guessed letters contains all elements of list of secret word
    if isWordGuessed(secretWord, lettersGuessed):
        message_win = "Congratulations, you won!"
        return message_win

    # game over:
    # user runs out of guesses, so jumps out of loop
    # False: list of guessed letters does not contain all elements of list of secret word
    # reveal the word to the user when the game end
    else:
        print (sketch_hangman(guessnum))
        message_loose = "Sorry, you ran out of guesses. The word was " + secretWord + "."
        return message_loose


secretWord = chooseWord(wordlist).lower()
print (hangman(secretWord))
