from django.urls import path, include
from rest_framework import routers
from .views import DrinkCategoryViewset

router = routers.DefaultRouter()
router.register(r'', DrinkCategoryViewset)

urlpatterns = [
    path('', include(router.urls)),
]