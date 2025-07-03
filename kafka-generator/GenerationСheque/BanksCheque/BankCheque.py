import datetime
import random

from BanksCheque.Purchase import Purchase
from Cursors import Cursors


class BankCheque:
    __cursors: Cursors = None
    __start_date = datetime.datetime(2024, 1, 1, 8, 0, 0, 0)

    @staticmethod
    def set_cursors(cursors: Cursors):
        BankCheque.__cursors = cursors

    @staticmethod
    def get_cursors() -> Cursors:
        return BankCheque.__cursors

    def __init__(self, purchase: Purchase):
        self.purchase = purchase
        self.cheque = self._generate_cheque()
        self.topic = self._set_topic()

    def _generate_cheque(self) -> dict:
        pass

    def _set_topic(self) -> str:
        pass

    def _create_purchases(self, purchase: dict) -> dict:
        pass

    @staticmethod
    def _bank_id(name: str) -> str:
        query = f"SELECT id FROM data.banks where name = '{name}'"
        cursor = BankCheque.get_cursors().cursor
        cursor.execute(query)
        return cursor.fetchall()[0][0]

    @staticmethod
    def _set_bank_id():
        pass

    def _generate_date(self):
        new_date = BankCheque.__start_date + datetime.timedelta(
            minutes=random.randint(2, 17),
            seconds=random.randint(0, 60),
            microseconds=random.randint(0, 99) * 1000
        )

        if new_date.hour >= 22:
            tomorrow = (BankCheque.__start_date + datetime.timedelta(1)).date()
            BankCheque.__start_date = datetime.datetime(
                tomorrow.year, tomorrow.month, tomorrow.day, 8, 0, 0, 0
            )
        else:
            BankCheque.__start_date = new_date

        return str(new_date)[:-3]
