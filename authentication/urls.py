from django.urls import path
from .views import RegisterAPIView,LoginAPIView,RegisteredBySuperUserAPIView,LoginWithTokenAuthenticationAPIView,SuperUserCheckAPIView

from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

     # <-- And here


urlpatterns=[
    path('login/',LoginAPIView.as_view(),name='login'),
    path('login/token/',LoginWithTokenAuthenticationAPIView.as_view(),name='login for token'),
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('special/register/',RegisteredBySuperUserAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('super-check/',SuperUserCheckAPIView.as_view(),name='superuser check'),



]
