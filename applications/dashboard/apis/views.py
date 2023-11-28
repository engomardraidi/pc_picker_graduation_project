from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .. import models
from . import serializers
from .functions import classification_cpu

class FieldView(generics.CreateAPIView):
    serializer_class = serializers.FieldSerializer

@api_view(['GET'])
def pc_configuration(request):
    objects = models.CPUField.filter_objects(field_id=1)
    print(objects[0].field.name)

    return Response({'result': len(objects)})