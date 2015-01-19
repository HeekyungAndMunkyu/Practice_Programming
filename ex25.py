# -*- coding: utf-8 -*-

def break_words(stuff):
	"""This function splits a string into words."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""It sorts words."""
	return sorted(words)

def print_first_word(words):
	"""Print the first world."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Print the last word."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""It returns the entire sentence after sorting."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Print the first and the last words."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Print the first and the last words after sorting the sentence."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_first_word(words)

