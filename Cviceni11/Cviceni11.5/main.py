import random
import time
import unittest

class LinkedListCounter:
    def __init__(self):
        self.data = []

    def populate_list(self, size, min_val, max_val):
        """
        Populate the list with random integers.
        :param size: Number of elements in the list.
        :param min_val: Minimum value of random integers.
        :param max_val: Maximum value of random integers.
        """
        self.data = [random.randint(min_val, max_val) for _ in range(size)]

    def count_occurrences(self, target):
        """
        Count occurrences of the target value in the list.
        :param target: Value to count.
        :return: Number of occurrences.
        """
        return self.data.count(target)

# Unit tests
class TestLinkedListCounter(unittest.TestCase):
    def setUp(self):
        """
        Set up a LinkedListCounter instance for testing.
        """
        self.counter = LinkedListCounter()
        self.size = 1_000_000  # 1 million values
        self.min_val = 1
        self.max_val = 999
        self.target = 186
        self.counter.populate_list(self.size, self.min_val, self.max_val)

    def test_count_occurrences(self):
        """
        Test if count_occurrences returns an integer and executes within 500 ms.
        """
        start_time = time.time()
        count = self.counter.count_occurrences(self.target)
        end_time = time.time()

        duration = (end_time - start_time) * 1000  # Convert to milliseconds
        self.assertIsInstance(count, int, "The count should be an integer.")
        self.assertLessEqual(duration, 500, "The operation took longer than 500 ms.")


    def test_populate_list(self):

        self.assertEqual(len(self.counter.data), self.size, "The list should have 1 million elements.")
        self.assertTrue(all(self.min_val <= x <= self.max_val for x in self.counter.data),
                    "All values should be within the specified range.")

if __name__ == "__main__":
    unittest.main()
