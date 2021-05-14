from django.shortcuts import render
from rest_framework import generics
from .models import DeliveryPersonProfile
from .serializer import DeliveryPersonDetailSerializer
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response


class DeliveryPersonProfileAPIView(generics.GenericAPIView):
	queryset					=		DeliveryPersonProfile.objects.all()
	authentication_classes		=		[TokenAuthentication,SessionAuthentication,JSONWebTokenAuthentication]
	permission_classes			=		[]
	serializer_class			=		DeliveryPersonDetailSerializer



	def get(self,request,*args,**kwargs):
		try:
			user			=		self.request.user
			profile 		=		DeliveryPersonProfile.objects.get(user=user)
			serializer      =		DeliveryPersonDetailSerializer(profile)
			return Response(serializer.data)
		except:
			return Response({"message":"No profile exist"})


class DeliveryPersonProfileCreateAPIView(generics.ListCreateAPIView):
	queryset					=		DeliveryPersonProfile.objects.all()
	authentication_classes		=		[TokenAuthentication,SessionAuthentication,JSONWebTokenAuthentication]
	permission_classes			=		[]
	serializer_class			=		DeliveryPersonDetailSerializer

	def post(self,request,*args,**kwargs):
		try:
			self.create(request,*args,**kwargs)
			return Response({"status":201,"message":"Sucessfully Created"})
		except:
			return Response({"message":"Invalid Form"})

	def perform_create(self,serializer):
		print(self.request.user)
		user       =   self.request.user
		serializer.save(user=user)


class DeliveryPersonRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset					=		DeliveryPersonProfile.objects.all()
	authentication_classes		=		[]
	permission_classes			=		[]
	serializer_class			=		DeliveryPersonDetailSerializer
	lookup_field                =       "id"

