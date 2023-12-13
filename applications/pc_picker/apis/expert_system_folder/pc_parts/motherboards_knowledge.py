from .....dashboard import models as models_dashboard
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS

class MotherboardsKnowledge(PCKnowledge):
    @Rule(AS.rule << InputFact(part='motherboard'))
    def get_motherboard(self, rule):
        Q_query = rule['Q_query']
        budget = rule['budget']

        if Q_query != None:
            motherboards = models_dashboard.Motherboard.filter_objects(Q_query, price__lte=budget).order_by('-price')
            if len(motherboards) == 0:
                motherboards = models_dashboard.Motherboard.filter_objects(Q_query, price__gte=budget).order_by('price')
            return None if len(motherboards) == 0 else motherboards[0]
        else:
            motherboards = models_dashboard.Motherboard.filter_objects(price__lte=budget).order_by('-price')
            if len(motherboards) == 0:
                motherboards = models_dashboard.Motherboard.filter_objects(price__gte=budget).order_by('price')
            return None if len(motherboards) == 0 else motherboards[0]