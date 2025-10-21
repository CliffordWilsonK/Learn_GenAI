"""
The TextBlob library is a key tool in natural language processing and text analysis.
It simplifies text processing, making it easy to work with text data.

Why TextBlob is a vibe:

Easy to Use: TextBlob is straightforward and allows you to perform tasks like sentiment analysis,
part-of-speech tagging, and text translation with just a few lines of code.
Spell Checking and Correction: It includes built-in spell-checking and correction features.
Text Analysis: You can analyze text to extract useful information like determining its sentiment
(positive, negative, or neutral) and summarize text data.
"""

from textblob import TextBlob

text = 'I love progamming and machine learnig.'
blob = TextBlob(text)

corrected_text = blob.correct()

# Print the corrected text
print('Original Text:', text)
print('Corrected Text:', corrected_text)