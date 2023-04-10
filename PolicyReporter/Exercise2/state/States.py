class States:
    """A collection of states for the finite state machine."""
    def __init__(self, states):
        self.states = states

    def get_state(self, state_name):
        return self.states[state_name]