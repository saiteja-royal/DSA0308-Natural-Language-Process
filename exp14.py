grammar = {
    "s": ["NP VP"],
    "NP": ["Det N"],
    "VP": ["V"],
    "Det": ["the"],
    "N_singular": ["boy", "girl", "student"],
    "N_plural": ["boys", "girls", "students"],
    "V_singular": ["runs", "plays", "eats"],
    "V_plural": ["run", "play", "eat"]
}
def check_agreement(sentence):
    words = sentence.lower().split()
    if len(words) != 3:
        return False
    determiner = words[0]
    noun = words[1]
    verb = words[2]
    if determiner not in grammar["Det"]:
        return False
    if noun in grammar["N_singular"]:
        if verb in grammar["V_singular"]:
            return True
        else:
            return False
    elif noun in grammar["N_plural"]:
        if verb in grammar["V_plural"]:
            return True
        else:
            return False
    return False
sentence = input("Enter a sentence: ")
if check_agreement(sentence):
    print("Correct sentence - Subject and Verb agree.")
else:
    print("Incorrect sentence - Subject and Verb do not agree.")
