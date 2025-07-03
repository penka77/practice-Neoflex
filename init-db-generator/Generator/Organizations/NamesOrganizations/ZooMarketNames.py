from Organizations.NamesOrganizations.OrganizationNames import OrganizationNames, Organization


class ZooMarketNames(OrganizationNames):
    def __init__(self):
        super().__init__()

    def get_mcc(self) -> list[int]:
        return [5995, 742]

    def _init_mcc(self) -> list[int]:
        return [5995, 742]

    def _init_store_chain(self) -> list[Organization]:
        return [
            Organization("ВанПачКэт", "budget", 23),
            Organization("Шаман Пэт", "budget", 22),
            Organization("Унесённые лакомствами", "middle", 15),
            Organization("Пэтангелион", "premium", 5),
            Organization("Бобик в гостях у Барбоса", "middle", 5)
        ]

    def _init_city_store_chain(self) -> dict[str, list[Organization]]:
        return {
            "Саратов": [Organization("Очень приятно, Плюша!", "middle", 100)],
            "Нижний Новгород": [Organization("Мой счастливый Котофей", "middle", 100)],
            "Москва": [Organization("Бездомный Бобик", "middle", 100)],
            "Санкт-Петербург": [Organization("Атака Мухтаров", "middle", 100)],
            "Пятигорск": [Organization("Мой сосед Василий", "middle", 100)],
            "Ялта": [Organization("ХодячийZoo!", "middle", 100)],
            "Челябинск": [Organization("Усы, лапы, хвост", "middle", 100)],
            "Екатеринбург": [Organization("Восхождение героя лотка", "middle", 100)],
            "Новосибирск": [Organization("Мастера МЯУ Online", "middle", 100)],
            "Красноярск": [Organization("Джунгли зовут!", "middle", 100)],
            "Владивосток": [Organization("Коготь рассекающий крысу", "middle", 100)],
            "Хабаровск": [Organization("Кот в сапогах", "middle", 100)]
        }

    def get_market_probability(self, local_probability: int = 30) -> dict[str, int]:
        return super().get_market_probability(local_probability)
