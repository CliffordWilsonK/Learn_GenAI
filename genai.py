import nltk

#Downloading stuff that will be used to tokenize the text
nltk.download('punkt')

sample_text = 'I am learning Generative AI'
tokens = nltk.word_tokenize(sample_text.lower())

print('Tokens:', tokens)