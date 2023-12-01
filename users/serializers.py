from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

	class Meta:

		model = get_user_model()
		fields = ('id', 'username')


class RegisterSerializer(serializers.Serializer):

	username = serializers.CharField(max_length=120)
	password = serializers.CharField(write_only=True)


class LoginSerializer(serializers.Serializer):

	username = serializers.CharField(max_length=120)
	password = serializers.CharField(write_only=True)
