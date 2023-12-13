from .....dashboard.models import InternalDrive
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS

class InternalDrivesKnowledge(PCKnowledge):
    def __get_internal_drive(self,budget):
        internal_drives = InternalDrive.filter_objects(price__lte=budget).order_by('-price')
        if len(internal_drives) == 0:
            internal_drives = InternalDrive.filter_objects(price__gte=budget).order_by('price')
        return None if len(internal_drives) == 0 else internal_drives[0]

    @Rule(AS.rule << InputFact())
    def get_internal_drive(self, rule):
        budget = rule['budget']

        return self.__get_internal_drive(budget)