from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .expert_system import ExpertSystem, MyFact

@api_view(['GET'])
def test_expert_system(request):
    # fact = MyFact(price=500)
    # expert_system = ExpertSystem()
    # expert_system.reset()
    # expert_system.declare(fact)
    # motherbords = expert_system.run()

    return Response({}, status=status.HTTP_200_OK)