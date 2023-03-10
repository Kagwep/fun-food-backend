# Create your views here.
from rest_framework import serializers, viewsets
from web.models import Drink
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

    # product= models.ForeignKey(Product,on_delete=models.CASCADE)
    # product_image_id = models.IntegerField()
    # product_other_image = models.ImageField(upload_to='product_images')

class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ("id","name","image","price","description","category","drink_category")
        
class DrinksViewset(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinksSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['drink_category']
    search_fields = ['=name', 'price']
    ordering_fields = ['price', 'id']
    ordering = ['id']