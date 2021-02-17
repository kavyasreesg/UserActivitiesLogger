from .serializers import UserDataSerializer
from .models import UserData
from rest_framework import viewsets


class UserDataView(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
