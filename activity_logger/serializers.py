from .models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    activity = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['name', 'place', 'activity']
