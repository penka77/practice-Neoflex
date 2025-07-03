import datetime
import random
import uuid

from Cities import Cities
from Organizations.GenerateOrganization.Terminal import Terminal
from Organizations.NamesOrganizations.OrganizationNames import OrganizationNames

from psycopg2._psycopg import cursor


class Organization:
    def __init__(self, cities: Cities, organization_names: OrganizationNames, city: str = None):
        self.cities = cities
        self.__organization_names = organization_names

        self.id = uuid.uuid4().__str__()
        self.mcc = random.choice(self.__organization_names.mcc)
        self.city = city if city else random.choice(self.cities.cities)
        self.store_chain = self.__generate_store_chain(self.city)
        self.type_budget = self.__organization_names.get_market_type_budget(self.store_chain)
        self.address = self.cities.generate_address(city)
        self.date_open = self.__generate_date().__str__()
        self.date_close = "NULL"

    def __generate_date(self) -> datetime.date:
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date(2024, 1, 1)
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        return start_date + datetime.timedelta(days=random_days)

    def __generate_store_chain(self, city: str) -> str:
        probabilities = self.__organization_names.get_market_probability()
        r, sum = random.randint(0, 99), 0

        for market, probability in probabilities.items():
            if sum <= r < sum + probability:
                if market == "local":
                    local_r, local_sum = random.randint(0, 99), 0
                    for local_organization in self.__organization_names.city_store_chain[city]:
                        if local_sum <= local_r < local_sum + local_organization.probability:
                            return local_organization.name
                        local_sum += local_organization.probability
                return market
            sum += probability

    def record(self, cursor: cursor):
        self.__check_unique(cursor)
        columns = "(id, address, name_market, type_budget, mcc, date_open, date_close)"
        values = (f"('{self.id}', '{self.address}', '{self.store_chain}', '{self.type_budget}', {self.mcc}, "
                  f"'{self.date_open}', {self.date_close})")
        insert_query = f"""INSERT INTO data.organizations {columns} VALUES {values}"""

        cursor.execute(insert_query)

    def record_terminals(self, cursor: cursor):
        terminals = [Terminal(self.id) for _ in range(0, 3)]

        for terminal in terminals:
            terminal.record(cursor)

    def __check_unique(self, cursor: cursor):
        def check(field_name: str, field: str) -> list:
            cursor.execute(f"select * from data.organizations where {field_name} = '{field}'")
            return cursor.fetchall()

        check_id = check("id", self.id)

        while check_id:
            self.id = uuid.uuid4().__str__()
            check_id = check("id", self.id)
