from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static
from billing.views import CardCreateAPIView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
    path('product/',include('product.urls')),
    path('customer/',include('customer.urls')),
    path('shops/',include('shopkeeper.urls')),
    path('auth/api/',obtain_jwt_token),
    path('cart/',include('cart.urls')),
    path('address/',include('addresses.urls')),
    path('orders/',include('orders.urls')),
    path('delivery/',include('delivery.urls')),
    path('collector/',include('collector.urls')),
    path('billing/',include('billing.urls')),
    path('ewallet/',include('ewallet.urls')),
    path('accounts/', include('allauth.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
