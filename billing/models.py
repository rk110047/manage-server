from django.db import models
from authentication.models import User
from django.db.models.signals import post_save
import stripe

# Create your models here.
#from accounts.models import Account
stripe.api_key = "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"



class BillingProfile(models.Model):
    User                =       models.OneToOneField(User,on_delete=models.CASCADE)
    email               =       models.EmailField(unique=True)
    active              =       models.BooleanField(default=True)
    stripe_id           =       models.CharField(max_length=120,null=True,blank=True)
    timestamp           =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)
    ammount             =       models.DecimalField(decimal_places=2,max_digits=10,default=0.00)


    def __str__(self):
        return self.email


def user_created_receiver(instance,sender,created,*args,**kwargs):
    if created:
        account = stripe.Account.create(
                      type="express",
                      country="US",
                      email=instance.email,
                      capabilities={
                        "card_payments": {"requested": True},
                        "transfers": {"requested": True},
                      },
                    )
        BillingProfile.objects.get_or_create(User=instance,email=instance.email,stripe_id=account.id)
#        Account.objects.get_or_create(User=instance)


post_save.connect(user_created_receiver,sender=User)

class Card(models.Model):
    User                =       models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    number              =       models.CharField(max_length=120)
    exp_month           =       models.CharField(max_length=120)
    exp_year            =       models.CharField(max_length=120)

    def __str__(self):
        return F"{self.User}"
