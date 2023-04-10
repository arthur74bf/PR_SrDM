from abc import ABC, abstractmethod


class StateInterface(ABC):
    """Abstract base class for different types of states in the finite state machine."""
    def __init__(self, name, val) :
        self.name = name
        self.val = val

    @abstractmethod
    def on_input(self, input_symbol, transitions):
        pass
