from django.urls import path, include
from .views import ReceipeApiView, ReceipeDetail, SignUpView, BreakfastApiView, LunchApiView, DinnerApiView

urlpatterns = [
    path('receipes/', ReceipeApiView.as_view(), name='api'),
    path('receipes/<int:pk>/', ReceipeDetail.as_view(), name='details'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('receipes/breakfast/',BreakfastApiView.as_view()),
    path('receipes/lunch/',LunchApiView.as_view()),
    path('receipes/dinner/',DinnerApiView.as_view()),
]
