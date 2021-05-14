from django.urls import path
from .views import EwalletDetailAPIView,PayMoney


urlpatterns = [
	path('detail/',EwalletDetailAPIView.as_view()),
	path('pay/',PayMoney.as_view())

]
