from django import forms
from restaurant.models import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'restauran_type_id',
            'name',
            'country',
            'city',
            'phone',
            'direction',
            'website',
            'image'
        ]
