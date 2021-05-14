from django.shortcuts import render,redirect
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from .serializer import StripeTokenSerializer,OrderDetailSerializer,OrderDetailSerializerForDelivery
from rest_framework.response import Response
from .models import Order
from cart.models import Cart,OrderItem
from .models import Order
from ewallet.models import EWallet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.utils import timezone 
import datetime
import stripe
import decimal
import smtplib
from decimal import Decimal
stripe.api_key = "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"




def send_email(clientEmail):
	#Ports 465 and 587 are intended for email client to email server communication - sending email
	server = smtplib.SMTP_SSL('mail.ezswiftshops.com', 465)

	#starttls() is a way to take an existing insecure connection and upgrade it to a secure connection using SSL/TLS.
	#server.starttls()

	#Next, log in to the server
	user = server.login('no-reply@ezswiftshops.com', 'ezswiftshops@1')
	print(user)
	msg = "orderSuccessfull"

	#Send the mail
	res = server.sendmail('no-reply@ezswiftshops.com',clientEmail , msg)
	print(res)

def shopMoneyAdd(shop,ammount):
	user 				=		shop.user
	account 			=		user.billingprofile
	ammount2 			=		Decimal(ammount)*Decimal(0.10)
	ammount             =       Decimal(ammount)-Decimal(ammount2)
	account.ammount 	=		Decimal(account.ammount)+Decimal(ammount)
	account.save()



def deliveryPersonMoneyAdd(deliveryBoy,ammount):
	user 				=		deliveryBoy.user
	account 			=		user.billingprofile
	ammount2 			=		Decimal(ammount)*Decimal(0.10)
	ammount             =       Decimal(ammount)
	account.ammount 	=		Decimal(account.ammount)+Decimal(ammount)
	account.save()

def orderdetail(request):
	order_id  = request.GET.get('order_id')
	query 	  =	Order.objects.get(order_id=order_id)
	query1    = query.cart.product
	return render(request,'detail.html',{"obj":query,"obj1":query1})

class OrdersAPIView(generics.ListAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,SessionAuthentication]



	def get_queryset(self):
		request 	        =	self.request
		billing_profile		=	request.user.billingprofile
		queryset			=	Order.objects.filter(billing_profile=billing_profile,ordered=True)
		return queryset



class OrdersDetailAPIView(generics.RetrieveAPIView):
	queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]
	lookup_field                =       "id"


class PlaceOrder(generics.GenericAPIView):
	queryset		    		= 		[]
	serializer_class			=		[]
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


	def get(self,request):
		request				=	self.request
		user 				=   request.user
		billing_profile     =   user.billingprofile
#		qs 					=	Cart.objects.filter(User=user,active=True)
#		try:
#			qs                  =   qs.first()
#			qs.active			=	False
#			qs.save()
#		except:
#			print(qs)	
#		qs1         		=   OrderItem.objects.filter(User=user,active=True)
#		try:
#			for x in qs1:
#				x.active		=	False
#				x.save()
#		except:
#			print(qs1)
		qs2					=	Order.objects.filter(billing_profile=billing_profile,active=True,ordered=False)
		try:
			status 			     =   self.request.GET.get('status')
			instruction 		 =	 self.request.GET.get('instructions')
			if status and instruction:
				if status=="HOME DELIVERY":
					delivery_schedule    =   self.request.GET.get('delivery_schedule')
					print(status)
					qs2                  	=   qs2.first()
					date                    =   str(datetime.datetime.now().date())
					time                    =   str(datetime.datetime.now().time())
					qs2.ordered_date     	=   "Date "+ date +" Time "+ time
					qs2.delivery_schedule	=	delivery_schedule
					qs2.delivery_status   	=   status
					qs2.special_instructions=   instruction
#					qs2.ordered          	=   True
					qs2.save()
				else:
					delivery_schedule    =   self.request.GET.get('delivery_schedule')
					print(status)
					qs2                  	=   qs2.first()
					date                    =   str(datetime.datetime.now().date())
					time                    =   str(datetime.datetime.now().time())
					qs2.ordered_date     	=   "Date "+ date +" Time "+ time
					qs2.total  				=	decimal.Decimal(qs2.total)-decimal.Decimal(qs2.shipping_total)
					qs2.shipping_total		=	0.00
					qs2.delivery_schedule	=	delivery_schedule
					qs2.delivery_status   	=   status
					qs2.special_instructions=   instruction
