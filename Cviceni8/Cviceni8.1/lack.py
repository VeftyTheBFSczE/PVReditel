# lack.py
from ikea_item import IkeaItem
from measureable_ikea_item import MeasureableIkeaItem

class LACK(IkeaItem, MeasureableIkeaItem):
    def __init__(self, shelf_number, aisle_letter, name, price, color, height, width, length):
        IkeaItem.__init__(self, shelf_number, aisle_letter, name, price)
        MeasureableIkeaItem.__init__(self, height, width, length)
        self.color = color