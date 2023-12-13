from .....dashboard.models import GPUField
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS

class GPUsKnowledge(PCKnowledge):
    @Rule(AS.rule << InputFact(pci_e=3))
    def get_gpu_with_pci_e_3(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        gpus = GPUField.filter_objects(field=field_id, gpu__pci_e=3, gpu__price__lte=budget).order_by('-gpu__price')
        if len(gpus) == 0:
            gpus = GPUField.filter_objects(field=field_id, gpu__pci_e=3, gpu__price__gte=budget).order_by('gpu__price')
        return None if len(gpus) == 0 else gpus[0]

    @Rule(AS.rule << InputFact(pci_e=4))
    def get_gpu_with_pci_e_4(self, rule):
        field_id = rule['field_id']
        budget = rule['budget']

        gpus = GPUField.filter_objects(field=field_id, gpu__pci_e=4, gpu__price__lte=budget).order_by('-gpu__price')
        if len(gpus) == 0:
            gpus = GPUField.filter_objects(field=field_id, gpu__pci_e=4, gpu__price__gte=budget).order_by('gpu__price')
        return None if len(gpus) == 0 else gpus[0]