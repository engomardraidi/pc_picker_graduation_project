from .....dashboard.models import RAMField
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS
import decimal

class RAMsKnowledge(PCKnowledge):
    def __get_ram(self, field_id, ram_type, max_ram_capacity, budget):
        rams = []
        perc = decimal.Decimal(0.03)

        while len(rams) == 0 and perc < 0.5:
            perc += decimal.Decimal(0.02)
            min_budget = budget - (budget * perc)
            max_budget = budget + (budget * perc)
            rams = RAMField.filter_objects(field=field_id, ram__type=ram_type, ram__size__lte=max_ram_capacity, ram__price__range=(min_budget, max_budget))

        if len(rams) == 0:
            return None

        closest_ram = rams[0].ram
        abs_diff = abs(budget - closest_ram.price)

        for ram in rams:
            abs_value = abs(budget - ram.ram.price)
            if abs_diff > abs_value:
                abs_diff = abs_value
                closest_ram = ram.ram

        return closest_ram

    @Rule(AS.rule << InputFact(type=3))
    def get_ram_with_socket_3(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']
        max_ram_capacity = rule['max_ram_capacity']

        return self.__get_ram(field_id, 3, max_ram_capacity, budget)

    @Rule(AS.rule << InputFact(type=4))
    def get_ram_with_socket_4(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']
        max_ram_capacity = rule['max_ram_capacity']

        return self.__get_ram(field_id, 4, max_ram_capacity, budget)

    @Rule(AS.rule << InputFact(type=5))
    def get_ram_with_socket_5(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']
        max_ram_capacity = rule['max_ram_capacity']

        return self.__get_ram(field_id, 5, max_ram_capacity, budget)

    @Rule(AS.rule << InputFact(type=2))
    def get_ram_with_socket_2(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']
        max_ram_capacity = rule['max_ram_capacity']

        return self.__get_ram(field_id, 2, max_ram_capacity, budget)

    @Rule(AS.rule << InputFact(type=1))
    def get_ram_with_socket_1(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']
        max_ram_capacity = rule['max_ram_capacity']

        return self.__get_ram(field_id, 1, max_ram_capacity, budget)