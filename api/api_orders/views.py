from django.shortcuts import render
    
from web.models import Order, Food, Drink, Fruits,Categorie

# Create your views here.
# Create your views here.
from rest_framework import serializers, viewsets
from web.models import Order,CustomUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission
from rest_framework.response import Response

    #  order_in_category= models.ForeignKey(Categorie,on_delete=models.CASCADE)
    # order_item = models.TextField()
    # order_quanitity= models.IntegerField()
    # order_price = models.IntegerField()
    # order_status = (("Delivered","Delivered"),
    #                 ("Pending"),"Pending"
    #                 )
    # order_status = models.CharField(max_length=200,choices=order_status, default="Pending")
    # delivery_location = models.CharField(max_length=700)

class OrderSerializer(serializers.ModelSerializer):
    item_details = serializers.SerializerMethodField(read_only=True)
    
    def get_item_details(self, order):
        category = order.category
        item_id = order.item_id
  
        category = Categorie.objects.get(id=category)
        
        category = category.name
        
        if category == "Foods":
            item = Food.objects.get(id=item_id)
        elif category == "Drinks":
            item = Drink.objects.get(id=item_id)
        elif category == "Fruits":
            item = Fruits.objects.get(id=item_id)
        else:
            item = None

        if item is not None:
            context = {
                "id": item.id,
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "image":item.image,
                "category": category
            }
            print(context)
            return context
        else:
            print("all")
            return None
                
    
    
        

    class Meta:
        model = Order
        
        fields = ["id", "category","item_details", "item_id", "order_count","order_made_by","order_price","order_added_on"]
        
    def create(self, validated_data):
        
        category = validated_data.pop('category')
        item_id = validated_data.pop('item_id')
        order_count = validated_data.pop('order_count')
        orderer = validated_data.pop('order_made_by')
        order_price = validated_data.pop('order_price')

        order_made_by = CustomUser.objects.get(id=orderer)
        
        new_order = Order.objects.create(
            category = category,
            item_id = item_id,
            order_count = order_count,
            order_made_by = order_made_by,
            order_price = order_price
           
        )
        
        return new_order
    
class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['product']
    # search_fields = ['=product', 'product_image_id']
    # ordering_fields = ['product', 'id']
    # ordering = ['id']

