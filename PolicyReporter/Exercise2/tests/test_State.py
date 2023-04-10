from unittest import TestCase

from Character import Character
from FinalState import FinalState
from State import State
from States import States
from Transition import Transition
from Transitions import Transitions


class TestState(TestCase):
    def setUp(self) -> None:
        self.states = States({
            'State0': FinalState('State0', 0),
            'State1': FinalState('State1', 1),
            'State2': FinalState('State2', 2),
        })
        self.char_0 = Character('0')
        self.char_1 = Character('1')
        self.state0 = State('State0', 0)
        self.state1 = FinalState('State1', 1)
        transition = Transition('State0', Character('0'), self.states.get_state('State0'))
        self.transitions = Transitions([transition])

    def test_on_input(self):
        self.assertEqual(self.state0.on_input(self.char_0, self.transitions), self.states.get_state('State0'))
