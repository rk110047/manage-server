from rest_framework import generics,mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.response import Response
from .models import Cart,OrderItem
from .serializer import CartDetailSerializer,OrderItemDetailSerializer,CartDetailforOrderSerializer,OrderItemSerializer
from product.models import Product,Content,ProductTax
from orders.serializer import OrderDetailSerializer
from django.shortcuts import redirect
from django.core import serializers
from orders.models import  Order
from billing.models import BillingProfile
from addresses.models import Address
from django.views import View
import json
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import decimal
from authentication.models import User

class ItemCreateAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       CartDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

    def get(self,request,product_id=None):
        request             =   self.request
        user                =   self.request.user
        data                =   self.request.GET.get('data')
        product             =   Product.objects.get(product_id=product_id)
        taxes               =   ProductTax.objects.filter(Product=product)
        print(taxes)
        total_tax           =   0.00
        for tax in taxes:
            total_tax       = decimal.Decimal(total_tax)+(decimal.Decimal(tax.Tax_percentage)/100) 
        print(total_tax)
        print(data)
        content             =   []
        try:
            data            =    data.split(",")
        except:
            pass
        try:
            for x in data:
                try:
                    x=int(x)
                    content.append(x)
                except:
                    pass
            print(content)
        except:
            pass
        if user.is_authenticated:
            orderitem            =  OrderItem.objects.filter(User=user,active=True)
            if orderitem.count()==0:
                product             =   Product.objects.get(product_id=product_id)
                item                =   OrderItem.objects.create()
                item.User           =   user
                item.product = product
                item.price          =   product.product_price
                item.save()
                content_Price       =   0.00
                for contents in content:
                                Contents         =   Content.objects.get(id=contents)
                                content_Price    =   decimal.Decimal(content_Price)+decimal.Decimal(Contents.content_price)
                                item.content.add(Contents)
                item.price         =   decimal.Decimal(item.price)+decimal.Decimal(content_Price)
                item.Product_price =   item.price
                tax_price          =   decimal.Decimal(item.price)*decimal.Decimal(total_tax)
                item.price         =   decimal.Decimal(item.price)+decimal.Decimal(tax_price)
                item.Tax           =   tax_price
                item.save()
                response    =   {"message":'item added succesfully'}
                return Response(response)
            else:
                try:
                    product             =   Product.objects.get(product_id=product_id)
                    item                =   OrderItem.objects.get(User=user,product=product,active=True)
                    price               =   decimal.Decimal(item.price)/item.quantity
                    price2              =   decimal.Decimal(item.Product_price)/item.quantity
                    price3              =   decimal.Decimal(item.Tax)/item.quantity
                    item.quantity       +=1
                    item.save()
                    item.Product_price   =   item.quantity*decimal.Decimal(price2)
                    item.price           =   item.quantity*decimal.Decimal(price)
                    item.Tax             =   item.quantity*decimal.Decimal(price3)
                    item.save()
                    response    =   {"message":'cart updated'}
                    return Response(response)
                except:
                    if orderitem.count()==0:
                        product             =   Product.objects.get(product_id=product_id)
                        print(orderitem.first())
                        item                =   OrderItem.objects.create()
                        item.User           =   user
                        item.product=product
                        item.price          =   product.product_price
                        content_Price       =   0.00
                        for contents in content:
                                Contents         =   Content.objects.get(id=contents)
                                content_Price    =   decimal.Decimal(content_Price)+decimal.Decimal(Contents.content_price)
                                item.content.add(Contents)
                        item.price         =   decimal.Decimal(item.price)+decimal.Decimal(content_Price)
                        item.Product_price =   item.price
                        tax_price          =   decimal.Decimal(item.price)*decimal.Decimal(total_tax)
                        item.price         =   decimal.Decimal(item.price)+decimal.Decimal(tax_price)
                        item.Tax           =   tax_price
                        item.save()
                        response    =   {"message":'item added succesfully'}
                        return Response(response)
                    else:
                        object =orderitem.first()
                        product             =   Product.objects.get(product_id=product_id)
                        print(product.shop_name)
                        if object.product.shop_name==product.shop_name:
                            product             =   Product.objects.get(product_id=product_id)
                            item                =   OrderItem.objects.create()
                            item.User           =   user
                            item.product=product
                            item.price          =   product.product_price
                            content_Price       =   0.00
                            for contents in content:
                                Contents         =   Content.objects.get(id=contents)
                                content_Price    =   decimal.Decimal(content_Price)+decimal.Decimal(Contents.content_price)
                                item.content.add(Contents)
                            item.price         =   decimal.Decimal(item.price)+decimal.Decimal(content_Price)
                            item.Product_price =   item.price
                            tax_price          =   decimal.Decimal(item.price)*decimal.Decimal(total_tax)
                            item.price         =   decimal.Decimal(item.price)+decimal.Decimal(tax_price)
                            item.Tax           =   tax_price
                            item.save()
                            response    =   {"message":'item added succesfully'}
                            return Response(response)
                        else:
                            orderitem.delete()
                            product             =   Product.objects.get(product_id=product_id)
                            item                =   OrderItem.objects.create()
                            item.User           =    user
                            item.product=product
                            item.price          =   product.product_price
                            content_Price       =   0.00
                            for contents in content:
                                Contents         =   Content.objects.get(id=contents)
                                content_Price    =   decimal.Decimal(content_Price)+decimal.Decimal(Contents.content_price)
                                item.content.add(Contents)
                            item.price         =   decimal.Decimal(item.price)+decimal.Decimal(content_Price)
                            item.Product_price =   item.price
                            tax_price          =   decimal.Decimal(item.price)*decimal.Decimal(total_tax)
                            item.price         =   decimal.Decimal(item.price)+decimal.Decimal(tax_price)
                            item.Tax           =   tax_price
                            item.save()
                            response    =   {"message":'item added succesfully'}
                            return Response(response)

        return redirect("/auth/login/")


