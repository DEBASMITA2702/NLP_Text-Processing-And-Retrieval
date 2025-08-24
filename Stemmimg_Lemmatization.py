import re
from nltk.stem import PorterStemmer
porter = PorterStemmer()    # Initializing Porter Stemmer
filename = "/content/output/tokenized_docs.txt"  # Providing the path to the input file 

with open(filename, "r") as file:     
    text = file.read()       # Reading the file entire content, as a single string

words = re.findall(r'\b[a-zA-Z]+\b', text)   # Extracting only alphabetic words using regex 

print("Following are the original words:")
print(words)        #Printing the original words extracted

stemmed_words = [porter.stem(word) for word in words]   # Applying stemming to each extracted word

print("Following are the stemmed words:")
print(stemmed_words)    #Printing the stemmed words 
