"""djangoRestaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import car.views
from car import views
from restaurant.views import princial_views
from restaurant.views import restaurant_type_views
from restaurant.views import restaurant_views
from restaurant.views import dish_views
from restaurant.views import comment_views
from restaurant.views import user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('WorldRestaurant/register', user_views.register, name='Register'),
    path('WorldRestaurant/login', user_views.loginView, name='login'),
    path('WorldRestaurant/logout', user_views.logout_v, name='logout'),
    path('WorldRestaurant', princial_views.listRestaurantType, name="WorldRestaurant"),
    path('WorldRestaurant/create/RestaurantType', restaurant_type_views.create, name="create_restaurant_type"),
    path('WorldRestaurant/delete/RestaurantType/<int:id>', restaurant_type_views.delete, name="delete_restaurant_type"),
    path('WorldRestaurant/update/RestaurantType/<int:id>', restaurant_type_views.update, name="update_restaurant_type"),
    path('WorldRestaurant/search/RestaurantType', restaurant_type_views.search, name="search_restaurant_type"),
    path('WorldRestaurant/RestaurantType/restaurants/<int:id>', restaurant_type_views.detail,
         name="detail_restaurant_type"),
    path('WorldRestaurant/Restaurants', restaurant_views.listRestaurants, name="restaurants"),
    path('WorldRestaurant/create/Restaurant', restaurant_views.create, name="create_restaurant"),
    path('WorldRestaurant/delete/Restaurant/<int:id>', restaurant_views.delete, name="delete_restaurant"),
    path('WorldRestaurant/update/Restaurant/<int:id>', restaurant_views.update, name="update_restaurant"),
    path('WorldRestaurant/search/Restaurant', restaurant_views.search, name="search_restaurant"),
    path('WorldRestaurant/Restaurant/food/<int:id>', restaurant_views.detail, name="restaurants_food"),
    path('WorldRestaurant/Restaurant/seach_food/<int:id>', restaurant_views.searchFood, name="search_restaurant_dish"),
    path('WorldRestaurant/Dish', dish_views.listDish, name="dish"),
    path('WorldRestaurant/create/Dish', dish_views.create, name="create_dish"),
    path('WorldRestaurant/delete/Dish/<int:id>', dish_views.delete, name="delete_dish"),
    path('WorldRestaurant/update/Dish/<int:id>', dish_views.update, name="update_dish"),
    path('WorldRestaurant/search/Dish', dish_views.search, name="search_dish"),
    path('WorldRestaurant/comment/Restaurant/<int:id>', comment_views.Comment, name="create_comment"),
    path('WorldRestaurant/car', car.views.list, name="car"),
    path('WorldRestaurant/add_car/<int:dish_id>', views.add_dish, name="add_car"),
    path('WorldRestaurant/delete_car/<int:dish_id>', car.views.delete_dish, name="delete_car"),
    path('WorldRestaurant/substract_car/<int:dish_id>', car.views.substract_dish, name="subtrac_car"),
    path('WorldRestaurant/comfirmer/', car.views.Confirmarcorreo, name="email"),
    path('WorldRestaurant/finish_compra/', car.views.clear_car, name="clear"),
    path('WorldRestaurant/enviar/', car.views.correo, name="enviarCorreo"),
]