'''class ItemCreateAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       CartDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,SessionAuthentication]

    def get(self,request,product_id=None):
        request             =   self.request
        user                =   self.request.user
        if user.is_authenticated:
            orderitem            =  OrderItem.objects.filter(User=user,active=True)
            if orderitem.count()==0:
                product             =   Product.objects.get(product_id=product_id)
                item                =   OrderItem.objects.create()
                item.User.add(user)
                item.product = product
                item.price          =   product.product_price
                item.save()
                response    =   {"message":'item added succesfully'}
                return Response(response)
            else:
                try:
                    product             =   Product.objects.get(product_id=product_id)
                    item                =   OrderItem.objects.get(User=user,product=product,active=True)
                    item.quantity       +=1
                    item.save()
                    item.price           =   item.quantity*product.product_price
                    item.save()
                    response    =   {"message":'cart updated'}
                    return Response(response)
                except:
                    if orderitem.count()==0:
                        product             =   Product.objects.get(product_id=product_id)
                        print(orderitem.first())
                        item                =   OrderItem.objects.create()
                        item.User.add(user)
                        item.product=product
                        item.price          =   product.product_price
                        item.save()
                        response    =   {"message":'item added succesfully'}
                        return Response(response)
                    else:
                        object =orderitem.first()
                        product             =   Product.objects.get(product_id=product_id)
                        print(product.shop_name)
                        if object.product.shop_name==product.shop_name:
                            product             =   Product.objects.get(product_id=product_id)
                            item                =   OrderItem.objects.create()
                            item.User.add(user)
                            item.product=product
                            item.price          =   product.product_price
                            item.save()
                            response    =   {"message":'item added succesfully'}
                            return Response(response)
                        else:
                            orderitem.delete()
                            product             =   Product.objects.get(product_id=product_id)
                            item                =   OrderItem.objects.create()
                            item.User.add(user)
                            item.product=product
                            item.price          =   product.product_price
                            item.save()
                            response    =   {"message":'item added succesfully'}
                            return Response(response)

        return redirect("/auth/login/")'''

class RemoveItemFromCartAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       CartDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,SessionAuthentication]

    def get(self,request,product_id=None):
        request             =        self.request
        user                =        request.user
        if user.is_authenticated:
            try:
                product     =         Product.objects.get(product_id=product_id)
                item        =         OrderItem.objects.get(User=user,product=product,active=True)
                price               =   decimal.Decimal(item.price)/item.quantity
                print(item.quantity)
                if item.quantity>1:
                    item.quantity -=1
                    item.save()
                    item.price           =   item.quantity*price
                    item.save()
                    response        =   {"message":"item updated"}
                    return Response(response)
                else:
                    OrderItem.objects.get(User=user,product=product).delete()
                    response        =   {"message":"item removed"}
                    return Response(response)
            except:
                response        =   {"message":"item is not in cart"}
                return Response(response)

        return redirect("/auth/login/")


class OrderItemQuantityDecreaseAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       CartDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

    def get(self,request,item_id=None):
        request             =        self.request
        user                =        request.user
        if user.is_authenticated:
            try:
                
                item        =         OrderItem.objects.get(item_id=item_id)
                product     =         item.product
                price       =         decimal.Decimal(item.price)/item.quantity
                price2       =         decimal.Decimal(item.Product_price)/item.quantity
                price3       =         decimal.Decimal(item.Tax)/item.quantity
                print(product)
                print(item.quantity)
                if item.quantity>1:
                    item.quantity -=1
                    item.save()
                    item.price           =   item.quantity*price
                    item.Product_price           =   item.quantity*price2
                    item.Tax              =   item.quantity*price3
                    item.save()
                    response        =   {"message":"item updated"}
                    return Response(response)
                else:
                    OrderItem.objects.get(item_id=item_id).delete()
                    response        =   {"message":"item removed"}
                    return Response(response)
            except:
                response        =   {"message":"item is not in cart"}
                return Response(response)

        return redirect("/auth/login/")

class OrderItemQuantityIncreaseAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       CartDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

    def get(self,request,item_id=None):
        request             =        self.request
        user                =        request.user
        if user.is_authenticated:
            try:
                
                item        =         OrderItem.objects.get(item_id=item_id)
                product     =         item.product
                price       =         decimal.Decimal(item.price)/item.quantity
                price2       =         decimal.Decimal(item.Product_price)/item.quantity
                price3       =         decimal.Decimal(item.Tax)/item.quantity
                print(product)
                print(item.quantity)
                item.quantity +=1
                item.save()
                item.price           =   item.quantity*price
                item.Product_price           =   item.quantity*price2
                item.Tax               =   item.quantity*price3
                item.save()
                response        =   {"message":"item updated"}
                return Response(response)
            except:
                response        =   {"message":"item is not in cart"}
                return Response(response)

        return redirect("/auth/login/")







