from rest_framework import serializers
from product.serializer import ProductDetailForCartSerializer,ProductContentSerializer
from .models import Cart
from .models import OrderItem

from product.serializer import ProductDetailSerializer


from drf_writable_nested.serializers import WritableNestedModelSerializer


class CartDetailSerializer(WritableNestedModelSerializer):
    # remove_from_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:remove_from_cart',lookup_field='product_id')
    delete_item_from_cart = serializers.HyperlinkedIdentityField(view_name='cart:delete_item_from_cart',lookup_field='item_id')
    # url             =   serializers.HyperlinkedIdentityField(view_name='product:detail product',lookup_field='product_id')
    product         =   ProductDetailSerializer()
    # item              =   serializers.SerializerMethodField()
    content        =   ProductContentSerializer(many=True)
    class Meta:
        model      = OrderItem
        fields     = ["item_id",
                    "product",
                  "quantity",
                "Product_price",
                "price",
               "Tax",
            "delete_item_from_cart",
	"content"]



class OrderItemDetailSerializer(WritableNestedModelSerializer):
    content        =   ProductContentSerializer(many=True)
    product         =   ProductDetailSerializer()
    add_in_favourites   =   serializers.HyperlinkedIdentityField(view_name='cart:add to favourites',lookup_field='item_id')
    class Meta:
        model      = OrderItem
        fields     = "__all__"

class CartDetailforOrderSerializer(WritableNestedModelSerializer):
    product         =   OrderItemDetailSerializer(many=True)
    class Meta:
        model      = Cart
        fields     = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model      = OrderItem
        fields     = "__all__"
        read_only_fields =["User"]
