from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=8,error_messages={"min_length":"Password is not long enough"})
    password2 = serializers.CharField(write_only=True,min_length=8,error_messages={"min_length":"Password is not long enough"})
    class Meta:
        model=User
        fields= '__all__'
    def validate(self,data):
        if data["password"]!=data["password2"]:
            raise serializers.ValidationError("Password does not match")
        return data
    def create(self,validated_data):
        user = User.objects.create(
        username = validated_data["username"],
        email= validated_data["email"],
        first_name=validated_data["first_name"],
        last_name =validated_data["last_name"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['id','username','first_name','last_name']
