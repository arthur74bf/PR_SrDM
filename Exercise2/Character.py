class Character:
    """Represents a single character in the alphabet."""
    def __init__(self, symbol):
        self.symbol = symbol

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.symbol == other.symbol
        return False

    def __hash__(self):
        return hash(self.symbol)
