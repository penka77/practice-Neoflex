from Cities import Cities
from Cursors import Cursors
from People.Humans.Young import Young
from People.Humans.MiddleAged import MiddleAged
from People.Humans.MiddleAgedPlus import MiddleAgedPlus
from People.Humans.Pensioner import Pensioner
from People.Humans.PreRetirement import PreRetirement
from People.Humans.PreRetirementPlus import PreRetirementPlus
from People.Humans.YoungMinus import YoungMinus
from People.Humans.YoungPlus import YoungPlus
from Recorder import Recorder


class RecordHumans(Recorder):
    def __init__(self):
        self.cities = Cities()

    def record(self, cursors: Cursors):
        for city, population in self.cities.population.items():
            for age, count in population.items():
                for _ in range(count):
                    if age == "young-":
                        YoungMinus(city).record(cursors)
                    elif age == "young":
                        Young(city).record(cursors)
                    elif age == "young+":
                        YoungPlus(city).record(cursors)
                    elif age == "middle":
                        MiddleAged(city).record(cursors)
                    elif age == "middle+":
                        MiddleAgedPlus(city).record(cursors)
                    elif age == "preretirement":
                        PreRetirement(city).record(cursors)
                    elif age == "preretirement+":
                        PreRetirementPlus(city).record(cursors)
                    elif age == "pensioner":
                        Pensioner(city).record(cursors)
