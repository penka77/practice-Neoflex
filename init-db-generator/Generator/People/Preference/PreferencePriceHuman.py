from People.Preference.PreferencePrice import PreferencePrice


class PreferencePriceHuman(PreferencePrice):
    def __init__(self, preference: int, budget: int, middle: int, premium: int):
        super().__init__(preference, budget, middle, premium)
