from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewset

router = routers.DefaultRouter()
router.register(r'', CategoryViewset)

urlpatterns = [
    path('', include(router.urls)),
]