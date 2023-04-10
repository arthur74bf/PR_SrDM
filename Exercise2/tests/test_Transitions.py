from unittest import TestCase

from Character import Character
from FinalState import FinalState
from State import State
from States import States
from Transition import Transition
from Transitions import Transitions


class TestTransitions(TestCase):
    def test_transitions_get_next_state(self):
        states = States({
            'State0': FinalState('State0', 0),
            'State1': FinalState('State1', 1),
            'State2': FinalState('State2', 2),
        })
        char_0 = Character('0')
        char_1 = Character('1')
        state0 = State('State0', 0)
        state1 = State('State1', 1)
        transition = Transition('State0', Character('0'), states.get_state('State0'))
        transitions = Transitions([transition])
        self.assertEqual(transitions.get_next_state('State0', char_0), states.get_state('State0'))
        self.assertIsNone(transitions.get_next_state('State0', char_1))
