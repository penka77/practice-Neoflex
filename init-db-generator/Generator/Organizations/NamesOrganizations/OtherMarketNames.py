from Organizations.NamesOrganizations.OrganizationNames import OrganizationNames, Organization


class OtherMarketNames(OrganizationNames):
    def __init__(self):
        super().__init__()

    def get_mcc(self) -> list[int]:
        return [5310, 5651]

    def _init_mcc(self) -> list[int]:
        return [5310, 5651]

    def _init_store_chain(self) -> list[Organization]:
        return [Organization("ПРО100", "budget", 100)]

    def _init_city_store_chain(self) -> dict[str, list[Organization]]:
        return {
            "Саратов": [],
            "Нижний Новгород": [],
            "Москва": [],
            "Санкт-Петербург": [],
            "Пятигорск": [],
            "Ялта": [],
            "Челябинск": [],
            "Екатеринбург": [],
            "Новосибирск": [],
            "Красноярск": [],
            "Владивосток": [],
            "Хабаровск": []
        }

    def get_market_probability(self, local_probability: int = 0) -> dict[str, int]:
        return super().get_market_probability(local_probability)
