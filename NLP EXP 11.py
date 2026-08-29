class TopDownParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.tokens = []
        self.pos = 0

    def parse(self, symbol):
        if symbol not in self.grammar:
            if self.pos < len(self.tokens) and self.tokens[self.pos] == symbol:
                self.pos += 1
                return True
            return False

        saved_pos = self.pos

        for production in self.grammar[symbol]:
            self.pos = saved_pos
            success = True

            for item in production:
                if not self.parse(item):
                    success = False
                    break

            if success:
                return True

        self.pos = saved_pos
        return False

    def accepts(self, sentence, start_symbol):
        self.tokens = sentence.split()
        self.pos = 0

        result = self.parse(start_symbol)

        return result and self.pos == len(self.tokens)


grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased"], ["saw"]]
}

parser = TopDownParser(grammar)

sentence = "the cat chased the dog"

if parser.accepts(sentence, "S"):
    print("Sentence is accepted by the grammar.")
else:
    print("Sentence is rejected by the grammar.")