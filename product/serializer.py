from rest_framework import serializers
from .models import Product,Categories,Content,ProductImages,ContentCategory,ProductTax
from shopkeeper.serializer import ShopDetailSerializer

class ProductAPISerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Product
        fields  =   "__all__"



class ProductSerializer(serializers.ModelSerializer):
    url             =   serializers.HyperlinkedIdentityField(view_name='product:detail product',lookup_field='product_id')
    shop_name       =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   ['product_id','user','product_image','product_name','product_price','description','shop_name','url']
        read_only_fields    =   ['shop_name']



class ProductDetailSerializer(serializers.ModelSerializer):
    taxes                =   serializers.HyperlinkedIdentityField(view_name='product:product tax list',lookup_field='product_id')
    content_category     =   serializers.HyperlinkedIdentityField(view_name='product:content category list',lookup_field='product_id')
#    contents             =   serializers.HyperlinkedIdentityField(view_name='product:product contents',lookup_field='product_id')
    images               =   serializers.HyperlinkedIdentityField(view_name='product:product images',lookup_field='product_id')
    add_to_cart          =    serializers.HyperlinkedIdentityField(view_name='cart:add_to_cart',lookup_field='product_id')
    remove_from_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:remove_from_cart',lookup_field='product_id')
    shop_name            =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   ['Aisle_number','Shelf_number','Shelf_side','content_category','product_id','product_image','add_to_cart','product_name','product_price','description','shop_name','remove_from_cart','images','taxes']
        # read_only_fields    =   ['product_id','user','shop_name']



class ProductDetailForCartSerializer(serializers.ModelSerializer):
    # add_to_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:add_to_cart',lookup_field='product_id')
    # shop_name       =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   '__all__'
        # read_only_fields    =   ['product_id','user','shop_name']


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Product
        fields  =   '__all__'
        read_only_fields    =   ['product_id','user','shop_name']



class ProductListOfUserSerializer(serializers.ModelSerializer):
    url             =   serializers.HyperlinkedIdentityField(view_name='product:detail of product',lookup_field='product_id')
    shop_name       =    ShopDetailSerializer(read_only=True)
    class Meta:
        model   =   Product
        fields  =   ['product_id','product_code','user','product_image','product_name','product_price','description','shop_name','quantity','url','Aisle_number','Shelf_number','Shelf_side']
        read_only_fields    =   ['shop_name']

class ProductDetailForListSerializer(serializers.ModelSerializer):
    taxes                =   serializers.HyperlinkedIdentityField(view_name='product:product tax list',lookup_field='product_id')
    # contents             =   serializers.HyperlinkedIdentityField(view_name='product:product contents',lookup_field='product_id')
    images               =   serializers.HyperlinkedIdentityField(view_name='product:product images',lookup_field='product_id')
    add_to_cart          =    serializers.HyperlinkedIdentityField(view_name='cart:add_to_cart',lookup_field='product_id')
    remove_from_cart     =    serializers.HyperlinkedIdentityField(view_name='cart:remove_from_cart',lookup_field='product_id')
    edit                 =      serializers.HyperlinkedIdentityField(view_name="product:edit product",lookup_field="product_id")
    shop_name            =    ShopDetailSerializer(read_only=True)
    content_category     =    serializers.HyperlinkedIdentityField(view_name='product:content category list',lookup_field='product_id')
    delete               =      serializers.HyperlinkedIdentityField(view_name="product:delete product",lookup_field="product_id")

    class Meta:
        model   =   Product
        fields  =  ['product_id','user','product_code','quantity','product_image','product_name','product_price','description','shop_name',"Category",'active','content_category','edit','delete','Aisle_number','Shelf_number','Shelf_side','remove_from_cart','images','taxes','add_to_cart']
        # read_only_fields    =   ['product_id','user','shop_name']


class ProductUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   =   Product
        fields  =   '__all__'
        read_only_fields    =   ['product_id','user','shop_name']

class CreateCatSerializer(serializers.ModelSerializer):
    class Meta:
        model    =   Categories
        fields   =   "__all__"


class ProductContentSerializer(serializers.ModelSerializer):
    class Meta:
        model    =   Content
        fields   =   "__all__"


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model    =   ProductImages
        fields   =   "__all__"

class CategoryContentSerializer(serializers.ModelSerializer):
    content      =   serializers.HyperlinkedIdentityField(view_name='product:product contents',lookup_field='id')
    class Meta:
        model    =   ContentCategory
        fields   =   "__all__"


class ProductTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   ProductTax
        fields  =   "__all__"
