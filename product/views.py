from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.response import Response
from .models import Product,Categories,Content,ProductImages,ContentCategory,ProductTax
from django.db.models import Q
from .serializer import ProductTaxSerializer,ProductAPISerializer,CategoryContentSerializer,ProductContentSerializer,ProductImagesSerializer,ProductSerializer,ProductDetailSerializer,ProductCreateSerializer,ProductListOfUserSerializer,ProductDetailForListSerializer,ProductUpdateSerializer,CreateCatSerializer
from django.contrib.auth.decorators import login_required
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class ProductTaxListAPIView(generics.ListCreateAPIView):
    queryset                =   ProductTax.objects.all()
    serializer_class        =   ProductTaxSerializer
    permission_classes      =   []
    authentication_classes  =   []

    def get(self,request,product_id=None):
        try:
            product             =    Product.objects.get(product_id=product_id)
            queryset            =    ProductTax.objects.filter(Product=product)
            serialize           =    ProductTaxSerializer(queryset, many=True,context={'request': request})
            return Response(serialize.data)
        except:
            return Response([])

class ProductTaxRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =   ProductTax.objects.all()
    serializer_class        =   ProductTaxSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'id'

class ProductTaxLCAPIView(generics.ListCreateAPIView):
    queryset                =   ProductTax.objects.all()
    serializer_class        =   ProductTaxSerializer
    permission_classes      =   []
    authentication_classes  =   []


class ProductRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductAPISerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'product_id'


