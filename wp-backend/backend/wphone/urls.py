from django.urls import path, include
from rest_framework import routers
from . import views
from .views import *


router = routers.DefaultRouter()
router.register(r'wishlist', wishlistViewSet)
router.register(r'submit', submitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # # /api/submit
    path('submit', views.submit, name='submit'),
]