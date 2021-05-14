from django.shortcuts import render
from .models import CustomerProfile
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from .serializer import CustomerProfileSerializer
from rest_framework import  generics
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class CreateProfileAPIView(generics.CreateAPIView):
    queryset                =       CustomerProfile.objects.all()
    serializer_class        =       CustomerProfileSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

    def post(self,request,*args,**kwargs):
        try:
            self.create(request,*args,**kwargs)
            response  =   {"message":"created","status":201}
            return Response(response,status=201)
        except:
            return Response({"message":"your form is invalid"})

    def perform_create(self,serializer):
        serializer.save(User=self.request.user,email=self.request.user.email)




class EditProfileAPIView(generics.UpdateAPIView):
    queryset                =       CustomerProfile.objects.all()
    serializer_class        =       CustomerProfileSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,SessionAuthentication,JSONWebTokenAuthentication]
    lookup_field            =       'User'


class CustomerListAPIView(generics.ListAPIView):
    queryset                =       CustomerProfile.objects.all()
    serializer_class        =       CustomerProfileSerializer
    permission_classes      =       []
    authentication_classes  =       []



class CustomerDetailAPIView(generics.GenericAPIView):
    queryset                =       CustomerProfile.objects.all()
    serializer_class        =       CustomerProfileSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,SessionAuthentication,JSONWebTokenAuthentication]


    def get(self,request,*args,**kwargs):
        request             =       self.request
        user                =       request.user
        qs                  =       CustomerProfile.objects.get(User=user)
        serialize           =       CustomerProfileSerializer(qs)
        return Response(serialize.data)