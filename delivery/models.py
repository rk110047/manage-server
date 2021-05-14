

from django.db import models
from authentication.models import User

class DeliveryPersonProfile(models.Model):
	user				=		models.OneToOneField(User,on_delete=models.CASCADE)
	first_name			=		models.CharField(max_length=120)
	last_name			=		models.CharField(max_length=120)
	person_photo		=		models.FileField(upload_to='delivery boy photo/')
	contact_number		=		models.CharField(max_length=120)
	address				=		models.CharField(max_length=120)
	state				=		models.CharField(max_length=120)
	city				=		models.CharField(max_length=120)
	postal_code			=		models.CharField(max_length=120)
	vehicle_number		=		models.CharField(max_length=120)
	licence_number		=		models.CharField(max_length=120)

#	def __str__(self):
#		return self.user
