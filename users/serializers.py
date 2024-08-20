from rest_framework import serializers
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password

class CreateUserSerializer(serializers.Serializer):
    
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(
        required=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+99999'. Up to 15 digits allowed."
            )
        ]
    )
    first_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    def validate_first_name(self, value):
        if value.isdigit():
            raise serializers.ValidationError("Username must be a string, not a number.")
        return value

    # validate other fields starting with validate_
    # def validate_email(self, value):
    #   pass

