from rest_framework import serializers
from .models import ShopProfile
from authentication.user.serializer import UserDetailSerializer

class ShopProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       ShopProfile
        fields      =       '__all__'
        read_only_fields        =         ['user']



class ShopDetailSerializer(serializers.ModelSerializer):
    user        =   UserDetailSerializer(read_only=True)
    class Meta:
        model       =       ShopProfile
        fields      =       ['user','shop_name']
