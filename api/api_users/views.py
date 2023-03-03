from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from web.models import CustomUser
from rest_framework import viewsets

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id','full_names', 'phone_number', 'location', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create(
            full_names=validated_data['full_names'],
            phone_number=validated_data['phone_number'],
            location=validated_data['location'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    




class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer