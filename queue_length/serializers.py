from rest_framework import serializers
from .models import  Logdata_put



class Logdata_putSerializer(serializers.ModelSerializer):
	class Meta:
		model=Logdata_put
		fields='__all__'