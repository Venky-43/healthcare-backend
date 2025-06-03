from rest_framework import viewsets
from api import models, serializers

class MappingViewSet(viewsets.ModelViewSet):
    queryset = models.PatientDoctorMapping.objects.all()
    serializer_class = serializers.MappingSerializer
