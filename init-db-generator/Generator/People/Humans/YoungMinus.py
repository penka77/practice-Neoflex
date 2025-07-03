from People.Humans.Human import Human
from People.Preference.PreferencePriceGroup import PreferencePriceGroup

from datetime import date


class YoungMinus(Human):
    def _date_range(self) -> dict[str, date]:
        return {"start_date": date(2000, 1, 1), "end_date": date(2006, 1, 1)}

    def _init_group_preference(self) -> dict[str, PreferencePriceGroup]:
        return {
            "supermarket": PreferencePriceGroup(340, 800, 0, None),
            "build_market": PreferencePriceGroup(20, 900, 0, None),
            "cafe": PreferencePriceGroup(420, 850, 0, None),
            "zoo_market": PreferencePriceGroup(20, 900, 0, None),
            "pharmacy": PreferencePriceGroup(110, 900, 0, None),
            "other_market": PreferencePriceGroup(0, 100, 0, None)
        }
