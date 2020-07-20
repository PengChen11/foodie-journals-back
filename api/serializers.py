# api/serializers.py
from rest_framework import serializers

from .models import Recipe, CustomUser
# from django.contrib.auth.models import User


class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'img_src_1', 'img_src_2', 'img_src_3', 'steps', 'ingredients', 'meal_type','description','difficulty','created_at', 'updated_at', 'author')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password',)
        extra_kwargs = {"password":{'write_only': True}}

    def save(self):
        account = CustomUser(
            email = self.validated_data['email'],
        )
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return CustomUser




class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name','last_name')
