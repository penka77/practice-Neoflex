from Organizations.GeneratePrice.Entities.Fields.Barcode import Barcode
from Organizations.GeneratePrice.Entities.NomenclatureMarket import NomenclatureMarket
from Organizations.GeneratePrice.Entities.Fields.Product import Product


class NomenclatureBuildMarket(NomenclatureMarket):
    def __init__(self):
        super().__init__()

    def _init_price(self) -> dict[str, list[Product]]:
        return {
            "construction": [
                Product("Гайка", "construction", "budget", 40, Barcode()),
                Product("Анкер", "construction", "budget", 120, Barcode()),
                Product("Молоток", "construction", "middle", 550, Barcode()),
                Product("Кусачки", "construction", "middle", 700, Barcode()),
                Product("Набор бит", "construction", "premium", 1700, Barcode()),
                Product("Перфоратор", "construction", "premium", 10000, Barcode())
            ],
            "renovation": [
                Product("Изолента", "renovation", "budget", 60, Barcode()),
                Product("Скотч", "renovation", "budget", 100, Barcode()),
                Product("Канцелярский нож", "renovation", "middle", 150, Barcode()),
                Product("Отвертка", "renovation", "middle", 400, Barcode()),
                Product("Шуруповерт", "renovation", "premium", 230, Barcode()),
                Product("Дрель", "renovation", "premium", 7000, Barcode())
            ],
            "garden": [
                Product("Быстросъем", "garden", "budget", 40, Barcode()),
                Product("Гном", "garden", "budget", 700, Barcode()),
                Product("Шланг", "garden", "middle", 1100, Barcode()),
                Product("Кресло", "garden", "middle", 4000, Barcode()),
                Product("Стол", "garden", "premium", 8000, Barcode()),
                Product("Качели", "garden", "premium", 1500, Barcode())
            ]
        }
