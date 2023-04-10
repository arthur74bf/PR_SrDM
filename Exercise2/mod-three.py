from Alphabet import Alphabet
from Builder import FSMBuilder
from Character import Character
from Transition import Transition
from Transitions import Transitions
from state.FinalState import FinalState
from state.States import States

if __name__ == '__main__':
    # Create Characters
    char_0 = Character('0')
    char_1 = Character('1')

    # Create the alphabet
    alphabet = Alphabet({char_0, char_1})

    # Define the states
    states = States({
        'State0': FinalState('State0', 0),
        'State1': FinalState('State1', 1),
        'State2': FinalState('State2', 2),
    })

    # Define the state transitions
    transition_list = [
        Transition('State0', Character('0'), states.get_state('State0')),
        Transition('State0', Character('1'), states.get_state('State1')),
        Transition('State1', Character('0'), states.get_state('State2')),
        Transition('State1', Character('1'), states.get_state('State0')),
        Transition('State2', Character('0'), states.get_state('State1')),
        Transition('State2', Character('1'), states.get_state('State2')),
    ]

    transitions = Transitions(transition_list)

    # Create a Builder instance and set the alphabet, states, and transitions
    builder = FSMBuilder().set_alphabet(alphabet).set_states(states).set_transitions(transitions)

    # Build the ModThreeFSM instance
    mod_three_fsm = builder.set_initial_state(states.get_state('State0')).build()

    # Process an input string
    input_string = '1101'
    remainder = mod_three_fsm.process_input(input_string)
    print(f"The input string '{input_string}' has remainder: {remainder}")

    input_string = '1110'
    remainder = mod_three_fsm.process_input(input_string)
    print(f"The input string '{input_string}' has remainder: {remainder}")

    input_string = '1111'
    remainder = mod_three_fsm.process_input(input_string)
    print(f"The input string '{input_string}' has remainder: {remainder}")

    input_string = '1110010011111001110011000' #30012312
    remainder = mod_three_fsm.process_input(input_string)
    print(f"The input string '{input_string}' has remainder: {remainder}")
