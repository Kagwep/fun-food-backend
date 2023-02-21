from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from web.models import Categorie
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ("id","name",)
        
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)