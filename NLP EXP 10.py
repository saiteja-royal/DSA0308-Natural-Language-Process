# Transformation-Based POS Tagging using Simple Rules
sentence = [
    ("The", "NN"),
    ("boys", "NN"),
    ("are", "NN"),
    ("playing", "NN"),
    ("football", "NN"),
    ("happily", "NN")
]

# Function to apply transformation rules
def transform_tags(tagged_sentence):
    transformed = []

    for word, tag in tagged_sentence:

        if word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ly"):
            tag = "RB"

        elif word.endswith("s"):
            tag = "NNS"

        elif word.lower() in ["a", "an", "the"]:
            tag = "DT"

        elif word.lower() in ["am", "is", "are", "was", "were"]:
            tag = "VBP"

        transformed.append((word, tag))

    return transformed

result = transform_tags(sentence)

print("Transformation-Based POS Tagging:\n")
print("{:<12}{}".format("Word", "Tag"))
print("-" * 20)

for word, tag in result:
    print("{:<12}{}".format(word, tag))