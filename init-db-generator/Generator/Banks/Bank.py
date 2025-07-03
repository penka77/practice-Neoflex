import random
import uuid
from datetime import date, timedelta

from psycopg2._psycopg import cursor

from Cities import Cities


class Bank:
    def __init__(self, name: str, abbreviation: str, city: str):
        self.id = uuid.uuid4().__str__()
        self.name = name
        self.abbreviation = abbreviation
        self.inn = self.__init_inn()
        self.ogrn = self.__init_ogrn()
        self.bik = self.__init_bik()
        self.phone = self.__init_phone()
        self.date_open = self.__init_date().__str__()
        self.head_office = Cities().generate_address(city)

    def __init_date(self) -> date:
        start_date = date(2000, 1, 1)
        end_date = date(2005, 1, 1)
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        return start_date + timedelta(days=random_days)

    def __init_inn(self) -> str:
        return str(random.randint(7000000000, 7999999999))

    def __init_ogrn(self) -> str:
        return str(random.randint(10000000000000, 19999999999999))

    def __init_bik(self) -> str:
        return f"0{random.randint(40000000, 49999999)}"

    def __init_phone(self) -> str:
        return f"8-800-{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"

    def record(self, cursor: cursor):
        self.__check_unique(cursor)
        columns = "(id, name, abbreviation, inn, ogrn, bik, phone, date_open, head_office)"

        values = (f"('{self.id}', '{self.name}', '{self.abbreviation}', '{self.inn}', '{self.ogrn}', '{self.bik}', "
                  f"'{self.phone}', '{self.date_open}', '{self.head_office}')")
        insert_query = f"""INSERT INTO data.banks {columns} VALUES {values}"""

        cursor.execute(insert_query)

    def __check_unique(self, cursor: cursor):
        def check(field_name: str, field: str) -> list:
            cursor.execute(f"select * from data.banks where {field_name} = '{field}'")
            return cursor.fetchall()

        check_id = check("id", self.id)

        while check_id:
            self.id = uuid.uuid4().__str__()
            check_id = check("id", self.id)

        check_inn = check("inn", self.inn)

        while check_inn:
            self.inn = self.__init_inn()
            check_inn = check("inn", self.inn)

        check_ogrn = check("ogrn", self.ogrn)

        while check_ogrn:
            self.ogrn = self.__init_ogrn()
            check_ogrn = check("ogrn", self.ogrn)

        check_bik = check("ogrn", self.bik)

        while check_bik:
            self.bik = self.__init_bik()
            check_bik = check("bik", self.bik)

        check_phone = check("phone", self.phone)

        while check_phone:
            self.bik = self.__init_phone()
            check_phone = check("phone", self.phone)