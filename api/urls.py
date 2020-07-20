from django.urls import path, include
from .views import RecipesList, RecipeDetail, BreakfastApiView, LunchApiView, DinnerApiView, RecipeCreate, UserCreate, UserListView, UserDetail

urlpatterns = [
    # recipe views
    path('recipes/', RecipesList.as_view()),
    path('recipes/<int:pk>/', RecipeDetail.as_view()),
    path('recipes/breakfast/',BreakfastApiView.as_view()),
    path('recipes/lunch/',LunchApiView.as_view()),
    path('recipes/dinner/',DinnerApiView.as_view()),
    path('recipes/create/', RecipeCreate.as_view()),
    # user views
    path('users/register/', UserCreate.as_view()),                          # create
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetail.as_view(),)
]
