# -*- coding: utf-8 -*-

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Class %%% is a kind of %%%", # is-a
    "class %%%(object):\n\tdef__init__(self, ***)":
        "Class %%% has __init__ which receives self and *** as parameters.", # has-a
    "class %%%(object):\n\tdef ***(self, @@@)":
        "Class %%% has a function named *** which receives self and @@@ as parameters.", # has-a
    "*** = %%%()":
        "Variable *** is an instance of class %%%",
    "***.***(@@@)":
        "Variable *** calls function *** with self and @@@ as parameters.",
    "***.*** = '***'":
        "Variable ***, to attribute ***, assigns ***."
}

# Do you want to practice sentences first?
if len(sys.argv) == 2 and sys.argv[1] == "English":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# Load words from the website
for word in urlopen(WORD_URL).readline():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # Fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # Fake remaining names
        for word in other_names:
            result = result.replace("***", word, 1)

        # Fake parameter list
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# Continue until pressing CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input(">")
            print "answer: %s\n\n" % answer
except EOFError:
    print "\nBye"
