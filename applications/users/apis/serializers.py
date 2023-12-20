from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'password']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        username = self.validated_data['username'].strip()
        email = self.validated_data['email'].strip()
        first_name = self.validated_data['first_name'].strip()
        last_name = self.validated_data['last_name'].strip()
        password = self.validated_data['password'].strip()

        if not str(username[0]).isalpha():
            raise serializers.ValidationError({'username': ['Username must contain characters.']})

        if len(str(first_name)) == 0:
            raise serializers.ValidationError({'first_name': ['This field may not be blank.']})

        if len(str(last_name)) == 0:
            raise serializers.ValidationError({'last_name': ['This field may not be blank.']})

        if len(password) < 8:
            raise serializers.ValidationError({'password': ['Password must contain at least 8 characters.']})

        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({'email': ['A user with that email already exists.']})

        user = User.objects.create_user(username = username,email = email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        return user