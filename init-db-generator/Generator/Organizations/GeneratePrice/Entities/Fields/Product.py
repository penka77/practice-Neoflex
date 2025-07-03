from Organizations.GeneratePrice.Entities.Fields.Barcode import Barcode


class Product:
    def __init__(self, name: str, type_product: str, type_budget: str, price: float, barcode: Barcode):
        self.name = name
        self.barcode = barcode
        self.type_product = type_product
        self.type_budget = type_budget
        self.price = price