from django.db import models
from billing.models import BillingProfile

# ADDRESS_TYPE_CHOICES=(('BIILING','billing'),('SHIPPING','shipping'))
class Address(models.Model):


    billingprofile          =      models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    # address_type         =      models.CharField(max_length=120,choices=ADDRESS_TYPE_CHOICES)
    name                    =      models.CharField(max_length=120,null=True,blank=True)
    address_line_1          =      models.CharField(max_length=120)
    address_line_2          =      models.CharField(max_length=120,null=True,blank=True)
    landmark                =      models.CharField(max_length=120,null=True,blank=True)
    city                    =      models.CharField(max_length=120)
    state                   =      models.CharField(max_length=120)
    country                 =      models.CharField(max_length=120,default='INDIA')
    zip_code                =      models.CharField(max_length=120,null=True,blank=True)
    phone_number            =      models.CharField(max_length=120,null=True,blank=True)
    alternate_phone_number        =      models.CharField(max_length=120,null=True,blank=True)


    def __str__(self):
        return str(self.billingprofile)
