import decimal
from experta import *
from django.db.models import Q
from ...dashboard import models as dashboard_models
from ...dashboard.apis import serializers as dashboard_serializers
from .functions import get_None_or_JSON, get_total_price

class InputFact(Fact):
    pass

class ExpertSystem(KnowledgeEngine):
    def __get_part(self, model, budget, Q_query=None, Q_query_field='price', order_field='price', **kwargs):
        price_query = f'{Q_query_field}__lte'
        new_Q_query = Q(**{price_query: budget}) if Q_query == None else Q(**{price_query: budget}) & Q_query
        parts = model.filter_objects(new_Q_query, **kwargs).order_by(f'-{order_field}')
        if len(parts) == 0:
            price_query = f'{Q_query_field}__gte'
            new_Q_query = Q(**{price_query: budget}) if Q_query == None else Q(**{price_query: budget}) & Q_query
            parts = model.filter_objects(new_Q_query, **kwargs).order_by(order_field)
        if len(parts) == 0:
            return None
        return parts[0]

    def __get_all_parts(self, field, budget, motherboard_Q_query=None):
        motherboard_budget = field.motherboard_budget * budget
        cpu_budget = field.cpu_budget * budget
        ram_budget = field.ram_budget * budget
        gpu_budget = field.gpu_budget * budget

        motherboard = self.__get_part(dashboard_models.Motherboard, motherboard_budget, Q_query=motherboard_Q_query)

        socket = motherboard.socket
        max_memory_size = motherboard.memory_max_capacity
        memory_type = motherboard.memory_type
        pci_e_3 = motherboard.pci_e_3
        pci_e_4 = motherboard.pci_e_4

        cpu = self.__get_part(dashboard_models.CPUField, cpu_budget, Q_query_field='cpu__price',field=field,cpu__socket=socket,order_field='cpu__price')
        ram = self.__get_part(dashboard_models.RAMField, ram_budget, Q_query_field='ram__price',field=field,ram__size__lte=max_memory_size, ram__memory_type=memory_type,order_field='ram__price')
        gpu = None
        gpu_3 = None
        gpu_4 = None

        if pci_e_3 + pci_e_4 == 0:
            pass
        else:
            if pci_e_3 > 0:
                gpu_3 = self.__get_part(dashboard_models.GPUField, gpu_budget, Q_query_field='gpu__price',field=field,gpu__pci_e=3,order_field='gpu__price')
            if pci_e_4 > 0:
                gpu_4 = self.__get_part(dashboard_models.GPUField, gpu_budget, Q_query_field='gpu__price',field=field,gpu__pci_e=4,order_field='gpu__price')

        if gpu_4 != None:
            gpu = gpu_4
        elif gpu_3 != None:
            gpu = gpu_3

        return motherboard, cpu, ram, gpu

    @Rule(AS.rule << InputFact(field_id=1))
    def pick_pc_for_programming(self, rule):
        field = dashboard_models.Field.get_object(rule['field_id'])
        budget = decimal.Decimal(rule['budget'])
        
        motherboard, cpu, ram, gpu = self.__get_all_parts(field, budget)
        
        return {
            'budget': budget,
            'total_price': get_total_price(motherboard, cpu, ram, gpu),
            'pc': {
                'motherboard': get_None_or_JSON(motherboard),
                'cpu':  get_None_or_JSON(cpu),
                'ram':  get_None_or_JSON(ram),
                'gpu':  get_None_or_JSON(gpu)
            }
        }

    @Rule(AS.rule << InputFact(field_id=2))
    def pick_pc_for_graphic_design(self, rule):
        field = dashboard_models.Field.get_object(rule['field_id'])
        budget = decimal.Decimal(rule['budget'])
        
        motherboard, cpu, ram, gpu = self.__get_all_parts(field, budget, motherboard_Q_query=~Q(pci_e_3=0) & ~Q(pci_e_4=0))
        
        return {
            'budget': budget,
            'total_price': get_total_price(motherboard, cpu, ram, gpu),
            'pc': {
                'motherboard': get_None_or_JSON(motherboard),
                'cpu':  get_None_or_JSON(cpu),
                'ram':  get_None_or_JSON(ram),
                'gpu':  get_None_or_JSON(gpu)
            }
        }