class CartAPIView(generics.ListAPIView):
    # queryset                =       OrderItem.objects.all()
    serializer_class        =       CartDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,SessionAuthentication]

    def get_queryset(self):
        request             =   self.request
        user                =   self.request.user
        if user.is_authenticated:
            cart=OrderItem.objects.filter(User=user,active=True)
            # cart  =  Cart.objects.get(User=user)
            # cart  = cart.product.all()
            # print(cart)
            # if cart:
            #     qs = cart.product.all()
            #     print(qs)
            return cart

    def get(self,request):
        request             =   self.request
        user                =   self.request.user
        if user.is_authenticated:
            order_item=OrderItem.objects.filter(product__isnull=True)
            order_item.delete()
            try:
                cart        =  Cart.objects.filter(User=user)
                object = Cart.objects.filter(User=user,active=True)
                for x in object:
                    object=x
                object = Cart.objects.get(User=user,active=True)
                for i in object.product.filter(active=False):
                    object.product.remove(i)
                if OrderItem.objects.filter(User=user,active=True):
                    qs = OrderItem.objects.filter(User=user,active=True)
                    for x in qs:
                        object.product.add(x)
                total = 0
                for x in object.product.all():
                    total    +=  x.price
                object.total_price  = total
                total = 0
                for x in object.product.all():
                    total    +=  x.quantity
                object.total_items  = total
                object.save()
                # qs = Cart.objects.get(User=user)
                # qs = Cart.objects.get(id=qs.id)
                # product = []
                # for x in object.product.all():
                #     products = x.product
                #     product.append({"product name":products.product_name,
                #                     "product price":products.product_price})
                queryset = self.get_queryset()
                serializer = CartDetailSerializer(queryset, many=True,context={'request': request})
                response        ={"products":serializer.data,'total_items':object.total_items,'cart_total':object.total_price,}
                return Response(response)
                # response        ={'data':{"products":product,'total items':qs.total_items,'cart total':qs.total_price,}}
                # return Response(response)

            except:
                object =  Cart.objects.create()
                object.User.add(user)
                object.save()
                if OrderItem.objects.filter(User=user,active=True):
                    qs = OrderItem.objects.filter(User=user,active=True)
                    for x in qs:
                        object.product.add(x)
                total = 0
                for x in object.product.all():
                    total    +=  x.price
                object.total_price  = total
                total = 0
                for x in object.product.all():
                    total    +=  x.quantity
                object.total_items  = total
                object.save()
                queryset = self.get_queryset()
                serializer = CartDetailSerializer(queryset, many=True,context={'request': request})
                print(serializer.data)
                response        ={"products":serializer.data,'total_items':object.total_items,'cart_total':object.total_price,}
                return Response(response)


        else:
            response        =   {"message":"create session login..."}
            return Response(response)

class CheckOutAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       []
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,SessionAuthentication]

    def get(self,request):
        request             =   self.request
        user                =   self.request.user
        if user.is_authenticated:
            try:
                cart_obj        =   Cart.objects.filter(User=user,active=True,product__isnull=False)
                cart_obj        =   cart_obj.first()
                cart            =   cart_obj.product.all()  
                orderitem       =   cart.first()
                shop            =   orderitem.product.shop_name 
                order_obj       =   Order.objects.filter(cart=cart_obj,active=True,ordered=False)
                order_obj       =   order_obj.first()
                order_obj.sub_total       =   decimal.Decimal(cart_obj.total_price)
                order_obj.service_charge  =   decimal.Decimal(cart_obj.total_price)*decimal.Decimal(0.10)
                order_obj.shipping_total = orderitem.product.shop_name.delivery_charges
                order_obj.total =   decimal.Decimal(cart_obj.total_price)+decimal.Decimal(orderitem.product.shop_name.delivery_charges)+decimal.Decimal(order_obj.service_charge)
                order_obj.shop  =   shop
                order_obj.save()
                print(order_obj)
                serializer      =   OrderDetailSerializer(order_obj,context={'request': request})
                response        =    {"orders":serializer.data}
                return Response(serializer.data)
            except:
                cart_obj                 =   Cart.objects.filter(User=user,active=True,product__isnull=False)
                cart_obj                 =   cart_obj.first()
                cart                     =   cart_obj.product.all()  
                orderitem                =   cart.first()
                shop                     =   orderitem.product.shop_name 
                print(orderitem.product.shop_name)
                billing_profile,created  =   BillingProfile.objects.get_or_create(User=user,email=user.email)
                shipping_address         =   Address.objects.filter(billingprofile=billing_profile)
                shipping_address         =   shipping_address.last()
                # print(shipping_address)
                # billing_address          =   Address.objects.filter(billingprofile=billing_profile,address_type="BIILING")
                # billing_address          =   billing_address.last()
                # print(billing_address)
                customer_profile         =   self.request.user.customerprofile
                order_obj                =   Order.objects.create(User=self.request.user,cart=cart_obj,shop=shop,billing_profile=billing_profile,shipping_address=shipping_address,customer=customer_profile)
                serializer      =   OrderDetailSerializer(order_obj,context={'request': request})
                response        =    {"orders":serializer.data}
                print("this one")
                return Response(serializer.data)

