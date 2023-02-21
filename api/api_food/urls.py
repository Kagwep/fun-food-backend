from django.urls import path, include
from rest_framework import routers
from .views import FoodViewset

router = routers.DefaultRouter()
router.register(r'', FoodViewset)

urlpatterns = [
    path('', include(router.urls)),
]