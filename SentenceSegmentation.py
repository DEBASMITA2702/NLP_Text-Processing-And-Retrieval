from util import *
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from re import split as resplit

class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = resplit(r'[.?!]', text)	  # splitting each sentence using terminators [.?!] using regex rules
		return segmentedText


	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')	# Using a pre-trained Punkt tokenizer with sentence-level tuning
		segmentedText = tokenizer.tokenize(text)  # Using the tokenizer to split text into sentences
		return segmentedText
