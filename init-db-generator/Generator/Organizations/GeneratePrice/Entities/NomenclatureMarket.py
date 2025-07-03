from Organizations.GeneratePrice.Entities.Fields.Product import Product


class NomenclatureMarket:
    def __init__(self):
        self.products = self._init_price()

    def _init_price(self) -> dict[str, list[Product]]: pass
