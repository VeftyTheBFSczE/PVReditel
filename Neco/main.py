class Bottle:
    def __init__(self, capacity_liters):
        self.capacity_liters = capacity_liters
        self.volume_liters = 0
        self.closed = False

    def check_status(self):
        if self.closed:
            raise ValueError("The bottle is closed. Cannot change the volume of liquid.")

    def set_volume_liters(self, volume):
        self.check_status()
        if volume < 0:
            raise ValueError("Volume cannot be negative.")
        if volume > self.capacity_liters:
            raise ValueError("Volume cannot exceed the bottle's capacity.")
        self.volume_liters = volume

    def get_volume_liters(self):
        return self.volume_liters

    def set_volume_milliliters(self, volume_ml):
        self.check_status()
        volume_liters = volume_ml / 1000.0
        self.set_volume_liters(volume_liters)

    def get_volume_milliliters(self):
        return self.volume_liters * 1000

    def empty(self):
        self.check_status()
        self.volume_liters = 0

    def close(self):
        self.closed = True

    def open(self):
        self.closed = False



bottle = Bottle(2)
bottle.set_volume_liters(1)
print(f"Bottle volume: {bottle.get_volume_liters()} liters")

bottle.set_volume_milliliters(1500)
print(f"Bottle volume: {bottle.get_volume_milliliters()} ml")

bottle.close()
try:
    bottle.set_volume_liters(1)
except ValueError as e:
    print(e)

bottle.open()
bottle.empty()
print(f"Bottle volume after emptying: {bottle.get_volume_liters()} liters")
