from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'FirstName', 'LastName', 'Email']
        
    def validate_Email(self, value):
        if not "@" in value or not "." in value:
            raise serializers.ValidationError("Email is not proper")
        return value

    def validate_Password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long")
        return value



