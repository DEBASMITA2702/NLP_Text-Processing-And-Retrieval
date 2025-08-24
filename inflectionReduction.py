from util import *
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('wordnet')		#wordNet dictionary required for lemmatization
nltk.download('omw-1.4')		#open Multilingual WordNet 


class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""
		
		lemmatizer = WordNetLemmatizer()	#Initializing WordNet Lemmatizer
		reducedText = []  	#Creating a list to store the lemmatized sentences

		#Iterating through each sentence in the text
		for sentence in text:  
			lemmatized_sentence = []  # Creating a list to store lemmatized words for the sentence

			#Iterating through each word in the sentence
			for word in sentence:
				lemma = lemmatizer.lemmatize(word)		#Applying lemmatization to each word
				lemmatized_sentence.append(lemma)  
			reducedText.append(lemmatized_sentence)

		return reducedText
