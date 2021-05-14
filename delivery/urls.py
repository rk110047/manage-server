from django.urls import path
from .views import DeliveryPersonProfileAPIView,DeliveryPersonProfileCreateAPIView,DeliveryPersonRUDAPIView


urlpatterns =[
	path('profile/',DeliveryPersonProfileAPIView.as_view(),name='delivery person profile'),
	path('profile/create/',DeliveryPersonProfileCreateAPIView.as_view(),name='delivery person profile create'),
	path('profile/RUD/<id>/',DeliveryPersonRUDAPIView.as_view(),name='delivery person RUD'),
]
