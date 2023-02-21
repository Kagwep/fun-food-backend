from django.urls import path, include
from rest_framework import routers
from .views import CocktailViewset

router = routers.DefaultRouter()
router.register(r'', CocktailViewset)

urlpatterns = [
    path('', include(router.urls)),
]