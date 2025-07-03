from Organizations.GeneratePrice.Entities.Fields.Barcode import Barcode
from Organizations.GeneratePrice.Entities.NomenclatureMarket import NomenclatureMarket
from Organizations.GeneratePrice.Entities.Fields.Product import Product


class NomenclatureSuperMarket(NomenclatureMarket):
    def __init__(self):
        super().__init__()

    def _init_price(self) -> dict[str, list[Product]]:
        return {
            "milk": [
                Product("Молоко", "milk", "budget", 60, Barcode()),
                Product("Наше", "milk", "budget", 65, Barcode()),
                Product("Деревня", "milk", "middle", 70, Barcode()),
                Product("Коровино", "milk", "middle", 75, Barcode()),
                Product("Ферма", "milk", "premium", 90, Barcode()),
                Product("Nature", "milk", "premium", 100, Barcode())
            ],
            "bread": [
                Product("Просто хлеб", "bread", "budget", 30, Barcode()),
                Product("Местный", "bread", "budget", 35, Barcode()),
                Product("Деревня", "bread", "middle", 40, Barcode()),
                Product("Мельница", "bread", "middle", 50, Barcode()),
                Product("Тонус", "bread", "premium", 80, Barcode()),
                Product("Эко", "bread", "premium", 100, Barcode())
            ],
            "grocery": [
                Product("Гречка", "grocery", "budget", 50, Barcode()),
                Product("Макароны", "grocery", "budget", 45, Barcode()),
                Product("Рис", "grocery", "budget", 60, Barcode()),
                Product("Чай", "grocery", "budget", 100, Barcode()),
                Product("Кофе", "grocery", "budget", 120, Barcode()),
                Product("Масло", "grocery", "budget", 11, Barcode())
            ],
            "crackers": [
                Product("4 корочки", "crackers", "budget", 30, Barcode()),
                Product("Мягкие", "crackers", "budget", 35, Barcode()),
                Product("Похрусteam", "crackers", "middle", 40, Barcode()),
                Product("Хрустики", "crackers", "middle", 45, Barcode()),
                Product("Suhariki", "crackers", "premium", 55, Barcode()),
                Product("Baget", "crackers", "premium", 60, Barcode())
            ],
            "chips": [
                Product("Бульба", "chips", "budget", 55, Barcode()),
                Product("Грация картошки", "chips", "budget", 60, Barcode()),
                Product("Leps", "chips", "middle", 90, Barcode()),
                Product("Potatos", "chips", "middle", 100, Barcode()),
                Product("Bringles", "chips", "premium", 170, Barcode()),
                Product("VIP Chips", "chips", "premium", 200, Barcode())
            ],
            "lemonade": [
                Product("Чувака", "lemonade", "budget", 50, Barcode()),
                Product("Подарочный", "lemonade", "budget", 70, Barcode()),
                Product("Белоголовка", "lemonade", "middle", 95, Barcode()),
                Product("КМВ", "lemonade", "middle", 100, Barcode()),
                Product("Phanta", "lemonade", "premium", 145, Barcode()),
                Product("7down", "lemonade", "premium", 15, Barcode())
            ],
            "washing": [
                Product("Зайчик", "washing", "budget", 60, Barcode()),
                Product("Стирка++", "washing", "budget", 65, Barcode()),
                Product("Мерсил", "washing", "middle", 70, Barcode()),
                Product("Гайд", "washing", "middle", 75, Barcode()),
                Product("Purity", "washing", "premium", 90, Barcode()),
                Product("Cleanliness", "washing", "premium", 100, Barcode())
            ],
            "soap": [
                Product("Хозяйственное", "soap", "budget", 30, Barcode()),
                Product("Душистое", "soap", "budget", 35, Barcode()),
                Product("Лав", "soap", "middle", 40, Barcode()),
                Product("Зелёная линия", "soap", "middle", 50, Barcode()),
                Product("Tenderness", "soap", "premium", 80, Barcode()),
                Product("Lovely", "soap", "premium", 100, Barcode())
            ],
            "dishwashing": [
                Product("Чистюля", "dishwashing", "budget", 50, Barcode()),
                Product("Тарелочкин", "dishwashing", "budget", 45, Barcode()),
                Product("Perry", "dishwashing", "middle", 60, Barcode()),
                Product("OAS", "dishwashing", "middle", 100, Barcode()),
                Product("Shine", "dishwashing", "premium", 120, Barcode()),
                Product("Brilliant", "dishwashing", "premium", 11, Barcode())
            ]
        }
