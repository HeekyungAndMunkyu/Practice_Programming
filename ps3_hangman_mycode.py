import random
import string

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def guessWhat():
    '''
    signals a new opportunity to guess

    returns: singleCheck if a single character,
        wordCheck if a word
    '''
    global guessCount += 1
    print 8 - global guessCount, 'guesses left'

    guess = raw_input('What\'s your guess?  ')

    if guess in 'abcdefghijklmnopqrstuvwxyz' and len(guess) == 1:
        singleCheck(guess)
    else:
        wordCheck(guess)

def singleCheck(guess):
    '''
    guess: a single character

    returns: True if it's included; False if not
    '''
    if guess in global secretWord:
        

    else:
        guessWhat()

def wordCheck(guess):
    '''
    guess: a word

    returns: True if secretWord; False if not
    '''
    if guess == global secretWord:
        print "You win!"
        exit(0)


def hangman(secretWord):
    '''
    game start
    '''
    global secretWordList = secretWord.split('')

    print "The secret word has", len(secretWord), "letters."
    print "You have 8 chances to make a guess."
    print "Guess a single character or a complete word."

    while guessCount <= 8:
        if guessCount == 8:
            print "Game over. You lose."
            exit(0)

        guessWhat()


# Load file
inFile = open("words.txt", 'r', 0)
print type(inFile)

line = inFile.readline()
print type(line), line

wordlist = string.split(line)
print wordlist

# Choose the secret word
secretWord = chooseWord(wordlist).lower()

# Game start!
guessCount = 0
hangman(secretWord)
