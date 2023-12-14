from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .expert_system_folder.fields_knowledge import FieldsKnowledge
from .expert_system_folder.input_fact import InputFact
from ...dashboard.models import Device, Field
from ...dashboard.apis.serializers import DeviceSerializer
from ...core.functions import get_detail_response
from ...core.constants import Constants

class ListOfDevices(ListAPIView):
    queryset = Device.get_objects()
    serializer_class = DeviceSerializer

@api_view(['POST'])
def pick_pc(request):
    field_id = request.data.get('field_id', None)
    budget = request.data.get('budget', None)

    if field_id == None or budget == None:
        return Response(get_detail_response(Constants.REQUEIRED_FIELDS), status=400)
    elif not isinstance(field_id,int) or not isinstance(budget,int):
        return Response(get_detail_response(Constants.NOT_A_NUMBER), status=400)

    if Field.get_object(field_id) == None:
        return Response(get_detail_response(Constants.FIELD_NOT_EXIST), status=404)

    expert_system = FieldsKnowledge()
    expert_system.reset()
    expert_system.declare(InputFact(field_id=field_id, budget=budget))
    result = expert_system.run()

    return Response({'result': result})