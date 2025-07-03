from People.Humans.Human import Human
from People.Preference.PreferencePriceGroup import PreferencePriceGroup

from datetime import date


class YoungPlus(Human):
    def _date_range(self) -> dict[str, date]:
        return {"start_date": date(1988, 1, 1), "end_date": date(1993, 12, 31)}

    def _init_group_preference(self) -> dict[str, PreferencePriceGroup]:
        return {
            "supermarket": PreferencePriceGroup(390, 250, 650, None),
            "build_market": PreferencePriceGroup(130, 200, 700, None),
            "cafe": PreferencePriceGroup(245, 200, 700, None),
            "zoo_market": PreferencePriceGroup(50, 400, 400, None),
            "pharmacy": PreferencePriceGroup(150, 200, 600, None),
            "other_market": PreferencePriceGroup(0, 100, None, None)
        }
