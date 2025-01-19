from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser


# Serializer for creating a new user (signup)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_id', 'email', 'first_name', 'last_name', 'gender',
                  'yrs_of_exp', 'coding_exp_in_yrs', 'batch_no', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            yrs_of_exp=validated_data.get('yrs_of_exp'),
            coding_exp_in_yrs=validated_data.get('coding_exp_in_yrs'),
            batch_no=validated_data.get('batch_no'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Serializer for login (authentication)
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user
