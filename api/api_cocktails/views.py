from django.shortcuts import render


from rest_framework import serializers, viewsets
from web.models import CockTail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

    # product= models.ForeignKey(Product,on_delete=models.CASCADE)
    # product_image_id = models.IntegerField()
    # product_other_image = models.ImageField(upload_to='product_images')

class CockTailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CockTail
        fields = ("id","cocktail_name","cocktail_price","cocktail_description","cocktail_image")
        
class CocktailViewset(viewsets.ModelViewSet):
    queryset = CockTail.objects.all()
    serializer_class = CockTailSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = (UserPermission,)
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['product']
    # search_fields = ['=product', 'product_image_id']
    # ordering_fields = ['product', 'id']
    # ordering = ['id']