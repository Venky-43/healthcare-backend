from rest_framework import generics
from django.contrib.auth.models import User
from api.serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer