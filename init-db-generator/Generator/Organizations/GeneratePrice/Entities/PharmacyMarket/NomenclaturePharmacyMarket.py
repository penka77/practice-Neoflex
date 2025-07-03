from Organizations.GeneratePrice.Entities.Fields.Barcode import Barcode
from Organizations.GeneratePrice.Entities.NomenclatureMarket import NomenclatureMarket
from Organizations.GeneratePrice.Entities.Fields.Product import Product


class NomenclaturePharmacyMarket(NomenclatureMarket):
    def __init__(self):
        super().__init__()

    def _init_price(self) -> dict[str, list[Product]]:
        return {
            "biologically_active": [
                Product("Витаминки", "biologically_active", "budget", 50, Barcode()),
                Product("Озверин", "biologically_active", "budget", 55, Barcode()),
                Product("Витамин D", "biologically_active", "middle", 70, Barcode()),
                Product("D3-формула", "biologically_active", "middle", 85, Barcode()),
                Product("Ногтерост", "biologically_active", "premium", 105, Barcode()),
                Product("Волосила", "biologically_active", "premium", 170, Barcode())
            ],
            "from_colds": [
                Product("Мукалтин", "from_colds", "budget", 60, Barcode()),
                Product("Кашлевит", "from_colds", "budget", 88, Barcode()),
                Product("Ингасол", "from_colds", "middle", 110, Barcode()),
                Product("Ринофолт", "from_colds", "middle", 150, Barcode()),
                Product("Амперин", "from_colds", "premium", 230, Barcode()),
                Product("Кинза", "from_colds", "premium", 400, Barcode())
            ],
            "etc": [
                Product("Вкуснетта", "etc", "budget", 50, Barcode()),
                Product("Итифен", "etc", "budget", 75, Barcode()),
                Product("Семирол", "etc", "middle", 100, Barcode()),
                Product("Носорин", "etc", "middle", 130, Barcode()),
                Product("Плесс", "etc", "premium", 150, Barcode()),
                Product("Имбафорт", "etc", "premium", 21, Barcode())
            ]
        }
