from django.urls import path, include
from rest_framework import routers
from .views import CheckoutViewset

router = routers.DefaultRouter()
router.register(r'', CheckoutViewset)

urlpatterns = [
    path('', include(router.urls)),
]