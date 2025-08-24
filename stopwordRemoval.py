from util import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class StopwordRemoval():
	
	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = []  #Creating a list to store processed sentences
		stop_words = set(stopwords.words('english'))  # Loading standard stopwords
		for sentence in text:  # Iterate over each tokenized sentence
			filtered_sentence = []

			for word in sentence:
				if word.lower() not in stop_words:
					filtered_sentence.append(word)  # Adding non-stopwords to the list

			stopwordRemovedText.append(filtered_sentence)  #Appending filtered sentence to the final list
		return stopwordRemovedText
