from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Address
from .serializer import AddressSerializer
from django.shortcuts import redirect
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class AddressCreateAPIView(generics.CreateAPIView):
    queryset                        =   Address.objects.all()
    serializer_class                =   AddressSerializer
    permission_classes              =   []
    authentication_classes          =   [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


    def post(self,request,*args,**kwargs):
        try:
            self.create(request,*args,**kwargs)
            return Response({"status":201})
        except:
            return Response({"message":"Invalid Address"})

    def perform_create(self,serializer):
        print(self.request.user)
        billingprofile       =   self.request.user.billingprofile
        serializer.save(billingprofile=billingprofile)

# class BillingAddressCreateAPIView(generics.CreateAPIView):
#     queryset                        =   Address.objects.all()
#     serializer_class                =   AddressSerializer
#     permission_classes              =   []
#     authentication_classes          =   [JSONWebTokenAuthentication,SessionAuthentication]


#     def post(self,request,*args,**kwargs):
#         try:
#             self.create(request,*args,**kwargs)
#             return Response({"status":201})
#         except:
#             return Response({"message":"Invalid Address"})
        

#     def perform_create(self,serializer):
#         billingprofile       =   self.request.user.billingprofile
#         serializer.save(billingprofile=billingprofile,address_type="BIILING")
