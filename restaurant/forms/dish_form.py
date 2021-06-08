from django import forms
from restaurant.models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            'restaurant_id',
            'image',
            'name',
            'description',
            'price'
        ]
