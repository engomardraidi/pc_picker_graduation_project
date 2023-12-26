from .....dashboard.models import Case
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS
import decimal

class CasesKnowledge(PCKnowledge):
    def __get_case(self, style_id, budget):
        cases = []
        perc = decimal.Decimal(0.03)

        while len(cases) == 0 and perc < 1:
            perc += decimal.Decimal(0.02)
            min_budget = budget - (budget * perc)
            max_budget = budget + (budget * perc)
            cases = Case.filter_objects(style=style_id, price__range=(min_budget, max_budget))

        closest_case = cases[0]
        abs_diff = abs(budget - closest_case.price)

        for case in cases:
            abs_value = abs(budget - case.price)
            if abs_diff > abs_value:
                abs_diff = abs_value
                closest_case = case

        return closest_case

    @Rule(AS.rule << InputFact(style_id=1))
    def get_standard_case(self, rule):
        style_id = rule['style_id']
        budget = rule['budget']

        return self.__get_case(style_id, budget)

    @Rule(AS.rule << InputFact(style_id=2))
    def get_gaming_case(self, rule):
        style_id = rule['style_id']
        budget = rule['budget']

        return self.__get_case(style_id, budget)