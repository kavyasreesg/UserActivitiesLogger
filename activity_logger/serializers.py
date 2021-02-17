from .models import UserData
from rest_framework import serializers


class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    activity = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = UserData
        fields = ['name', 'place', 'activity']
