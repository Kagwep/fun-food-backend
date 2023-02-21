from django.urls import path, include
from rest_framework import routers
from .views import WhishlistViewset

router = routers.DefaultRouter()
router.register(r'', WhishlistViewset)

urlpatterns = [
    path('', include(router.urls)),
]