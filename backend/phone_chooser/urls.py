# urls.py
from django.urls import include, path
from rest_framework import routers
from .views import wishlistViewSet

router = routers.DefaultRouter()
router.register(r'wishlist', wishlistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]