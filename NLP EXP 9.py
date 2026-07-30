# Rule-Based Part-of-Speech Tagging using Regular Expressions

import nltk
from nltk.tag import RegexpTagger
from nltk.tokenize import word_tokenize

nltk.download('punkt')

patterns = [
    (r'.*ing$', 'VBG'),      # Gerunds (running, playing)
    (r'.*ed$', 'VBD'),       # Past tense verbs (walked)
    (r'.*es$', 'VBZ'),       # Verbs ending with 'es' (goes)
    (r'.*ould$', 'MD'),      # Modal verbs (could, would)
    (r'.*\'s$', 'NN$'),      # Possessive nouns
    (r'.*s$', 'NNS'),        # Plural nouns
    (r'^[0-9]+$', 'CD'),     # Cardinal numbers
    (r'.*ly$', 'RB'),        # Adverbs
    (r'.*able$', 'JJ'),      # Adjectives
    (r'.*', 'NN')            # Default: Noun
]

tagger = RegexpTagger(patterns)

text = "The boys are playing football happily"

tokens = word_tokenize(text)

tagged = tagger.tag(tokens)

print("Rule-Based POS Tagging:\n")

for word, tag in tagged:
    print(f"{word:12} --> {tag}")