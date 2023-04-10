from ModThreeFSM import ModThreeFSM


class FSMBuilder:
    """Builder class for constructing the finite state machine."""
    def __init__(self):
        self.alphabet = None
        self.states = None
        self.transitions = None
        self.initial_state = None

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet
        return self

    def set_states(self, states):
        self.states = states
        return self

    def set_transitions(self, transitions):
        self.transitions = transitions
        return self

    def set_initial_state(self, initial_state):
        self.initial_state = initial_state
        return self

    def build(self):
        return ModThreeFSM(self.initial_state, self.alphabet, self.states, self.transitions)
