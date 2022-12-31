from django.urls import path, include
from rest_framework import routers
from . import views
from .views import *
from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'token': csrf_token})


urlpatterns = [
    path('submit', views.submit, name='submit'),
    path('get_csrf_token/', get_csrf_token),
    path('edit_wishlist', views.edit_wishlist, name='edit_wishlist'),
    path('get_wishlist', views.get_wishlist, name='get_wishlist'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('submit_new_password', views.submit_new_password, name='submit_new_password'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('set_secure', views.set_secure, name='set_secure'),
    path('get_categories', views.get_categories, name='get_categories'),
    path('subscribe_newsletter', views.subscribe_newsletter, name='subscribe_newsletter'),
]