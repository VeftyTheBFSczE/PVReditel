import unittest

class Bottle:
    def __init__(self, capacity_liters):
        self.capacity_liters = capacity_liters
        self.volume_liters = 0
        self.is_closed = False

    def set_volume_liters(self, volume):
        if not self.is_closed:
            if volume <= self.capacity_liters:
                self.volume_liters = volume
            else:
                self.volume_liters = self.capacity_liters

    def get_volume_liters(self):
        return self.volume_liters

    def set_volume_milliliters(self, volume):
        if not self.is_closed:
            volume_liters = volume / 1000
            if volume_liters <= self.capacity_liters:
                self.volume_liters = volume_liters
            else:
                self.volume_liters = self.capacity_liters

    def get_volume_milliliters(self):
        return self.volume_liters * 1000

    def empty_bottle(self):
        if not self.is_closed:
            self.volume_liters = 0

    def close_bottle(self):
        self.is_closed = True

    def open_bottle(self):
        self.is_closed = False

class TestBottle(unittest.TestCase):
    def test_initial_state(self):
        bottle = Bottle(2)
        self.assertEqual(bottle.get_volume_liters(), 0)
        self.assertFalse(bottle.is_closed)

    def test_set_volume_liters(self):
        bottle = Bottle(2)
        bottle.set_volume_liters(1.5)
        self.assertEqual(bottle.get_volume_liters(), 1.5)
        bottle.set_volume_liters(3)
        self.assertEqual(bottle.get_volume_liters(), 2)

    def test_set_volume_milliliters(self):
        bottle = Bottle(2)
        bottle.set_volume_milliliters(1500)
        self.assertEqual(bottle.get_volume_liters(), 1.5)
        bottle.set_volume_milliliters(3000)
        self.assertEqual(bottle.get_volume_liters(), 2)

    def test_empty_bottle(self):
        bottle = Bottle(2)
        bottle.set_volume_liters(1.5)
        bottle.empty_bottle()
        self.assertEqual(bottle.get_volume_liters(), 0)

    def test_close_bottle(self):
        bottle = Bottle(2)
        bottle.close_bottle()
        self.assertTrue(bottle.is_closed)
        bottle.set_volume_liters(1.5)
        self.assertEqual(bottle.get_volume_liters(), 0)
        bottle.empty_bottle()
        self.assertEqual(bottle.get_volume_liters(), 0)

    def test_open_bottle(self):
        bottle = Bottle(2)
        bottle.close_bottle()
        bottle.open_bottle()
        self.assertFalse(bottle.is_closed)
        bottle.set_volume_liters(1.5)
        self.assertEqual(bottle.get_volume_liters(), 1.5)

if __name__ == '__main__':
    unittest.main()