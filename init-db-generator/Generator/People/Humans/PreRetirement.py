from People.Humans.Human import Human
from People.Preference.PreferencePriceGroup import PreferencePriceGroup

from datetime import date


class PreRetirement(Human):
    def _date_range(self) -> dict[str, date]:
        return {"start_date": date(1970, 1, 1), "end_date": date(1975, 12, 31)}

    def _init_group_preference(self) -> dict[str, PreferencePriceGroup]:
        return {
            "supermarket": PreferencePriceGroup(430, 200, 600, None),
            "build_market": PreferencePriceGroup(160, 80, 750, None),
            "cafe": PreferencePriceGroup(140, 120, 620, None),
            "zoo_market": PreferencePriceGroup(80, 300, 500, None),
            "pharmacy": PreferencePriceGroup(160, 80, 600, None),
            "other_market": PreferencePriceGroup(0, 100, 0, None)
        }
