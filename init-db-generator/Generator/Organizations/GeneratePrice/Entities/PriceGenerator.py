from Organizations.GeneratePrice.Entities.NomenclatureMarket import NomenclatureMarket
from Organizations.GeneratePrice.Entities.Fields.Product import Product
from Organizations.GeneratePrice.Entities.CoeffMarkets import CoeffMarkets
from Organizations.NamesOrganizations.OrganizationNames import OrganizationNames
from Organizations.NamesOrganizations.SuperMarketNames import SuperMarketNames


class PriceGenerator:
    def __init__(self, markets: OrganizationNames, nomenclature: NomenclatureMarket, coeff_markets: CoeffMarkets):
        # nomenclature - список позиций для магазинов и цены
        # markets - позиции в конкретном магазине и коэфф.
        self.nomenclature = nomenclature
        self.coeff_markets = coeff_markets
        self.markets = markets.get_all_market_names()
        self.prices = self.__prices()

    def __prices(self) -> dict[str, list[Product]]:
        result = {market: [] for market in self.markets}

        # идём по позициям в чеках(молоко, хлеб и т.д)
        # type_product - позиция в чеке(молоко, хлеб и т.д)
        # positions_in_supermarket - словарь с информацией о коэфф. для конкретных позиций в магазинах
        for type_product, positions_in_supermarket in self.coeff_markets.positions.items():
            # supermarket - название магазина
            # products - словарь с информацией о коэфф. для конкретных позиций в магазине
            for supermarket, products in positions_in_supermarket.items():
                # product- наименование позиции
                # coeff - коэфф. на позицию для магазина supermarket
                for product_name, coeff in products.items():
                    product = list(
                        filter(lambda x: x.name == product_name, self.nomenclature.products[type_product])
                    )[0]

                    result[supermarket].append(
                        Product(
                            product_name, product.type_product, product.type_budget,
                            round(product.price * coeff, 2), product.barcode
                        )
                    )

        return result
