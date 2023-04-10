from unittest import TestCase

from Alphabet import Alphabet
from Character import Character


class TestAlphabet(TestCase):
    def test_alphabet_validity(self):
        char_0 = Character('0')
        char_1 = Character('1')
        alphabet = Alphabet({char_0, char_1})
        self.assertTrue(alphabet.is_valid(char_0))
        self.assertFalse(alphabet.is_valid(Character('2')))
