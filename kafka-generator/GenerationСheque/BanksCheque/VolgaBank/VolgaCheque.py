import uuid

from BanksCheque.BankCheque import BankCheque


class VolgaCheque(BankCheque):
    bank_id = None

    def _generate_cheque(self) -> dict:
        return {
            "bank_id": VolgaCheque.bank_id,
            "client_info": {
                "card": f'**** **** {self.purchase.card["id"][-9:]}',
                "bank": self.purchase.card["bank"],
                "pay_system": self.purchase.card["payment_system"]
            },
            "market_info": {
                "terminal": self.purchase.terminal["id"],
                "transaction": f"VLG-{uuid.uuid4()}",
                "date": self._generate_date(),
                "market": self.purchase.market["id"],
                "mcc": self.purchase.market["mcc"],
                "address": self.purchase.market["address"]
            },
            "products": list(map(lambda x: self._create_purchases(x), self.purchase.purchaces))
        }

    def _create_purchases(self, purchase: dict) -> dict:
        return {
            "name": purchase["position_name"],
            "budget": purchase["type_budget"],
            "price": purchase["price"],
            "product_type": purchase["type_product"]
        }

    def _set_topic(self) -> str:
        return "volga_topic"

    @staticmethod
    def set_bank_id():
        VolgaCheque.bank_id = BankCheque._bank_id("ВОЛГА")
