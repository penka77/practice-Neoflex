from People.Humans.Human import Human
from People.Preference.PreferencePriceGroup import PreferencePriceGroup

from datetime import date


class MiddleAged(Human):
    def _date_range(self) -> dict[str, date]:
        return {"start_date": date(1982, 1, 1), "end_date": date(1987, 12, 31)}

    def _init_group_preference(self) -> dict[str, PreferencePriceGroup]:
        return {
            "supermarket": PreferencePriceGroup(400, 200, 700, None),
            "build_market": PreferencePriceGroup(150, 150, 700, None),
            "cafe": PreferencePriceGroup(200, 150, 650, None),
            "zoo_market": PreferencePriceGroup(70, 250, 500, None),
            "pharmacy": PreferencePriceGroup(150, 100, 700, None),
            "other_market": PreferencePriceGroup(0, 100, 0, None)
        }
