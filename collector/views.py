from django.shortcuts import render
from .serializer import CollectorProfileSerializer
from rest_framework import generics
from .models import CollectorProfile
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response


class CollectorPersonProfileAPIView(generics.GenericAPIView):
	queryset					=		CollectorProfile.objects.all()
	authentication_classes		=		[TokenAuthentication,SessionAuthentication,JSONWebTokenAuthentication]
	permission_classes			=		[]
	serializer_class			=		CollectorProfileSerializer



	def get(self,request,*args,**kwargs):
		try:
			user			=		self.request.user
			profile 		=		CollectorProfile.objects.get(user=user)
			serializer      =		CollectorProfileSerializer(profile)
			return Response(serializer.data)
		except:
			return Response({"message":"No profile exist"})



class CollectorPersonProfileCreateAPIView(generics.ListCreateAPIView):
	queryset					=		CollectorProfile.objects.all()
	authentication_classes		=		[TokenAuthentication,SessionAuthentication,JSONWebTokenAuthentication]
	permission_classes			=		[]
	serializer_class			=		CollectorProfileSerializer

	def post(self,request,*args,**kwargs):
		try:
			self.create(request,*args,**kwargs)
			return Response({"status":201,"message":"Sucessfully Created"})
		except:
			return Response({"message":"Invalid Form"})

	def perform_create(self,serializer):
		print(self.request.data)
		print(self.request.user)
		user       =   self.request.user
		serializer.save(user=user)

class CollectorPersonRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset					=		CollectorProfile.objects.all()
	authentication_classes		=		[]
	permission_classes			=		[]
	serializer_class			=		CollectorProfileSerializer
	lookup_field                =       "id"


