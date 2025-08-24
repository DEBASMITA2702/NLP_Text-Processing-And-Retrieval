import nltk
nltk.download('punkt_tab')
import json
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')      #Tokenizer model for word tokenization
nltk.download('stopwords')  #This is the standard NLTK stopwords list

with open('/content/cranfield/cran_docs.json', 'r') as file:       # Here, we are loading the cran_docs.json from the Cranfield dataset
    cranfield_data = json.load(file)

totalTokens = []        # Creating a list to store all the tokens

#Iterating through each document in the Cranfield dataset
for doc in cranfield_data:
    if 'body' in doc:
        document_text = doc['body']   #Extracting only 'body' from the document
        document_text = document_text.lower()   #Converting the text to lowercase(for case insensitivity)
        tokenized_words = word_tokenize(document_text)    #Tokenizing the words present in the document

        for word in tokenized_words:
            totalTokens.append(word)        #Adding the tokenized words

wordFrequency = Counter(totalTokens)   # Count the occurrences of each word
threshold = int(0.02 * len(wordFrequency))    # Selecting only 2% of the most frequent words
corpus_stopwords = {word for word, freq in wordFrequency.most_common(threshold)}

nltk_stopwords = set(stopwords.words('english'))    #Loading standard NLTK stopwords
common_stopwords = corpus_stopwords.intersection(nltk_stopwords)    # Here we are finding the common words in both the lists

#Fetching all the word counts here
nltk_stopwords_count = len(nltk_stopwords)
corpus_stopwords_count = len(corpus_stopwords)
common_stopwords_count = len(common_stopwords)

#Printing first 20 stopwords only in each case
print(f"\nNLTK Stopwords ({nltk_stopwords_count} words)")
print(sorted(list(nltk_stopwords))[:20])

print(f"\nCorpus-Specific Stopwords ({corpus_stopwords_count} words)")
print(sorted(list(corpus_stopwords))[:20])

print(f"\nCommon Stopwords in Both Lists ({common_stopwords_count} words)")
print(sorted(list(common_stopwords))[:20])
