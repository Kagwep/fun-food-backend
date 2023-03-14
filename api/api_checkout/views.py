import ast
import string
from django.shortcuts import render
from web.models import Order, Food, Drink, Fruits,Categorie,OrderCheckout,Checkout
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

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
    orderer = serializers.CharField(write_only =True,required= False,allow_blank= True,allow_null=False)
    latitude = serializers.CharField(write_only =True,required= False,allow_blank= True,allow_null=False)
    longitude = serializers.CharField(write_only =True,required= False,allow_blank= True,allow_null=False)
    order_number = serializers.CharField(write_only =True,required= False,allow_blank= True,allow_null=False)
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
                
    #     latitide = models.CharField(max_length=700)
    # longitude = models.CharField(max_length=200)
    
        

    class Meta:
        model = OrderCheckout
        
        fields = ["id","item_details",'latitude','longitude','orderer','items','order_amount', 'order_price','order_number']
        read_only_fields = ['order_amount', 'order_price']
        
    def create(self, validated_data):
        items = validated_data.pop('items')
        # category = validated_data.pop('category')
        # item = validated_data.pop('item')
        # order_amount = validated_data.pop('order_count')
        orderer = validated_data.pop('orderer')
        # order_price = validated_data.pop('order_price')
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')
        # order_status = validated_data.pop('order_status')
        order_number = validated_data.pop('order_number')

        order_made_by = CustomUser.objects.get(id=orderer)
        
        
    #         item_id = models.IntegerField()
    # category= models.IntegerField()
    # order_count = models.IntegerField()
    # order_price = models.IntegerField()
    # order_made_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    # order_added_on = models.DateTimeField(auto_now_add=True)
    
        
        order_total_price = 0
        new_order_items = []
        string = items[0]
        numbers = string.split(',')
        numbers = list(map(int, numbers))
  
        for el in numbers:
            print(el)
            order = Order.objects.get(id=el)
            
            order_total_price += order.order_price 
        
            new_order = OrderCheckout.objects.create(
                category = order.category,
                item = order.item_id,
                order_amount = order.order_count,
                order_made_by = order.order_made_by,
                order_price = order.order_price,
            
            )
            
            new_order_items.append(new_order.id)
            
            order.delete()
            
        print(new_order_items)
        
        comp_order = Checkout.objects.create(
            
            orderer = order_made_by,
            ordered_items  = new_order_items,
            order_total_price = order_total_price,
            latitude = latitude,
            longitude = longitude,
            order_status = 1,
            order_number = order_number,
            
        )
        
        return new_order
    
class CheckoutViewset(viewsets.ModelViewSet):
    queryset = OrderCheckout.objects.all()
    serializer_class = CheckoutSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['order_made_by','id']
    # search_fields = ['=name', 'price']
    ordering_fields = ['order_price', 'id']
    ordering = ['id']
 
    #  orderer =  orderer=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    # ordered_items = models.CharField(max_length=1000)
    # order_total_price = models.IntegerField()
    # order_placed_at = models.DateTimeField(auto_now_add=True)
    # latitude = models.CharField(max_length=700,null=True)
    # longitude = models.CharField(max_length=200,null=True)
    # order_status = (("Delivered","Delivered"),
    #                 ("Pending","Pending")
    #                 )
    # order_status   
    
class CompleteOrderSerializer(serializers.ModelSerializer):
    
    order_placed_at = serializers.ReadOnlyField()
    # status = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = Checkout
        fields = ["orderer","ordered_items","order_total_price","order_placed_at","latitude","longitude","order_status","order_placed_at","status","order_number"]
    
    def get_status(self, obj):
        return obj.get_order_status_display()
    
class CompleteOrderViewset(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CompleteOrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['order_status','id','orderer',]
    search_fields = ['order_total_price', 'order_number']
    ordering_fields = ['order_total_price', 'id']
    ordering = ['id']
    
class OderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderCheckout.objects.all()
    serializer_class = CheckoutSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['order_made_by','id']
    # search_fields = ['=name', 'price']
    ordering_fields = ['order_price', 'id']
    ordering = ['id']
    
    def list(self, request):
        ids = request.query_params.get('ids')
        if ids:
            id_list = ids.split(',')
            queryset = self.filter_queryset(self.get_queryset().filter(id__in=id_list))
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return super().list(request)