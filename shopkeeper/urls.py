from django.urls import path
from .views import ShopProfileCreateAPIView,ShopsAPIView,ShopProfileDetailAPIView,ShopProfileEditAPIView,ShopsListAPIView,ShopCategoriesLCAPIView,ShopSearchAPIView


app_name="shop"

urlpatterns=[
    path('create-shop-profile/',ShopProfileCreateAPIView.as_view(),name='shop profile'),
    path('detail/',ShopProfileDetailAPIView.as_view(),name='shop detail'),
    path('edit/<id>',ShopProfileEditAPIView.as_view(),name='shop edit'),
    # path('create-shop-profile/image/',ShopImageCreateAPIView.as_view(),name="shop image"),
    # path('create-shop-profile/image/edit/<shop>',ShopImageUpdateAPIView.as_view(),name="edit shop image"),
    path('',ShopsAPIView.as_view(),name='shops'),
    path('list/',ShopsListAPIView.as_view(),name='shops list'),
    path('shopcat/LC/',ShopCategoriesLCAPIView.as_view(),name='shop categories'),
    path('search/',ShopSearchAPIView.as_view())



]



