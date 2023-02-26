from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from web.models import FruitssCategorie
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

class FriutCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitssCategorie
        fields = ("id","drink_name",)
        
class FruitCategoryViewset(viewsets.ModelViewSet):
    queryset = FruitssCategorie.objects.all()
    serializer_class = FriutCategorySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)