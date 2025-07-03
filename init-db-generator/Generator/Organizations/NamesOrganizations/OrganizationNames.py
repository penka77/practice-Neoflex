class Organization:
    # класс хранит в себе имя организации, её целевую аудиторию и вероятность генерации организации
    def __init__(self, name: str, type_budget: str, probability: int):
        self.name = name
        self.type_budget = type_budget
        self.probability = probability


class OrganizationNames:
    def __init__(self):
        self.mcc = self._init_mcc()
        self.store_chain = self._init_store_chain()
        self.city_store_chain = self._init_city_store_chain()

    def get_mcc(self) -> list[int]: pass
    def _init_mcc(self) -> list[int]: pass
    def _init_store_chain(self) -> list[Organization]: pass
    def _init_city_store_chain(self) -> dict[str, list[Organization]]: pass

    def get_all_market_names(self) -> list[str]:
        return self.get_local_market_names() + self.get_without_local_market_names()

    def get_local_market_names(self) -> list[str]:
        markets = list(map(lambda x: [market.name for market in x], self.city_store_chain.values()))
        return sum(markets, [])

    def get_without_local_market_names(self) -> list[str]:
        return list(map(lambda x: x.name, self.store_chain))

    def get_name_market_from_city(self, city: str) -> list[str]:
        return list(map(lambda x: x.name, self.city_store_chain[city]))

    def get_market_probability(self, local_probability: int = 0) -> dict[str, int]:
        result = {"local": local_probability}

        for market in self.store_chain:
            result[market.name] = market.probability

        return result

    def get_market_type_budget(self, market: str) -> str:
        organization = list(
            filter(lambda x: x.name == market, self.store_chain + sum(list(self.city_store_chain.values()), []))
        )[0]

        return organization.type_budget

