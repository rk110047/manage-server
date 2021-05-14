from django.urls import path
from .views import AddressCreateAPIView
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('',csrf_exempt(AddressCreateAPIView.as_view()),name="address create"),
    # path('billing/',csrf_exempt(BillingAddressCreateAPIView.as_view()),name="billing address create")

]
