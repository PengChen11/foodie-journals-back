from django.urls import path, include
from .views import ReceipeApiView, ReceipeDetail, SignUpView

urlpatterns = [
    path('receipes/', ReceipeApiView.as_view(), name='api'),
    path('receipes/<int:pk>/', ReceipeDetail.as_view(), name='details'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