class CheckOutAPIView2(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       []
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,SessionAuthentication]

    def get(self,request,id=None):
        request             =   self.request
        user                =   User.objects.get(id=id)
        if user.is_authenticated:
            try:
                cart_obj        =   Cart.objects.filter(User=user,active=True,product__isnull=False)
                cart_obj        =   cart_obj.first()
                cart            =   cart_obj.product.all()  
                orderitem       =   cart.first()
                shop            =   orderitem.product.shop_name 
                order_obj       =   Order.objects.filter(cart=cart_obj,active=True,ordered=False)
                order_obj       =   order_obj.first()
                order_obj.sub_total       =   decimal.Decimal(cart_obj.total_price)
                order_obj.service_charge  =   decimal.Decimal(cart_obj.total_price)*decimal.Decimal(0.10)
                order_obj.shipping_total = orderitem.product.shop_name.delivery_charges
                order_obj.total =   decimal.Decimal(cart_obj.total_price)+decimal.Decimal(orderitem.product.shop_name.delivery_charges)+decimal.Decimal(order_obj.service_charge)
                order_obj.shop  =   shop
                order_obj.save()
                print(order_obj)
                serializer      =   OrderDetailSerializer(order_obj,context={'request': request})
                response        =    {"orders":serializer.data}
                return Response(serializer.data)
            except:
                cart_obj                 =   Cart.objects.filter(User=user,active=True,product__isnull=False)
                cart_obj                 =   cart_obj.first()
                cart                     =   cart_obj.product.all()  
                orderitem                =   cart.first()
                shop                     =   orderitem.product.shop_name 
                print(orderitem.product.shop_name)
                billing_profile,created  =   BillingProfile.objects.get_or_create(User=user,email=user.email)
                shipping_address         =   Address.objects.filter(billingprofile=billing_profile)
                shipping_address         =   shipping_address.last()
                # print(shipping_address)
                # billing_address          =   Address.objects.filter(billingprofile=billing_profile,address_type="BIILING")
                # billing_address          =   billing_address.last()
                # print(billing_address)
                customer_profile         =   user.customerprofile
                order_obj                =   Order.objects.create(User=user,cart=cart_obj,shop=shop,billing_profile=billing_profile,shipping_address=shipping_address,customer=customer_profile)
                serializer      =   OrderDetailSerializer(order_obj,context={'request': request})
                response        =    {"orders":serializer.data}
                print("this one")
                return Response(serializer.data)


class OrderItemDeleteAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       OrderItemDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,SessionAuthentication]

    def get(self,request,item_id=None):
        request             =        self.request
        user                =        request.user
        if user.is_authenticated:
            try:
                item        =         OrderItem.objects.get(User=user,item_id=item_id)
                item.delete()
                response        =   {"message":"item removed"}
                return Response(response)
            except:
                response        =   {"message":"item is not in cart"}
                return Response(response)

        return redirect("/auth/login/")


class getCartAPIView(generics.RetrieveAPIView):
    queryset                =       Cart.objects.all()
    serializer_class        =       CartDetailforOrderSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,SessionAuthentication]
    lookup_field            =       "id"


class orderItemCartAPIView(generics.RetrieveAPIView):
    queryset                =       OrderItem.objects.all()
    serializer_class        =       OrderItemDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,SessionAuthentication]
    lookup_field            =       "item_id"


class orderItemRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =       OrderItem.objects.all()
    serializer_class        =       OrderItemDetailSerializer
    permission_classes      =       []
    authentication_classes  =       []
    lookup_field            =       "item_id"

