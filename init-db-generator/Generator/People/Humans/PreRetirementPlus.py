from People.Humans.Human import Human
from People.Preference.PreferencePriceGroup import PreferencePriceGroup

from datetime import date


class PreRetirementPlus(Human):
    def _date_range(self) -> dict[str, date]:
        return {"start_date": date(1964, 1, 1), "end_date": date(1969, 12, 31)}

    def _init_group_preference(self) -> dict[str, PreferencePriceGroup]:
        return {
            "supermarket": PreferencePriceGroup(440, 500, 350, None),
            "build_market": PreferencePriceGroup(155, 100, 720, None),
            "cafe": PreferencePriceGroup(100, 150, 650, None),
            "zoo_market": PreferencePriceGroup(90, 350, 450, None),
            "pharmacy": PreferencePriceGroup(170, 300, 500, None),
            "other_market": PreferencePriceGroup(0, 100, 0, None)
        }
