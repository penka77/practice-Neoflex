from Banks.RecordBanks import RecordBanks
from Cursors import Cursors
from Organizations.GenerateOrganization.RecordOrganization import RecordOrganization
from Organizations.GeneratePrice.RecordPrice import RecordPrice
from People.RecordHumans import RecordHumans
from Recorder import Recorder


class RecordInformation(Recorder):
    def __init__(self):
        self.banks_recorder = RecordBanks()
        self.organizations_recorder = RecordOrganization()
        self.prices_recorder = RecordPrice()
        self.humans_recorder = RecordHumans()

    def record(self, cursors: Cursors):
        self.banks_recorder.record(cursors)
        print("Запись банков завершена!")

        self.organizations_recorder.record(cursors)
        print("Запись организаций завершена!")

        self.prices_recorder.record(cursors)
        print("Запись цен завершена!")

        self.humans_recorder.record(cursors)
        print("Запись людей завершена!")

        print("Запись завершена!")
