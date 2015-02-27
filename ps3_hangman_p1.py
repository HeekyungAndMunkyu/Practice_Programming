# Hangman Part 1: Is the Word Guessed?

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far

    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
    '''

    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            return False

    return True
