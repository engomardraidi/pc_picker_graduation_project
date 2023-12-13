from .expert_system_abc import ExpertSystem
import decimal
from experta import Rule, AS
from django.db.models import Q
from ....dashboard.apis.pc import PC
from ....dashboard import models as dashboard_models
from .input_fact import InputFact
from .pc_parts.motherboards_knowledge import MotherboardsKnowledge
from .pc_parts.cpus_knowledge import CPUsKnowledge
from .pc_parts.rams_knowledge import RAMsKnowledge
from .pc_parts.gpus_knowledge import GPUsKnowledge
from .pc_parts.cases_knowledge import CasesKnowledge
from .pc_parts.internal_drive_knowledge import InternalDrivesKnowledge
from .pc_parts.power_supply_knowledge import PowerSuppliesKnowledge

class FieldsKnowledge(ExpertSystem):
    def init_expert(self):
        self.motherboard_knowledge = MotherboardsKnowledge()
        self.cpus_knowledge = CPUsKnowledge()
        self.rams_knowledge = RAMsKnowledge()
        self.gpus_knowledge = GPUsKnowledge()
        self.cases_knowledge = CasesKnowledge()
        self.internal_drives_knowledge = InternalDrivesKnowledge()
        self.power_supplies_knowledge = PowerSuppliesKnowledge()

        self.motherboard_knowledge.reset()
        self.cpus_knowledge.reset()
        self.rams_knowledge.reset()
        self.gpus_knowledge.reset()
        self.cases_knowledge.reset()        
        self.internal_drives_knowledge.reset()
        self.power_supplies_knowledge.reset()

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
        pc = PC()

        motherboard_budget = field.motherboard_budget * budget
        cpu_budget = field.cpu_budget * budget
        ram_budget = field.ram_budget * budget
        gpu_budget = field.gpu_budget * budget
        case_budget = field.case_budget * budget
        internal_drive_budget = field.internal_drive_budget * budget
        power_supply_budget = field.power_supply_budget * budget

        self.motherboard_knowledge.declare(InputFact(part='motherboard', budget=motherboard_budget, Q_query=motherboard_Q_query))
        pc.motherboard = self.motherboard_knowledge.run()

        socket = pc.motherboard.socket
        max_memory_size = pc.motherboard.memory_max_capacity
        ram_type = pc.motherboard.ram_type
        pci_e_3 = pc.motherboard.pci_e_3
        pci_e_4 = pc.motherboard.pci_e_4

        self.cpus_knowledge.declare(InputFact(field_id=field.id, socket=socket.id, budget=cpu_budget))
        self.rams_knowledge.declare(InputFact(field_id=field.id, type=ram_type.id, max_ram_capacity=max_memory_size, budget=ram_budget))
        
        pc.cpu = self.cpus_knowledge.run()
        pc.ram = self.rams_knowledge.run()

        gpu_3 = None
        gpu_4 = None

        if pci_e_3 + pci_e_4 == 0:
            pass
        else:
            if pci_e_3 > 0:
                self.gpus_knowledge.declare(InputFact(field_id=field.id, pci_e=3, budget=gpu_budget))
                gpu_3 = self.gpus_knowledge.run()
            if pci_e_4 > 0:
                self.gpus_knowledge.declare(InputFact(field_id=field.id, pci_e=4, budget=gpu_budget))
                gpu_4 = self.gpus_knowledge.run()

        if gpu_4 != None:
            pc.gpu = gpu_4
        elif gpu_3 != None:
            pc.gpu = gpu_3

        self.cases_knowledge.declare(InputFact(budget=case_budget))
        pc.case_part = self.cases_knowledge.run()

        self.internal_drives_knowledge.declare(InputFact(budget=internal_drive_budget))
        pc.internal_drive = self.internal_drives_knowledge.run()

        self.power_supplies_knowledge.declare(InputFact(budget=power_supply_budget))
        pc.power_supply = self.power_supplies_knowledge.run()

        return pc

    @Rule(AS.rule << InputFact(field_id=1))
    def pick_pc_for_programming(self, rule):
        self.init_expert()
        field = dashboard_models.Field.get_object(rule['field_id'])
        budget = decimal.Decimal(rule['budget'])
        
        pc = self.__get_all_parts(field, budget)
        
        return pc.get_pc_parts_as_JSON()

    @Rule(AS.rule << InputFact(field_id=2))
    def pick_pc_for_graphic_design(self, rule):
        self.init_expert()
        field = dashboard_models.Field.get_object(rule['field_id'])
        budget = decimal.Decimal(rule['budget'])
        
        pc = self.__get_all_parts(field, budget, motherboard_Q_query=~Q(pci_e_3=0) & ~Q(pci_e_4=0))
        
        return pc.get_pc_parts_as_JSON()