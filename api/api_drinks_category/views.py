from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from web.models import DrinksCategorie
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

class DrinkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinksCategorie
        fields = ("id","drink_name",)
        
class DrinkCategoryViewset(viewsets.ModelViewSet):
    queryset = DrinksCategorie.objects.all()
    serializer_class = DrinkCategorySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)