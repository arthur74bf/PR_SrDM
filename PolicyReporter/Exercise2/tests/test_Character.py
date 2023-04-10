from unittest import TestCase

from Character import Character


class TestCharacter(TestCase):
    def test_character_equality(self):
        c1 = Character('0')
        c2 = Character('0')
        c3 = Character('1')
        self.assertEqual(c1, c2)
        self.assertNotEqual(c1, c3)