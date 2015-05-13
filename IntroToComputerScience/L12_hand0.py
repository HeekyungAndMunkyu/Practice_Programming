# Given random alphabet list, find a word out of the list!

import random

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE / 3

        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1

        for i in range(numVowels, self.HAND_SIZE):
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1

    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        for letter in sorted(self.hand.keys()):
            output += letter * self.hand[letter]
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.

        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Make a dict for word
        #print 'update activated'
        wordHand = {}
        for char in word:
            wordHand[char] = wordHand.get(char, 0) + 1

        #print 'wordHand', wordHand


        # True if word in self.hand
        for k in wordHand:
            #print k, 'in wordHand'
            if wordHand.get(k, 0) > self.hand.get(k, 0):

                return False
        # Update hand
        for k in wordHand:
            self.hand[k] = self.hand[k] - wordHand[k]
        return True


print 'Game Start!'
print

myHand = Hand(12)
print 'Find a word out of this random alphabet list: ', myHand
print '(The length of the list:', myHand.calculateLen(),')'

print
word = raw_input('Did you find a word? Please type in a word in lowercase >> ')
if myHand.update(word):
    print '\t',word, ' in the list!'
    print
    print 'Updated list without the word: ', myHand
else:
    print '\t', word, ' NOT in the list...'


print 'THE END'
