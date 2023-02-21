from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework import serializers, viewsets
from web.models import whishlist,Categorie,Food,Fruits,Drink
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

    # item_name = models.CharField(max_length=200)
    # item_in_category = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    # item = models.TextField()

class WhishlistSerializer(serializers.ModelSerializer):
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
        model = whishlist
        fields = ("id","item_id","category","item_details")
        
        
    def create(self, validated_data):
        category = validated_data.pop('category')
        # category = Categorie.objects.get(name=category)
        # category = category.id
        item_id = validated_data.pop('item_id')
      

        
        new_item = whishlist.objects.create(
            category = category,
            item_id = item_id,
 
        )
        
        return new_item
        
class WhishlistViewset(viewsets.ModelViewSet):
    queryset = whishlist.objects.all()
    serializer_class = WhishlistSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['product']
    # search_fields = ['=product', 'product_image_id']
    # ordering_fields = ['product', 'id']
    # ordering = ['id']