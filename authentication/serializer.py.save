from rest_framework import serializers
from .models import User
from django.utils import timezone
from django.conf import settings
import datetime


from rest_framework_jwt.settings import api_settings

jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
jwt_payload_response_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta                    = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']



class RegisterSerializer(serializers.ModelSerializer):
    password                    =   serializers.CharField(style={'input_type':'password'},max_length=120,min_length=8,write_only=True)
    confirm_password            =   serializers.CharField(style={'input_type':'password'},max_length=120,min_length=8,write_only=True)
    token                       =   serializers.SerializerMethodField(read_only=True)
    expires                     =   serializers.SerializerMethodField(read_only=True)



    class Meta:
        model   =   User
        fields  =   ['username','email','password','confirm_password','token','expires']

    def get_token(self,obj):
        payload     = jwt_payload_handler(obj)
        token       = jwt_encode_handler(payload)
        return token

    def get_expires(self,obj):
        expires    =   timezone.now()+expire_delta
        return expires


    def validate(self,data):
        confirm_password    =   data['confirm_password']
        password            =   data['password']
        if not self.do_password_match(password,confirm_password):
            return serializers.ValidationError({'password':'password do not match.'})
        return data

    def create(self,validated_data):
        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)

    def do_password_match(self,password1,password2):
        return password1==password2




class LoginSerializer(serializers.Serializer):
    username    =   serializers.CharField(max_length=120)
    password    =   serializers.CharField(
        style={'input_type':'password'},
        max_length=128, min_length=6, write_only=True, )


class RegisterSerializerBySuperUser(serializers.ModelSerializer):
    password                    =   serializers.CharField(style={'input_type':'password'},max_length=120,min_length=8,write_only=True)
    confirm_password            =   serializers.CharField(style={'input_type':'password'},max_length=120,min_length=8,write_only=True)
    token                       =   serializers.SerializerMethodField(read_only=True)
    expires                     =   serializers.SerializerMethodField(read_only=True)



    class Meta:
        model   =   User
        fields  =   ['username','role','email','password','confirm_password','token','expires']

    def get_token(self,obj):
        payload     = jwt_payload_handler(obj)
        token       = jwt_encode_handler(payload)
        return token

    def get_expires(self,obj):
        expires    =   timezone.now()+expire_delta
        return expires


    def validate(self,data):
        confirm_password    =   data['confirm_password']
        password            =   data['password']
        if not self.do_password_match(password,confirm_password):
            return serializers.ValidationError({'password':'password do not match.'})
        return data

    def create(self,validated_data):
        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)

    def do_password_match(self,password1,password2):
        return password1==password2
