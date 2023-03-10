
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from web.models import PricessCategorie
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

class PricesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PricessCategorie
        fields = ("id","p_name",)
        
class PricesCategoryViewset(viewsets.ModelViewSet):
    queryset = PricessCategorie.objects.all()
    serializer_class = PricesCategorySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)