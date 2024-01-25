from .expert_system_abc import ExpertSystem
import decimal
from experta import Rule, AS
from ....dashboard.models import Mobile, MobileUse
from ..functions import get_mobile_as_json
from .input_fact import InputFact
import decimal

class MobilesKnowledge(ExpertSystem):
    def __get_mobiles(self, field_id, budget):
        perc = decimal.Decimal(0.03)
        mobiles = []

        while len(mobiles) < 5 and perc < decimal.Decimal(1):
            perc += decimal.Decimal(0.03)
            min_budget = budget - (budget * perc)
            max_budget = budget + (budget * perc)
            mobiles = MobileUse.filter_objects(use__id__in=field_id, mobile__price__range=(min_budget, max_budget)).distinct('mobile')

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[1]))
    def pick_mobile_for_performance_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([1], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[2]))
    def pick_mobile_for_camera_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([2], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[3]))
    def pick_mobile_for_battery_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([3], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[4]))
    def pick_mobile_for_browsing_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([4], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[1,2]))
    def pick_mobile_for_performance_and_camera_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([1,2], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[1,3]))
    def pick_mobile_for_performance_and_battery_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([1,3], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[2,3]))
    def pick_mobile_for_camera_and_battery_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([2,3], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[2,4]))
    def pick_mobile_for_camera_and_browsing_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([2,4], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[3,4]))
    def pick_mobile_for_battery_and_browsing_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([3,4], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[1,2,3]))
    def pick_mobile_for_perfrormance_and_camera_and_battery_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([1,2,3], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles

    @Rule(AS.rule << InputFact(field_id=[2,3,4]))
    def pick_mobile_for_camera_and_battery_and_browsing_use(self, rule):
        budget = decimal.Decimal(rule['budget'])
        
        list_mobiles = self.__get_mobiles([2,3,4], budget)
        mobiles = []

        for mobile in list_mobiles:
            mobiles.append(get_mobile_as_json(mobile.mobile, budget))

        return mobiles