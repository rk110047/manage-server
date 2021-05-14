from django.db import models
from shopkeeper.models import ShopProfile
from cart.models import Cart
from billing.models import BillingProfile
from addresses.models import Address
from .utils import unique_id_generator
from authentication.models import User
from delivery.models import DeliveryPersonProfile
from django.db.models.signals import pre_save,post_save
from customer.models import CustomerProfile
import decimal
from collector.models import CollectorProfile

class Order(models.Model):
    order_status_choices=(('GENERATED','generated'),('ORDER READY','order ready'),('ACCEPTED BY SHOP','acceped by shop'),('OUT FOR DELIVERY','out for delivery'),('SHIPPED','shipped'),('REFUNDED','refunded'),('CANCELLED','cancelled'))
    delivery_choices    =(('HOME DELIVERY','home delivery'),('PERSONAL PICKUP','personal pickup'))

    billing_profile =   models.ForeignKey(BillingProfile,null=True,blank=True,on_delete=models.CASCADE)
    shipping_address=   models.ForeignKey(Address,on_delete=models.CASCADE)
    delivery_person =   models.ForeignKey(DeliveryPersonProfile,on_delete=models.CASCADE,null=True,blank=True) 
    # shipping_address =   models.ForeignKey(Address,related_name='shipping_address',on_delete=models.CASCADE)
    shop            =   models.ForeignKey(ShopProfile,on_delete=models.CASCADE)
    order_id        =   models.CharField(max_length=120,blank=True)
    cart            =   models.ForeignKey(Cart,on_delete=models.CASCADE)
    sub_total               =   models.DecimalField(default=0.00,decimal_places=2,max_digits=100)
    service_charge          =   models.DecimalField(default=0.00,decimal_places=2,max_digits=100)
    shipping_total  =   models.DecimalField(default=0.00,decimal_places=2,max_digits=100)
    total           =   models.DecimalField(default=0.00,decimal_places=2,max_digits=100)
    order_status    =   models.CharField(max_length=120,choices=order_status_choices,default='generated')
    delivery_status =   models.CharField(max_length=120,choices=delivery_choices,default='home delivery')
    ordered_date    =   models.CharField(max_length=120,null=True,blank=True)
    order_preparation_time     =   models.CharField(max_length=120,null=True,blank=True)
    delivery_schedule           =   models.CharField(max_length=120,default="no schedule",null=True,blank=True)
    active          =   models.BooleanField(default=True)
    order_ready     =   models.BooleanField(default=False)
    accepted_by_shop=   models.BooleanField(default=False)
    ordered         =   models.BooleanField(default=False)
    cancelled       =   models.BooleanField(default=False)
    shipped         =   models.BooleanField(default=False)
    customer        =   models.ForeignKey(CustomerProfile,on_delete=models.CASCADE)
    User            =   models.ForeignKey(User,on_delete=models.CASCADE)
    special_instructions = models.CharField(max_length=400,null=True,blank=True,default="")
    appoint_collector       =   models.BooleanField(default=False)
    collector               =   models.ForeignKey(CollectorProfile,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total          =   self.cart.total_price
        cart                =   self.cart.product.all()  
        orderitem           =   cart.first()
        self.sub_total      =   cart_total
        self.service_charge =   decimal.Decimal(cart_total)*decimal.Decimal(0.15)
        shipping_total      =   orderitem.product.shop_name.delivery_charges
        self.shipping_total =   orderitem.product.shop_name.delivery_charges
        new_total           =   decimal.Decimal(cart_total)+decimal.Decimal(shipping_total)+decimal.Decimal(self.service_charge)
        self.total          =   new_total
        self.save()
        return new_total



def pre_save_order_id_creator(instance,sender,*args,**kwargs):
    if not instance.order_id:
        instance.order_id = unique_id_generator(instance)


pre_save.connect(pre_save_order_id_creator,sender=Order)


def post_save_order_total(instance,sender,created,*args,**kwargs):
    if not created:
        cart_obj        =   instance
        cart_id         =   cart_obj.id
        qs              =   Order.objects.filter(cart_id=cart_id)
        if qs.count()==1:
            order_obj   =   qs.first()
            order_obj.update_total()

post_save.connect(post_save_order_total,sender=Cart)



def post_save_order_total_saver(instance,sender,created,*args,**kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_order_total_saver,sender=Order)
