from django.urls import path, include
from rest_framework import routers
from .views import CheckoutViewset,CompleteOrderViewset,OderItemViewSet

router = routers.DefaultRouter()
router.register(r'order', CheckoutViewset,'order')
router.register(r'order-comp', CompleteOrderViewset,'order-comp')
router.register(r'order-checks', OderItemViewSet,'order-checks')

urlpatterns = [
    path('', include(router.urls)),
]