import unittest
def scitani(a, b):
    return a + b
class TestScitani(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(scitani(1, 1), 2)
        self.assertEqual(scitani(-1, 1), 0)
        self.assertEqual(scitani(1, -1), 0)
        self.assertEqual(scitani(2, 3), 5)

    def test_real_numbers(self):
        self.assertAlmostEqual(scitani(1.1, 2.2), 3.3)
        self.assertAlmostEqual(scitani(-1.1, 1.1), 0.0)
        self.assertAlmostEqual(scitani(1.5, -1.5), 0.0)
        self.assertAlmostEqual(scitani(2.5, 3.5), 6.0)

    def test_complex_numbers(self):
        self.assertEqual(scitani(3, 2j), 3+2j)
        self.assertEqual(scitani(1.2e3, 3j), 1200+3j)
        self.assertEqual(scitani(complex(1, 1), complex(1, 1)), 2+2j)
        self.assertEqual(scitani((3).real, (4j).real),3)


if __name__ == '__main__':
    unittest.main()