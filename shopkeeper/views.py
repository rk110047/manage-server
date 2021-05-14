from django.shortcuts import render
from rest_framework import generics
from .models import ShopProfile,ShopCategories
from django.db.models import Q
from .serializer import ShopProfileCreateSerializer,ShopsSerializer,ShopProfileDetailSerializer,ShopCatSerializer
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class ShopProfileCreateAPIView(generics.CreateAPIView):
    queryset                =   ShopProfile
    permission_classes      =   []
    authentication_classes  =   [TokenAuthentication,SessionAuthentication]
    serializer_class        =   ShopProfileCreateSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class ShopsAPIView(generics.ListAPIView):
	authentication_classes  =   []
	serializer_class        =   ShopsSerializer
	permission_classes      =   []

	def get_queryset(self):
		request 	= 	self.request
		queryset    =	ShopProfile.objects.filter(active=True)
		query       =   request.GET.get('q')
		if query is not None:
			queryset 		= 	queryset.filter(Q(shop_name__icontains=query))
			# return shops
		return queryset

class ShopProfileDetailAPIView(generics.GenericAPIView):
    queryset                =   ShopProfile
    permission_classes      =   []
    authentication_classes  =   [TokenAuthentication,SessionAuthentication]
    serializer_class        =   ShopProfileDetailSerializer

    def get(self,request):
        user 			= 		self.request.user
        print(user)
        shopProfile     =		ShopProfile.objects.get(user=user)
        # shopImage       =		ShopImage.objects.get(shop=user.shopprofile)
        serialize  		=		ShopProfileDetailSerializer(shopProfile,context={'request': request})
        # serialize1 		=		ShopImageSerializer(shopImage,context={'request': request})
        # serialize       =       serialize.data
        # serialize.update(serialize1.data)
        return Response(serialize.data)

class ShopProfileEditAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset                =   ShopProfile
	permission_classes      =   []
	authentication_classes  =   [TokenAuthentication]
	serializer_class        =   ShopProfileCreateSerializer
	lookup_field			=		"id"

class ShopsListAPIView(generics.ListAPIView):
	authentication_classes  =   [TokenAuthentication,SessionAuthentication]
	serializer_class        =   ShopProfileDetailSerializer
	permission_classes      =   []

	def get_queryset(self):
		request 	= 	self.request
		queryset    =	ShopProfile.objects.all()
		return queryset

# class ShopImageCreateAPIView(generics.CreateAPIView):
# 	queryset                =   ShopImage
# 	permission_classes      =   []
# 	authentication_classes  =   [SessionAuthentication,JSONWebTokenAuthentication]
# 	serializer_class        =   ShopImageSerializer
	

# 	def perform_create(self,serializer):
# 		serializer.save(shop=self.request.user.shopprofile)

# class ShopImageUpdateAPIView(generics.UpdateAPIView):
# 	queryset                =   ShopImage
# 	permission_classes      =   []
# 	authentication_classes  =   [SessionAuthentication,JSONWebTokenAuthentication]
# 	serializer_class        =   ShopImageSerializer
# 	lookup_field			=	"shop"
	

	# def perform_create(self,serializer):
	# 	serializer.save(shop=self.request.user.shopprofile)


class ShopCategoriesLCAPIView(generics.ListCreateAPIView):
    queryset                =   ShopCategories.objects.all()
    serializer_class        =   ShopCatSerializer
    permission_classes      =   []
    authentication_classes  =   []
class ShopSearchAPIView(generics.ListAPIView):
    # queryset                =   Product.objects.all()
    serializer_class        =   ShopsSerializer
    permission_classes      =   []
    authentication_classes  =   []



    def get_queryset(self):
        request    =    self.request
        queryset   =    ShopProfile.objects.all()
        query      =    request.GET.get('category')
        if query is not None:
            queryset     =    queryset.filter(Category=query)

        return queryset
