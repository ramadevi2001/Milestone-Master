from rest_framework import serializers # type: ignore
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'Password': {'write_only': True}}  # Ensure password is write-only

    def validate_Email(self, value):
        if "@" not in value or "." not in value:
            raise serializers.ValidationError("Email is not proper")
        return value

    def validate_Password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long")
        return value

    def create(self, validated_data):
        # Encrypt the password before saving
        validated_data['Password'] = make_password(validated_data['Password'])
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        # Encrypt the password if it's being updated
        if 'Password' in validated_data:
            validated_data['Password'] = make_password(validated_data['Password'])
        return super(UserSerializer, self).update(instance, validated_data)
