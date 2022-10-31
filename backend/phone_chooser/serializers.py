from rest_framework import serializers
from .models import *

class wishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = wishlist
        fields = ('id', 'name', 'price', 'link', 'image')