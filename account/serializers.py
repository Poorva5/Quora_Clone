from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=False)

    class Meta:
        model = models.UserData
        fields = ['id', 'email', 'password']

    def create(self, validated_data):
        user = models.UserData.objects.create_user(validated_data['email'])
        user.set_password(validated_data['password'])
        return user




