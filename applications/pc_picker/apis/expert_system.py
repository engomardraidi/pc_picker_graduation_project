from experta import *
from ...dashboard import models as dashboard_models
from ...dashboard.apis import serializers as dashboard_serializers

class MyFact(Fact):
    pass

class ExpertSystem(KnowledgeEngine):
    @Rule(MyFact(price=500))
    def pick_pc(self):
        min_price = 300
        max_price = 700
        try:
            motherboards = dashboard_models.Motherboard.objects.filter(price__range=(min_price, max_price))
            serializer = dashboard_serializers.MotherboardSerializer(motherboards, many=True)
            return serializer.data
        except dashboard_models.Motherboard.DoesNotExist:
            return []
