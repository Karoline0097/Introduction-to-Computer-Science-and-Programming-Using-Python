# Problem Set 3

* For this problem, you will implement a variation of the classic wordgame Hangman. 
* In this problem, you will implement a function, called hangman, that will start up and carry out an interactive Hangman game between a player and the computer. Before we get to this function, we'll first implement a few helper functions to get you going.

* For this problem, you will need the code files ps3_hangman.py and words.txt. Be sure to save them in same directory. 
* The file ps3_hangman.py has a number of already implemented helper functions you can use while writing up your solution. 
* do all of your coding for this problem within this file because you will be writing a program that depends on each function you write.
* Read and understand how to use each helper function by reading the docstrings:
```
# -----------------------------------
# Helper code
# helper functions
    .
    .
    .
# (end of helper code)
# -----------------------------------
```

* Requirements for your game:
   - The computer must select a word at random from the list of available words that was provided in words.txt. The functions for loading the word list and selecting a random word have already been provided for you in ps3_hangman.py.
   - The game must be interactive; the flow of the game should go as follows:
   - At the start of the game, let the user know how many letters the computer's word contains.
   - Ask the user to supply one guess (i.e. letter) per round.
   - The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.
   - After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.
   - A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).
   - A user loses a guess only when s/he guesses incorrectly.
   - If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try again.
   - The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.

* Sample Output of a winning game
```
	Loading word list from file...
	55900 words loaded.
	Welcome to the game, Hangman!
	I am thinking of a word that is 4 letters long.
	-------------
	You have 8 guesses left.
	Available letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Good guess: _ a_ _
	------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! You've already guessed that letter: _ a_ _
	------------
	You have 8 guesses left.
	Available letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: s
	Oops! That letter is not in my word: _ a_ _
	------------
	You have 7 guesses left.
	Available letters: bcdefghijklmnopqrtuvwxyz
	Please guess a letter: t
	Good guess: ta_ t
	------------
	You have 7 guesses left.
	Available letters: bcdefghijklmnopqruvwxyz
	Please guess a letter: r
	Oops! That letter is not in my word: ta_ t
	------------
	You have 6 guesses left.
	Available letters: bcdefghijklmnopquvwxyz
	Please guess a letter: m
	Oops! That letter is not in my word: ta_ t
	------------
	You have 5 guesses left.
	Available letters: bcdefghijklnopquvwxyz
	Please guess a letter: c
	Good guess: tact
	------------
	Congratulations, you won!
```

* Sample Output of a losing game
```
    Loading word list from file...
	55900 words loaded.
	Welcome to the game Hangman!
	I am thinking of a word that is 4 letters long
	-----------
	You have 8 guesses left
	Available Letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: a
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 7 guesses left
	Available Letters: bcdefghijklmnopqrstuvwxyz
	Please guess a letter: b
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 6 guesses left
	Available Letters: cdefghijklmnopqrstuvwxyz
	Please guess a letter: c
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 5 guesses left
	Available Letters: defghijklmnopqrstuvwxyz
	Please guess a letter: d
	Oops! That letter is not in my word: _ _ _ _
	-----------
	You have 4 guesses left
	Available Letters: efghijklmnopqrstuvwxyz
	Please guess a letter: e
	Good guess: e_ _ e
	-----------
	You have 4 guesses left
	Available Letters: fghijklmnopqrstuvwxyz
	Please guess a letter: f
	Oops! That letter is not in my word: e_ _ e
	-----------
	You have 3 guesses left
	Available Letters: ghijklmnopqrstuvwxyz
	Please guess a letter: g
	Oops! That letter is not in my word: e_ _ e
	-----------
	You have 2 guesses left
	Available Letters: hijklmnopqrstuvwxyz
	Please guess a letter: h
	Oops! That letter is not in my word: e_ _ e
	-----------
	You have 1 guesses left
	Available Letters: ijklmnopqrstuvwxyz
	Please guess a letter: i
	Oops! That letter is not in my word: e_ _ e
	-----------
	Sorry, you ran out of guesses. The word was else. 
```

## Problem 1 - Is the Word Guessed
* First, implement the function `isWordGuessed` that takes in two parameters - a string, `secretWord`, and a list of letters, `lettersGuessed`. This function returns a boolean - `True` if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and `False` otherwise.
* Example Usage:
```
>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(isWordGuessed(secretWord, lettersGuessed))
False
```

## Problem 2 - Getting the User's Guess
* Next, implement the function `getGuessedWord` that takes in two parameters - a string, `secretWord`, and a list of letters, `lettersGuessed`. This function returns a string that is comprised of letters and underscores, based on what letters in `lettersGuessed` are in `secretWord`.
* Example Usage:
```
>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'
```
* When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string. This is called usability - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!
* For this function, you may assume that all the letters in `secretWord` and `lettersGuessed` are lowercase.

## Problem 3 - Printing Out all Available Letters
* Next, implement the function `getAvailableLetters` that takes in one parameter - a list of letters, `lettersGuessed`. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in `lettersGuessed`.
* Example Usage:
```
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
```
* Note that this function should return the letters in alphabetical order, as in the example above. 
* For this function, you may assume that all the letters in `lettersGuessed` are lowercase.
