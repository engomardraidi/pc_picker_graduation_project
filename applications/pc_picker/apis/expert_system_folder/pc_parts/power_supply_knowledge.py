from .....dashboard.models import PowerSupply
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS

class PowerSuppliesKnowledge(PCKnowledge):
    def __get_power_supply(self,budget):
        power_supplies = PowerSupply.filter_objects(price__lte=budget).order_by('-price')
        if len(power_supplies) == 0:
            power_supplies = PowerSupply.filter_objects(price__gte=budget).order_by('price')
        return None if len(power_supplies) == 0 else power_supplies[0]

    @Rule(AS.rule << InputFact())
    def get_power_supply(self, rule):
        budget = rule['budget']

        return self.__get_power_supply(budget)