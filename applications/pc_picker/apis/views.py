import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .expert_system import ExpertSystem, InputFact
from ...dashboard import models as models_dashboard
from ...dashboard.apis import serializers  as serializers_dashboard
from jinja2 import Template

@api_view(['GET'])
def test_expert_system(request):
    field_id = request.data.get('field_id', None)
    budget = request.data.get('budget', None)

    expert_system = ExpertSystem()
    expert_system.reset()
    expert_system.declare(InputFact(field_id=field_id, budget=budget))
    result = expert_system.run()

    return Response({'result': result})