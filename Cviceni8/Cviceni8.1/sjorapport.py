# sjorapport.py
from ikea_item import IkeaItem
from plastic_waste_ikea_item import PlasticWasteIkeaItem

class SJÖRAPPORT(IkeaItem, PlasticWasteIkeaItem):
    def __init__(self, shelf_number, aisle_letter, name, price, expiration_date, weight, plastic_weight):
        IkeaItem.__init__(self, shelf_number, aisle_letter, name, price)
        PlasticWasteIkeaItem.__init__(self, plastic_weight)
        self.expiration_date = expiration_date
        self.weight = weight