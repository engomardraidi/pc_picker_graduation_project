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
from rest_framework.pagination import PageNumberPagination

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

@api_view(['GET'])
def pick_motherboards(request):
    paginator = PageNumberPagination()
    motherbords = dashboard_models.Motherboard.get_active_objects()
    result = paginator.paginate_queryset(motherbords, request)
    serializer = dashboard_serializers.MotherboardSerializer(result, many=True)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def pick_cpus(request):
    field_id = request.data.get('field_id', None)
    motherboard_id = request.data.get('motherboard_id', None)

    if not isinstance(motherboard_id, int) or not isinstance(field_id, int):
        return Response({'details': 'Informations are not complete'}, status=400)

    motherboard = dashboard_models.Motherboard.get_object(motherboard_id)

    if motherboard is None:
        return Response({'details': 'Not found cpus compatabile with selected motherboard'}, status=404)

    paginator = PageNumberPagination()
    cpus = dashboard_models.CPU.filter_objects(cpufield__field__id=field_id, socket=motherboard.socket)
    result = paginator.paginate_queryset(cpus, request)
    serializer = dashboard_serializers.CPUSerializer(result, many=True)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def pick_rams(request):
    field_id = request.data.get('field_id', None)
    motherboard_id = request.data.get('motherboard_id', None)

    if not isinstance(motherboard_id, int) or not isinstance(field_id, int):
        return Response({'details': 'Informations are not complete'}, status=400)

    motherboard = dashboard_models.Motherboard.get_object(motherboard_id)

    if motherboard is None:
        return Response([], status=404)
    
    paginator = PageNumberPagination()
    rams = dashboard_models.RAM.filter_objects(ramfield__field__id=field_id, type=motherboard.ram_type, size__lte=motherboard.memory_max_capacity)
    result = paginator.paginate_queryset(rams, request)
    serializer = dashboard_serializers.RAMSerializer(result, many=True)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def pick_gpus(request):
    field_id = request.data.get('field_id', None)
    motherboard_id = request.data.get('motherboard_id', None)

    if not isinstance(motherboard_id, int) or not isinstance(field_id, int):
        return Response([], status=400)

    motherboard = dashboard_models.Motherboard.get_object(motherboard_id)

    if motherboard is None:
        return Response([])

    if motherboard.pci_e_3 + motherboard.pci_e_4 == 0:
        return Response([], status=404)

    paginator = PageNumberPagination()
    gpus = []
    if motherboard.pci_e_3 > 0 and motherboard.pci_e_4 > 0:
        gpus = dashboard_models.GPU.filter_objects(gpufield__field__id=field_id)
    else:
        gpus = dashboard_models.GPU.filter_objects(gpufield__field__id=field_id, pci_e=3 if motherboard.pci_e_3 > 0 else 4)
    result = paginator.paginate_queryset(gpus, request)
    serializer = dashboard_serializers.GPUSerializer(result, many=True)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def pick_cases(request):
    field_id = request.data.get('field_id', None)

    if not isinstance(field_id, int):
        return Response({'details': 'Informations are not complete'}, status=400)

    field = dashboard_models.Field.get_object(field_id)

    if field is None:
        return Response([])

    paginator = PageNumberPagination()
    cases = dashboard_models.Case.filter_objects(style=field.case_style)
    result = paginator.paginate_queryset(cases, request)
    serializer = dashboard_serializers.CaseSerializer(result, many=True)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def pick_internal_drives(request):
    paginator = PageNumberPagination()
    internal_drives = dashboard_models.InternalDrive.get_active_objects()
    result = paginator.paginate_queryset(internal_drives, request)
    serializer = dashboard_serializers.InternalDriveSerializer(result, many=True)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def pick_power_supplies(request):
    paginator = PageNumberPagination()
    power_supplies = dashboard_models.PowerSupply.get_active_objects()
    result = paginator.paginate_queryset(power_supplies, request)
    serializer = dashboard_serializers.PowerSupplySerializer(result, many=True)

    return paginator.get_paginated_response(serializer.data)