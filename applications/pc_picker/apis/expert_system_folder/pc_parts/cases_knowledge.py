from .....dashboard.models import Case
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS

class CasesKnowledge(PCKnowledge):
    def __get_case(self,budget):
        cases = Case.filter_objects(price__lte=budget).order_by('-price')
        if len(cases) == 0:
            cases = Case.filter_objects(price__gte=budget).order_by('price')
        return None if len(cases) == 0 else cases[0]

    @Rule(AS.rule << InputFact())
    def get_case(self, rule):
        budget = rule['budget']

        return self.__get_case(budget)