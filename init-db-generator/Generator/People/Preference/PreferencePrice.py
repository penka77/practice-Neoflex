class PreferencePrice:
    def __init__(self, preference: int, budget: int | None, middle: int | None, premium: int | None):
        self.preference = preference
        # Если поле равно нулю, то это остаток, если None не рассматривается
        self.budget = budget
        self.middle = middle
        self.premium = premium

    def to_dict(self) -> dict[str, int | None]:
        return {
            "preference": self.preference,
            "budget": self.budget,
            "middle": self.middle,
            "premium": self.premium
        }

    def __str__(self):
        return self.to_dict().__str__()