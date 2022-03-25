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


## Problem 2 - Dealing with Hands

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


## Problem 3 - Valid Words

* verify that a word given by a player obeys the rules of the game. 
* A valid word is in the word list; and it is composed entirely of letters from the current hand. 
* Implement the `isValidWord` function.


## Problem 4 - Hand Length
* implement the helper `calculateHandlen` function


## Problem 5 - Playing a Hand
* implement the `playHand` function. This function allows the user to play out a single hand. 
* Do not assume that there will always be 7 letters in a hand! The parameter `n` represents the size of the hand.

## Problem 6 - Playing a Game
* A game consists of playing multiple hands.
* We need to implement one final function `playGame` to complete our word-game program. For the game, you should use the `HAND_SIZE` constant to determine the number of cards in a hand.
* Game Output:
```
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points

Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points

Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points

Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points.

Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.
Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```


## Problem 7 - Computer Choosing a Word and Playing a Hand
* dependent on your functions from ps4a.py
* enable your computer (SkyNet) to play the game
* You may notice that things run a bit slowly when the computer plays. This is to be expected - the wordList has 83667 words


## `compChooseWord`

* creates a computer player that is legal, but not always the best
* Test Cases to Understand the Code: 
```
>>> compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6) 
appels 
>>> compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5) 
acta 
>>> compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12) 
immanent 
>>> compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12) 
None
```

## `compPlayHand`

* allows the computer to play a given hand
* Test Cases to Understand the Code: 
```
compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
Current Hand: a p p s e l
"appels" earned 110 points. Total: 110 points
Total score: 110 points.

compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
Current Hand: a a c b t "acta" 
earned 24 points. Total: 24 points 
Current Hand: b Total score: 24 points. 

compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
Current Hand: a a e e i i m m n n t t
"immanent" earned 96 points. Total: 96 points
Current Hand: a e t i
"ait" earned 9 points. Total: 105 points
Current Hand: e
Total score: 105 points.
```


## Problem 7 - You and your Computer

* give the computer the option to play by re-implementing the `playGame` function
* You may notice that things run slowly when the computer plays. This is to be expected.
* Game Output:
```
Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Current Hand: a s r e t t t
Enter word, or a "." to indicate that you are finished: tatters
"tatters" earned 99 points. Total: 99 points

Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c

Current Hand:  a s r e t t t
"stretta" earned 99 points. Total: 99 points

Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: me
Invalid command.

Enter u to have yourself play, c to have the computer play: you
Invalid command.

Enter u to have yourself play, c to have the computer play: c

Current Hand:  a c e d x l n
"axled" earned 65 points. Total: 65 points

Current Hand:  c n
Total score: 65 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n

Enter u to have yourself play, c to have the computer play: u

Current Hand: a p y h h z o
Enter word, or a "." to indicate that you are finished: zap 
"zap" earned 42 points. Total: 42 points

Current Hand: y h h o
Enter word, or a "." to indicate that you are finished: oy
"oy" earned 10 points. Total: 52 points

Current Hand: h h
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 52 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r

Enter u to have yourself play, c to have the computer play: c

Current Hand:  a p y h h z o
"hypha" earned 80 points. Total: 80 points

Current Hand:  z o
Total score: 80 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```
