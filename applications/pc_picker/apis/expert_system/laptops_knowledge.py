from .expert_system_abc import ExpertSystem
import decimal
from experta import Rule, AS
from ....dashboard.models import Laptop
from ..functions import get_laptop_as_json
from .input_fact import InputFact
import decimal

class LaptopsKnowledge(ExpertSystem):
    def __get_laptops(self, field_id, budget):
        perc = decimal.Decimal(0.03)
        laptops = []

        while len(laptops) < 5:
            perc += decimal.Decimal(0.03)
            min_budget = budget - (budget * perc)
            max_budget = budget + (budget * perc)
            laptops = Laptop.filter_objects(laptopuse__use__id=field_id, price__range=(min_budget, max_budget))

        return laptops

    @Rule(AS.rule << InputFact(field_id=1))
    def pick_laptop_for_home_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_laptops = self.__get_laptops(1, budget)
        laptops = []

        for laptop in list_laptops:
            laptops.append(get_laptop_as_json(laptop, budget))

        return laptops

    @Rule(AS.rule << InputFact(field_id=2))
    def pick_laptop_for_workstation_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_laptops = self.__get_laptops(2, budget)
        laptops = []

        for laptop in list_laptops:
            laptops.append(get_laptop_as_json(laptop, budget))

        return laptops

    @Rule(AS.rule << InputFact(field_id=3))
    def pick_laptop_for_gaming_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_laptops = self.__get_laptops(3, budget)
        laptops = []

        for laptop in list_laptops:
            laptops.append(get_laptop_as_json(laptop, budget))

        return laptops