from rest_framework import serializers
from .models import EWallet



class EwalletSerializer(serializers.ModelSerializer):
	class Meta:
		model   = EWallet
		fields  = "__all__"
