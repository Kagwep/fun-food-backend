from django.urls import path, include
from rest_framework import routers
from .views import TokenViewSet

router = routers.DefaultRouter()
router.register(r'tokens', TokenViewSet,'tokens')

urlpatterns = [
    path('', include(router.urls)),

]