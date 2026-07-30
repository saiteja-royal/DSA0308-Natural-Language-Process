import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, DefaultTagger

# Download dataset
nltk.download('treebank')

# Training data
train_data = treebank.tagged_sents()

# Default tagger (assigns NN if word is unknown)
default_tagger = DefaultTagger('NN')

# Unigram tagger with backoff
tagger = UnigramTagger(train_data, backoff=default_tagger)

# Test sentence
sentence = "The quick brown fox jumps over the lazy dog".split()

# POS Tagging
tagged = tagger.tag(sentence)

print("Stochastic POS Tagging\n")
for word, tag in tagged:
    print(f"{word:10} --> {tag}")