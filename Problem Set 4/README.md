# Problem Set 4

* files  - ps4a.py, ps4b.py, test_ps4a.py and words.txt
* ps4a.py has a number of already implemented functions you can use while writing up your solution.
* read and understand how to use each helper function by reading the docstrings
* This problem set is structured so that you will write a number of modular functions and then glue them together to form the complete word playing game. 

* Instead of waiting until the entire game is ready, you should test each function you write, individually, before moving on. This approach is known as unit testing, and it will help you debug your code. Use test_ps4a.py.
* If your code passes the unit tests you will see a SUCCESS message; otherwise you will see a FAILURE message. These tests aren't exhaustive. You will want to test your code in other ways too.
* test_getWordScore()
Test the getWordScore() implementation.
* test_updateHand()
Test the updateHand() implementation.
* test_isValidWord()
Test the isValidWord() implementation.

## Problem 1 - Word Scores

* first implement code that allows us to calculate the score for a single word. 
* The function `getWordScore` should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.
* Scoring Rules
   - score for the hand is the sum of the scores for each word formed.
   - score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.
   - Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary `SCRABBLE_LETTER_VALUES` that maps each lowercase letter to its Scrabble letter value.
   - Do not assume that there are always 7 letters in a hand! The parameter `n` is the number of letters required for a bonus score (the maximum number of letters in the hand). Our goal is to keep the code modular
   
