grammer={
    "s":["NP VP"],
    "NP":["Det N"],
    "VP":["V"],
    "Det":["the"],
    "N_singular":["boy","girl","student"],
    "N_plural":["boys","girls","students"],
    "V_singular":["runs","plays","eats"],
    "V_plural":["run","play","eat"]
}

def check_agreement(sentence):
    words = sentence.lower().split()
    
    if len(words) != 3:
        return False
    
    determiner, noun, verb = words
    
    if noun in grammer["N_singular"] and verb in grammer["V_singular"]:
        return True
    
    if noun in grammer["N_plural"] and verb in grammer["V_plural"]:
        return True
    
    return False

sentences = ["The boy runs", "The boys play", "The girl eats", "The girls runs", "The students eats"]

for s in sentences:
    if check_agreement(s):
        print(f"'{s}' is grammatically correct.")
    else:
        print(f"'{s}' is grammatically incorrect.")