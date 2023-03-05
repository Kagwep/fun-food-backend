from django.shortcuts import render
from web.models import Order, Food, Drink, Fruits,Categorie,OrderCheckout,Checkout


# # Create your views here.
# class OrderCheckout(models.Model):
#     
#     item = models.IntegerField()
#     category = models.IntegerField()
#     order_amount = models.IntegerField()
#     order_status = (("Delivered","Delivered"),
#                     ("Pending","Pending")
#                     )
#     order_status = models.CharField(max_length=200,choices=order_status, default=order_status[1][0])
#     delivery_location = models.CharField(max_length=700)
#     order_date = models.DateTimeField(auto_now_add=True)
#     order_made_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     order_price = models.IntegerField()
    
# class Checkout(models.Model):
#     orderer =  orderer=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     ordered_items = models.CharField(max_length=1000)
#     order_total_price = models.IntegerField()
#     order_placed_at = models,models.IntegerField()
#     delivery_location = models.CharField(max_length=700)


from rest_framework import serializers, viewsets
from web.models import Order,CustomUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission
from rest_framework.response import Response

    # order_in_category= models.ForeignKey(Categorie,on_delete=models.CASCADE)
    # order_item = models.TextField()
    # order_quanitity= models.IntegerField()
    # order_price = models.IntegerField()
    # order_status = (("Delivered","Delivered"),
    #                 ("Pending"),"Pending"
    #                 )
    # order_status = models.CharField(max_length=200,choices=order_status, default="Pending")
    # delivery_location = models.CharField(max_length=700)

class CheckoutSerializer(serializers.ModelSerializer):
    item_details = serializers.SerializerMethodField(read_only=True)
    items = serializers.ListField(child=serializers.CharField(), write_only=True)
    
    
    def get_item_details(self, order):
        category = order.category
        item = order.item
  
        category = Categorie.objects.get(id=category)
        
        category = category.name
        
        if category == "Foods":
            item = Food.objects.get(id=item)
        elif category == "Drinks":
            item = Drink.objects.get(id=item)
        elif category == "Fruits":
            item = Fruits.objects.get(id=item)
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
        model = OrderCheckout
        
        fields = ["id", "category","item","item_details", "order_amount","order_price","order_made_by","order_price","order_date","delivery_location","items"]
        
    def create(self, validated_data):
        items = validated_data.pop('items')
        category = validated_data.pop('category')
        item = validated_data.pop('item')
        order_amount = validated_data.pop('order_count')
        orderer = validated_data.pop('order_made_by')
        order_price = validated_data.pop('order_price')
        delivery_location = validated_data.pop('delivery_location')
        # order_status = validated_data.pop('order_status')

        order_made_by = CustomUser.objects.get(id=orderer)
        
        order_total_price = 0
        
        new_order = OrderCheckout.objects.create(
            category = category,
            item = item,
            order_amount = order_amount,
            order_made_by = order_made_by,
            order_price = order_price,
            delivery_location = delivery_location
           
        )
        
        comp_order = Checkout.objects.create(
            
            orderer = order_made_by,
            ordered_items  = items,
            order_total_price = order_total_price,
            delivery_location = delivery_location,
            
        )
        
        return comp_order
    
class CheckoutViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = CheckoutSerializer