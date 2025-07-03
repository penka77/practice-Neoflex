from People.Humans.Human import Human
from People.Preference.PreferencePriceGroup import PreferencePriceGroup

from datetime import date


class MiddleAgedPlus(Human):
    def _date_range(self) -> dict[str, date]:
        return {"start_date": date(1976, 1, 1), "end_date": date(1981, 12, 31)}

    def _init_group_preference(self) -> dict[str, PreferencePriceGroup]:
        return {
            "supermarket": PreferencePriceGroup(420, 100, 700, None),
            "build_market": PreferencePriceGroup(165, 100, 700, None),
            "cafe": PreferencePriceGroup(155, 120, 650, None),
            "zoo_market": PreferencePriceGroup(80, 190, 600, None),
            "pharmacy": PreferencePriceGroup(155, 50, 700, None),
            "other_market": PreferencePriceGroup(0, 100, 0, None)
        }
