import uuid
import datetime

from BanksCheque.BankCheque import BankCheque
from BanksCheque.Purchase import Purchase
from Connections import Connections
from Cursors import Cursors


class YeniseiCheque(BankCheque):
    bank_id = None

    def _generate_cheque(self) -> dict:
        return {
            "bank_id": YeniseiCheque.bank_id,
            "info_client": {
                "card": f'**** **** {self.purchase.card["id"][-9:]}',
                "bank": self.purchase.card["bank"],
                "pay_system": self.purchase.card["payment_system"]
            },
            "info_transaction": {
                "id_terminal": self.purchase.terminal["id"],
                "os_terminal": self.purchase.terminal["os"],
                "number_transaction": f"YNS-{uuid.uuid4()}",
                "datetime": self._generate_date()
            },
            "info_market": {
                "market": self.purchase.market["id"],
                "mcc": self.purchase.market["mcc"],
                "address": self.purchase.market["address"]
            },
            "list_orders": list(map(lambda x: self._create_purchases(x), self.purchase.purchaces))
        }

    def _create_purchases(self, purchase: dict) -> dict:
        return {
            "name_position": purchase["position_name"],
            "budget": purchase["type_budget"],
            "price": purchase["price"]
        }

    def _set_topic(self) -> str:
        return "yenisei_topic"

    @staticmethod
    def set_bank_id():
        YeniseiCheque.bank_id = BankCheque._bank_id("ЕНИСЕЙ")