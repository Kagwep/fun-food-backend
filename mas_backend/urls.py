"""mas_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls")),
    path('api/categories/', include("api.api_categories.urls")),
    path('api/drink_categories/', include("api.api_drinks_category.urls")),
    path('api/fruit_categories/', include("api.api_fruits_category.urls")),
    path('api/prices_categories/', include("api.api_fruit_prices_categories.urls")),
    path('api/foods/', include("api.api_food.urls")),
    path('api/drinks/', include("api.api_drinks.urls")),
    path('api/orders/', include("api.api_orders.urls")),
    path('api/wishlist/', include("api.api_wishlist.urls")),
    path('api/cocktails/', include("api.api_cocktails.urls")),
    path('api/fruits/', include("api.api_fruits.urls")),
    path('api/all/', include("api.api_all.urls")),
    path('api/users/', include("api.api_users.urls")),
    path('api/', include("api.api_tokens.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)