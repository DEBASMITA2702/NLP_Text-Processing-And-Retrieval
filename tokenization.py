from util import *
import re  
import nltk
from nltk.tokenize import TreebankWordTokenizer, word_tokenize


class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""
    
		tokenizedText = [re.findall(r'\b\w+\b', sentence) for sentence in text]  #Using regex to split on spaces.
		return tokenizedText


	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizer = TreebankWordTokenizer()	 #initializing the Penn Treebank Tokenizer
		tokenizedText = [tokenizer.tokenize(sentence) for sentence in text]  #tokenizing each sentence using the Penn tokenizer
		return tokenizedText