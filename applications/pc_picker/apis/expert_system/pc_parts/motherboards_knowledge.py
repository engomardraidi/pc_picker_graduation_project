from .....dashboard import models as models_dashboard
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS
import decimal

class MotherboardsKnowledge(PCKnowledge):
    @Rule(AS.rule << InputFact(part='motherboard'))
    def get_motherboard(self, rule):
        Q_query = rule['Q_query']
        budget = rule['budget']
        motherboards = []
        perc = decimal.Decimal(0.03)

        while len(motherboards) == 0 and perc < 2:
            perc += decimal.Decimal(0.02)
            min_budget = budget - (budget * perc)
            max_budget = budget + (budget * perc)
            if Q_query != None:
                motherboards = models_dashboard.Motherboard.filter_objects(Q_query, price__range=(min_budget, max_budget))
            else:
                motherboards = models_dashboard.Motherboard.filter_objects(price__range=(min_budget, max_budget))

        return motherboards