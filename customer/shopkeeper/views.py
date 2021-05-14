from django.shortcuts import render
from rest_framework import generics
from .models import ShopProfile
from .serializer import ShopProfileCreateSerializer
from rest_framework.authentication import SessionAuthentication

class ShopProfileCreateAPIView(generics.CreateAPIView):
    queryset                =   ShopProfile
    permission_classes      =   []
    authentication_classes  =   [SessionAuthentication]
    serializer_class        =   ShopProfileCreateSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
