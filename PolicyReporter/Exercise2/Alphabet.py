from typing import Set

from Character import Character


class Alphabet:
    """Represents the input alphabet for the finite state machine."""
    def __init__(self, characters: Set[Character]):
        self.characters = characters

    def is_valid(self, input_symbol: Character) -> bool:
        """Checks if the input symbol is a valid character in the alphabet."""
        return input_symbol in self.characters
