import random
import uuid
from math import ceil
from random import randint, choice
from datetime import date, timedelta
from psycopg2._psycopg import cursor

from Cities import Cities
from Cursors import Cursors
from People.Card import Card
from People.Preference.PreferencePriceGroup import PreferencePriceGroup
from People.Preference.PreferencePriceHuman import PreferencePriceHuman


class Human:
    def __init__(self, city: str = None):
        self.id = uuid.uuid4().__str__()
        self.gender = random.choice(["муж", "жен"])
        self.birthday = self.__init_birthday()
        self.cities = Cities()
        self.city = city if city else choice(self.cities.cities)

        self.cards = self.__init_cards()
        self.preferences = self.__init_preference(self._init_group_preference())

    def __init_birthday(self) -> date:
        date_range = self._date_range()
        delta = date_range["end_date"] - date_range["start_date"],
        random_days = randint(0, delta[0].days)

        return date_range["start_date"] + timedelta(days=random_days)

    def __init_cards(self) -> list[Card]:
        count_card = random.randint(1, 3)
        return [Card(self.id) for _ in range(0, count_card)]

    def __init_preference(self, preferences: dict[str, PreferencePriceGroup]) -> dict[str, PreferencePriceHuman]:
        coeff = self.cities.coeff_markets[self.city]

        pref_human = dict()
        pref_human["supermarket"] = self.__init_preference_segment(preferences["supermarket"], coeff["supermarket"])
        pref_human["build_market"] = self.__init_preference_segment(preferences["build_market"], coeff["build_market"])
        pref_human["cafe"] = self.__init_preference_segment(preferences["cafe"], coeff["cafe"])
        pref_human["zoo_market"] = self.__init_preference_segment(preferences["zoo_market"], coeff["zoo_market"])
        pref_human["pharmacy"] = self.__init_preference_segment(preferences["pharmacy"], coeff["pharmacy"])
        pref_human = self.__calculation_other(pref_human, preferences["other_market"])
        return pref_human

    def __init_preference_segment(self, preference_group: PreferencePriceGroup, coeff: float) -> PreferencePriceHuman:
        pref_with_coeff = preference_group.preference * coeff
        preference = randint(int(pref_with_coeff * 0.9), int(pref_with_coeff * 1.1))

        budget = 0
        middle = 0
        premium = 0

        if preference_group.budget is None:
            if preference_group.middle == 0:
                premium = randint(int(preference_group.premium * 0.9), int(preference_group.premium * 1.1))
                middle = 1000 - premium
            else:
                middle = randint(int(preference_group.middle * 0.9), int(preference_group.middle * 1.1))
                premium = 1000 - middle
        elif preference_group.middle is None:
            if preference_group.budget == 0:
                premium = randint(int(preference_group.premium * 0.9), int(preference_group.premium * 1.1))
                budget = 1000 - premium
            else:
                budget = randint(int(preference_group.budget * 0.9), int(preference_group.budget * 1.1))
                premium = 1000 - budget
        else:
            if preference_group.budget == 0:
                middle = randint(int(preference_group.middle * 0.9), int(preference_group.middle * 1.1))
                budget = 1000 - middle
            else:
                budget = randint(int(preference_group.budget * 0.9), int(preference_group.budget * 1.1))
                middle = 1000 - budget

        return PreferencePriceHuman(preference, budget, middle, premium)

    def __calculation_other(
            self, pref_human: dict[str, PreferencePriceHuman], preference: PreferencePriceGroup
    ) -> dict[str, PreferencePriceHuman]:
        def calc() -> int:
            return (1000 - pref_human["supermarket"].preference - pref_human["build_market"].preference -
                    pref_human["cafe"].preference - pref_human["zoo_market"].preference -
                    pref_human["pharmacy"].preference)

        preference_other = calc()

        if preference_other < 0:
            compensation = int(ceil(abs(preference_other / 5)))
            pref_human["supermarket"].preference = pref_human["supermarket"].preference - compensation
            pref_human["build_market"].preference = pref_human["build_market"].preference - compensation
            pref_human["cafe"].preference = pref_human["cafe"].preference - compensation
            pref_human["zoo_market"].preference = pref_human["zoo_market"].preference - compensation
            pref_human["pharmacy"].preference = pref_human["pharmacy"].preference - compensation

        pref_other = PreferencePriceHuman(calc(), 1000, 0, 0)
        pref_other.preference = calc()
        pref_human["other_market"] = pref_other
        return pref_human

    def _date_range(self) -> dict[str, date]:
        pass

    def _init_group_preference(self) -> dict[str, PreferencePriceGroup]:
        pass

    def record(self, cursors: Cursors):
        self.__check_unique(cursors.cursor_metrics)

        columns_for_metrics = "(id, city, supermarket, build_market, cafe, zoo_market, pharmacy, other_market)"
        values_for_metrics = (
            f"('{self.id}', "
            f"'{self.city}', "
            f"{self.preferences["supermarket"].preference}, "
            f"{self.preferences["build_market"].preference}, "
            f"{self.preferences["cafe"].preference}, "
            f"{self.preferences["zoo_market"].preference}, "
            f"{self.preferences["pharmacy"].preference}, "
            f"{self.preferences["other_market"].preference})"
        )
        insert_query = f"""INSERT INTO metrics.preferences {columns_for_metrics} VALUES {values_for_metrics}"""
        cursors.cursor_metrics.execute(insert_query)

        for table, preference in self.preferences.items():
            self.__record_preferences(cursors.cursor_metrics, table, preference)

        for card in self.cards:
            card.record(cursors.cursor)

        columns = "(id, gender, birthday)"
        values = f"('{self.id}', '{self.gender}', '{self.birthday}')"
        insert_query = f"""INSERT INTO data.peoples {columns} VALUES {values}"""
        cursors.cursor.execute(insert_query)

    def __record_preferences(self, cursor: cursor, table: str, preference: PreferencePriceHuman):
        columns = "(id, budget, middle, premium)"
        values = f"('{self.id}', {preference.budget}, {preference.middle}, {preference.premium})"

        insert_query = f"""INSERT INTO metrics.{table} {columns} VALUES {values}"""
        cursor.execute(insert_query)

    def __check_unique(self, cursor: cursor):
        def check(field_name: str, field: str) -> list:
            cursor.execute(f"select * from metrics.preferences where {field_name} = '{field}'")
            return cursor.fetchall()

        check_id = check("id", self.id)

        while check_id:
            self.id = uuid.uuid4().__str__()
            check_id = check("id", self.id)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "birthday": self.birthday.__str__(),
            "city": self.city,
            "preference": {key: value.to_dict() for key, value in self.preferences.items()}
        }

    def __str__(self) -> str:
        return self.to_dict().__str__()
