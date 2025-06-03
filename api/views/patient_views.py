from rest_framework import viewsets, permissions
from api import models, serializers

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
