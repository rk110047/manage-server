from django.urls import path
from .views import orderdetail,EWalletPaymentAPIView,StripPaymentForWalletAPIView,StripPaymentAPIView,OrdersForCollection,AppointACollectorAPIView,ActiveCollectorPersonOrder,PickOrderForCollection,OrdersDetailAPIView,OrdersAPIView,PlaceOrder,ShopOrdersAPIView,OrderForDelivery,PickOrderForDelivery,OutForDelivery,CancelDelivery,AcceptOrderByShop,OrdersRecieved,OrderShipped,ActiveDeliveryPersonOrder,OrdersShippedByDeliveryPersonAPIView,ShopActiveOrdersAPIView,OrderReadyAPIView

app_name="order"

urlpatterns =[
	path("order-detail/",orderdetail,name="detail"),
	path("",OrdersAPIView.as_view(),name='orders'),
        path("detail/<id>",OrdersDetailAPIView.as_view(),name='order detail'),
	path("ordersfordelivery/",OrderForDelivery.as_view(),name="order for delivery"),
	path("ordersfordelivery/shipped/",OrdersShippedByDeliveryPersonAPIView.as_view(),name="order shipped by delivery person"),
	path("ordersfordelivery/active/",ActiveDeliveryPersonOrder.as_view(),name="active delivery"),
	path("ordersfordelivery/add_person/<id>/",PickOrderForDelivery.as_view(),name="delivery"),
	path("ordersfordelivery/outfordelivery/<id>/",OutForDelivery.as_view(),name="out for delivery"),
	path("ordersfordelivery/cancel-delivery/<id>/",CancelDelivery.as_view(),name="cancel delivery"),
	path("ordersfordelivery/accept-order/<id>/",AcceptOrderByShop.as_view(),name="accept order"),
	path("ordersfordelivery/ship-order/<id>/",OrderShipped.as_view(),name="ship order"),
	path("ordersfordelivery/order-ready/<id>/",OrderReadyAPIView.as_view(),name="order ready"),
	path("shoporders/",OrdersRecieved.as_view(),name='shop orders'),
	path("shoporders/active/",ShopActiveOrdersAPIView.as_view(),name='shop active orders'),
	path("shoporders/old/",ShopOrdersAPIView.as_view(),name='shop old orders'),
	path("place/",PlaceOrder.as_view(),name="place order"),
	path("ordersforcollection/",OrdersForCollection.as_view()),
	path("ordersforcollection/<id>/",PickOrderForCollection.as_view(),name="pick order for collection"),
	path("ordersforcollection/active/order/",ActiveCollectorPersonOrder.as_view()),
	path("ordersforcollection/appoint_collector/<id>/",AppointACollectorAPIView.as_view(),name="appoint collector"),
        path('stripe-checkout-payment/',StripPaymentAPIView.as_view()),
        path('stripe-wallet-payment/',StripPaymentForWalletAPIView.as_view()),
        path('ewallet-checkout-payment/',EWalletPaymentAPIView.as_view())

]
