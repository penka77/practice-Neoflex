import uuid
import datetime

from BanksCheque.BankCheque import BankCheque
from BanksCheque.Purchase import Purchase
from Connections import Connections
from Cursors import Cursors


class ObCheque(BankCheque):
    bank_id = None

    def _generate_cheque(self) -> dict:
        return {
            "bank": ObCheque.bank_id,
            "transaction": f"OB-{uuid.uuid4()}",
            "transaction_time": self._generate_date(),
            "terminal_id": self.purchase.terminal["id"],
            "terminal_imei": self.purchase.terminal["imei"],
            "card": f'**** **** {self.purchase.card["id"][-9:]}',
            "card_bank": self.purchase.card["bank"],
            "payment_system": self.purchase.card["payment_system"],
            "market_data": {
                "market": self.purchase.market["id"],
                "name_market": self.purchase.market["name_market"],
                "mcc": self.purchase.market["mcc"],
                "address": self.purchase.market["address"]
            },
            "orders": list(map(lambda x: self._create_purchases(x), self.purchase.purchaces))
        }

    def _create_purchases(self, purchase: dict) -> dict:
        return {
            "position": purchase["position_name"],
            "category": purchase["type_budget"],
            "cost": purchase["price"],
            "barcode": purchase["barcode"],
            "type": purchase["type_product"]
        }

    def _set_topic(self) -> str:
        return "ob_topic"

    @staticmethod
    def set_bank_id():
        ObCheque.bank_id = BankCheque._bank_id("ОБЬ")