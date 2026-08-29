class State:
    def __init__(self, lhs, rhs, dot, start):
        self.lhs = lhs
        self.rhs = rhs
        self.dot = dot
        self.start = start

    def is_complete(self):
        return self.dot == len(self.rhs)

    def next_symbol(self):
        if self.dot < len(self.rhs):
            return self.rhs[self.dot]
        return None

    def advance(self):
        return State(self.lhs, self.rhs, self.dot + 1, self.start)

    def __eq__(self, other):
        return (self.lhs, self.rhs, self.dot, self.start) == \
               (other.lhs, other.rhs, other.dot, other.start)

    def __hash__(self):
        return hash((self.lhs, tuple(self.rhs), self.dot, self.start))

    def __repr__(self):
        rhs = self.rhs[:]
        rhs.insert(self.dot, "•")
        return f"{self.lhs} -> {' '.join(rhs)}, ({self.start})"


def earley_parse(grammar, sentence, start_symbol):
    words = sentence.split()
    n = len(words)

    chart = [set() for _ in range(n + 1)]

    chart[0].add(State("γ", [start_symbol], 0, 0))

    for i in range(n + 1):
        changed = True

        while changed:
            changed = False
            states = list(chart[i])

            for state in states:

                # Predictor
                next_sym = state.next_symbol()

                if next_sym in grammar:
                    for production in grammar[next_sym]:
                        new_state = State(next_sym, production, 0, i)

                        if new_state not in chart[i]:
                            chart[i].add(new_state)
                            changed = True

                # Scanner
                elif next_sym is not None and i < n:
                    if next_sym == words[i]:
                        new_state = state.advance()

                        if new_state not in chart[i + 1]:
                            chart[i + 1].add(new_state)

                # Completer
                elif state.is_complete():
                    for old_state in list(chart[state.start]):
                        if old_state.next_symbol() == state.lhs:
                            new_state = old_state.advance()

                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

    print("\nEarley Chart:")

    for i, states in enumerate(chart):
        print(f"\nChart[{i}]")

        for s in states:
            print(s)

    final_state = State("γ", [start_symbol], 1, 0)

    if final_state in chart[n]:
        print("\nSentence Accepted")
    else:
        print("\nSentence Rejected")


# Grammar
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["John"], ["Mary"]],
    "VP": [["V", "NP"]],
    "V": [["likes"], ["sees"]]
}


# Input Sentence
sentence = "John likes Mary"

earley_parse(grammar, sentence, "S")