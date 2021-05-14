from django.urls import path
from .views import CheckOutAPIView2,OrderItemCreateAPIView,CartAPIView,ItemCreateAPIView,RemoveItemFromCartAPIView,CheckOutAPIView,OrderItemDeleteAPIView,getCartAPIView,orderItemCartAPIView,orderItemRUDAPIView,orderItemLCAPIView,FavouriteOrderItemsAPIView,FavouriteItemCreateAPIView,AddToFavourites,OrderItemQuantityDecreaseAPIView,OrderItemQuantityIncreaseAPIView



app_name="cart"


urlpatterns=[
    path('',CartAPIView.as_view(),name='cart'),
    path('get/<id>',getCartAPIView.as_view()),
    path('order_item/<item_id>',orderItemCartAPIView.as_view(),name="order_item"),
    path('checkout/',CheckOutAPIView.as_view(),name='cart'),
    path('checkout2/<id>/',CheckOutAPIView2.as_view(),name='cart2'),
    path('add_to_cart/<product_id>/',ItemCreateAPIView.as_view(),name="add_to_cart"),
    path('remove_from_cart/<product_id>/',RemoveItemFromCartAPIView.as_view(),name="remove_from_cart"),
    path('delete_item_from_cart/<item_id>/',OrderItemDeleteAPIView.as_view(),name="delete_item_from_cart"),
    path('LC/order_item/',orderItemLCAPIView.as_view()),
    path('RUD/order_item/<item_id>/',orderItemRUDAPIView.as_view()),
    path('order_item/infavourites/',FavouriteOrderItemsAPIView.as_view()),
    path('order_item/add_in_favourites/<item_id>',AddToFavourites.as_view(),name="add to favourites"),
    path('order_item/infavourites/add_to_cart/<item_id>',FavouriteItemCreateAPIView.as_view()),
    path('order_item/create/',OrderItemCreateAPIView.as_view()),
    path('order_item/quantity_decrease/<item_id>/',OrderItemQuantityDecreaseAPIView.as_view()),
    path('order_item/quantity_increase/<item_id>/',OrderItemQuantityIncreaseAPIView.as_view())



]
