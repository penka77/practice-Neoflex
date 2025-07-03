from Organizations.NamesOrganizations.OrganizationNames import OrganizationNames, Organization


class PharmacyMarketNames(OrganizationNames):
    def __init__(self):
        super().__init__()

    def get_mcc(self) -> list[int]:
        return [5912, 5122]

    def _init_mcc(self) -> list[int]:
        return [5912, 5122]

    def _init_store_chain(self) -> list[Organization]:
        return [
            Organization("Молодость", "budget", 25),
            Organization("Таблетница", "budget", 27),
            Organization("Аспирин", "middle", 23),
            Organization("36 и 6", "premium", 5),
            Organization("120 на 80", "middle", 5)
        ]

    def _init_city_store_chain(self) -> dict[str, list[Organization]]:
        return {
            "Саратов": [Organization("Здоровье", "middle", 100)],
            "Нижний Новгород": [Organization("Гиппократ", "middle", 100)],
            "Москва": [Organization("Кремлёвская", "middle", 100)],
            "Санкт-Петербург": [Organization("Аптеки у дома", "middle", 100)],
            "Пятигорск": [Organization("Кавказское долголетие", "middle", 100)],
            "Ялта":[Organization("Крымская здравница", "middle", 100)],
            "Челябинск": [Organization("Здравствуйте!", "middle", 100)],
            "Екатеринбург": [Organization("Богатырь", "middle", 100)],
            "Новосибирск": [Organization("Кедр", "middle", 100)],
            "Красноярск": [Organization("Сибирь", "middle", 100)],
            "Владивосток": [Organization("Омега", "middle", 100)],
            "Хабаровск": [Organization("Будь Здоров!", "middle", 100)]
        }

    def get_market_probability(self, local_probability: int = 15) -> dict[str, int]:
        return super().get_market_probability(local_probability)

