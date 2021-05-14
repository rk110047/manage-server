from django.db import models
from authentication.models import User


class CustomerProfile(models.Model):
    Customer_id         =    models.AutoField(primary_key=True)
    User                =    models.OneToOneField(User,on_delete=models.CASCADE)
    # profile_image       =    models.FileField(upload_to='profile_pic/',null=True)
    first_name          =    models.CharField(max_length=20)
    # middle_name         =    models.CharField(max_length=20,null=True,blank=True)
    last_name           =    models.CharField(max_length=20,null=True,blank=True)
    email               =    models.EmailField()
    phone_Number        =    models.CharField(max_length=120,null=True,blank=True)
    # address_line_1      =    models.CharField(max_length=120,null=True,blank=True)
    town_city           =    models.CharField(max_length=120,null=True,blank=True)
    # state               =    models.CharField(max_length=120,null=True,blank=True)
    # country             =    models.CharField(max_length=120,null=True,blank=True)
    zip_code            =    models.CharField(max_length=20,null=True,blank=True)



    def __str__(self):
        return F"{self.User}"
