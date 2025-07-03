from Banks.Bank import Bank
from Cursors import Cursors
from Recorder import Recorder


class RecordBanks(Recorder):
    def __init__(self):
        self.banks = [
            Bank("ВОЛГА", "ВЛГ", "Саратов"),
            Bank("ЕНИСЕЙ", "ЕНС", "Красноярск"),
            Bank("ОБЬ", "ОБЬ", "Новосибирск"),
            Bank("АМУР", "АМР", "Хабаровск"),
            Bank("НЕВА", "НЕВ", "Санкт-Петербург")
        ]

    def record(self, cursors: Cursors):
        for bank in self.banks:
            bank.record(cursors.cursor)
