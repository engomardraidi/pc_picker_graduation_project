from .....dashboard.models import PowerSupply
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS
import decimal

class PowerSuppliesKnowledge(PCKnowledge):
    def __get_power_supply(self,budget):
        power_supplies = []
        perc = decimal.Decimal(0.03)

        while len(power_supplies) == 0 and perc < 1:
            perc += decimal.Decimal(0.02)
            min_budget = budget - (budget * perc)
            max_budget = budget + (budget * perc)
            power_supplies = PowerSupply.filter_objects(price__range=(min_budget, max_budget))

        closest_power_supplie = power_supplies[0]
        abs_diff = abs(budget - closest_power_supplie.price)

        for power_supplie in power_supplies:
            abs_value = abs(budget - power_supplie.price)
            if abs_diff > abs_value:
                abs_diff = abs_value
                closest_power_supplie = power_supplie
        
        return closest_power_supplie

    @Rule(AS.rule << InputFact())
    def get_power_supply(self, rule):
        budget = rule['budget']

        return self.__get_power_supply(budget)