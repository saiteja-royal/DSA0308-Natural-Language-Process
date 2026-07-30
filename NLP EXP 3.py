import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

# Sample words
words = ["running", "studies", "better", "playing", "cars", "children"]

# Initialize Stemmer and Lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Morphological Analysis using NLTK\n")

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"Word: {word}")
    print(f"Stem: {stem}")
    print(f"Lemma: {lemma}")
    print("-" * 25)