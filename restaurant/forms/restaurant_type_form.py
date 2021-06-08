from django import forms
from restaurant.models import RestaurantType


class RestaurantTypeForm(forms.ModelForm):
    class Meta:
        model = RestaurantType
        fields = [
            'name',
            'image'
        ]
