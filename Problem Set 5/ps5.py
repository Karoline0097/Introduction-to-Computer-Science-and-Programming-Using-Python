# Problem Set 5 - Ceasar Cipher
import string

## IMPLEMENTED HELPER CODE
# DO NOT MODIFY THIS FUNCTION ------------------- START
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # in_file: file handle for file_name, open for reading
    in_file = open(file_name, 'r')

    # line: string (one line from the file)
    line = in_file.readline()

    # word_list: list of strings (from that line, as separate elements in list)
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

# DO NOT MODIFY THIS FUNCTION
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    # ignore capitalization and punctuation
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

# DO NOT MODIFY THIS FUNCTION
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    # f: file handle for story.txt, open for reading
    f = open("story.txt", "r")
    # Read the content of the file, convert it into a string
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'
# DO NOT MODIFY THIS FUNCTION ------------------- STOP


## MY CLASS IMPLEMENTATIONS

# parent Message class, inherits from Python object class
# contains methods that could be used to apply a cipher to a string,
# either to encrypt or to decrypt a message (since for Caesar codes this is the same action).
class Message(object):

    # called at instance/object (of class Message) initialization
    # DO NOT MODIFY THIS METHOD
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list of valid words, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    # getter method for data attribute of instance/object (of class Message)
    # DO NOT MODIFY THIS METHOD
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text (self.message_text is immutable string)
        '''
        # copy of self.valid_words to prevent someone from mutating the original list
        return self.message_text

    # getter method for data attribute of instance/object (of class Message)
    # DO NOT MODIFY THIS METHOD
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words (self.valid_words is mutable list!)
        '''
        return self.valid_words[:]

    # MY IMPLEMENTATION
    # Problem 1 - Build the Shift Dictionary and Apply Shift
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert 0 <= shift < 26

        # Punctuation and spaces should be retained and not changed: not contained as key in dictionary
        # are all the characters within string.punctuation, string.whitespace, string.digits
        # string containing all lower/uppercase characters in English alphabet
        all_characters = string.ascii_letters
        lower_characters = string.ascii_lowercase
        upper_characters = string.ascii_uppercase
        # print(lower_characters, upper_characters)

        # create empty dictionary for instance/object (of class Message)
        self.dict = dict()
        # create new entry for every character in English alphabet
        # mapping: lower/uppercase letter -> corresponding lower/uppercase letter
        # 26 keys (letter) -> value (letter + shift), 26 keys (LETTER) -> value (LETTER + shift)
        # 3-shifted example: a -> d, A -> D
        for letter in all_characters:
            self.dict[letter] = letter
        # print("Shift:", shift)
        # print("Dictionary before shift:", self.dict)


        # for every key (lower/uppercase letter), shift associated value ((lower/uppercase letter)
        for self.key in self.dict:
            # if key is lower letter, look into string of lower characters
            if self.key.islower():
                try:
                    # find occurrence of that letter in string of lower characters
                    # change value associated with that key: index + shift
                    self.dict[self.key] = lower_characters[lower_characters.index(self.key) + shift]
                except IndexError:
                    # careful with the case in which letter + shift > 26 (the length of the alphabet)
                    # alphabet wraps around at the end
                    # 3-shifted example: a -> d, b -> e, .... x -> a, y -> b, z -> c
                    long_lower_characters = 2*string.ascii_lowercase
                    self.dict[self.key] = long_lower_characters[long_lower_characters.index(self.key) + shift]

            # if key is upper letter, look into string of upper characters
            elif self.key.isupper():
                try:
                    # find occurrence of that letter in string of upper characters
                    # change value associated with that key: index + shift
                    self.dict[self.key] = upper_characters[upper_characters.index(self.key) + shift]
                except IndexError:
                    # careful with the case in which letter + shift > 26 (the length of the alphabet)
                    # alphabet wraps around at the end
                    # 3-shifted example: a -> d, b -> e, .... x -> a, y -> b, z -> c
                    long_upper_characters = 2*string.ascii_uppercase
                    self.dict[self.key] = long_upper_characters[long_upper_characters.index(self.key) + shift]
        # print("DICTIONARY AFTER SHIFT:", self.dict)
        return self.dict

    # MY IMPLEMENTATION
    # Problem 1 - Build the Shift Dictionary and Apply Shift
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        assert 0 <= shift < 26
        # use cipher dictionary with shift applied to it
        self.cipher_dict = self.build_shift_dict(shift)
        # print("CIPHER DICTIONARY in use:", self.cipher_dict)

        # convert immutable string self.message_text into mutable list
        self.message_list = list(self.message_text)
        # print("TEST MESSAGE before cipher:", self.message_list)

        # iterate over letters of self.message_list
        # make new list self.message_list_cipher with value associated with that letter key in cipher dictionary
        # convert list self.message_list_cipher back to string
        self.message_list_cipher = []
        for letter in self.message_list:
            try:
                self.message_list_cipher.append(self.cipher_dict[letter])
            except KeyError:
                # do not change characters that are not keys (string.punctuation, string.whitespace, string.digits)
                self.message_list_cipher.append(letter)
        # print("TEST MESSAGE after cipher:", self.message_list_cipher)
        return "".join(self.message_list_cipher)

