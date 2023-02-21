# from django.urls import path, include
# from rest_framework import routers
# from .views import CombinedItemsViewSet

# router = routers.DefaultRouter()
# router.register(r'', CombinedItemsViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework import routers
from .views import FruitHomeViewset,FoodHomeViewset,DrinkHomeViewset

router = routers.DefaultRouter()
router.register(r'home-drinks', DrinkHomeViewset,basename='home-drinks')
router.register(r'home-fruits', FruitHomeViewset,basename='home-fruits')
router.register(r'home-food', FoodHomeViewset,'home-food')

urlpatterns = [
    path('', include(router.urls)),
]