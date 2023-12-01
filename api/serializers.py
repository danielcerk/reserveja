from rest_framework import serializers
from application.models import *

class restauranteSerializer(serializers.ModelSerializer):

	class Meta:

		model = restaurante
		fields = ('nome', 'descricao', 'foto', 'user', 'created_at')
