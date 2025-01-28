
import unittest


def scitani(a, b):

    if  type(a) in (list,tuple,dict,set)  or type(b)  in (list,tuple,dict,set):
        raise TypeError
    elif type(a) == None or type(b) == None:
        raise TypeError
    elif type(a) == str or type(b) == str:
        raise ValueError
    elif type(a) not in (int, float) or type(b) not in (int, float):

        raise TypeError

    if type(b) in (int,float) and type(a) in (int,float):
        return a + b

class TestScitani(unittest.TestCase):
    def test_bad_input(self):
        with self.assertRaises(ValueError):
            scitani("AHOJ", 100)
        with self.assertRaises(ValueError):
            scitani(100, "AHOJ")
        with self.assertRaises(TypeError):
            scitani(None, None)
        with self.assertRaises(TypeError):
            scitani([4, 5, 6], [1, 2, 3])
        with self.assertRaises(TypeError):
            scitani({56,"ansfoa"}, 5)

        with self.assertRaises(TypeError):
                scitani("aknd", {56, "ansfoa"})

if __name__ == '__main__':
    unittest.main()
