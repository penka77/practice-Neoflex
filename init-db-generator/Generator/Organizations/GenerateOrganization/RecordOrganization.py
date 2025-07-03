from psycopg2._psycopg import cursor

from Cities import Cities
from Cursors import Cursors
from Organizations.GenerateOrganization.Organization import Organization
from Organizations.NamesOrganizations.BuildMarketNames import BuildMarketNames
from Organizations.NamesOrganizations.CafeMarketNames import CafeMarketNames
from Organizations.NamesOrganizations.OrganizationNames import OrganizationNames
from Organizations.NamesOrganizations.OtherMarketNames import OtherMarketNames
from Organizations.NamesOrganizations.PharmacyMarketNames import PharmacyMarketNames
from Organizations.NamesOrganizations.SuperMarketNames import SuperMarketNames
from Organizations.NamesOrganizations.ZooMarketNames import ZooMarketNames
from Recorder import Recorder


class RecordOrganization(Recorder):
    def __init__(self):
        self.cities = Cities()

        self.supermarket = SuperMarketNames()
        self.build_market = BuildMarketNames()
        self.cafe_market = CafeMarketNames()
        self.pharmacy_market = PharmacyMarketNames()
        self.zoo_market = ZooMarketNames()
        self.other_market = OtherMarketNames()

    def __record_mcc(self, cursor: cursor):
        def insert_into(type_organization: str, list_mcc: list[int]):
            columns = "(mcc, type_organization)"

            for mcc in list_mcc:
                values = f"({mcc}, '{type_organization}')"
                insert_query = f"""INSERT INTO data.mcc {columns} VALUES {values}"""
                cursor.execute(insert_query)

        insert_into("Супермаркеты", self.supermarket.get_mcc())
        insert_into("Стройка, ремонт, сад", self.build_market.get_mcc())
        insert_into("Кафе", self.cafe_market.get_mcc())
        insert_into("Аптеки", self.pharmacy_market.get_mcc())
        insert_into("Зоотовары", self.zoo_market.get_mcc())
        insert_into("Разное", self.other_market.get_mcc())

    def record(self, cursors: Cursors):
        self.__record_mcc(cursors.cursor)

        def record_organizations(count: int, marketNames: OrganizationNames, city: str):
            for _ in range(count):
                market = Organization(self.cities, marketNames, city)
                market.record(cursors.cursor)
                market.record_terminals(cursors.cursor_metrics)

        for city in self.cities.cities:
            record_organizations(self.cities.score_markets[city]["other_market"], self.other_market, city)
            record_organizations(self.cities.score_markets[city]["build_market"], self.build_market, city)
            record_organizations(self.cities.score_markets[city]["cafe"], self.cafe_market, city)
            record_organizations(self.cities.score_markets[city]["pharmacy"], self.pharmacy_market, city)
            record_organizations(self.cities.score_markets[city]["zoo_market"], self.zoo_market, city)
            record_organizations(self.cities.score_markets[city]["supermarket"], self.supermarket, city)