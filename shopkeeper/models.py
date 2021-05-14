from django.db import models
from authentication.models import User
from django.db.models.signals import post_save




class ShopCategories(models.Model):
    category_name        =       models.CharField(max_length=120)
    image                =       models.ImageField(upload_to='ShopCategories/',blank=True,null=True)

    def __str__(self):
        return self.category_name



class ShopProfile(models.Model):
    user                =   models.OneToOneField(User,on_delete=models.CASCADE)
    shop_name           =   models.CharField(max_length=120,blank=False,null=False)
    address_line_1      =   models.CharField(max_length=120,blank=False,null=False)
    address_line_2      =   models.CharField(max_length=120,blank=False,null=False)
    town_city           =   models.CharField(max_length=120,blank=False,null=False)
    country             =   models.CharField(max_length=120,blank=False,null=False)
    shop_image          =   models.FileField(upload_to='shops/',null=True, verbose_name="")
    contact             =   models.CharField(max_length=120,blank=False,null=False)
    email_address       =   models.EmailField(unique=True)
    timming             =   models.CharField(max_length=120,blank=False,null=False)
    shop_details        =   models.TextField()
    active              =   models.BooleanField(default=True)
    delivery_charges    =   models.DecimalField(default=0.00,max_digits=10,decimal_places=2,blank=True,null=True)
    Category        =   models.ForeignKey(ShopCategories,on_delete=models.SET_NULL,null=True)
    personal_pickup_limit = models.IntegerField(default=10,null=True,blank=True)





    def __str__(self):
        return self.shop_name

# class ShopImage(models.Model):
#     shop                =   models.OneToOneField(ShopProfile,on_delete=models.CASCADE)
#     shopimage          =   models.FileField(upload_to='shopimage/',null=True, verbose_name="")

#     def __str__(self):
#         return F"{self.shop}"

# def shop_image_created_receiver(instance,sender,created,*args,**kwargs):
#     if created:
#         ShopImage.objects.get_or_create(shop=instance)

# post_save.connect(shop_image_created_receiver,sender=ShopProfile)
