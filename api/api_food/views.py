from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework import serializers, viewsets
from web.models import Food
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

    # food_name = models.CharField( max_length=400)
    # food_image = models.CharField(max_length=700)
    # food_description = models.TextField()
    # food_price = models.IntegerField(default=0)
    # food_category = models.ForeignKey(Categorie,on_delete=models.CASCADE)

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("id","name","price","description","image","category")
        
class FoodViewset(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price']
    search_fields = ['=name', 'description']
    ordering_fields = ['price', 'id']
    ordering = ['id']