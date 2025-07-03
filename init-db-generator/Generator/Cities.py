import random


class Cities:
    def __init__(self):
        self.cities = [
            "Саратов", "Нижний Новгород", "Москва", "Санкт-Петербург", "Пятигорск",
            "Ялта", "Челябинск", "Екатеринбург", "Новосибирск", "Красноярск",
            "Владивосток", "Хабаровск"
        ]

        self.streets = [
            "Ленина", "Вишнёвая", "Речная", "Земляная", "Лесная", "Весенняя", "Летняя",
            "Осенняя", "Зимняя", "Дачная", "Октябрьская", "Бульварная", "Просёлочная",
            "Мирная", "Международная", "Косая", "Гагарина", "Пушкина", "Рабочая", "Советская",
            "Роз"
        ]

        self.score_markets = {
            "Саратов": {"supermarket": 150, "build_market": 120, "cafe": 50, "pharmacy": 40, "zoo_market": 20, "other_market": 10},
            "Нижний Новгород": {"supermarket": 210, "build_market": 168, "cafe": 70, "pharmacy": 56, "zoo_market": 29, "other_market": 14},
            "Москва": {"supermarket": 2175, "build_market": 1740, "cafe": 725, "pharmacy": 580, "zoo_market": 290, "other_market": 145},
            "Санкт-Петербург": {"supermarket": 840, "build_market": 672, "cafe": 280, "pharmacy": 225, "zoo_market": 112, "other_market": 56},
            "Пятигорск": {"supermarket": 45, "build_market": 36, "cafe": 20, "pharmacy": 12, "zoo_market": 10, "other_market": 3},
            "Ялта": {"supermarket": 15, "build_market": 12, "cafe": 15, "pharmacy": 4, "zoo_market": 10, "other_market": 1},
            "Челябинск": {"supermarket": 195, "build_market": 156, "cafe": 65, "pharmacy": 52, "zoo_market": 26, "other_market": 13},
            "Екатеринбург": {"supermarket": 255, "build_market": 204, "cafe": 85, "pharmacy": 68, "zoo_market": 34, "other_market": 17},
            "Новосибирск": {"supermarket": 273, "build_market": 219, "cafe": 91, "pharmacy": 73, "zoo_market": 37, "other_market": 19},
            "Красноярск": {"supermarket": 210, "build_market": 168, "cafe": 70, "pharmacy": 56, "zoo_market": 28, "other_market": 14},
            "Владивосток": {"supermarket": 105, "build_market": 84, "cafe": 35, "pharmacy": 28, "zoo_market": 14, "other_market": 7},
            "Хабаровск": {"supermarket": 113, "build_market": 90, "cafe": 38, "pharmacy": 30, "zoo_market": 15, "other_market": 8},
        }

        self.coeff_markets = {
            "Саратов": {"supermarket": 1, "build_market": 1, "cafe": 1, "pharmacy": 1, "zoo_market": 1, "other_market": 1},
            "Нижний Новгород": {"supermarket": 1, "build_market": 1, "cafe": 1, "pharmacy": 1, "zoo_market": 1.1, "other_market": 1},
            "Москва": {"supermarket": 0.95, "build_market": 1, "cafe": 1, "pharmacy": 0.95, "zoo_market": 1, "other_market": 1},
            "Санкт-Петербург": {"supermarket": 1, "build_market": 1, "cafe": 1, "pharmacy": 1.25, "zoo_market": 0.95, "other_market": 1},
            "Пятигорск": {"supermarket": 0.9, "build_market": 0.9, "cafe": 1.2, "pharmacy": 0.9, "zoo_market": 0.9, "other_market": 1},
            "Ялта": {"supermarket": 1.2, "build_market": 0.8, "cafe": 1.2, "pharmacy": 0.8, "zoo_market": 0.9, "other_market": 1},
            "Челябинск": {"supermarket": 0.9, "build_market": 1.1, "cafe": 1, "pharmacy": 1.1, "zoo_market": 0.9, "other_market": 1},
            "Екатеринбург": {"supermarket": 0.9, "build_market": 1.1, "cafe": 1, "pharmacy": 1.12, "zoo_market": 1.5, "other_market": 1},
            "Новосибирск": {"supermarket": 1.1, "build_market": 1.11, "cafe": 1, "pharmacy": 1.15, "zoo_market": 1, "other_market": 1},
            "Красноярск": {"supermarket": 1.11, "build_market": 1.1, "cafe": 1, "pharmacy": 1.16, "zoo_market": 1, "other_market": 1},
            "Владивосток": {"supermarket": 1.1, "build_market": 1.11, "cafe": 1, "pharmacy": 1.1, "zoo_market": 1, "other_market": 1},
            "Хабаровск": {"supermarket": 1.12, "build_market": 1.14, "cafe": 1, "pharmacy": 1.11, "zoo_market": 1, "other_market": 1},
        }

        self.population = {
            "Саратов": {
                "young-": 1503, "young": 1350, "young+": 1197, "middle": 1125, "middle+": 1125,
                "preretirement": 1053, "preretirement+": 900, "pensioner": 747
            },
            "Нижний Новгород": {
                "young-": 2004, "young": 1800, "young+": 1596, "middle": 1500, "middle+": 1500,
                "preretirement": 1404, "preretirement+": 1200, "pensioner": 996
            },
            "Москва": {
                "young-": 5000, "young": 4500, "young+": 3990, "middle": 3750, "middle+": 3750,
                "preretirement": 3500, "preretirement+": 3000, "pensioner": 2490
            },
            "Санкт-Петербург": {
                "young-": 3340, "young": 3000, "young+": 2660, "middle": 2500, "middle+": 2500,
                "preretirement": 2340, "preretirement+": 2000, "pensioner": 1660
            },
            "Пятигорск": {
                "young-": 334, "young": 300, "young+": 266, "middle": 250, "middle+": 250,
                "preretirement": 234, "preretirement+": 200, "pensioner": 166
            },
            "Ялта": {
                "young-": 125, "young": 112, "young+": 100, "middle": 94, "middle+": 94,
                "preretirement": 88, "preretirement+": 75, "pensioner": 62
            },
            "Челябинск": {
                "young-": 1954, "young": 1755, "young+": 1556, "middle": 1463, "middle+": 1463,
                "preretirement": 1367, "preretirement+": 1170, "pensioner": 971
            },
            "Екатеринбург": {
                "young-": 2555, "young": 2295, "young+": 2035, "middle": 1913, "middle+": 1913,
                "preretirement": 1790, "preretirement+": 1530, "pensioner": 1270
            },
            "Новосибирск": {
                "young-": 2722, "young": 2445, "young+": 2168, "middle": 2038, "middle+": 2037,
                "preretirement": 1907, "preretirement+": 1630, "pensioner": 1353
            },
            "Красноярск": {
                "young-": 2004, "young": 1800, "young+": 1596, "middle": 1500, "middle+": 1500,
                "preretirement": 1404, "preretirement+": 1200, "pensioner": 996
            },
            "Владивосток": {
                "young-": 1002, "young": 900, "young+": 798, "middle": 750, "middle+": 750,
                "preretirement": 702, "preretirement+": 600, "pensioner": 498
            },
            "Хабаровск": {
                "young-": 1086, "young": 975, "young+": 865, "middle": 813, "middle+": 812,
                "preretirement": 760, "preretirement+": 650, "pensioner": 540
            }
        }

    def generate_address(self, city: str) -> str:
        street = random.choice(self.streets)
        return f"{random.randint(100000, 999999)}, г. {city}, ул. {street}, д. {random.randint(1, 100)}"