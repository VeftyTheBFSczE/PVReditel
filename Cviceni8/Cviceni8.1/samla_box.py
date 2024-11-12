# samla_box.py
from ikea_item import IkeaItem
from measureable_ikea_item import MeasureableIkeaItem
from plastic_waste_ikea_item import PlasticWasteIkeaItem

class SAMLA_BOX(IkeaItem, MeasureableIkeaItem, PlasticWasteIkeaItem):
    def __init__(self, shelf_number, aisle_letter, name, price, volume, height, width, length, plastic_weight):
        IkeaItem.__init__(self, shelf_number, aisle_letter, name, price)
        MeasureableIkeaItem.__init__(self, height, width, length)
        PlasticWasteIkeaItem.__init__(self, plastic_weight)
        self.volume = volume