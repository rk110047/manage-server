from rest_framework import serializers
from .models import ShopProfile,ShopCategories
from authentication.user.serializer import UserDetailSerializer

class ShopProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       ShopProfile
        fields      =       '__all__'
        read_only_fields        =  ['user']



class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       ShopProfile
        fields      =       ['shop_name']

class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       ShopProfile
        fields      =       '__all__'


class ShopProfileDetailSerializer(serializers.ModelSerializer):
    edit            =       serializers.HyperlinkedIdentityField(view_name='shop:shop edit',lookup_field='id')
    
    class Meta:
        model       =       ShopProfile
        fields      =       [ 'user','shop_name','address_line_1','address_line_2','town_city',
    'country',
    'shop_image',
    'contact',
    'email_address',
    'timming',
    'shop_details',
    'active',
    'edit',
     'delivery_charges','personal_pickup_limit']


# class ShopImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model               =   ShopImage
#         fields              =   "__all__"
#         read_only_fields    =   ["shop"]


class ShopCatSerializer(serializers.ModelSerializer):
    class Meta:
        model    =   ShopCategories
        fields   =   "__all__"
