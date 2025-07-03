import random


class Barcode:
    def __init__(self):
        self.country_code = random.randint(100, 999)
        self.creator_code = random.randint(1000, 9999)
        self.product_code = random.randint(10000, 99999)
        self.control_code = random.randint(0, 9)

    def __str__(self):
        return f"{self.country_code} {self.creator_code} {self.product_code} {self.control_code}"