class orderItemLCAPIView(generics.ListCreateAPIView):
    queryset                =       OrderItem.objects.all()
    serializer_class        =       OrderItemDetailSerializer
    permission_classes      =       []
    authentication_classes  =       []


class FavouriteOrderItemsAPIView(generics.ListAPIView):
    queryset                =       OrderItem.objects.all()
    serializer_class        =       OrderItemDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [SessionAuthentication,TokenAuthentication,JSONWebTokenAuthentication]

    def get_queryset(self):
        User                =       self.request.user
        queryset            =       OrderItem.objects.filter(User=User,inFavourite=True)
        return queryset


class FavouriteItemCreateAPIView(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       CartDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

    def get(self,request,item_id=None):
        request             =   self.request
        user                =   self.request.user
        order_item          =   OrderItem.objects.get(item_id=item_id)
        product             =   order_item.product
        product_id          =   product.product_id
        product             =   Product.objects.get(product_id=product_id)
        taxes               =   ProductTax.objects.filter(Product=product)
        print(taxes)
        total_tax           =   0.00
        for tax in taxes:
            total_tax       = decimal.Decimal(total_tax)+(decimal.Decimal(tax.Tax_percentage)/100)
        content             =   order_item.content.all()
        print(product)
        for i in content:
            print(i)
            print(i.content_price)
        if user.is_authenticated:
            orderitem            =  OrderItem.objects.filter(User=user,active=True)
            if orderitem.count()==0:
                product             =   Product.objects.get(product_id=product_id)
                item                =   OrderItem.objects.create()
                item.User           =   user
                item.product = product
                item.price          =   product.product_price
                content_Price       =   0.00
                for contents in content:
                                content_Price    =   decimal.Decimal(content_Price)+decimal.Decimal(contents.content_price)
                                item.content.add(contents)
                item.price         =   decimal.Decimal(item.price)+decimal.Decimal(content_Price)
                item.Product_price =   item.price
                tax_price          =   decimal.Decimal(item.price)*decimal.Decimal(total_tax)
                item.price         =   decimal.Decimal(item.price)+decimal.Decimal(tax_price)
                item.Tax           =   tax_price
                item.save()
                response    =   {"message":'item added succesfully'}
                return Response(response)
            else:
                try:
                    product             =   Product.objects.get(product_id=product_id)
                    item                =   OrderItem.objects.get(User=user,product=product,active=True)
                    price               =   decimal.Decimal(item.price)/item.quantity
                    price2              =   decimal.Decimal(item.Product_price)/item.quantity
                    price3              =   decimal.Decimal(item.Tax)/item.quantity
                    item.quantity       +=1
                    item.save()
                    item.Product_price   =   item.quantity*decimal.Decimal(price2)
                    item.price           =   item.quantity*decimal.Decimal(price)
                    item.Tax             =   item.quantity*decimal.Decimal(price3)
                    item.save()
                    response    =   {"message":'cart updated'}
                    return Response(response)
                except:
                    if orderitem.count()==0:
                        product             =   Product.objects.get(product_id=product_id)
                        print(orderitem.first())
                        item                =   OrderItem.objects.create()
                        item.User           =   user
                        item.product=product
                        item.price          =   product.product_price
                        content_Price       =   0.00
                        for contents in content:
                                        content_Price    =   decimal.Decimal(content_Price)+decimal.Decimal(contents.content_price)
                                        item.content.add(contents)
                        item.price         =   decimal.Decimal(item.price)+decimal.Decimal(content_Price)
                        item.Product_price =   item.price
                        tax_price          =   decimal.Decimal(item.price)*decimal.Decimal(total_tax)
                        item.price         =   decimal.Decimal(item.price)+decimal.Decimal(tax_price)
                        item.Tax           =   tax_price
                        item.save()
                        response    =   {"message":'item added succesfully'}
                        return Response(response)
                    else:
                        object =orderitem.first()
                        product             =   Product.objects.get(product_id=product_id)
                        print(product.shop_name)
                        if object.product.shop_name==product.shop_name:
                            product             =   Product.objects.get(product_id=product_id)
                            item                =   OrderItem.objects.create()
                            item.User           =     user
                            item.product=product
                            item.price          =   product.product_price
                            content_Price       =   0.00
                            for contents in content:
                                            content_Price    =   decimal.Decimal(content_Price)+decimal.Decimal(contents.content_price)
                                            item.content.add(contents)
                            item.price         =   decimal.Decimal(item.price)+decimal.Decimal(content_Price)
                            item.Product_price =   item.price
                            tax_price          =   decimal.Decimal(item.price)*decimal.Decimal(total_tax)
                            item.price         =   decimal.Decimal(item.price)+decimal.Decimal(tax_price)
                            item.Tax           =   tax_price
                            item.save()
                            response    =   {"message":'item added succesfully'}
                            return Response(response)
                        else:
                            orderitem.delete()
                            product             =   Product.objects.get(product_id=product_id)
                            item                =   OrderItem.objects.create()
                            item.User           =    user
                            item.product=product
                            item.price          =   product.product_price
                            content_Price       =   0.00
                            for contents in content: 
                                            content_Price    =   decimal.Decimal(content_Price)+decimal.Decimal(contents.content_price)
                                            item.content.add(contents)
                            item.price         =   decimal.Decimal(item.price)+decimal.Decimal(content_Price)
                            item.Product_price =   item.price
                            tax_price          =   decimal.Decimal(item.price)*decimal.Decimal(total_tax)
                            item.price         =   decimal.Decimal(item.price)+decimal.Decimal(tax_price)
                            item.Tax           =   tax_price
                            item.save()
                            response    =   {"message":'item added succesfully'}
                            return Response(response)

        return redirect("/auth/login/")

class AddToFavourites(generics.GenericAPIView):
    queryset                =       []
    serializer_class        =       OrderItemDetailSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]

    def get(self,request,item_id=None):
        order_item          =   OrderItem.objects.get(item_id=item_id)
        if order_item.inFavourite==True:
            order_item.inFavourite=False
            order_item.save()
            return Response({"message":"Removed From Favourites"})
        else :
            order_item.inFavourite=True
            order_item.save()
            return Response({"message":"Added To Favourites"})



