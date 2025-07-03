import random

from Cursors import Cursors


class Purchase:
    __cursors: Cursors = None

    @staticmethod
    def set_cursors(cursors: Cursors):
        Purchase.__cursors = cursors

    def get_cursors(self) -> Cursors:
        return Purchase.__cursors

    def __init__(self):
        self.human = self.__read_human()
        self.card = self.__get_card(self.human["id"])
        market_type, self.market = self.__choice_market()
        self.terminal = self.__get_terminal(self.market["id"])
        self.purchaces = self.__get_positions_purchase(market_type, self.market["name_market"])

    def __read_human(self) -> dict:
        schema = ["id", "city", "supermarket", "build_market", "cafe", "zoo_market", "pharmacy", "other_market"]
        query = "SELECT * FROM metrics.preferences ORDER BY random() * extract(epoch FROM now()) limit 1"
        cursor = self.get_cursors().cursor_metrics
        cursor.execute(query)
        return dict(zip(schema, cursor.fetchall()[0]))

    def __get_card(self, id_human: str) -> dict:
        schema = ["id", "owner", "bank", "payment_system"]
        query = (f"SELECT * FROM data.cards "
                 f"where owner = '{id_human}' "
                 f"ORDER BY random() * extract(epoch FROM now()) limit 1")
        cursor = self.get_cursors().cursor
        cursor.execute(query)
        return dict(zip(schema, cursor.fetchall()[0]))

    def __choice_market(self) -> (str, dict):
        choice = random.randint(0, 1000)
        if choice <= self.human["supermarket"]:
            return "supermarket", self.__choice_market_from_type_budget("supermarket")

        build_choice = self.human["supermarket"] + self.human["build_market"]
        if choice <= build_choice:
            return "build_market", self.__choice_market_from_type_budget("build_market")

        cafe_choice = build_choice + self.human["cafe"]
        if choice <= cafe_choice:
            return "cafe", self.__choice_market_from_type_budget("cafe")

        zoo_choice = cafe_choice + self.human["zoo_market"]
        if choice <= zoo_choice:
            return "zoo_market", self.__choice_market_from_type_budget("zoo_market")

        pharmacy_choice = zoo_choice + self.human["pharmacy"]
        if choice <= pharmacy_choice:
            return "pharmacy", self.__choice_market_from_type_budget("pharmacy")
        else:
            return "other_market", self.__choice_market_from_type_budget("other_market")

    def __choice_market_from_type_budget(self, market_type: str):
        schema = ["budget", "middle", "premium"]
        schema_to_query = ", ".join(schema)
        query = f"SELECT {schema_to_query} FROM metrics.{market_type} where id = '{self.human["id"]}'"
        cursor = self.get_cursors().cursor_metrics
        cursor.execute(query)
        metrics = dict(zip(schema, cursor.fetchall()[0]))

        choice = random.randint(0, 1000)

        if choice <= metrics["budget"]:
            return self.__choice_organization(market_type, "budget")
        elif choice <= metrics["budget"] + metrics["middle"]:
            return self.__choice_organization(market_type, "middle")
        else:
            return self.__choice_organization(market_type, "premium")

    def __choice_organization(self, market_type: str, budget: str) -> dict:
        mcc_list = {
            "supermarket": "(5411, 5499)",
            "build_market": "(5200, 5211)",
            "cafe": "(5814, 5811)",
            "zoo_market": "(5995, 742)",
            "pharmacy": "(5912, 5122)",
            "other_market": "(5310, 5651)"
        }

        mcc = mcc_list[market_type]
        schema = ["id", "address", "name_market", "type_budget", "mcc", "date_open", "date_close"]
        query = (f"SELECT * FROM data.organizations "
                 f"where mcc in {mcc} and type_budget = '{budget}' and address like '%{self.human["city"]}%' "
                 f"ORDER BY random() * extract(epoch FROM now()) limit 1")
        cursor = self.get_cursors().cursor
        cursor.execute(query)
        return dict(zip(schema, cursor.fetchall()[0]))

    def __get_terminal(self, id_market: str) -> dict:
        schema = ["id", "market", "bank", "imei", "os"]
        query = (f"SELECT * FROM metrics.terminals "
                 f"where market = '{id_market}' "
                 f"ORDER BY random() * extract(epoch FROM now()) limit 1")
        cursor = self.get_cursors().cursor_metrics
        cursor.execute(query)
        return dict(zip(schema, cursor.fetchall()[0]))

    def __get_positions_purchase(self, market_type: str, market_name: str) -> list[dict]:
        count_positions = {
            "supermarket": 10,
            "build_market": 6,
            "cafe": 4,
            "zoo_market": 4,
            "pharmacy": 5,
            "other_market": 6
        }

        schema = ["name_market", "position_name", "barcode", "type_product", "type_budget", "price"]
        query = (f"SELECT * FROM metrics.market_prices "
                 f"where name_market = '{market_name}' "
                 f"ORDER BY random() * extract(epoch FROM now()) "
                 f"limit {random.randint(1, count_positions[market_type])}")
        cursor = self.get_cursors().cursor_metrics
        cursor.execute(query)
        return list(map(lambda x: dict(zip(schema, x)), cursor.fetchall()))
