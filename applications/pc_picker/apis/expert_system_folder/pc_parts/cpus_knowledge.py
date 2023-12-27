from .....dashboard.models import CPUField
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS
import decimal

class CPUsKnowledge(PCKnowledge):
    def __get_cpu(self, field_id, cpu_socket, budget):
        cpus = []
        perc = decimal.Decimal(0.03)

        while len(cpus) == 0 and perc < 1.6:
            perc += decimal.Decimal(0.02)
            min_budget = budget - (budget * perc)
            max_budget = budget + (budget * perc)
            cpus = CPUField.filter_objects(field=field_id, cpu__socket=cpu_socket, cpu__price__range=(min_budget, max_budget))

        if len(cpus) == 0:
            return None

        closest_cpu = cpus[0].cpu
        abs_diff = abs(budget - closest_cpu.price)

        for cpu in cpus:
            abs_value = abs(budget - cpu.cpu.price)
            if abs_diff > abs_value:
                abs_diff = abs_value
                closest_cpu = cpu.cpu

        return closest_cpu

    @Rule(AS.rule << InputFact(socket=11))
    def get_cpu_with_socket_11(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 11, budget)

    @Rule(AS.rule << InputFact(socket=3))
    def get_cpu_with_socket_3(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 3, budget)

    @Rule(AS.rule << InputFact(socket=1))
    def get_cpu_with_socket_1(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 1, budget)

    @Rule(AS.rule << InputFact(socket=8))
    def get_cpu_with_socket_8(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 8, budget)

    @Rule(AS.rule << InputFact(socket=6))
    def get_cpu_with_socket_6(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 6, budget)

    @Rule(AS.rule << InputFact(socket=9))
    def get_cpu_with_socket_9(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 9, budget)

    @Rule(AS.rule << InputFact(socket=2))
    def get_cpu_with_socket_2(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 2, budget)

    @Rule(AS.rule << InputFact(socket=13))
    def get_cpu_with_socket_13(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 13, budget)

    @Rule(AS.rule << InputFact(socket=12))
    def get_cpu_with_socket_12(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 12, budget)

    @Rule(AS.rule << InputFact(socket=4))
    def get_cpu_with_socket_4(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 4, budget)

    @Rule(AS.rule << InputFact(socket=5))
    def get_cpu_with_socket_5(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 5, budget)

    @Rule(AS.rule << InputFact(socket=15))
    def get_cpu_with_socket_15(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 15, budget)

    @Rule(AS.rule << InputFact(socket=7))
    def get_cpu_with_socket_7(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_cpu(field_id, 7, budget)