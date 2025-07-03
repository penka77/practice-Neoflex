from People.Humans.Human import Human
from People.Preference.PreferencePriceGroup import PreferencePriceGroup

from datetime import date


class Pensioner(Human):
    def _date_range(self) -> dict[str, date]:
        return {"start_date": date(1958, 1, 1), "end_date": date(1963, 12, 31)}

    def _init_group_preference(self) -> dict[str, PreferencePriceGroup]:
        return {
            "supermarket": PreferencePriceGroup(500, 700, 200, None),
            "build_market": PreferencePriceGroup(100, 500, 450, None),
            "cafe": PreferencePriceGroup(50, 700, 200, None),
            "zoo_market": PreferencePriceGroup(90, 400, 400, None),
            "pharmacy": PreferencePriceGroup(220, 600, 350, None),
            "other_market": PreferencePriceGroup(0, 100, 0, None)
        }
