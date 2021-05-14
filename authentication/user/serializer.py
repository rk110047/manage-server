from rest_framework import serializers
from authentication.models import User




class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       User
        fields      =   ['username']
