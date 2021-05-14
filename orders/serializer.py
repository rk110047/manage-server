from rest_framework import serializers
from .models import Order
from delivery.serializer import DeliveryPersonDetailSerializer
from addresses.serializer import AddressSerializer
from shopkeeper.serializer import ShopsSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from cart.serializer import CartDetailforOrderSerializer,OrderItemDetailSerializer,CartDetailSerializer
from product.serializer import ProductDetailSerializer
from customer.serializer import CustomerProfileSerializer 



class OrderDetailSerializer(WritableNestedModelSerializer):
	customer        		= 	CustomerProfileSerializer()
	cart 					= 	CartDetailforOrderSerializer()
	shipping_address		= 	AddressSerializer()
	shop					=	ShopsSerializer()
	delivery_person         =   DeliveryPersonDetailSerializer()
	outfordelivery 		    =	serializers.HyperlinkedIdentityField(view_name="order:out for delivery",lookup_field="id")
	cancel_order		    =	serializers.HyperlinkedIdentityField(view_name="order:cancel delivery",lookup_field="id")
	click_order_ready 		    =	serializers.HyperlinkedIdentityField(view_name="order:order ready",lookup_field="id")	
	ship_order                              =       serializers.HyperlinkedIdentityField(view_name="order:ship order",lookup_field="id")
	click_appoint_collector =	serializers.HyperlinkedIdentityField(view_name="order:appoint collector",lookup_field="id")	
	order_detail            =	serializers.HyperlinkedIdentityField(view_name="order:order detail",lookup_field="id")	


	class Meta:
		model 		= Order
		fields 		= "__all__"


class OrderDetailSerializerForDelivery(WritableNestedModelSerializer):

	cart 					= 	CartDetailforOrderSerializer()
	shipping_address		= 	AddressSerializer()
	customer        		= 	CustomerProfileSerializer()
	shop					=	ShopsSerializer()
	delivery_person         =   DeliveryPersonDetailSerializer()
	acceptbyperson          =   serializers.HyperlinkedIdentityField(view_name="order:delivery",lookup_field="id")
	outfordelivery 		    =	serializers.HyperlinkedIdentityField(view_name="order:out for delivery",lookup_field="id")
	cancel_order		    =	serializers.HyperlinkedIdentityField(view_name="order:cancel delivery",lookup_field="id")
	accept_order			=	serializers.HyperlinkedIdentityField(view_name="order:accept order",lookup_field="id")
	ship_order 				=	serializers.HyperlinkedIdentityField(view_name="order:ship order",lookup_field="id")	
	click_order_ready 		    =	serializers.HyperlinkedIdentityField(view_name="order:order ready",lookup_field="id")	
	click_appoint_collector =	serializers.HyperlinkedIdentityField(view_name="order:appoint collector",lookup_field="id")
	acceptforcollection		=	serializers.HyperlinkedIdentityField(view_name="order:pick order for collection",lookup_field="id")
	order_detail            =	serializers.HyperlinkedIdentityField(view_name="order:order detail",lookup_field="id")	

	class Meta:
		model 		= Order
		fields 		= "__all__"

class StripeTokenSerializer(serializers.Serializer):
    token     =   serializers.CharField(max_length=120)
