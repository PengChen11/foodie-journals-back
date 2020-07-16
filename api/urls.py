from django.urls import path, include
from .views import ReceipeApiView, ReceipeDetail, SignUpView, BreakfastApiView, LunchApiView, DinnerApiView

urlpatterns = [
    path('recipes/', ReceipeApiView.as_view(), name='api'),
    path('recipes/<int:pk>/', ReceipeDetail.as_view(), name='details'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('recipes/breakfast/',BreakfastApiView.as_view()),
    path('recipes/lunch/',LunchApiView.as_view()),
    path('recipes/dinner/',DinnerApiView.as_view()),
]
