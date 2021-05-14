from django.urls import path
from .views import CreateProfileAPIView,EditProfileAPIView,CustomerListAPIView,CustomerDetailAPIView



urlpatterns=[
    path('create/',CreateProfileAPIView.as_view()),
    path('detail/',CustomerDetailAPIView.as_view()),
    path('update/<User>/',EditProfileAPIView.as_view()),
    path('list/',CustomerListAPIView.as_view())


]
