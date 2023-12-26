from .....dashboard.models import GPUField
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS
import decimal

class GPUsKnowledge(PCKnowledge):
    def __get_gpu(self, field_id, pci_e, budget):
        gpus = []
        perc = decimal.Decimal(0.03)

        while len(gpus) == 0 and perc < 0.5:
            perc += decimal.Decimal(0.02)
            min_budget = budget - (budget * perc)
            max_budget = budget + (budget * perc)
            gpus = GPUField.filter_objects(field=field_id, gpu__pci_e=pci_e, gpu__price__range=(min_budget, max_budget))

        if len(gpus) == 0:
            return None

        closest_gpu = gpus[0].gpu
        abs_diff = abs(budget - closest_gpu.price)

        for gpu in gpus:
            abs_value = abs(budget - gpu.gpu.price)
            if abs_diff > abs_value:
                abs_diff = abs_value
                closest_gpu = gpu.gpu

        return closest_gpu

    @Rule(AS.rule << InputFact(pci_e=3))
    def get_gpu_with_pci_e_3(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_gpu(field_id, 3, budget)

    @Rule(AS.rule << InputFact(pci_e=4))
    def get_gpu_with_pci_e_4(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        return self.__get_gpu(field_id, 4, budget)