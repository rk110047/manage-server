from .models import DeliveryPersonProfile
from rest_framework import serializers



class DeliveryPersonDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=	DeliveryPersonProfile
		fields		=		"__all__"
		read_only_fields    =        ["user"]
