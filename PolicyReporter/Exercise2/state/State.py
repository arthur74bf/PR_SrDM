from StateInterface import StateInterface


class State(StateInterface):
    """Represents a non-final state in the finite state machine."""
    def on_input(self, input_symbol, transitions):
        return transitions.get_next_state(self.name, input_symbol)