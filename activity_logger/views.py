from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets


class UserDataView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
