
from django.db import models
from shopkeeper.models import ShopProfile
from authentication.models import User
import random
import string

def random_string_generator(size=10,char=string.digits):
    return ''.join(random.choice(char) for _ in range(size))


def unique_code_generator(instance):
    '''for unique order_id generation'''

    product_new_code        =   random_string_generator()
    klass           	  =   instance.__class__
    qs              	 =   klass.objects.filter(product_code=product_new_code).exists()

    return unique_code_generator(instance) if qs else product_new_code

class Brand(models.Model):
    brand_name      =       models.CharField(max_length=120)
    brand_image     =       models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.brand_name
    class Meta:
        # unique_together = ['album', 'order']
        ordering = ['brand_name']


class SubCategory(models.Model):
    category_name        =       models.CharField(max_length=120)
    image                =       models.FileField(upload_to='SubCategory',null=True,blank=True)

    def __str__(self):
        return self.category_name


class Categories(models.Model):
    category_name        =       models.CharField(max_length=120)
    image                =       models.ImageField(upload_to='Categories/',blank=True,null=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_id      =   models.AutoField(primary_key=True)
    product_code    =   models.CharField(max_length=120,null=True,blank=True)
    user            =   models.ForeignKey(User,on_delete=models.CASCADE)
    shop_name       =   models.ForeignKey(ShopProfile,on_delete=models.CASCADE)
    product_name    =   models.CharField(max_length=120,blank=False,null=False)
    product_price   =   models.DecimalField(max_digits=10,decimal_places=2)
    product_image   =   models.FileField(upload_to='product_images/', null=True, verbose_name="")
    # product_color   =   models.CharField(max_length=120)
    # product_size    =   models.CharField(max_length=120)
    # brand_name      =   models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True)
    quantity        =   models.CharField(max_length=120,blank=False,null=False)
    # slug            =   models.SlugField()
    Category        =   models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)
    description     =   models.TextField()
    active          =   models.BooleanField(default=True)
    Aisle_number    =   models.CharField(max_length=120,blank=True,null=True)
    Shelf_number    =   models.CharField(max_length=120,blank=True,null=True)
    Shelf_side      =   models.CharField(max_length=120,blank=True,null=True)




    def __str__(self):
        return  self.product_name

    @property
    def owner(self):
        return self.user

def pre_save_product_code_creator(instance,sender,*args,**kwargs):
    if not instance.product_code:
        instance.product_code = unique_code_generator(instance)

models.signals.pre_save.connect(pre_save_product_code_creator,sender=Product)

class ProductItem(models.Model):
    user             =   models.ForeignKey(User,on_delete=models.CASCADE)
    Product          =   models.ForeignKey(Product,on_delete=models.CASCADE)





class ProductImages(models.Model):
    Product          =   models.ForeignKey(Product,on_delete=models.CASCADE)
    image            =   models.FileField(upload_to='Product_Images/', null=True, verbose_name="")

    def __str__(self):
        return  F"{self.Product}"


class ContentCategory(models.Model):
    Product              =       models.ForeignKey(Product,on_delete=models.CASCADE)
    category_name        =       models.CharField(max_length=120)
    requried             =       models.IntegerField(blank=True,null=True)
    # content              =       models.ManyToManyField(Content)
    description              =   models.CharField(max_length=200,blank=True,null=True)



    def __str__(self):
        return self.category_name

class Content(models.Model):
    ContentCategory          =   models.ForeignKey(ContentCategory,on_delete=models.CASCADE)
    content                  =   models.CharField(max_length=120,blank=True,null=True)
    content_price            =   models.DecimalField(default=0.00,max_digits=10,decimal_places=2,blank=True,null=True)
    description              =   models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return  self.content

class ProductTax(models.Model):
    Product             =   models.ForeignKey(Product,on_delete=models.CASCADE)
    Tax_name            =   models.CharField(max_length=120,blank=True,null=True)
    Tax_percentage      =   models.DecimalField(default=0.00,max_digits=10,decimal_places=3,blank=True,null=True)


    def __str__(self):
        return self.Tax_name
