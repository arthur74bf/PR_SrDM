from unittest import TestCase

from State import State
from States import States


class TestStates(TestCase):
    def test_states_get_state(self):
        state0 = State('State0', 0)
        state1 = State('State1', 1)
        states = States({'State0': state0, 'State1': state1})
        self.assertEqual(states.get_state('State0'), state0)
        self.assertNotEqual(states.get_state('State0'), state1)
