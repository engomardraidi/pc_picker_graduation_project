from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .expert_system_folder.fields_knowledge import FieldsKnowledge
from .expert_system_folder.input_fact import InputFact
from ...dashboard.apis.serializers import DeviceSerializer, FieldReadSerializer
from ...core.functions import get_detail_response
from ...core.constants import Constants
from ...dashboard import models as dashboard_models
from ...dashboard.apis import serializers as dashboard_serializers

class ListOfDevices(ListAPIView):
    queryset = dashboard_models.Device.get_objects()
    serializer_class = DeviceSerializer

class ListOfFields(ListAPIView):
    queryset = dashboard_models.Field.get_objects()
    serializer_class = FieldReadSerializer

@api_view(['POST'])
def pick_pc(request):
    field_id = request.data.get('field_id', None)
    budget = request.data.get('budget', None)

    if field_id == None or budget == None:
        return Response(get_detail_response(Constants.REQUEIRED_FIELDS), status=400)
    elif not isinstance(field_id,int) or not isinstance(budget,int):
        return Response(get_detail_response(Constants.NOT_A_NUMBER), status=400)

    if dashboard_models.Field.get_object(field_id) == None:
        return Response(get_detail_response(Constants.FIELD_NOT_EXIST), status=404)

    expert_system = FieldsKnowledge()
    expert_system.reset()
    expert_system.declare(InputFact(field_id=field_id, budget=budget))
    result = expert_system.run()

    return Response({'num_of_PCs': len(result), 'PCs': result})

@api_view(['POST'])
def pick_cpus(request):
    field_id = request.data.get('field_id', None)
    motherboard_id = request.data.get('motherboard_id', None)

    if not isinstance(motherboard_id, int) or not isinstance(field_id, int):
        return Response({'details': 'Informations are not complete'}, status=400)

    motherboard = dashboard_models.Motherboard.get_object(motherboard_id)

    if motherboard is None:
        return Response({'details': 'Not found cpus compatabile with selected motherboard'}, status=404)

    cpus = dashboard_models.CPU.filter_objects(cpufield__field__id=field_id, socket=motherboard.socket)
    serializer = dashboard_serializers.CPUSerializer(cpus, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def pick_rams(request):
    field_id = request.data.get('field_id', None)
    motherboard_id = request.data.get('motherboard_id', None)

    if not isinstance(motherboard_id, int) or not isinstance(field_id, int):
        return Response({'details': 'Informations are not complete'}, status=400)

    motherboard = dashboard_models.Motherboard.get_object(motherboard_id)

    if motherboard is None:
        return Response({'details': 'Not found rams compatabile with selected motherboard'}, status=404)

    rams = dashboard_models.RAM.filter_objects(ramfield__field__id=field_id, type=motherboard.ram_type, size__lte=motherboard.memory_max_capacity)
    serializer = dashboard_serializers.RAMSerializer(rams, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def pick_gpus(request):
    field_id = request.data.get('field_id', None)
    motherboard_id = request.data.get('motherboard_id', None)

    if not isinstance(motherboard_id, int) or not isinstance(field_id, int):
        return Response({'details': 'Informations are not complete'}, status=400)

    motherboard = dashboard_models.Motherboard.get_object(motherboard_id)

    if motherboard is None:
        return Response([])

    if motherboard.pci_e_3 + motherboard.pci_e_4 == 0:
        return Response({'details': 'Not found gpus compatabile with selected motherboard'}, status=404)
    gpus = []
    if motherboard.pci_e_3 > 0 and motherboard.pci_e_4 > 0:
        gpus = dashboard_models.GPU.filter_objects(gpufield__field__id=field_id)
    else:
        gpus = dashboard_models.GPU.filter_objects(gpufield__field__id=field_id, pci_e=3 if motherboard.pci_e_3 > 0 else 4)
    serializer = dashboard_serializers.GPUSerializer(gpus, many=True)

    return Response(serializer.data)