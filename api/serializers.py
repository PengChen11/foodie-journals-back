# api/serializers.py
from rest_framework import serializers

from .models import Receipe


class ReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        fields = ('id', 'title', 'img_src_1', 'img_src_2', 'img_src_3', 'steps', 'ingredients', 'meal_type','description','difficulty','created_at', 'updated_at', 'author')
