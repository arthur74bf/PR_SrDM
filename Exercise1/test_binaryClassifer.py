from unittest import TestCase

from binaryClassifer import find_threshold


class Test(TestCase):
    def test_find_threshold(self):
        # Prepare a simple metrics dictionary for testing purposes
        metrics_dict = {
            0.1: (50, 45, 5, 0),
            0.2: (45, 49, 1, 5),
            0.3: (40, 50, 0, 10),
            0.4: (35, 50, 0, 15),
        }
        result = list(find_threshold(1,))
        expected_result = []
        self.assertEqual(result, expected_result)

        result = list(find_threshold(None,))
        expected_result = []
        self.assertEqual(result, expected_result)

        # Test the find_threshold function with a recall threshold of 0.9
        result = list(find_threshold(metrics_dict, recall_threshold=0.9))
        expected_result = [0.1,0.2]
        self.assertEqual(result, expected_result)

        # Test the find_threshold function with a recall threshold of 0.8
        result = list(find_threshold(metrics_dict, recall_threshold=0.8))
        expected_result = [0.1, 0.2, 0.3]
        self.assertEqual(result, expected_result)

        # Test the find_threshold function with a recall threshold of 0.7
        result = list(find_threshold(metrics_dict, recall_threshold=0.7))
        expected_result = [0.1, 0.2, 0.3, 0.4]
        self.assertEqual(result, expected_result)
        # self.fail()
