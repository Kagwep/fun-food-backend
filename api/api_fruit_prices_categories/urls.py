from django.urls import path, include
from rest_framework import routers
from .views import PricesCategoryViewset

router = routers.DefaultRouter()
router.register(r'', PricesCategoryViewset)

urlpatterns = [
    path('', include(router.urls)),
]