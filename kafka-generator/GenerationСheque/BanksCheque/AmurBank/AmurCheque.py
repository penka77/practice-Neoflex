import uuid

from BanksCheque.BankCheque import BankCheque


class AmurCheque(BankCheque):
    bank_id = None

    def _generate_cheque(self) -> dict:
        return {
            "bank_id": AmurCheque.bank_id,
            "info_client": {
                "card": f'**** **** {self.purchase.card["id"][-9:]}',
                "bank": self.purchase.card["bank"],
                "pay_system": self.purchase.card["payment_system"]
            },
            "info_transaction": {
                "terminal": self.purchase.terminal["id"],
                "transaction": f"AMR-{uuid.uuid4()}",
                "datetime": self._generate_date()
            },
            "info_market": {
                "market": self.purchase.market["id"],
                "mcc": self.purchase.market["mcc"],
                "address": self.purchase.market["address"]
            },
            "purchases": list(map(lambda x: self._create_purchases(x), self.purchase.purchaces))
        }

    def _create_purchases(self, purchase: dict) -> dict:
        return {
            "position": purchase["position_name"],
            "barcode": purchase["barcode"],
            "price": purchase["price"],
        }
        
    def _set_topic(self) -> str:
        return "amur_topic"

    @staticmethod
    def set_bank_id():
        AmurCheque.bank_id = BankCheque._bank_id("АМУР")