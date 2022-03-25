# Problem Set 3 - Hangman game
# For this problem, you will implement a variation of the classic wordgame Hangman.
# For this problem, you will need the code files ps3_hangman.py and words.txt. (same directory!)

# implement a function, called hangman, that will start up and carry out an interactive Hangman game
# between a player and the computer.
# Before we get to this function, we'll first implement a few helper functions to keep the code modular.



# -----------------------------------
# Helper code
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

# Problem 1 - Is the Word Guessed
# Example Usage:
# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))
# False
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # MY IMPLEMENTATION
    # assume that all the letters in secretWord and lettersGuessed are lowercase
    # convert string secret word into list of letters
    l_secretWord = list(secretWord)
    # Check if list of guessed letters contains all elements of list of secret word using all()
    # return true if all letters of secret word are contained in guessed letters
    if all(elem in lettersGuessed for elem in l_secretWord):
        return True
    else:
        return False

# Problem 2 - Getting the User's Guess
# Example Usage:
# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))
# '_ pp_ e'
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # MY IMPLEMENTATION
    # convert string secret word into list of letters
    list_secret_word = list(secretWord)

    # underscores, to indicate how many unguessed letters are left in the string
    # displays as many _ as letters contained in secret word
    n_underscore = len(secretWord)
    already_guessed = n_underscore * "_"
    list_already_guessed = list(already_guessed)

    # for every underscore at index i, evaluate if
    index = 0
    for underscore in list_already_guessed:
        # letter at index i in secret word exists in list of guessed letters
        # if letter exists, change underscore at index i to this letter
        if list_secret_word[index] in lettersGuessed:
            list_already_guessed[index] = list_secret_word[index]
        # if it does not exist, do nothing with this underscore and move on to next underscore
        index = index + 1

    # add spacing between underscores for usability
    return " ".join(list_already_guessed)

# Problem 3 - Printing Out all Available Letters
# Example Usage:
# print(getAvailableLetters(lettersGuessed))
# abcdfghjlmnoqtuvwxyz
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far.
    Assume that all the letters in lettersGuessed are lowercase
    returns: string, comprised of letters that represents what letters have not
      yet been guessed, in alphabetical order.
    '''
    # MY IMPLEMENTATION
    # available alphabet
    import string
    # string
    alphabet = string.ascii_lowercase
    # list
    list_alphabet = list(alphabet)

    # for every letter in list of guessed letters
    for letter in lettersGuessed:
        # evaluate if letter is (still) in list of available alphabet
        if letter in list_alphabet:
            # if so, delete that letter from list of available alphabet
            list_alphabet.remove(letter)
        # else, do nothing and move on to next letter in list of guessed letters
    # return string of available alphabet that has not yet been guessed
    return "".join(list_alphabet)

# Problem 4 - The Game
# interactive game of Hangman between the user and the computer.
# take advantage of the three helper functions:
# isWordGuessed, getGuessedWord, and getAvailableLetters
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
    # MY IMPLEMENTATION
    print ("Welcome to the game Hangman!")
    # start of the game, let the user know how many letters the computer's word contains
    print ("I am thinking of a word that is", len(secretWord), "letters long.")

    # let user guess letters, create list containing guessed letters
    # (initial: no guessed letters)
    letters_guessed = []

    # user is allowed 8 guesses
    guess_num = 8

    # user can play as many rounds as number of guesses left
    # play while guesses are left
    while guess_num > 0:
        print ("-------------")
        print ("You have", guess_num, "guesses left.")
        print ("Available letters:", getAvailableLetters(letters_guessed))

        # ask user to supply one guess (letter) per round
        # convert user input to lower case
        player_letter = input("Please guess a letter: ")
        player_letter = player_letter.lower()

        # The user should receive feedback immediately after each guess
        # about whether their guess appears in the computers word.

        # user guess not correct
        if player_letter not in secretWord:
            # user guess is not correct and already appeared
            if player_letter in letters_guessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, letters_guessed))
            else:
                # user loses a guess only when s/he guesses incorrectly for first time
                # add guessed letter to list containing guessed letters
                letters_guessed.append(player_letter)
                guess_num = guess_num - 1
                print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, letters_guessed))

        # user guess already appeared
        elif player_letter in letters_guessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, letters_guessed))
            # add guessed letter to list containing guessed letters
            letters_guessed.append(player_letter)

        # user guess correct
        elif player_letter in secretWord:
            # add guessed letter to list containing guessed letters
            letters_guessed.append(player_letter)
            print ("Good guess: " + getGuessedWord(secretWord, letters_guessed))
            # winning game:
            # user has not yet run out of guesses, so is still in loop
            # if, immediately after last guess, secret word is completed:
            # True: list of guessed letters contains all elements of list of secret word
            if isWordGuessed(secretWord, letters_guessed):
                # break out of loop, to prevent infinite loop
                # directly print out winning message
                break

    # game should end when ...
    print ("------------")

    # winning game:
    # player has constructed full word
    # True: list of guessed letters contains all elements of list of secret word
    if isWordGuessed(secretWord, letters_guessed):
        message_win = "Congratulations, you won!"
        return message_win

    # game over:
    # user runs out of guesses, so jumps out of loop
    # False: list of guessed letters does not contain all elements of list of secret word
    # reveal the word to the user when the game end
    else:
        message_loose = "Sorry, you ran out of guesses. The word was " + secretWord + "."
        return message_loose


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

# Test cases
# winning game
# secretWord ="tact"
# print(hangman(secretWord))

# losing game
# secretWord ="else"
# print(hangman(secretWord))