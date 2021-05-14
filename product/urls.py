from django.urls import path
from .views import ProductRUDAPIView,ProductLCAPIView,ContentCategoryRUDAPIView,ContentCategoryLCAPIView,ContentCategoryListAPIView,CategoriesRUDAPIView,ProductImagesListAPIView,ProductImagesRUDAPIView,ProductCreateAPIView,ProductContentListAPIView,ProductContentRUDAPIView,ProductListAPIView,ProductSearchAPIView,ProductUpdateAPIView,ProductDetailAPIView,GetProductById,ProductDetailForScannerAPIView,ProductListOfUserAPIView,ProductDetailOfListAPIView,ProductEditAPIView,ProductDeleteAPIView,CategoriesAPIView,CategoriesListAPIView,ProductImagesLCAPIView,ProductContentLCAPIView,ProductTaxLCAPIView,ProductTaxRUDAPIView,ProductTaxListAPIView


app_name='product'

urlpatterns=[
    path('',ProductListAPIView.as_view(),name='products'),
    path('LC/',ProductLCAPIView.as_view(),name='product LC'),
    path('RUD/<product_id>/',ProductRUDAPIView.as_view(),name='product RUD'),
    path('create/',ProductCreateAPIView.as_view(),name='create product'),
    path('search/',ProductSearchAPIView.as_view(),name='search product'),
    path('listofuser/',ProductListOfUserAPIView.as_view(),name='user products list'),
    path('update/<product_id>',ProductUpdateAPIView.as_view(),name='update product'),
    path('detail/<product_id>',ProductDetailAPIView.as_view(),name='detail product'),
    path('detailoflist/<product_id>',ProductDetailOfListAPIView.as_view(),name='detail of product'),
    path('edit/<product_id>',ProductEditAPIView.as_view(),name='edit product'),
    path('delete/<product_id>',ProductDeleteAPIView.as_view(),name='delete product'),
    path('scan/<product_code>',ProductDetailForScannerAPIView.as_view(),name='scan and get'),
    path('shop_product/<user>',GetProductById.as_view(),name="shops product"),
    path('create/cat/',CategoriesAPIView.as_view(),name="create cat"),
    path('list/cat/',CategoriesListAPIView.as_view(),name="list cat"),
    path('cat/RUD/<id>',CategoriesRUDAPIView.as_view()),
    path('contents/<id>',ProductContentListAPIView.as_view(),name="product contents"),
    path('contents/RUD/<id>',ProductContentRUDAPIView.as_view(),name="contents RUD"),
    path('contents/LC/',ProductContentLCAPIView.as_view()),
    path('images/LC/',ProductImagesLCAPIView.as_view()),
    path('images/<product_id>',ProductImagesListAPIView.as_view(),name="product images"),
    path('images/RUD/<id>',ProductImagesRUDAPIView.as_view(),name="images RUD"),
    path('content_category/<product_id>/',ContentCategoryListAPIView.as_view(),name="content category list"),
    path('contentcategory/create/',ContentCategoryLCAPIView.as_view(),name="content category create"),
    path('contentcategory/RUD/<id>',ContentCategoryRUDAPIView.as_view(),name="content category RUD"),
    path('tax/LC/',ProductTaxLCAPIView.as_view(),name="product tax LC"),
    path('tax/<product_id>/',ProductTaxListAPIView.as_view(),name="product tax list"),
    path('tax/RUD/<id>/',ProductTaxRUDAPIView.as_view(),name="product tax RUD"),


]
