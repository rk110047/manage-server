from django.shortcuts import render
from .serializer import RegisterSerializer,LoginSerializer,RegisterSerializerBySuperUser
from rest_framework import generics,mixins,status
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate,login
from rest_framework_jwt.settings import api_settings
from utils.permissions import NonRegisteredUserOnly,SuperUserOnly
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token

jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
jwt_payload_response_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER





class LoginAPIView(generics.GenericAPIView):
    serializer_class    =       LoginSerializer
    permission_classes     =   [NonRegisteredUserOnly]
    authentication_classes =   []

    def post(self,request):
        print(request.data)
        username    =   request.data.get('username')
        password    =   request.data.get('password')
        print(username)
        print(password)
        user        =   authenticate(username=username,password=password)
        print(user)
        if user is not None:
            payload     = jwt_payload_handler(user)
            token       = jwt_encode_handler(payload)
            login(request,user)
            response = jwt_payload_response_handler(token,user,request=request)
            return Response(response, status=status.HTTP_200_OK)
        response = {
        "data": {
            "message": "Your login information is invalid",
            "status": "invalid"
        }
    }
        return Response(response, status=status.HTTP_200_OK)


class LoginWithTokenAuthenticationAPIView(generics.GenericAPIView):
    serializer_class    =       LoginSerializer
    permission_classes     =   [NonRegisteredUserOnly]
    authentication_classes =   []

    def post(self,request):
        print(request.data)
        username    =   request.data.get('username')
        password    =   request.data.get('password')
        print(username)
        print(password)
        user        =   authenticate(username=username,password=password)
        print(user)
        if user is not None:
            # login(user,request)
            #TOKEN STUFF
            token, _ = Token.objects.get_or_create(user = user)
            #token_expire_handler will check, if the token is expired it will generate new one
            # is_expired, token = token_expire_handler(token)     # The implementation will be described further

            return Response({ 
                'token': token.key,'id':user.id
            }, status=status.HTTP_200_OK)
        response = {
        "data": {
            "message": "Your login information is invalid",
            "status": "invalid"
        }
    }
        return Response(response, status=status.HTTP_200_OK)





# #TOKEN STUFF
#     token, _ = Token.objects.get_or_create(user = user)
    
#     #token_expire_handler will check, if the token is expired it will generate new one
#     is_expired, token = token_expire_handler(token)     # The implementation will be described further
#     user_serialized = UserSerializer(user)

#     return Response({
#         'user': user_serialized.data, 
#         'expires_in': expires_in(token),
#         'token': token.key
#     }, status=HTTP_200_OK)


class RegisterAPIView(generics.CreateAPIView):
     queryset               =   User.objects.all()
     permission_classes     =   [NonRegisteredUserOnly]
     authentication_classes =   []
     serializer_class       =   RegisterSerializer

     def post(self,request,*args,**kwargs):
        try:
            return self.create(request,*args,**kwargs)
        except:
            return Response({"message":"provided details is invalid"})



class RegisteredBySuperUserAPIView(generics.CreateAPIView):
     queryset               =   User.objects.all()
     permission_classes     =   [SuperUserOnly]
     authentication_classes =   [TokenAuthentication,SessionAuthentication]
     serializer_class       =   RegisterSerializerBySuperUser

class SuperUserCheckAPIView(generics.GenericAPIView):
    permission_classes     =   []
    authentication_classes =   [TokenAuthentication,SessionAuthentication]
    
    def get(self,request):
        request            =    self.request
        user               =    request.user
        if user.is_staff:
            return Response({"status":200})
        else:
            return Response({"status":400})