#					qs2.ordered          	=   True
					qs2.save()	
			elif status:
				if status=="HOME DELIVERY":
					delivery_schedule    =   self.request.GET.get('delivery_schedule')
					print(status)
					qs2                  	=   qs2.first()
					date                    =   str(datetime.datetime.now().date())
					time                    =   str(datetime.datetime.now().time())
					qs2.ordered_date     	=   "Date "+ date +" Time "+ time
					qs2.delivery_schedule	=	delivery_schedule
					qs2.delivery_status   	=   status
#					qs2.ordered          	=   True
					qs2.save()
				else:
					delivery_schedule    =   self.request.GET.get('delivery_schedule')
					print(status)
					qs2                  	=   qs2.first()
					date                    =   str(datetime.datetime.now().date())
					time                    =   str(datetime.datetime.now().time())
					qs2.ordered_date     	=   "Date "+ date +" Time "+ time
					qs2.total  				=	decimal.Decimal(qs2.total)-decimal.Decimal(qs2.shipping_total)
					qs2.shipping_total		=	0.00
					qs2.delivery_schedule	=	delivery_schedule
					qs2.delivery_status   	=   status
#					qs2.ordered          	=   True
					qs2.save()
			else:
				qs2                  	=   qs2.first()
				qs2.ordered_date     	=   datetime.datetime.now().date()
#				qs2.ordered          	=   True
				print(qs2.ordered)
				qs2.save()
		except:
			qs2					=	Order.objects.filter(billing_profile=billing_profile,active=True,ordered=False)
			qs2                  =   qs2.first()
			qs2.ordered_date     =   datetime.datetime.now().date()
#			qs2.ordered          =   True
			qs2.save()
			print("ActiveDeliveryPersonOrder")
		return Response("ok")

'''class PlaceOrder(generics.GenericAPIView):
	queryset		    		= 		[]
	serializer_class			=		[]
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,SessionAuthentication]


	def get(self,request):
		request				=	self.request
		user 				=   request.user
		billing_profile     =   user.billingprofile
		qs 					=	Cart.objects.filter(User=user,active=True)
		try:
			qs                  =   qs.first()
			qs.active			=	False
			qs.save()
		except:
			print(qs)	
		qs1         		=   OrderItem.objects.filter(User=user,active=True)
		try:
			for x in qs1:
				x.active		=	False
				x.save()
		except:
			print(qs1)
		qs2					=	Order.objects.filter(billing_profile=billing_profile,active=True,ordered=False)
		try:
			status 			     =   self.request.GET.get('status')
			if status:
				delivery_schedule    =   self.request.GET.get('delivery_schedule')
                                qs2                     =   qs2.first()
			        qs2.delivery_schedule	=   delivery_schedule
				qs2.delivery_status   	=   status
				qs2.ordered          	=   True
				qs2.save()
			else:
				qs2                  	=   qs2.first()
				qs2.ordered_date     	=   datetime.datetime.now().date()
				qs2.ordered          	=   True
				qs2.save()
		except:
			qs2					=	Order.objects.filter(billing_profile=billing_profile,active=True,ordered=False)
			qs2                  =   qs2.first()
			qs2.ordered_date     =   datetime.datetime.now().date()
			qs2.ordered          =   True
			qs2.save()
		return Response("ok")'''



class ShopOrdersAPIView(generics.ListAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,SessionAuthentication]



	def get_queryset(self):
		request 	        =	self.request
		shop				=	request.user.shopprofile
		queryset			=	Order.objects.filter(shop=shop,shipped=True)
		return queryset



class OrderForDelivery(generics.ListAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializerForDelivery
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]



	def get_queryset(self):
		request 	        =	self.request
		shop				=	request.user.deliverypersonprofile
		queryset			=	Order.objects.filter(delivery_status="HOME DELIVERY",order_status="ORDER READY",cancelled=False,delivery_person=None,ordered=True)
		return queryset


class OrdersRecieved(generics.ListAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializerForDelivery
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,SessionAuthentication]



	def get_queryset(self):
		request 	        =	self.request
		shop				=	request.user.shopprofile
		queryset			=	Order.objects.filter(shop=shop,order_status="generated",cancelled=False,delivery_person=None,ordered=True)
		return queryset


