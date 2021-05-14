from django.shortcuts import render,redirect
from .models import Card,BillingProfile
from .serializer import CardSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from ewallet.models import EWallet

from django.http import HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib.auth import authenticate,login

# Create your views here.
import stripe
stripe.api_key = "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"


class CardCreateAPIView(generics.CreateAPIView):
    queryset                        =   Card.objects.all()
    serializer_class                =   CardSerializer
    permission_classes              =   []
    authentication_classes          =   [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


    def post(self,request,*args,**kwargs):
        self.create(request,*args,**kwargs)
        card = stripe.Token.create(
			  card={
			    "number": "4242424242424242",
			    "exp_month": 10,
			    "exp_year": 2021,
			    "cvc": "314",
			  },
			)
        return Response({"token":card.id})

    def perform_create(self,serializer):
        print(self.request.user)
        User       =   self.request.user
        serializer.save(User=User)





def Strip_Payment_Form(request):
	order_id     =   request.GET.get('order_id')
	print(order_id)
	if request.method=="POST":
		order_id     =   request.GET.get('order_id')
		print(request.POST)
		token    =  request.POST["stripeToken"]
		return redirect(F"https://management.ezswiftshops.com/orders/stripe-checkout-payment/?order_id={order_id}&token={token}")
	context={"order_id":order_id}
	return render(request,'stripe-form.html',context)




def thankyou(request):
	return render(request,'thankyou.html',{})


def failed(request):
	return render(request,'failed.html',{})
def Wallet_Stripe_Payment_Form(request):
	amount     =   request.GET.get('amount')
	id         =   request.GET.get('id')
	if request.method=="POST":
		id         =   request.GET.get('id')
		amount     =   request.GET.get('amount')
		print(request.POST)
		token    =  request.POST["stripeToken"]
		return redirect(F"http://100.25.15.160/orders/stripe-wallet-payment/?amount={amount}&token={token}&id={id}")
	context={"amount":amount,'id':id}
	return render(request,'strip-form-for-wallet.html',context)




def withdraw(request):

	if request.method=="POST":
		email=request.POST.get('email')
		ammount=float(request.POST.get('ammount'))
		balance=float(request.POST.get('accountAmmount'))
		remainder=balance-ammount

		if remainder<0:
			return HttpResponse('not sufficient balance')
		updated_rows = BillingProfile.objects.filter(email=email).update(ammount=remainder)
		if updated_rows:
			return HttpResponse('success')
	else:
		profile=BillingProfile.objects.all()
		#pagination
		paginator=Paginator(profile,7)
		page_number=request.GET.get('page')
		page_obj=paginator.get_page(page_number)

		return render(request,'withdraw.html',{'profile':page_obj})


def adminLogin(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('/billing/withdraw/')
		else:
			return HttpResponse('not login')

		#return render(request, 'withdraww.html')
	return render(request,'adminLogin.html')
		
