from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .. import models
from . import serializers
from . import functions

class FieldView(generics.CreateAPIView):
    serializer_class = serializers.FieldSerializer

@api_view(['GET'])
def pc_configuration(request):
    return Response({'result': None})