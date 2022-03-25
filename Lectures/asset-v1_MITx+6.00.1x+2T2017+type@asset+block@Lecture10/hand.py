import random 

class Hand(object):

    # method to initialize instance (self) of class Hand
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand when instance self is initialized
        self.dealNewHand()

    # method of class Hand
    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        # dictionary maps char (string) to number of occurrences (int) in hand
        self.hand = {}

        # Build the hand with random vowels (minimum number required) and consonants (rest of hand)
        numVowels = self.HAND_SIZE // 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1

    # method of class Hand
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        # Length of handString string must be equal to self.HAND_SIZE n
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        # sets the hand attribute to a dictionary containing the letters of handString
        # dictionary maps char (string) to number of occurrences (int) in handString
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1

    # method of class Hand
    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans

    # string method of class Hand to define behaviour of instance (self) when printed out
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.
        In other words, this does not assume that however many times
        a letter appears in word, self.hand has at least as many of that letter in it.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        # make copy of self.hand (dictionary)
        # do not mutate self.hand (dictionary) as iterating over it, only mutate copy self.hand_cop
        self.hand_cop = self.hand.copy()

        # evaluate if every letter that appears in word (string) appears as many times in self.hand (dictionary)
        # for every letter in word, look up:
        for letter in word:

            # if letter is key in copy self.hand_cop (dictionary)
            if letter in self.hand_cop:
                # if so, evaluate if value associated with that key is > 0 in copy of self.hand (dictionary)

                # if value associated with that key is > 0 in copy of self.hand (dictionary)
                if self.hand_cop[letter] > 0:
                    # letter is available in copy of self.hand,
                    # so update copy of self.hand (dictionary) by decreasing value associated to that letter by 1
                    self.hand_cop[letter] = self.hand_cop[letter] - 1

                # if value associated with that key is <= 0 in copy of self.hand (dictionary)
                else:
                    return False

            # if letter is not key in copy self.hand_cop (dictionary)
            else:
                return False

        # if loop has ended successfully (did not return Flase), this code will be reached to
        # update self.hand, using up the letters in the given word and return True
        self.hand = self.hand_cop
        return True

    
myHand = Hand(7)
myHand.setDummyHand('aazzmsp')
print(myHand)
print(myHand.calculateLen())

# test case: return False, do not update self.hand
print(myHand.update('maze'))
print(myHand)

# test case: return True, update self.hand
print(myHand.update('maze'))
print(myHand)
