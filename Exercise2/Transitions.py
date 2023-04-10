class Transitions:
    """A collection of transitions for the finite state machine."""
    def __init__(self, transition_list ):
        self.transitions = {}
        for transition in transition_list:
            key = (transition.from_state, transition.input_symbol)
            self.transitions[key] = transition.to_state

    def get_next_state(self, current_state, input_symbol):
        """Get the next state based on the current state and input symbol."""
        key = (current_state, input_symbol)
        return self.transitions.get(key)
