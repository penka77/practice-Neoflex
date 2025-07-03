from Organizations.NamesOrganizations.OrganizationNames import OrganizationNames, Organization


class CafeMarketNames(OrganizationNames):
    def __init__(self):
        super().__init__()

    def get_mcc(self) -> list[int]:
        return [5814, 5811]

    def _init_mcc(self) -> list[int]:
        return [5814, 5811]

    def _init_store_chain(self) -> list[Organization]:
        return [Organization("Вкусная точка", "middle", 8)]

    def _init_city_store_chain(self) -> dict[str, list[Organization]]:
        return {
            "Саратов": self.__init_saratov_store_chain(),
            "Нижний Новгород": self.__init_nn_store_chain(),
            "Москва": self.__init_moscow_store_chain(),
            "Санкт-Петербург": self.__init_spb_store_chain(),
            "Пятигорск": self.__init_pyatigorsk_store_chain(),
            "Ялта": self.__init_yalta_store_chain(),
            "Челябинск": self.__init_chelybinsk_store_chain(),
            "Екатеринбург": self.__init_ekb_store_chain(),
            "Новосибирск": self.__init_novosibirsk_store_chain(),
            "Красноярск": self.__init_krasnoyarsk_store_chain(),
            "Владивосток": self.__init_vladivostok_store_chain(),
            "Хабаровск": self.__init_khabarovsk_store_chain()
        }

    def __init_saratov_store_chain(self) -> list[Organization]:
        return [
            Organization("Шаурмичка", "budget", 100),
            Organization("Столовая №1", "budget", 100),
            Organization("ОГО!", "middle", 100),
            Organization("Семейное", "middle", 100),
            Organization("Премиум", "premium", 100)
        ]

    def __init_nn_store_chain(self) -> list[Organization]:
        return [
            Organization("Шаурmoney", "budget", 100),
            Organization("Как у Мамы", "budget", 100),
            Organization("АнтиКаф", "middle", 100),
            Organization("Пицц", "middle", 100),
            Organization("Origato", "premium", 100)
        ]

    def __init_moscow_store_chain(self) -> list[Organization]:
        return [
            Organization("Шаурмейстер", "budget", 100),
            Organization("Столовка", "budget", 100),
            Organization("Ролик", "middle", 100),
            Organization("Пиццкин", "middle", 100),
            Organization("Метрополь", "premium", 100)
        ]

    def __init_spb_store_chain(self) -> list[Organization]:
        return [
            Organization("Шаверма", "budget", 100),
            Organization("Советская столовая", "budget", 100),
            Organization("Царские роллы", "middle", 100),
            Organization("Pizzza", "middle", 100),
            Organization("ЛенинГРАД", "premium", 100)
        ]

    def __init_pyatigorsk_store_chain(self) -> list[Organization]:
        return [
            Organization("Это КАВКАЗ!", "budget", 100),
            Organization("У Бабули", "budget", 100),
            Organization("Лермонтоff", "middle", 100),
            Organization("Канатка", "middle", 100),
            Organization("У Машука", "premium", 100)
        ]

    def __init_yalta_store_chain(self) -> list[Organization]:
        return [
            Organization("Поешь-Попей", "budget", 100),
            Organization("Уютненько", "budget", 100),
            Organization("Крым", "middle", 100),
            Organization("У моря", "middle", 100),
            Organization("Массандра", "premium", 100)
        ]

    def __init_chelybinsk_store_chain(self) -> list[Organization]:
        return [
            Organization("Класс!", "budget", 100),
            Organization("ЧерМет", "budget", 100),
            Organization("Лось", "middle", 100),
            Organization("Пицца-ролло", "middle", 100),
            Organization("Паназия", "premium", 100)
        ]

    def __init_ekb_store_chain(self) -> list[Organization]:
        return [
            Organization("Бургерная", "budget", 100),
            Organization("Исеть", "budget", 100),
            Organization("Италиано", "middle", 100),
            Organization("Азиано", "middle", 100),
            Organization("Sverdlovsk", "premium", 100)
        ]

    def __init_novosibirsk_store_chain(self) -> list[Organization]:
        return [
            Organization("Котлеткино", "budget", 100),
            Organization("Снег!", "budget", 100),
            Organization("Сибирские пельмени", "middle", 100),
            Organization("rock-n-roll", "middle", 100),
            Organization("Рёберная", "premium", 100)
        ]

    def __init_krasnoyarsk_store_chain(self) -> list[Organization]:
        return [
            Organization("ВКУСНО!", "budget", 100),
            Organization("Морозная тарелка", "budget", 100),
            Organization("Семейка", "middle", 100),
            Organization("Рыбки?", "middle", 100),
            Organization("Могучий Енисей", "premium", 100)
        ]

    def __init_vladivostok_store_chain(self) -> list[Organization]:
        return [
            Organization("Крабсбургер", "budget", 100),
            Organization("Салатница", "budget", 100),
            Organization("Чавыча", "middle", 100),
            Organization("Чао!", "middle", 100),
            Organization("Нихао", "premium", 100)
        ]

    def __init_khabarovsk_store_chain(self) -> list[Organization]:
        return [
            Organization("Посиделки", "budget", 100),
            Organization("Таёжное", "budget", 100),
            Organization("ФоБО!", "middle", 100),
            Organization("Кибимпаб", "middle", 100),
            Organization("5000", "premium", 100)
        ]

    def get_market_probability(self, local_probability: int = 92) -> dict[str, int]:
        return super().get_market_probability(local_probability)

