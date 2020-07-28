from .models import Recipe, CustomUser
from .serializers import RecipesSerializer, UserCreateSerializer, UserListSerializer
from .permissions import IsAuthorOrReadOnly

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend

# Recipes views
class RecipesList(ListAPIView):
    search_fields = ['description', 'title', 'ingredients', 'meal_type', 'difficulty']
    filter_backends = (filters.SearchFilter,)
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer

class UserRecipesList(ListAPIView):
    search_fields = ['author']
    filter_backends = (filters.SearchFilter,)
    queryset = Recipe.objects.all()
    # queryset = Recipe.objects.filter(author=1)
    serializer_class = RecipesSerializer

class RecipeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer

class RecipeCreate(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer

class BreakfastApiView(ListAPIView):
    queryset = Recipe.objects.filter(meal_type='Breakfast')
    serializer_class = RecipesSerializer

class LunchApiView(ListAPIView):
    queryset = Recipe.objects.filter(meal_type='Lunch')
    serializer_class = RecipesSerializer

class DinnerApiView(ListAPIView):
    queryset = Recipe.objects.filter(meal_type='Dinner')
    serializer_class = RecipesSerializer


# User views
class UserCreate(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = ()

class UserListView(ListAPIView):
    search_fields = ['email']
    filter_backends = (filters.SearchFilter,)
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer



