from django.db import models
from authentication.models import User
from django.db.models.signals import post_save,pre_save
from .utils import unique_id_generator



class EWallet(models.Model):
    wallet_id           =       models.CharField(max_length=120,blank=True)
    User                =       models.OneToOneField(User,on_delete=models.CASCADE)
    email               =       models.EmailField(unique=True)
    active              =       models.BooleanField(default=True)
    timestamp           =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)
    money               =       models.DecimalField(default=0.00,max_digits=20,decimal_places=2)


    def __str__(self):
        return self.email

def user_created_receiver(instance,sender,created,*args,**kwargs):
    if created:
        EWallet.objects.get_or_create(User=instance,email=instance.email)

post_save.connect(user_created_receiver,sender=User)



def pre_save_wallet_id_creator(instance,sender,*args,**kwargs):
    if not instance.wallet_id:
        instance.wallet_id = unique_id_generator(instance)


pre_save.connect(pre_save_wallet_id_creator,sender=EWallet)


