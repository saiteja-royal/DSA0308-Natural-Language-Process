class PorterStemmer:

    @staticmethod
    def is_vowel(word, index):
        ch = word[index].lower()

        if ch in "aeiou":
            return True

        if ch == "y":
            if index == 0:
                return False
            return not PorterStemmer.is_vowel(word, index - 1)

        return False

    @staticmethod
    def measure(stem):
        m = 0
        i = 0
        n = len(stem)

        while i < n:

            while i < n and not PorterStemmer.is_vowel(stem, i):
                i += 1

            while i < n and PorterStemmer.is_vowel(stem, i):
                i += 1

            if i < n:
                m += 1

        return m

    @staticmethod
    def contains_vowel(word):
        for i in range(len(word)):
            if PorterStemmer.is_vowel(word, i):
                return True
        return False

    @staticmethod
    def ends_with_double_consonant(word):
        if len(word) < 2:
            return False

        return (
            word[-1] == word[-2]
            and not PorterStemmer.is_vowel(word, len(word) - 1)
        )

    @staticmethod
    def cvc(word):
        if len(word) < 3:
            return False

        if (
            not PorterStemmer.is_vowel(word, len(word) - 3)
            and PorterStemmer.is_vowel(word, len(word) - 2)
            and not PorterStemmer.is_vowel(word, len(word) - 1)
            and word[-1] not in "wxy"
        ):
            return True

        return False

    # ---------------- Step 1a ----------------

    @staticmethod
    def step1a(word):

        if word.endswith("sses"):
            return word[:-2]

        elif word.endswith("ies"):
            return word[:-2]

        elif word.endswith("ss"):
            return word

        elif word.endswith("s"):
            return word[:-1]

        return word

    # ---------------- Step 1b ----------------

    @staticmethod
    def step1b(word):

        if word.endswith("eed"):
            stem = word[:-3]

            if PorterStemmer.measure(stem) > 0:
                return stem + "ee"

            return word

        if word.endswith("ed"):
            stem = word[:-2]

            if PorterStemmer.contains_vowel(stem):
                word = stem

        elif word.endswith("ing"):
            stem = word[:-3]

            if PorterStemmer.contains_vowel(stem):
                word = stem

        else:
            return word

        if word.endswith(("at", "bl", "iz")):
            word += "e"

        elif (
            PorterStemmer.ends_with_double_consonant(word)
            and word[-1] not in "lsz"
        ):
            word = word[:-1]

        elif PorterStemmer.measure(word) == 1 and PorterStemmer.cvc(word):
            word += "e"

        return word

    # ---------------- Step 1c ----------------

    @staticmethod
    def step1c(word):

        if word.endswith("y"):
            stem = word[:-1]

            if PorterStemmer.contains_vowel(stem):
                return stem + "i"

        return word

    # ---------------- Step 2 ----------------

    @staticmethod
    def step2(word):

        rules = [
            ("ational", "ate"),
            ("tional", "tion"),
            ("enci", "ence"),
            ("anci", "ance"),
            ("izer", "ize"),
            ("abli", "able"),
            ("alli", "al"),
            ("entli", "ent"),
            ("eli", "e"),
            ("ousli", "ous"),
            ("ization", "ize"),
            ("ation", "ate"),
            ("ator", "ate"),
            ("alism", "al"),
            ("iveness", "ive"),
            ("fulness", "ful"),
            ("ousness", "ous"),
            ("aliti", "al"),
            ("iviti", "ive"),
            ("biliti", "ble"),
            ("logi", "log"),
        ]

        for suffix, replacement in rules:

            if word.endswith(suffix):
                stem = word[:-len(suffix)]

                if PorterStemmer.measure(stem) > 0:
                    return stem + replacement

        return word

    # ---------------- Step 3 ----------------

    @staticmethod
    def step3(word):

        rules = [
            ("icate", "ic"),
            ("ative", ""),
            ("alize", "al"),
            ("iciti", "ic"),
            ("ical", "ic"),
            ("ful", ""),
            ("ness", ""),
        ]

        for suffix, replacement in rules:

            if word.endswith(suffix):
                stem = word[:-len(suffix)]

                if PorterStemmer.measure(stem) > 0:
                    return stem + replacement

        return word
     # ---------------- Step 4 ----------------

    @staticmethod
    def step4(word):

        suffixes = [
            "al",
            "ance",
            "ence",
            "er",
            "ic",
            "able",
            "ible",
            "ant",
            "ement",
            "ment",
            "ent",
            "ion",
            "ou",
            "ism",
            "ate",
            "iti",
            "ous",
            "ive",
            "ize",
        ]

        for suffix in suffixes:
            if not word.endswith(suffix):
                continue

            stem = word[:-len(suffix)]

            # For 'ion', the stem must end with 's' or 't'; for others only measure > 1
            if (
                PorterStemmer.measure(stem) > 1
                and (suffix != "ion" or (len(stem) > 0 and stem[-1] in "st"))
            ):
                return stem

        return word

    # ---------------- Step 5a ----------------

    @staticmethod
    def step5a(word):

        if word.endswith("e"):
            stem = word[:-1]
            m = PorterStemmer.measure(stem)

            if m > 1:
                return stem

            if m == 1 and not PorterStemmer.cvc(stem):
                return stem

        return word

    # ---------------- Step 5b ----------------

    @staticmethod
    def step5b(word):

        if (
            PorterStemmer.measure(word) > 1
            and word.endswith("ll")
        ):
            return word[:-1]

        return word

    # ---------------- Stem Function ----------------

    @staticmethod
    def stem(word):

        if len(word) <= 2:
            return word.lower()

        word = word.lower()

        word = PorterStemmer.step1a(word)
        word = PorterStemmer.step1b(word)
        word = PorterStemmer.step1c(word)
        word = PorterStemmer.step2(word)
        word = PorterStemmer.step3(word)
        word = PorterStemmer.step4(word)
        word = PorterStemmer.step5a(word)
        word = PorterStemmer.step5b(word)

        return word


# ---------------- Main Program ----------------

if __name__ == "__main__":

    print("=== Porter Stemmer ===")

    while True:

        word = input("\nEnter a word (or 'exit' to quit): ").strip()

        if word.lower() == "exit":
            print("Program terminated.")
            break

        if word == "":
            print("Please enter a valid word.")
            continue

        stemmed = PorterStemmer.stem(word)

        print("Original Word :", word)
        print("Stemmed Word  :", stemmed)