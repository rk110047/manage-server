from django.db import models
from authentication.models import User
# Create your models here.
class CollectorProfile(models.Model):
	user				=		models.OneToOneField(User,on_delete=models.CASCADE)
	first_name			=		models.CharField(max_length=120)
	last_name			=		models.CharField(max_length=120)
	person_photo		=		models.FileField(upload_to='delivery boy photo/',null=True,blank=True)
	contact_number		=		models.CharField(max_length=120)
	address				=		models.CharField(max_length=120)
	state				=		models.CharField(max_length=120)
	city				=		models.CharField(max_length=120)
	postal_code			=		models.CharField(max_length=120)
	id_number			=		models.CharField(max_length=120)





	def __str__(self):
		return self.first_name + self.last_name
