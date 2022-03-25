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

## Problem 2 - Word Scores

the majority of this problem consists of learning how to read code

### Representing hands
* A hand is the set of letters held by a player during the game. The player is initially dealt a set of random letters.
* For example, the player could start out with the following hand: `a, q, l, m, u, i, l`. In our program, a hand will be represented as a dictionary: the keys are (lowercase) letters and the values are the number of times the particular letter is repeated in that hand. The above hand would be represented as:
`hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}`
### Converting words into dictionary representation
* `getFrequencyDict`, near the top of ps4a.py. When given a string of letters as an input, it returns a dictionary where the keys are letters and the values are the number of times that letter is represented in the input string. 
* As you can see, this is the same kind of dictionary we use to represent hands.
* For example:
```
>>> getFrequencyDict("hello")
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```
### Displaying a hand
* Given a hand represented as a dictionary, we want to display it in a user-friendly way. 
### Generating a random hand
* The hand a player is dealt is a set of letters chosen at random.The `dealHand` function generates this random hand. The function takes as input a positive integer `n`, and returns a new object, a hand containing n lowercase letters. 
### Removing letters from a hand (you implement this)
* The player starts with a hand, a set of letters. 
* As the player spells out words, letters from this set are used up. 
* For example, the player could start out with the following hand: `a, q, l, m, u, i, l`. The player could choose to spell the word `quail` . This would leave the following letters in the player's hand: `l, m`. 
* implement the function `updateHand`, which takes in two inputs - a `hand` and a `word` (string). 
* `updateHand` uses letters from the hand to spell the word, and then returns a copy of the `hand`, containing only the letters remaining. 
* For example:
```
>>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
>>> displayHand(hand) # Implemented for you
a q l l m u i
>>> hand = updateHand(hand, 'quail') # You implement this function!
>>> hand
{'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
>>> displayHand(hand)
l m  
```
