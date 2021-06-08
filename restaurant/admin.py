from django.contrib import admin
from .models import *

admin.site.register(RestaurantType)
admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(Dish)