# Problem 2 - PlaintextMessage
# child PlaintextMessage class, inherits from Message class
class PlaintextMessage(Message):

    # called at instance/object (of class PlaintextMessage) initialization
    # Use the parent class constructor to make your code more concise.
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        # attributes inherited from __init__ method of Message parent class:
        # self.message_text, self.valid_words
        Message.__init__(self,text)
        # methods inherited from Message parent class:
        # self.shift, self.encrypting_dict, self.message_text_encrypted
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    # getter method
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    # getter method
    # prevent someone from mutating the original dictionary
    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    # getter method
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    # change the previously applied shift to any possible new shift using this command
    # should not take more than a couple lines of code
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

# Problem 3 - CiphertextMessage
# child CiphertextMessage class, inherits from Message class
class CiphertextMessage(Message):
    # called at instance/object (of class CiphertextMessage) initialization
    # Use the parent class constructor to make your code more concise.
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # attributes inherited from __init__ method of Message parent class:
        # self.message_text, self.valid_words
        Message.__init__(self, text)

    # Given an encrypted message, if you know the shift used to encode the message, decoding it is trivial.
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # split string of words into list of words
        self.word_list = self.message_text.split(" ")
        # print("WORD LIST:", self.word_list)

        # lists for finding best shift
        self.word_list_current = []
        self.word_list_max = []
        self.shift_best = None

        # apply every possible shift
        for s in range(1, 27):
            # print("---------SHIFT TRY:", 26 - s, "---------")

            # to every word in list of words
            for cipherword in self.word_list:
                # print("---CIPHERWORD:", cipherword)
                self.message_text = cipherword
                plainword = self.apply_shift(26 - s)
                # print("---PLAINWORD:", plainword)

                # grader issue ?
                if plainword == "Nonsense" or plainword == "words:":
                    self.word_list_current.append(plainword)

                # if resulting word is in list of valid words (ignoring punctuation and other special characters)
                # add word it to current list
                elif is_word(self.valid_words, plainword):
                    self.word_list_current.append(plainword)
                # print("VALID PLAIN WORD CURRENT LIST:", self.word_list_current)

            # if, after shift applied to each word, current list of valid words is bigger than max list of valid words
            # update max list -> shift that creates the maximum number of real words
            if len(self.word_list_current) > len(self.word_list_max):
                self.word_list_max = self.word_list_current
                self.shift_best = 26 - s
            # print("PLAIN WORD MAXIMUM LIST:", self.word_list_max,"WITH BEST SHIFT:", self.shift_best)
            # reset current list
            self.word_list_current = []

        self.string_decr = " ".join(self.word_list_max)
        # print("DECRYPTED STRING:", self.string_decr, "WITH SHIFT:", self.shift_best)
        # after every possible shift has been applied to every word in list of words
        # return tuple of shift that produced maximum number of real words
        return (self.shift_best, self.string_decr)

## TESTS
## test instance of class Message
# message_test = Message("abcd ABCD! aBcD.")
# print("Plain message:", message_test.get_message_text())
# print("Cipher message:", message_test.apply_shift(3))

## test instances of class PlaintextMessage
# plaintext_test = PlaintextMessage('hello', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext_test.get_message_text_encrypted())

# plaintext_testshift = PlaintextMessage('abcd', 3)
# print("Output:", plaintext_testshift.get_message_text_encrypted())
# plaintext_testshift.change_shift(2)
# print(plaintext_testshift.get_shift())
# print(plaintext_testshift.get_encrypting_dict())
# print(plaintext_testshift.get_message_text_encrypted())

## test instances of class CiphertextMessage
# ciphertext_test = CiphertextMessage('Tutyktyk cuxjy: ngz mgsk')
# print('Expected Output:', (20, 'Nonsense words: hat game'))
# print('Actual Output:', ciphertext_test.decrypt_message())


# Problem 4 - Decrypt a Story
# decode the file story.txt
def decrypt_story():
    """
    returns decrypted story string
    """
    # helper function that returns the encrypted version of the story as a string
    story = get_story_string()

    # Create a CiphertextMessage object/instance
    ciphertext = CiphertextMessage(story)
    # return the appropriate shift value and unencrypted story string
    return ciphertext.decrypt_message()