class PickOrderForDelivery(generics.GenericAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


	def  get(self,request,id=None,*args,**kwargs):
		order                    =	Order.objects.get(id=id)
		if order.delivery_person==None:
			user				     =	self.request.user
			delivery_person		     =	user.deliverypersonprofile
			pending					 =	Order.objects.filter(delivery_person=  delivery_person,cancelled=False,shipped=False)
			if pending.count()==0:
				order                    =	Order.objects.get(id=id)
				order.delivery_person    =  delivery_person
				order.save()
				print(delivery_person)
				return Response({"message":"order accepted"})
			else:
				response      = {"message":"already have another order"}
				return Response(response)

		else:
			response      = {"message":"already accepted by other delivery person"}
			return Response(response)



class ActiveDeliveryPersonOrder(generics.ListAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializerForDelivery
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

	def get_queryset(self):
		user				     =	self.request.user
		delivery_person		     =	user.deliverypersonprofile
		pending					 =	Order.objects.filter(delivery_person=  delivery_person,cancelled=False,shipped=False)
		# serialize                =  OrderDetailSerializerForDelivery(pending,context={'request': request})
		return pending
	




class OutForDelivery(generics.GenericAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


	def  get(self,request,id=None,*args,**kwargs):
		order                    =	Order.objects.get(id=id)
		order.order_status		 =	'OUT FOR DELIVERY'
		order.save()
		return Response({"message":"out for delivery"})

class CancelDelivery(generics.GenericAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


	def  get(self,request,id=None,*args,**kwargs):
		order                    =	Order.objects.get(id=id)
		order.order_status		 =	'CANCELLED'
		order.cancelled 		 =	True
		order.save()
		return Response({"message":"delivery cancelled"})
class OrderShipped(generics.GenericAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


	def  get(self,request,id=None,*args,**kwargs):
		order                    =	Order.objects.get(id=id)
		if order.shipped==False:
			order.order_status		 =	'SHIPPED'
			order.shipped            =   True
			order.save()
			shopMoneyAdd(order.shop,order.sub_total)
			if order.delivery_person:
				deliveryPersonMoneyAdd(order.delivery_person,order.shipping_total)
			return Response({"message":"order shipped"})
		return Response({"message":"already shipped"})

class AcceptOrderByShop(generics.GenericAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


	def  get(self,request,id=None,*args,**kwargs):
		try:
			order_preparation_time   =  self.request.GET.get("order_preparation_time")
			if len(order_preparation_time)==0:
				return Response({"message":"please set preparation time "})
			else:
				order                    =	Order.objects.get(id=id)
				order.order_preparation_time = order_preparation_time
				order.order_status		 =	'ACCEPTED BY SHOP'
				order.accepted_by_shop   =   True
				order.save()
				return Response({"message":"order accepted by shop"})
		except:
			return Response({"message":"please set preparation time "})
		



class ShopActiveOrdersAPIView(generics.ListAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

	def get_queryset(self):
		shop                    =        self.request.user.shopprofile
		queryset                =        Order.objects.filter(accepted_by_shop=True,shop=shop,cancelled=False,shipped=False)
		return queryset



class OrdersShippedByDeliveryPersonAPIView(generics.ListAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

	def get_queryset(self):
		delivery       			=		self.request.user.deliverypersonprofile
		queryset 				=		Order.objects.filter(delivery_person=delivery,order_status="SHIPPED")
		return queryset


class OrderReadyAPIView(generics.GenericAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


	def  get(self,request,id=None,*args,**kwargs):
		order                    =	Order.objects.get(id=id)
		order.order_status		 =	'ORDER READY'
		order.order_ready        =   True
		order.save()
		return Response({"message":"order ready"})



class PickOrderForCollection(generics.GenericAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


	def  get(self,request,id=None,*args,**kwargs):
		order                    =	Order.objects.get(id=id)
		if order.collector==None:
			user				     =	self.request.user
			collector		     	 =	user.collectorprofile
			pending					 =	Order.objects.filter(collector=  collector,cancelled=False,shipped=False,order_ready=False)
			if pending.count()==0:
				order                    =	Order.objects.get(id=id)
				order.collector          =  collector
				order.save()
				print(collector)
				return Response({"message":"order accepted"})
			else:
				response      = {"message":"already have another order"}
				return Response(response)

		else:
			response      = {"message":"already accepted by other delivery person"}
			return Response(response)


class ActiveCollectorPersonOrder(generics.ListAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializerForDelivery
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

	def get_queryset(self):
		user				     =	self.request.user
		collector		         =	user.collectorprofile
		pending					 =	Order.objects.filter(collector=  collector,cancelled=False,shipped=False,order_ready=False)
		# serialize                =  OrderDetailSerializerForDelivery(pending,context={'request': request})
		return pending

class AppointACollectorAPIView(generics.GenericAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializer
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


	def  get(self,request,id=None,*args,**kwargs):
		order                    =	Order.objects.get(id=id)
		order.appoint_collector        =   True
		order.save()
		return Response({"message":"order appoint for collector"})

class OrdersForCollection(generics.ListAPIView):
	# queryset		    		= 		Order.objects.all()
	serializer_class			=		OrderDetailSerializerForDelivery
	permission_classes  		=    	[]
	authentication_classes		=		[TokenAuthentication,SessionAuthentication]



	def get_queryset(self):
		request 	        =	self.request
		collector			=	request.user.collectorprofile
		queryset			=	Order.objects.filter(order_ready=False,cancelled=False,collector=None,ordered=True,appoint_collector=True)
		return queryset


class StripPaymentAPIView(generics.GenericAPIView):
	# queryset                =       OrderItem.objects.all()
    serializer_class        =       StripeTokenSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


    def get(self,request):
    	order_id          =   self.request.GET.get("order_id")
    	order		      =	Order.objects.get(order_id=order_id)
    	user              =   order.User
    	amount			  =	int(decimal.Decimal(order.total)*decimal.Decimal(100))
    	token             = self.request.GET.get("token")
    	charge            = stripe.Charge.create(
		  amount=amount,
		  currency="usd",
		  description=order_id,
		  source=token,)
    	if charge.status=="succeeded":
    		qs 					=	Cart.objects.filter(User=user,active=True)
    		try:
    			qs                  =   qs.first()
    			qs.active			=	False
    			qs.save()
    		except:
    			print(qs)
    		qs1         		=   OrderItem.objects.filter(User=user,active=True)
    		try:
    			for x in qs1:
    				x.active		=	False
    				x.save()
    		except:
    			print(qs1)
    		order.ordered=True
    		order.save()
    		send_email(user.email)
    		return redirect("https://management.ezswiftshops.com/billing/thankyou/")
    	return redirect("https://management.ezswiftshops.com/billing/failed/")


class StripPaymentForWalletAPIView(generics.GenericAPIView):
	# queryset                =       OrderItem.objects.all()
    serializer_class        =       StripeTokenSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


    def get(self,request):
    	print(self.request.GET.get("amount"))
    	amount            =   int(decimal.Decimal(self.request.GET.get("amount"))*decimal.Decimal(100))
    	token             = self.request.GET.get("token")
    	Id                = self.request.GET.get("id")
    	wallet            =  EWallet.objects.get(id=Id)
    	charge            = stripe.Charge.create(
		  amount=amount,
		  currency="usd",
		  description=Id,
		  source=token,)
    	if charge.status=="succeeded":
    		wallet.money  = decimal.Decimal(wallet.money)+decimal.Decimal(self.request.GET.get("amount"))
    		wallet.save()
    		return redirect("https://management.ezswiftshops.com/billing/thankyou/")
    	return redirect("https://management.ezswiftshops.com/billing/failed/")


class EWalletPaymentAPIView(generics.GenericAPIView):
	# queryset                =       OrderItem.objects.all()
    serializer_class        =       StripeTokenSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


    def get(self,request):
    	order_id          =   self.request.GET.get("order_id")
    	order		      =	Order.objects.get(order_id=order_id)
    	user              =   order.User
    	amount			  =	decimal.Decimal(order.total)
    	if decimal.Decimal(user.ewallet.money)>decimal.Decimal(amount):
    		user.ewallet.money  =  decimal.Decimal(user.ewallet.money)-decimal.Decimal(amount)
    		user.ewallet.save()
    		qs 					=	Cart.objects.filter(User=user,active=True)
    		try:
    			qs                  =   qs.first()
    			qs.active			=	False
    			qs.save()
    		except:
    			print(qs)
    		qs1         		=   OrderItem.objects.filter(User=user,active=True)
    		try:
    			for x in qs1:
    				x.active		=	False
    				x.save()
    		except:
    			print(qs1)
    		order.ordered=True
    		order.save()
    		return Response({"status":200})
    	return Response({"status":402})
