from Organizations.GeneratePrice.Entities.Fields.Barcode import Barcode
from Organizations.GeneratePrice.Entities.NomenclatureMarket import NomenclatureMarket
from Organizations.GeneratePrice.Entities.Fields.Product import Product


class NomenclatureOtherMarket(NomenclatureMarket):
    def __init__(self):
        super().__init__()

    def _init_price(self) -> dict[str, list[Product]]:
        return {
            "stationery": [
                Product("Ластик", "stationery", "budget", 20, Barcode()),
                Product("Карандаш", "stationery", "budget", 25, Barcode()),
                Product("Ручка шариковая", "stationery", "middle", 30, Barcode()),
                Product("Ручка гелевая", "stationery", "middle", 50, Barcode()),
                Product("Скрепки", "stationery", "premium", 75, Barcode()),
                Product("Фломастеры", "stationery", "premium", 150, Barcode())
            ],
            "for_kitchen": [
                Product("Губка", "for_kitchen", "budget", 35, Barcode()),
                Product("Тёрка", "for_kitchen", "budget", 40, Barcode()),
                Product("Прихватки", "for_kitchen", "middle", 200, Barcode()),
                Product("Половник", "for_kitchen", "middle", 250, Barcode()),
                Product("Подставка для столовых приборов", "for_kitchen", "premium", 550, Barcode()),
                Product("Менажница", "for_kitchen", "premium", 1000, Barcode())
            ],
            "for_everyday": [
                Product("Щетка", "for_everyday", "budget", 45, Barcode()),
                Product("Мыло", "for_everyday", "budget", 60, Barcode()),
                Product("Жидкое мыло", "for_everyday", "middle", 100, Barcode()),
                Product("Губки меламиновые", "for_everyday", "middle", 170, Barcode()),
                Product("Средство для мытья полов", "for_everyday", "premium", 450, Barcode()),
                Product("Средство для мытья ковров", "for_everyday", "premium", 60, Barcode())
            ]
        }
