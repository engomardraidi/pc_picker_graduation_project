from .....dashboard.models import Case
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS
import decimal

class CasesKnowledge(PCKnowledge):
    def __get_case(self,budget):
        cases = []
        perc = decimal.Decimal(0.03)

        while len(cases) == 0 and perc < 1:
            perc += decimal.Decimal(0.02)
            min_budget = budget - (budget * perc)
            max_budget = budget + (budget * perc)
            cases = Case.filter_objects(price__range=(min_budget, max_budget))

        closest_case = cases[0]
        abs_diff = abs(budget - closest_case.price)

        for case in cases:
            abs_value = abs(budget - case.price)
            if abs_diff > abs_value:
                abs_diff = abs_value
                closest_case = case

        return closest_case

    @Rule(AS.rule << InputFact())
    def get_case(self, rule):
        budget = rule['budget']

        return self.__get_case(budget)