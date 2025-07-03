from Organizations.GeneratePrice.Entities.CoeffMarkets import CoeffMarkets


class CoeffOtherMarket(CoeffMarkets):
    def __init__(self):
        super().__init__()

    def _init_positions(self) -> dict[str, dict[str, dict[str, float]]]:
        return {
            "stationery": self.__stationery_positions(),
            "for_kitchen": self.__for_kitchen_positions(),
            "for_everyday": self.__for_everyday_positions()
        }

    def __stationery_positions(self) -> dict[str, dict[str, float]]:
        return {
            "ПРО100": {
                "Ластик": 1.0, "Карандаш": 1.0, "Ручка шариковая": 1.0,
                "Ручка гелевая": 1.0, "Скрепки": 1.0, "Фломастеры": 1.0
            }
        }

    def __for_kitchen_positions(self) -> dict[str, dict[str, float]]:
        return {
            "ПРО100": {
                "Губка": 1.0, "Тёрка": 1.0, "Прихватки": 1.0, "Половник": 1.0,
                "Подставка для столовых приборов": 1.0, "Менажница": 1.0
            }
        }

    def __for_everyday_positions(self) -> dict[str, dict[str, float]]:
        return {
            "ПРО100": {
                "Щетка": 1.0, "Мыло": 1.0, "Жидкое мыло": 1.0, "Губки меламиновые": 1.0,
                "Средство для мытья полов": 1.0, "Средство для мытья ковров": 1.0
            }
        }