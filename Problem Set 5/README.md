# Problem Set 5

* Encryption - the process of obscuring or encoding messages to make them unreadable until they are decrypted
* Decryption - making encrypted messages readable again by decoding them
* Cipher - algorithm for performing encryption and decryption
* Plaintext - the original message
* Ciphertext - the encrypted message. Note: a ciphertext still contains all of the original message information, even if it looks like gibberish.

### The Caesar Cipher

* The idea of the Caesar Cipher is to pick an integer and shift every letter of your message by that integer. 
* In other words, suppose the shift is k . Then, all instances of the i-th letter of the alphabet that appear in the plaintext should become the (i+k)-th letter of the alphabet in the ciphertext. 
* You will need to be careful with the case in which i + k > 26 (the length of the alphabet). 
* Here is what the whole alphabet looks like shifted three spots to the right:

```
Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
 3-shift:  d e f g h i j k l m n o p q r s t u v w x y z a b c
```
* Using the above key, we can quickly translate the message "happy" to "kdssb" 
* note how the 3-shifted alphabet wraps around at the end, so x -> a, y -> b, and z -> c
* English alphabet for this problem
* treat uppercase and lowercase letters individually, so that uppercase letters are always mapped to an uppercase letter, and lowercase letters are always mapped to a lowercase letter. If an uppercase letter maps to "A", then the same lowercase letter should map to "a". 
* Punctuation and spaces should be retained and not changed. For example, a plaintext message with a comma should have a corresponding ciphertext with a comma in the same position.
```
|    plaintext    |  shift    |  ciphertext      |
| ----------------|-----------|------------------|
| 'abcdef'        |    2      |  'cdefgh'        |
| 'Hello, World!' |    5      |  'Mjqqt, Btwqi!' |
| ''              | any value |  ''              |
```
* ps6.py - a file containing three classes that you will have to implement.
* words.txt - a file containing valid English words (should be in the same folder as your ps6..py file).
* story.txt - a file containing an encrypted message that you will have to decode (should be in the same folder as your ps6..py file).


## Problem 1 - Build the Shift Dictionary and Apply Shift

* The `git status`Message class contains methods that could be used to apply a cipher to a string, either to encrypt or to decrypt a message (since for Caesar codes this is the same action).

* Implement the methods in the class `git status`Message according to the specifications in ps6.py. The methods you should fill in are:
* `git status`build_shift_dict(self, shift) method. Be sure that your dictionary includes both lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".
* `git status`apply_shift(self, shift) method. You may find it easier to use `git status`build_shift_dict(self, shift). Remember that spaces and punctuation should not be changed by the cipher.


## Problem 2 - PlaintextMessage

* `PlaintextMessage` is a subclass of `Message` and has methods to encode a string using a specified shift value. Our class will always create an encoded version of the message, and will have methods for changing the encoding.

* Implement the methods in the class `PlaintextMessage` according to the specifications in ps6.py. The methods you should fill in are:
* `__init__(self, text, shift)`: Use the parent class constructor to make your code more concise.
* The getter method `get_shift(self)`
* The getter method `get_encrypting_dict(self)`: This should return a COPY of `self.encrypting_dict` to prevent someone from mutating the original dictionary.
* The getter method `get_message_text_encrypted(self)`
* `change_shift(self, shift)`: Think about what other methods you can use to make this easier. It shouldn’t take more than a couple lines of code.


## Problem 3 - CiphertextMessage

* Given an encrypted message, if you know the shift used to encode the message, decoding it is trivial. 
* If `message` is the encrypted message, and `s` is the shift used to encrypt the message, then `apply_shift(message, 26-s)` gives you the original plaintext message.
* The problem, of course, is that you don’t know the shift. But our encryption method only has 26 distinct possible values for the shift! We know English is the main language of these emails, so if we can write a program that tries each shift and maximizes the number of English words in the decoded message, we can decrypt their cipher!
* A simple indication of whether or not the correct shift has been found is if most of the words obtained after a shift are valid words.
* Note that this only means that most of the words obtained are actual words. It is possible to have a message that can be decoded by two separate shifts into different sets of words. While there are various strategies for deciding between ambiguous decryptions, for this problem we are only looking for a simple solution.

* Implement the methods in the class `git status`:
* `__init__(self, text)`: Use the parent class constructor to make your code more concise.
* `decrypt_message(self)`: You may find the helper `is_word(wordlist, word)` function  and the string method `split()` useful. Note that `is_word` will ignore punctuation and other special characters when considering whether a word is valid.


## Problem 4 - Decrypt a Story
* Now that you have all the pieces to the puzzle, please use them to decode the file story.txt. 
* The file ps6.py contains a helper function `get_story_string()` that returns the encrypted version of the story as a string. Create a `CiphertextMessage` object using the story string and use `decrypt_message` to return the appropriate shift value and unencrypted story string.
