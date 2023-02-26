from django.urls import path, include
from rest_framework import routers
from .views import FruitCategoryViewset

router = routers.DefaultRouter()
router.register(r'', FruitCategoryViewset)

urlpatterns = [
    path('', include(router.urls)),
]