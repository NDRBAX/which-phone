from django.shortcuts import render
from rest_framework import viewsets
from .models import wishlist
from .serializers import wishlistSerializer


class wishlistViewSet(viewsets.ModelViewSet):
    queryset = wishlist.objects.all()
    serializer_class = wishlistSerializer