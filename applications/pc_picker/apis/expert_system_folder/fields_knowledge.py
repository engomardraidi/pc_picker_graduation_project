from .expert_system_abc import ExpertSystem
import decimal
from experta import Rule, AS
from django.db.models import Q
from ..pc import PC
from ....dashboard.models import Field
from .input_fact import InputFact
from .pc_parts.motherboards_knowledge import MotherboardsKnowledge
from .pc_parts.cpus_knowledge import CPUsKnowledge
from .pc_parts.rams_knowledge import RAMsKnowledge
from .pc_parts.gpus_knowledge import GPUsKnowledge
from .pc_parts.cases_knowledge import CasesKnowledge
from .pc_parts.internal_drive_knowledge import InternalDrivesKnowledge
from .pc_parts.power_supply_knowledge import PowerSuppliesKnowledge

class FieldsKnowledge(ExpertSystem):
    def __init_expert(self):
        self.motherboard_knowledge = MotherboardsKnowledge()
        self.cpus_knowledge = CPUsKnowledge()
        self.rams_knowledge = RAMsKnowledge()
        self.gpus_knowledge = GPUsKnowledge()
        self.cases_knowledge = CasesKnowledge()
        self.internal_drives_knowledge = InternalDrivesKnowledge()
        self.power_supplies_knowledge = PowerSuppliesKnowledge()

        self.__reset_knowledge()

    def __reset_knowledge(self):
        self.motherboard_knowledge.reset()
        self.cpus_knowledge.reset()
        self.rams_knowledge.reset()
        self.gpus_knowledge.reset()
        self.cases_knowledge.reset()        
        self.internal_drives_knowledge.reset()
        self.power_supplies_knowledge.reset()

    def __get_all_parts(self, field_id, budget, motherboard_Q_query=None):
        field = Field.get_object(field_id)
        if field == None:
            return 'the field you want not exist'

        pcs = []
        motherboard_budget = field.motherboard_budget * budget
        cpu_budget = field.cpu_budget * budget
        ram_budget = field.ram_budget * budget
        gpu_budget = field.gpu_budget * budget
        case_budget = field.case_budget * budget
        internal_drive_budget = field.internal_drive_budget * budget
        power_supply_budget = field.power_supply_budget * budget

        self.motherboard_knowledge.declare(InputFact(part='motherboard', budget=motherboard_budget, Q_query=motherboard_Q_query))
        motherboards = self.motherboard_knowledge.run()

        for motherboard in motherboards:
            pc = PC(motherboard=motherboard)
            socket = pc.motherboard.socket
            max_memory_size = pc.motherboard.memory_max_capacity
            ram_type = pc.motherboard.ram_type
            pci_e_3 = pc.motherboard.pci_e_3
            pci_e_4 = pc.motherboard.pci_e_4

            self.cpus_knowledge.declare(InputFact(field_id=field.id, socket=socket.id, budget=cpu_budget))
            pc.cpu = self.cpus_knowledge.run()

            self.rams_knowledge.declare(InputFact(field_id=field.id, type=ram_type.id, max_ram_capacity=max_memory_size, budget=ram_budget))
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

            pcs.append(pc)
            self.__reset_knowledge()

        return pcs

    @Rule(AS.rule << InputFact(field_id=1))
    def pick_pc_for_programming(self, rule):
        self.__init_expert()
        budget = decimal.Decimal(rule['budget'])
        
        list_pcs = self.__get_all_parts(1, budget, motherboard_Q_query=~Q(pci_e_3=0) | ~Q(pci_e_4=0))
        pcs = []
        for pc in list_pcs:
            pc.append(pc.get_pc_parts_as_JSON(budget))
        return pcs

    @Rule(AS.rule << InputFact(field_id=2))
    def pick_pc_for_graphic_design(self, rule):
        self.__init_expert()
        budget = decimal.Decimal(rule['budget'])
        
        list_pcs = self.__get_all_parts(2, budget, motherboard_Q_query=~Q(pci_e_3=0) | ~Q(pci_e_4=0))
        pcs = []
        for pc in list_pcs:
            pc.append(pc.get_pc_parts_as_JSON(budget))
        return pcs

    @Rule(AS.rule << InputFact(field_id=3))
    def pick_pc_for_gaming(self, rule):
        self.__init_expert()
        budget = decimal.Decimal(rule['budget'])
        
        list_pcs = self.__get_all_parts(3, budget, motherboard_Q_query=~Q(pci_e_3=0) | ~Q(pci_e_4=0))
        pcs = []
        for pc in list_pcs:
            pc.append(pc.get_pc_parts_as_JSON(budget))
        return pcs

    @Rule(AS.rule << InputFact(field_id=4))
    def pick_pc_for_office(self, rule):
        self.__init_expert()
        budget = decimal.Decimal(rule['budget'])
        
        list_pcs = self.__get_all_parts(4, budget)
        pcs = []
        for pc in list_pcs:
            pc.append(pc.get_pc_parts_as_JSON(budget))
        return pcs