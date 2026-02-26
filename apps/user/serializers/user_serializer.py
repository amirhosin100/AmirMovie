from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.user.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(write_only=True)
    password_2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password_1',
            'password_2',
        )

    def validate(self, data):
        password_1 = data.get('password_1')
        password_2 = data.get('password_2')

        if password_1 != password_2:
            raise ValidationError('Passwords do not match')

        return data

    def create(self, validated_data):
        password = validated_data.pop('password_1')
        username = validated_data.pop('username')

        user = User.objects.create_user(username=username, password=password)

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'national_code',
        )
        read_only_fields = ('username',)