from Character import Character
from FSM import FSM


class ModThreeFSM(FSM):
    """Modulo-3 finite state machine implementation."""
    def process_input(self, input_string: str) -> bool:
        current_state = self.current_state

        for symbol in input_string:
            character = Character(symbol)
            if not self.alphabet.is_valid(character):
                raise ValueError(f"Invalid symbol '{symbol}' in input string")
            current_state = self.transitions.get_next_state(current_state.name, character)

        if self.is_final_state(current_state):
            return current_state.get_final_state_val()

    def is_final_state(self, state):
        return hasattr(state, "get_final_state_val")
