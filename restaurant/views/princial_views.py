from django.shortcuts import render
from django.shortcuts import render, redirect
from restaurant.models import RestaurantType
from restaurant.models import Restaurant
# Create your views here.

def listRestaurantType(request):
    list=RestaurantType.objects.all()
    return render(request,'principal\index.html',{'restaurantTypes':list})

