# Program to perform Part-of-Speech (POS) Tagging using NLTK
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The quick brown fox jumps over the lazy dog."

words = word_tokenize(text)

pos_tags = nltk.pos_tag(words)

print("Part-of-Speech Tags:\n")
for word, tag in pos_tags:
    print(f"{word:10} --> {tag}")