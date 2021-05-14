from django.urls import path
from .views import CollectorPersonProfileAPIView,CollectorPersonProfileCreateAPIView,CollectorPersonRUDAPIView


urlpatterns =[
	path('profile/',CollectorPersonProfileAPIView.as_view(),name='delivery person profile'),
	path('profile/create/',CollectorPersonProfileCreateAPIView.as_view(),name='delivery person profile create'),
	path('profile/RUD/<id>/',CollectorPersonRUDAPIView.as_view(),name='delivery person RUD'),
]
