from Cities import Cities
from Cursors import Cursors
from Organizations.GeneratePrice.Entities.BuildMarket.CoeffBuildMarket import CoeffBuildMarket
from Organizations.GeneratePrice.Entities.BuildMarket.NomenclatureBuildMarket import NomenclatureBuildMarket
from Organizations.GeneratePrice.Entities.CafeMarket.CoeffCafeMarket import CoeffCafeMarket
from Organizations.GeneratePrice.Entities.CafeMarket.NomenclatureCafeMarket import NomenclatureCafeMarket
from Organizations.GeneratePrice.Entities.OtherMarket.CoeffOtherMarket import CoeffOtherMarket
from Organizations.GeneratePrice.Entities.OtherMarket.NomenclatureOtherMarket import NomenclatureOtherMarket
from Organizations.GeneratePrice.Entities.PharmacyMarket.CoeffPharmacyMarket import CoeffPharmacyMarket
from Organizations.GeneratePrice.Entities.PharmacyMarket.NomenclaturePharmacyMarket import NomenclaturePharmacyMarket

from Organizations.GeneratePrice.Entities.PriceGenerator import PriceGenerator
from Organizations.GeneratePrice.Entities.SuperMarket.CoeffSuperMarket import CoeffSuperMarket
from Organizations.GeneratePrice.Entities.SuperMarket.NomenclatureSuperMarket import NomenclatureSuperMarket

from psycopg2._psycopg import cursor

from Organizations.GeneratePrice.Entities.ZooMarket.CoeffZooMarket import CoeffZooMarket
from Organizations.GeneratePrice.Entities.ZooMarket.NomenclatureZooMarket import NomenclatureZooMarket
from Organizations.NamesOrganizations.BuildMarketNames import BuildMarketNames
from Organizations.NamesOrganizations.CafeMarketNames import CafeMarketNames
from Organizations.NamesOrganizations.OtherMarketNames import OtherMarketNames
from Organizations.NamesOrganizations.PharmacyMarketNames import PharmacyMarketNames
from Organizations.NamesOrganizations.SuperMarketNames import SuperMarketNames
from Organizations.NamesOrganizations.ZooMarketNames import ZooMarketNames
from Recorder import Recorder


class RecordPrice(Recorder):
    def __init__(self):
        self.cities = Cities()
        self.super_market = PriceGenerator(SuperMarketNames(), NomenclatureSuperMarket(), CoeffSuperMarket())
        self.build_market = PriceGenerator(BuildMarketNames(), NomenclatureBuildMarket(), CoeffBuildMarket())
        self.cafe_market = PriceGenerator(CafeMarketNames(), NomenclatureCafeMarket(), CoeffCafeMarket())
        self.pharmacy_market = PriceGenerator(PharmacyMarketNames(), NomenclaturePharmacyMarket(), CoeffPharmacyMarket())
        self.zoo_market = PriceGenerator(ZooMarketNames(), NomenclatureZooMarket(), CoeffZooMarket())
        self.other_market = PriceGenerator(OtherMarketNames(), NomenclatureOtherMarket(), CoeffOtherMarket())

    def record(self, cursors: Cursors):
        self.__record_prices(cursors.cursor_metrics, self.super_market)
        self.__record_prices(cursors.cursor_metrics, self.build_market)
        self.__record_prices(cursors.cursor_metrics, self.cafe_market)
        self.__record_prices(cursors.cursor_metrics, self.pharmacy_market)
        self.__record_prices(cursors.cursor_metrics, self.zoo_market)
        self.__record_prices(cursors.cursor_metrics, self.other_market)

    def __record_prices(self, cursor: cursor, generator: PriceGenerator):
        for market, positions in generator.prices.items():
            for position in positions:
                columns = "(name_market, position_name, barcode, type_product, type_budget, price)"
                values = f"('{market}', '{position.name}', '{position.barcode.__str__()}', '{position.type_product}', '{position.type_budget}', '{position.price}')"
                insert_query = f"""INSERT INTO metrics.market_prices {columns} VALUES {values}"""
                cursor.execute(insert_query)

