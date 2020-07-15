from rest_framework import generics

from .models import Receipe
from .serializers import ReceipeSerializer
# from .permissions import IsAuthorOrReadOnly

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

# Create your views here.
class ReceipeApiView(generics.ListCreateAPIView):
    queryset = Receipe.objects.all()
    serializer_class = ReceipeSerializer

class ReceipeDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Receipe.objects.all()
    serializer_class = ReceipeSerializer


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    # success_url = 'https://foodie-journals-front-end.vercel.app/signup'
    # template_name = 'signup.html'


class BreakfastApiView(generics.ListCreateAPIView):
    queryset = Receipe.objects.filter(meal_type='Breakfast')
    serializer_class = ReceipeSerializer

class LunchApiView(generics.ListCreateAPIView):
    queryset = Receipe.objects.filter(meal_type='Lunch')
    serializer_class = ReceipeSerializer

class DinnerApiView(generics.ListCreateAPIView):
    queryset = Receipe.objects.filter(meal_type='Dinner')
    serializer_class = ReceipeSerializer