class OrderItemCreateAPIView(generics.CreateAPIView):
    queryset                =       OrderItem.objects.all()
    serializer_class        =       OrderItemSerializer
    permission_classes      =       []
    authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


    def Post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    def perform_create(self,serializer):
        user        =  self.request.user
        orderitem   =  OrderItem.objects.filter(User=user,active=True)
        print(user)
        product      = self.request.data["product"]
        product      = Product.objects.get(product_id=product)
        quantity     = self.request.data["quantity"]
        content      = self.request.data["content"]
        print(self.request.data)
        price        = decimal.Decimal(product.product_price)
        User         = self.request.user
        object =orderitem.first()
        if orderitem.count()==0:
            for x in content:
                print(type(x))
                content    =  Content.objects.get(id=x)
                price      =  decimal.Decimal(content.content_price)+decimal.Decimal(price)
            price        = decimal.Decimal(price)*decimal.Decimal(quantity)
            serializer.save(User=User,quantity=quantity)
        else:
            if object.product.shop_name==product.shop_name:
                for x in content:
                    print(type(x))
                    content    =  Content.objects.get(id=x)
                    price      =  decimal.Decimal(content.content_price)+decimal.Decimal(price)
                price        = decimal.Decimal(price)*decimal.Decimal(quantity)
                serializer.save(User=User,quantity=quantity)
            else:
                orderitem.delete()
                for x in content:
                    print(type(x))
                    content    =  Content.objects.get(id=x)
                    price      =  decimal.Decimal(content.content_price)+decimal.Decimal(price)
                price        = decimal.Decimal(price)*decimal.Decimal(quantity)
                serializer.save(User=User,quantity=quantity)
