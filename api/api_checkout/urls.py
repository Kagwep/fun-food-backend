from django.urls import path, include
from rest_framework import routers
from .views import CheckoutViewset,CompleteOrderViewset

router = routers.DefaultRouter()
router.register(r'', CheckoutViewset)
router.register(r'order-comp', CompleteOrderViewset,'order-comp')

urlpatterns = [
    path('', include(router.urls)),
]