class ProductLCAPIView(generics.ListCreateAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductAPISerializer
    permission_classes      =   []
    authentication_classes  =   []


class ProductImagesListAPIView(generics.ListCreateAPIView):
    queryset                =   ProductImages.objects.all()
    serializer_class        =   ProductImagesSerializer
    permission_classes      =   []
    authentication_classes  =   []

    def get(self,request,product_id=None):
        try:
            product             =    Product.objects.get(product_id=product_id)
            queryset            =    ProductImages.objects.filter(Product=product)
            serialize           =    ProductImagesSerializer(queryset, many=True,context={'request': request})
            return Response(serialize.data)
        except:
            return Response([])

class ProductImagesRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =   ProductImages.objects.all()
    serializer_class        =   ProductImagesSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'id'

class ProductImagesLCAPIView(generics.ListCreateAPIView):
    queryset                =   ProductImages.objects.all()
    serializer_class        =   ProductImagesSerializer
    permission_classes      =   []
    authentication_classes  =   []




class ProductContentListAPIView(generics.ListCreateAPIView):
    queryset                =   Content.objects.all()
    serializer_class        =   ProductContentSerializer
    permission_classes      =   []
    authentication_classes  =   []

    def get(self,request,id=None):
        try:
            product             =    ContentCategory.objects.get(id=id)
            queryset            =    Content.objects.filter(ContentCategory=product)
            serialize           =    ProductContentSerializer(queryset, many=True,context={'request': request})
            return Response(serialize.data)
        except:
            return Response([])

class ProductContentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =   Content.objects.all()
    serializer_class        =   ProductContentSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'id'



class ProductContentLCAPIView(generics.ListCreateAPIView):
    queryset                =   Content.objects.all()
    serializer_class        =   ProductContentSerializer
    permission_classes      =   []
    authentication_classes  =   []




class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductDetailSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'product_id'

class ProductDetailForScannerAPIView(generics.RetrieveAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductDetailSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'product_code'



class ProductListAPIView(generics.ListAPIView):
    # queryset                =   Product.objects.all()
    serializer_class        =   ProductSerializer
    permission_classes      =   []
    authentication_classes  =   []



    def get_queryset(self):
        request    =    self.request
        print(request.user)
        queryset   =    Product.objects.filter(active=True)
        print(queryset)
        return queryset


class ProductSearchAPIView(generics.ListAPIView):
    # queryset                =   Product.objects.all()
    serializer_class        =   ProductSerializer
    permission_classes      =   []
    authentication_classes  =   []



    def get_queryset(self):
        request    =    self.request
        queryset   =    Product.objects.all()
        query      =    request.GET.get('q')
        query2      =    request.GET.get('category')
        if query is not None:
            queryset     =    queryset.filter(Q(product_name__icontains=query))
                                                # Q(brand_name__icontains=query))
                                                # Q(shop__icontains=query))

        if query2 is not None:
            queryset     =    queryset.filter(Category=query2)

        return queryset



class ProductCreateAPIView(generics.CreateAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductCreateSerializer
    permission_classes      =   []
    authentication_classes  =   [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

    # @login_required
    def post(self,request,*args,**kwargs):
        try:
            self.create(request,*args,**kwargs)
            return Response({"status":201,"message":"product created"})
        except:
            return Response({"message":"form invaild and price,quantity are integer field"})

    def perform_create(self,serializer):
        shop_name       =   self.request.user.shopprofile
        serializer.save(user=self.request.user,shop_name=shop_name)


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductCreateSerializer
    permission_classes      =   [IsOwnerOrReadOnly]
    authentication_classes  =   [SessionAuthentication]
    lookup_field            =   'product_id'


class GetProductById(generics.ListAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductListOfUserSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'user'
    
    def get(self,request,user,*args,**kwargs):
        queryset     =    Product.objects.filter(user=user) 
        serializer   =    ProductListOfUserSerializer(queryset,many=True,context={'request': request})       
        return Response(serializer.data)
    

class ProductListOfUserAPIView(generics.GenericAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductListOfUserSerializer
    permission_classes      =   []
    authentication_classes  =   [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]



    def get(self,request):
        # request    =    self.request
        user       =    request.user
        queryset   =    Product.objects.filter(user=user)
        print(queryset)
        # query      =    request.GET.get('q')
        serialize  =    ProductListOfUserSerializer(queryset,context={'request': request},many=True)
        return Response(serialize.data)



class ProductDetailOfListAPIView(generics.RetrieveAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductDetailForListSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   'product_id'


class ProductEditAPIView(generics.UpdateAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductUpdateSerializer
    permission_classes      =   []
    authentication_classes  =   [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]
    lookup_field            =   'product_id'


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset                =   Product.objects.all()
    serializer_class        =   ProductUpdateSerializer
    permission_classes      =   []
    authentication_classes  =   [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]
    lookup_field            =   'product_id'


class CategoriesAPIView(generics.CreateAPIView):
    queryset                =   Categories.objects.all()
    serializer_class        =   CreateCatSerializer
    permission_classes      =   []
    authentication_classes  =   []

class CategoriesListAPIView(generics.ListAPIView):
    queryset                =   Categories.objects.all()
    serializer_class        =   CreateCatSerializer
    permission_classes      =   []
    authentication_classes  =   []

class CategoriesRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =   Categories.objects.all()
    serializer_class        =   CreateCatSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field            =   "id"    


class ContentCategoryListAPIView(generics.GenericAPIView):
    # serailizer_class        =   CategoryContentSerializer
    permission_classes      =   []
    authentication_classes  =   []
    queryset                =   ContentCategory.objects.all()


    def get(self,request,product_id=None):
        queryset            =   ContentCategory.objects.filter(Product=product_id)
        print(queryset)
        serialize           =   CategoryContentSerializer(queryset,many=True,context={'request': request})
        print(serialize.data)
        return Response(serialize.data)


class ContentCategoryLCAPIView(generics.ListCreateAPIView):
    queryset                =   ContentCategory.objects.all()
    permission_classes      =   []
    authentication_classes  =   []
    serializer_class        =   CategoryContentSerializer


class ContentCategoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =   ContentCategory.objects.all()
    permission_classes      =   []
    authentication_classes  =   []
    serializer_class        =   CategoryContentSerializer
    lookup_field            =    "id"

