# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    lowerDouble = lower * 2    # for alphabet at the end to be shifted
    upperDouble = upper * 2    # for alphabet at the end to be shifted

    cipherDict = {}    # result dict

    # key(plaintext) : value(ciphertext)
    for i in lower:
        iIndex = lower.find(i)
        cipherDict[i] = lowerDouble[iIndex + shift]

    for i in upper:
        iIndex = upper.find(i)
        cipherDict[i] = upperDouble[iIndex + shift]

    return cipherDict



def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    # text -> list
    textList = []
    for char in text:
        textList.append(char)

    # plain list -> cipher list
    for i in range(len(textList)):
        if textList[i] in string.ascii_lowercase or textList[i] in string.ascii_uppercase:
            textList[i] = coder[textList[i]]

    # list -> text
    return ''.join(textList)


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """

    coder = buildCoder(shift)
    return applyCoder(text, coder)
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    shifted_text_list = []

    biggest_num_validwords = 0
    biggest_shift = 0

    # for shift in range(26)
    for shift in range(26):
        # applyShift(text, shift)
        shifted_text = applyShift(text, shift)
        # shifted text.split
        shifted_text_list = shifted_text.split()

        # count the number of valid words
        candidate_num_validwords = 0

        for word in shifted_text_list:
            if isWord(wordList, word):
                candidate_num_validwords += 1

        # if number of valid words bigger than the biggest so far
        if candidate_num_validwords > biggest_num_validwords:
            # replace it
            biggest_num_validwords = candidate_num_validwords
            biggest_shift = shift


    # return shift(int)
    return biggest_shift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
#    text = getStoryString()
    text = open("fable.txt", "r").read()
    print 'Cipher Text'
    print text
    print
    print 'Plain Text'
    best_shift = findBestShift(wordList, text)
    return applyShift(text, best_shift)
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
#    wordList = loadWords()
#    s = applyShift('Hello, world!', 8)
#    bestShift = findBestShift(wordList, s)
#    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    print decryptStory()
