from abc import ABC, abstractmethod


class FSM(ABC):
    """Abstract base class for the finite state machine."""
    def __init__(self, initial_state, alphabet, states, transitions):
        self.current_state = initial_state
        self.alphabet = alphabet
        self.states = states
        self.transitions = transitions

    @abstractmethod
    def process_input(self, input_string):
        pass

    @abstractmethod
    def is_final_state(self):
        pass