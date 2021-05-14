from django.urls import path
from .views import Strip_Payment_Form,CardCreateAPIView,thankyou,failed,Wallet_Stripe_Payment_Form,withdraw,adminLogin


urlpatterns =[
	path('card-form/',Strip_Payment_Form),
	path('card-form-for-wallet/',Wallet_Stripe_Payment_Form),
	path('thankyou/',thankyou),
	path('failed/',failed),
	path('withdraw/',withdraw,name="withdraw"),
	path('adminLogin/',adminLogin,name="adminLogin"),

]
