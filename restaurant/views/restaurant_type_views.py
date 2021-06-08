from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from restaurant.models import RestaurantType
from restaurant.models import Restaurant
from restaurant.forms import RestaurantTypeForm


def search(request):
    search = request.POST.get('search', False)
    filter = RestaurantType.objects.filter(name__startswith=search)
    return render(request, 'principal\search_restaurantType.html', {'restaurantTypes': filter})


def detail(request, id):
    detail = RestaurantType.objects.get(pk=id)
    filter = Restaurant.objects.filter(restauran_type_id__name=detail)
    return render(request, 'restaurant\\type_food.html', {'restaurants': filter})


@permission_required('restaurant.add_restaurant_type')
def create(request):
    form = RestaurantTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("WorldRestaurant")

    context = {
        'form': form
    }

    return render(request, "restaurant_type/form_save.html", context)

@permission_required('restaurant.change_restaurant_type')
def update(request,id):
    restaurntType=RestaurantType.objects.get(id=id)
    form =RestaurantTypeForm(request.POST or None, instance=restaurntType)
    if form.is_valid():
        form.save()
        return redirect("WorldRestaurant")
    contex={
        'form':form
    }
    return render(request,"restaurant_type/form_update.html",contex)

@permission_required('restaurant.delete_restaurant_type')
def delete(request,id):
    restaurantType=RestaurantType.objects.get(pk=id)
    restaurantType.delete()
    return redirect("WorldRestaurant")
