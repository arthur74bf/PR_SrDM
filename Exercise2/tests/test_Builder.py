from unittest import TestCase
from Alphabet import Alphabet
from Builder import FSMBuilder
from Character import Character
from FinalState import FinalState
from ModThreeFSM import ModThreeFSM
from State import State
from StateInterface import StateInterface
from States import States
from Transition import Transition
from Transitions import Transitions

class TestFSMBuilder(TestCase):
    def setUp(self) -> None:
        char_0 = Character('0')
        char_1 = Character('1')
        alphabet = Alphabet({char_0, char_1})
        state0 = FinalState('State0',0)
        state1 = FinalState('State1',1)
        state2 = FinalState('State2',2)
        states = States({'State0': state0, 'State1': state1, 'State2': state2})
        transition_list = [
            Transition('State0', char_0, state0),
            Transition('State0', char_1, state1),
            Transition('State1', char_0, state2),
            Transition('State1', char_1, state0)
        ]
        transitions = Transitions(transition_list)
        builder = FSMBuilder()
        self.mod_three_fsm = (
            builder.set_alphabet(alphabet)
            .set_states(states)
            .set_transitions(transitions)
            .set_initial_state(state0)
            .build()
        )

    def test_set_alphabet(self):
        self.assertIsInstance(self.mod_three_fsm.alphabet, Alphabet)

    def test_set_states(self):
        self.assertIsInstance(self.mod_three_fsm.states, States)

    def test_set_transitions(self):
        self.assertIsInstance(self.mod_three_fsm.transitions, Transitions)

    def test_set_initial_state(self):
        self.assertIsInstance(self.mod_three_fsm.current_state, StateInterface)

    def test_builder_build(self):

        self.assertIsInstance(self.mod_three_fsm, ModThreeFSM)