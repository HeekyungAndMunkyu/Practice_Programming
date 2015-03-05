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
		self.word = word.lower()
    def isWordIn(self, text):
		for punc in string.punctuation:
			print punc, type(punc)
			text = text.replace(punc, ' ')
			print text
		print text
		text.strip(string.punctuation)
		print text
		return self.word in text.lower().split()

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

test = NewsStory('','Boston; 769876*()newyork','','','')
foo = TitleTrigger('Boston')
foo.evaluate(test)
