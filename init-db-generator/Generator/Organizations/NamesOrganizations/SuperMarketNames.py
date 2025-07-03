from Organizations.NamesOrganizations.OrganizationNames import OrganizationNames, Organization


class SuperMarketNames(OrganizationNames):
    def __init__(self):
        super().__init__()

    def get_mcc(self) -> list[int]:
        return [5411, 5499]

    def _init_mcc(self) -> list[int]:
        return [5411, 5499]

    def _init_store_chain(self) -> list[Organization]:
        return [
            Organization("У дома!", "budget", 23),
            Organization("Дёшево!", "budget", 22),
            Organization("Покупочка", "middle", 15),
            Organization("Дорого-Богато", "premium", 5),
            Organization("ГиперПрод", "middle", 5)
        ]

    def _init_city_store_chain(self) -> dict[str, list[Organization]]:
        return {
            "Саратов": [Organization("Стерлядка", "middle", 100)],
            "Нижний Новгород": [Organization("Горький", "middle", 100)],
            "Москва": [Organization("Столичный", "middle", 100)],
            "Санкт-Петербург": [Organization("Нева-маркет", "middle", 100)],
            "Пятигорск": [Organization("Машук", "middle", 100)],
            "Ялта": [Organization("Курортные продукты", "middle", 100)],
            "Челябинск": [Organization("Суровые продукты", "middle", 100)],
            "Екатеринбург": [Organization("Уралочка", "middle", 100)],
            "Новосибирск": [Organization("Снежное", "middle", 100)],
            "Красноярск": [Organization("Сибирская щедрость", "middle", 100)],
            "Владивосток": [Organization("Дальневосточное море", "middle", 100)],
            "Хабаровск": [Organization("Дальневосточный", "middle", 100)]
        }

    def get_market_probability(self, local_probability: int = 30) -> dict[str, int]:
        return super().get_market_probability(local_probability)
