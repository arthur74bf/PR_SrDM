from unittest import TestCase

from Alphabet import Alphabet
from Builder import FSMBuilder
from Character import Character
from FinalState import FinalState
from ModThreeFSM import ModThreeFSM
from State import State
from States import States
from Transition import Transition
from Transitions import Transitions


class TestModThreeFSM(TestCase):
    def test_mod_three_fsm_process_input(self):
        char_0 = Character('0')
        char_1 = Character('1')
        alphabet = Alphabet({char_0, char_1})
        state0 = FinalState('State0', 0)
        state1 = FinalState('State1', 1)
        state2 = FinalState('State2', 2)
        states = States({'State0': state0, 'State1': state1, 'State2': state2})
        transition_list = [
            Transition('State0', char_0, state0),
            Transition('State0', char_1, state1),
            Transition('State1', char_0, state2),
            Transition('State1', char_1, state0),
        ]
        transitions = Transitions(transition_list)
        builder = FSMBuilder().set_alphabet(alphabet).set_states(states).set_transitions(transitions)
        mod_three_fsm = builder.set_initial_state(states.get_state('State0')).build()
        self.assertTrue(mod_three_fsm.process_input('10'))
        self.assertFalse(mod_three_fsm.process_input('100'))
        with self.assertRaises(ValueError):
            mod_three_fsm.process_input('102')

    def test_is_final_state(self):
        char_0 = Character('0')
        char_1 = Character('1')
        alphabet = Alphabet({char_0, char_1})
        state0 = FinalState('State0', 0)
        state1 = FinalState('State1', 1)
        state2 = FinalState('State2', 2)
        states = States({'State0': state0, 'State1': state1, 'State2': state2})
        transition_list = [
            Transition('State0', char_0, state0),
            Transition('State0', char_1, state1),
            Transition('State1', char_0, state2),
            Transition('State1', char_1, state0),
        ]
        transitions = Transitions(transition_list)
        builder = FSMBuilder().set_alphabet(alphabet).set_states(states).set_transitions(transitions)
        mod_three_fsm = builder.set_initial_state(states.get_state('State0')).build()

        state0 = FinalState('State0', 0)
        result = mod_three_fsm.is_final_state(state0)
        self.assertTrue(result)
