import uuid
import datetime

from BanksCheque.BankCheque import BankCheque
from BanksCheque.Purchase import Purchase
from Connections import Connections
from Cursors import Cursors


class NevaCheque(BankCheque):
    bank_id = None

    def _generate_cheque(self) -> dict:
        return {
            "id_bank": NevaCheque.bank_id,
            "transaction": f"NV-{uuid.uuid4()}",
            "transaction_time": self._generate_date(),
            "terminal_id": self.purchase.terminal["id"],
            "terminal_os": self.purchase.terminal["os"],
            "card_number": f'**** **** {self.purchase.card["id"][-9:]}',
            "bank_card": self.purchase.card["bank"],
            "pay_system": self.purchase.card["payment_system"],
            "market_id": self.purchase.market["id"],
            "market_name": self.purchase.market["name_market"],
            "mcc": self.purchase.market["mcc"],
            "market_address": self.purchase.market["address"],
            "buys": list(map(lambda x: self._create_purchases(x), self.purchase.purchaces))
        }

    def _create_purchases(self, purchase: dict) -> dict:
        return {
            "position": purchase["position_name"],
            "category": purchase["type_budget"],
            "price": purchase["price"],
        }

    def _set_topic(self) -> str:
        return "neva_topic"

    @staticmethod
    def set_bank_id():
        NevaCheque.bank_id = BankCheque._bank_id("НЕВА")
