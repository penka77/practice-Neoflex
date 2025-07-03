import random
import uuid

from psycopg2._psycopg import cursor


class Terminal:
    def __init__(self, market: str):
        self.id = uuid.uuid4().__str__()
        self.market = market
        self.bank = random.choice(["ВОЛГА", "ЕНИСЕЙ", "ОБЬ", "АМУР", "НЕВА"])
        self.imei = str(random.randint(100000000000000, 999999999999999))
        self.os = random.choice(["РОСА ОС", "ДОЖДЬ ОС", "СНЕГ ОС"])

    def record(self, cursor: cursor):
        self.__check_unique(cursor)
        columns = "(id, market, bank, imei, os)"
        values = f"('{self.id}', '{self.market}', '{self.bank}', '{self.imei}', '{self.os}')"
        insert_query = f"""INSERT INTO metrics.terminals {columns} VALUES {values}"""

        cursor.execute(insert_query)

    def __check_unique(self, cursor: cursor):
        def check(field_name: str, field: str) -> list:
            cursor.execute(f"select * from metrics.terminals where {field_name} = '{field}'")
            return cursor.fetchall()

        check_id = check("id", self.id)

        while check_id:
            self.id = uuid.uuid4().__str__()
            check_id = check("id", self.id)

        check_imei = check("imei", self.imei)

        while check_imei:
            self.imei = str(random.randint(100000000000000, 999999999999999))
            check_imei = check("imei", self.imei)