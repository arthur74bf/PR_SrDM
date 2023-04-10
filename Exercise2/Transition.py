from Character import Character
from StateInterface import StateInterface


class Transition:
    """Represents a state transition in the finite state machine."""
    def __init__(self, from_state: StateInterface, input_symbol: Character, to_state: StateInterface):
        self.from_state = from_state
        self.input_symbol = input_symbol
        self.to_state = to_state