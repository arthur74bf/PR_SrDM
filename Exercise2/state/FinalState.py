from StateInterface import StateInterface


class FinalState(StateInterface):
    """Represents a final state in the finite state machine."""
    def on_input(self, input_symbol, transitions):
        return transitions.get_next_state(self.name, input_symbol)

    def get_final_state_val(self):
        return self.val
