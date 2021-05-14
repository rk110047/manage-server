from django.shortcuts import render
import decimal
# Create your views here.
from rest_framework.response import Response
from .serializer import EwalletSerializer
from .models import EWallet
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication,TokenAuthentication


class EwalletDetailAPIView(generics.GenericAPIView):
    queryset                =   EWallet
    permission_classes      =   []
    authentication_classes  =   [TokenAuthentication,SessionAuthentication]
    serializer_class        =   EwalletSerializer

    def get(self,request):
        user 			= 		self.request.user
        ewallet     =		EWallet.objects.get(User=user)
        serialize  		=		EwalletSerializer(ewallet,context={'request': request})
        return Response(serialize.data)

class PayMoney(generics.GenericAPIView):
    queryset                =   EWallet
    permission_classes      =   []
    authentication_classes  =   [TokenAuthentication,SessionAuthentication]
    serializer_class        =   EwalletSerializer

    def get(self,request):
        user 			= 		self.request.user
        wallet_id		=		self.request.GET.get('wallet_id')
        ewallet     	=		EWallet.objects.get(wallet_id=wallet_id)
        amount			=		self.request.GET.get('amount')
        if decimal.Decimal(user.ewallet.money)>=decimal.Decimal(amount):
        	ewallet.money  	=	decimal.Decimal(amount)+decimal.Decimal(ewallet.money)
        	ewallet.save()
        	user.ewallet.money =	decimal.Decimal(user.ewallet.money)-decimal.Decimal(amount)
        	user.ewallet.save()
        	return Response({'message':"payment successful"})
        return Response({'message':"payment failed"})
