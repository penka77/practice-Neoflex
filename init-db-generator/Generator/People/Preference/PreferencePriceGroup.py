from People.Preference.PreferencePrice import PreferencePrice


class PreferencePriceGroup(PreferencePrice):
    def __init__(self, preference: int, budget: int | None, middle: int | None, premium: int | None):
        super().__init__(preference, budget, middle, premium)

