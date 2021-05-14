from rest_framework import serializers
from .models import CollectorProfile



class CollectorProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = CollectorProfile
		fields = "__all__"
		read_only_fields    =        ["user"]



