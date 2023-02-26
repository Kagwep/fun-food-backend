from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework import serializers, viewsets
from web.models import Fruits
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

    # product= models.ForeignKey(Product,on_delete=models.CASCADE)
    # product_image_id = models.IntegerField()
    # product_other_image = models.ImageField(upload_to='product_images')

class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = ("id","name","price","description","image","category","in_category")
        
class FruitsViewset(viewsets.ModelViewSet):
    queryset = Fruits.objects.all()
    serializer_class = FruitsSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['in_category']
    search_fields = ['=name', 'description']
    ordering_fields = ['price', 'id']
    ordering = ['id']