from People.Humans.Human import Human
from People.Preference.PreferencePriceGroup import PreferencePriceGroup

from datetime import date


class Young(Human):
    def _date_range(self) -> dict[str, date]:
        return {"start_date": date(1994, 1, 1), "end_date": date(1999, 12, 31)}

    def _init_group_preference(self) -> dict[str, PreferencePriceGroup]:
        return {
            "supermarket": PreferencePriceGroup(340, 280, 630, None),
            "build_market": PreferencePriceGroup(90, 700, 100, None),
            "cafe": PreferencePriceGroup(270, 230, 670, None),
            "zoo_market": PreferencePriceGroup(50, 200, 700, None),
            "pharmacy": PreferencePriceGroup(130, 300, 550, None),
            "other_market": PreferencePriceGroup(0, 100, 0, None)
        }
