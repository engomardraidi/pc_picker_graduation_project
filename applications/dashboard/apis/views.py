from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Motherboard


@api_view(['GET'])
def pc_configuration(request):
    motherboards = Motherboard.get_objects()

    return Response({'len': len(motherboards), 'pcs': []})