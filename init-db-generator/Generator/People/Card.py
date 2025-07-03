import random

from psycopg2._psycopg import cursor


class Card:
    def __init__(self, owner: str):
        self.number = self.__generate_number()
        self.owner = owner
        self.bank = random.choice(["ВОЛГА", "ЕНИСЕЙ", "ОБЬ", "АМУР", "НЕВА"])
        self.payment_system = random.choice(["БАЙКАЛ", "ЛАДОГА", "КАСПИЙ"])

    def __generate_number(self) -> str:
        def generate() -> str:
            num = random.randint(0, 9999)

            if num < 10:
                return f"000{num}"
            elif num < 100:
                return f"00{num}"
            elif num < 1000:
                return f"0{num}"
            else:
                return str(num)

        return f"{random.randint(1000, 9999)} {generate()} {generate()} {generate()}"

    def record(self, cursor: cursor):
        self.__check_unique(cursor)
        columns = "(number, owner, bank, payment_system)"

        values = f"('{self.number}', '{self.owner}', '{self.bank}', '{self.payment_system}')"
        insert_query = f"""INSERT INTO data.cards {columns} VALUES {values}"""

        cursor.execute(insert_query)

    def __check_unique(self, cursor: cursor):
        def check(field_name: str, field: str) -> list:
            cursor.execute(f"select * from data.cards where {field_name} = '{field}'")
            return cursor.fetchall()

        check_number = check("number", self.number)

        while check_number:
            self.number = self.__generate_number()
            check_number = check("number", self.number)
