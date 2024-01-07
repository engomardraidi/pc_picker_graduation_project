from .....dashboard.models import InternalDrive
from ..pc_knowledge import PCKnowledge
from ..input_fact import InputFact
from experta import Rule, AS
import decimal

class InternalDrivesKnowledge(PCKnowledge):
    def __get_internal_drive(self,budget):
        internal_drives = []
        perc = decimal.Decimal(0.03)

        while len(internal_drives) == 0 and perc <= 1:
            perc += decimal.Decimal(0.02)
            min_budget = budget - (budget * perc)
            max_budget = budget + (budget * perc)
            internal_drives = InternalDrive.filter_objects(price__range=(min_budget, max_budget))

        if len(internal_drives) == 0:
            return None

        closest_internal_drive = internal_drives[0]
        abs_diff = abs(budget - closest_internal_drive.price)

        for internal_drive in internal_drives:
            abs_value = abs(budget - internal_drive.price)
            if abs_diff > abs_value:
                abs_diff = abs_value
                closest_internal_drive = internal_drive

        return closest_internal_drive

    @Rule(AS.rule << InputFact())
    def get_internal_drive(self, rule):
        budget = rule['budget']

        return self.__get_internal_drive(budget)