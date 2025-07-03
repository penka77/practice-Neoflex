from Organizations.GeneratePrice.Entities.Fields.Barcode import Barcode
from Organizations.GeneratePrice.Entities.NomenclatureMarket import NomenclatureMarket
from Organizations.GeneratePrice.Entities.Fields.Product import Product


class NomenclatureZooMarket(NomenclatureMarket):
    def __init__(self):
        super().__init__()

    def _init_price(self) -> dict[str, list[Product]]:
        return {
            "medicines": [
                Product("БлошекНет", "medicines", "budget", 90, Barcode()),
                Product("Глистогон", "medicines", "budget", 120, Barcode()),
                Product("ОтБлох", "medicines", "middle", 210, Barcode()),
                Product("Кулакса", "medicines", "middle", 300, Barcode()),
                Product("СинусКот", "medicines", "premium", 700, Barcode()),
                Product("АмПет", "medicines", "premium", 1200, Barcode())
            ],
            "accessories": [
                Product("Мятный шарик", "accessories", "budget", 60, Barcode()),
                Product("Брелок", "accessories", "budget", 100, Barcode()),
                Product("Мышка", "accessories", "middle", 150, Barcode()),
                Product("Мячик", "accessories", "middle", 200, Barcode()),
                Product("Поводок", "accessories", "premium", 440, Barcode()),
                Product("Комбенизон", "accessories", "premium", 1000, Barcode())
            ],
            "services": [
                Product("Укол", "services", "budget", 60, Barcode()),
                Product("Осмотр", "services", "budget", 700, Barcode()),
                Product("Вакцинация", "services", "middle", 1200, Barcode()),
                Product("Кастрация", "services", "middle", 2000, Barcode()),
                Product("Стерилизация", "services", "premium", 3000, Barcode()),
                Product("Санация", "services", "premium", 400, Barcode())
            ]
        }
