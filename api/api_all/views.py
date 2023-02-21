from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from rest_framework.response import Response

# Create your views here.
from rest_framework import serializers, viewsets,status
from web.models import Drink,Fruits,Food
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

    # product= models.ForeignKey(Product,on_delete=models.CASCADE)
    # product_image_id = models.IntegerField()
    # product_other_image = models.ImageField(upload_to='product_images')
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = '__all__'
        
        
class FoodHomeViewset(viewsets.ModelViewSet):
    queryset = Food.objects.filter().order_by('id')[:5]
    serializer_class = FoodSerializer

class DrinkHomeViewset(viewsets.ModelViewSet):
    queryset = Drink.objects.filter().order_by('id')[:5]
    serializer_class = DrinkSerializer

class FruitHomeViewset(viewsets.ModelViewSet):
    queryset = Fruits.objects.filter().order_by('id')[:5]
    serializer_class = FruitSerializer

# class CombinedItemsSerializer(serializers.Serializer):
#     food_items = FoodSerializer(many=True)
#     drink_items = DrinkSerializer(many=True)
#     fruit_items = FruitSerializer(many=True)
    
    
    
# class CombinedItemsViewSet(viewsets.ModelViewSet):
#     food_items = Food.objects.filter().order_by('id')[:5]
#     drink_items = Drink.objects.filter().order_by('id')[:5]
#     fruit_items = Fruits.objects.filter().order_by('id')[:5]
#     combined_items = list(food_items) + list(drink_items) + list(fruit_items)
#     queryset = combined_items
#     serializer_class = CombinedItemsSerializer

    # def list(self, request):
    #     food_items = Food.objects.filter().order_by('id')[:5]
    #     drink_items = Drink.objects.filter().order_by('id')[:5]
    #     fruit_items = Fruits.objects.filter().order_by('id')[:5]

    #     combined_items = list(food_items) + list(drink_items) + list(fruit_items)

    #     serializer = self.serializer_class(combined_items, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

# class AllSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Drink
#         fields = ("id","name","image","price","price","description","category")
        
# class DrinksViewset(viewsets.ModelViewSet):
    
#     food_items = Food.objects.filter().order_by('id')[:5]
#     drink_items = Drink.objects.filter().order_by('id')[:5]
#     fruit_items = Fruits.objects.filter().order_by('id')[:5]

#     combined_items = list(food_items) + list(drink_items) + list(fruit_items)
    
#     queryset = combined_items
#     serializer_class = AllSerializer
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = (UserPermission,)
#     # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     # filterset_fields = ['product']
#     # search_fields = ['=product', 'product_image_id']
#     # ordering_fields = ['product', 'id']
#     # ordering = ['id']