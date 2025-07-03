from Organizations.NamesOrganizations.OrganizationNames import OrganizationNames, Organization


class BuildMarketNames(OrganizationNames):
    def __init__(self):
        super().__init__()

    def get_mcc(self) -> list[int]:
        return [5200, 5211]

    def _init_mcc(self) -> list[int]:
        return [5200, 5211]

    def _init_store_chain(self) -> list[Organization]:
        return [
            Organization("Всё что нужно", "budget", 23),
            Organization("Стройся", "budget", 22),
            Organization("Молотково", "middle", 15),
            Organization("Luxary Renovation", "premium", 5),
            Organization("ШкафоБаза", "middle", 5)
        ]

    def _init_city_store_chain(self) -> dict[str, list[Organization]]:
        return {
            "Саратов": [Organization("Моё добро", "middle", 100)],
            "Нижний Новгород": [Organization("Домашний мастер", "middle", 100)],
            "Москва": [Organization("Похорошела", "middle", 100)],
            "Санкт-Петербург": [Organization("Строим ТУТ!", "middle", 100)],
            "Пятигорск": [Organization("Строимся", "middle", 100)],
            "Ялта": [Organization("Стройкино", "middle", 100)],
            "Челябинск": [Organization("Молот и Наковальня", "middle", 100)],
            "Екатеринбург": [Organization("Малахит", "middle", 100)],
            "Новосибирск": [Organization("Ремонтово", "middle", 100)],
            "Красноярск": [Organization("Прекрасная квартира!", "middle", 100)],
            "Владивосток": [Organization("ЗаБей!", "middle", 100)],
            "Хабаровск": [Organization("Саморезкино", "middle", 100)]
        }

    def get_market_probability(self, local_probability: int = 30) -> dict[str, int]:
        return super().get_market_probability(local_probability)
