# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


class NewsStory(object):

	def __init__(self, guid, title, subject, summary, link):
		self.guid = guid
		self.title = title
		self.subject = subject
		self.summary = summary
		self.link = link


	def getGuid(self):
		return self.guid
	def getTitle(self):
		return self.title
	def getSubject(self):
		return self.subject
	def getSummary(self):
		return self.summary
	def getLink(self):
		return self.link

	def __str__(self):
		return self.title + ', ' +self.subject + ', ' + self.summary








#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    def __init__(self, word):
		super(WordTrigger, self).__init__()
		self.word = word
    def isWordIn(self, text):
		for punc in string.punctuation:
			print punc, type(punc)
			text = text.replace(punc, ' ')
			print text
		print text
		text.strip(string.punctuation)
		print text
		return self.word.lower() in text.lower().split()


# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

#test = NewsStory('','Boston; 769876*()newyork','','','')
#foo = TitleTrigger('Boston')
#foo.evaluate(test)

class PhraseTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def evaluate(self, story):
        return self.word in story.getSubject() or self.word in story.getTitle()\
        or self.word in story.getSummary()


def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering)
    filteredList = []


    for story in stories:

#		print 'for story, visited '
		print story
        for trigger in triggerlist:
            print trigger
            if trigger.evaluate(story):
                print trigger.evaluate(story)
                if story not in filteredList:
                    filteredList.append(story)
        return filteredList


pt = PhraseTrigger("New York City")
a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
noa = NewsStory('', "something something new york city", '', '', '')
nob = NewsStory('', '', "something something new york city", '', '')
noc = NewsStory('', '', '', "something something new york city", '')

class MatchTrigger(Trigger):
    def __init__(self, story):
        self.story = story
    def evaluate(self, story):
        return story == self.story
	def __str__(self):
		return story.getSubject()

triggers = [MatchTrigger(a), MatchTrigger(nob)]
stories = [a, b, c, noa, nob, noc]
filteredStories = filterStories(stories, triggers)
print 'result', filteredStories
