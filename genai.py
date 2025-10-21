import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

#Downloading stuff that will be used to tokenize the text
nltk.download('punkt')

sentence = 'I am learning Generative AI'
tokens = word_tokenize(sentence)
bigrams = list(ngrams(tokens, 2))

print(bigrams)