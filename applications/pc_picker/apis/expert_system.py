from experta import *
from ...dashboard import models as dashboard_models
from ...dashboard.apis import serializers as dashboard_serializers

class InputFact(Fact):
    pass

class ExpertSystem(KnowledgeEngine):
    @Rule(InputFact(field_id=1))
    def pick_pc_for_programming(self):
        return 'programming'
