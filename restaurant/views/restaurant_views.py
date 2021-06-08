from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from restaurant.models import Restaurant
from restaurant.models import Comment
from restaurant.models import Dish
from restaurant.forms import RestaurantForm
from django.db.models import Avg


# Create your views here.

def listRestaurants(request):
    list = Restaurant.objects.all()
    return render(request, 'restaurant\index.html', {'restaurant': list})


def search(request):
    search = request.POST.get('search', False)
    filter = Restaurant.objects.filter(name__startswith=search)
    return render(request, 'restaurant\search_restaurant.html', {'restaurant': filter})


def searchFood(request, id):
    search = request.POST.get('search', False)
    restaurant = Restaurant.objects.get(id=id)
    dish = Dish.objects.filter(name__startswith=search)
    comment = Comment.objects.filter(restaurant_id__name=restaurant)
    comment_avg = comment.aggregate(Avg('qualification'))
    comment_count = comment.count()
    return render(request, 'restaurant\search_food_restaurant.html',
                  {'restaurant': restaurant, 'dish': dish, 'comment': comment, 'comment_avg': comment_avg,
                   'comment_count': comment_count})


def detail(request, id):
    restaurant = Restaurant.objects.get(id=id)
    dish = Dish.objects.filter(restaurant_id__name=restaurant)
    comment = Comment.objects.filter(restaurant_id__name=restaurant)
    comment_avg = comment.aggregate(Avg('qualification'))
    comment_count = comment.count()
    return render(request, 'dish\\restaurant_detail.html',
                  {'restaurant': restaurant, 'dish': dish, 'comment': comment, 'comment_avg': comment_avg,
                   'comment_count': comment_count})


@permission_required('restaurant.add_restaurant')
def create(request):
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("restaurants")

    context = {
        'form': form
    }

    return render(request, "restaurant/form_save.html", context)


@permission_required('restaurant.change_restaurant')
def update(request, id):
    restaurant = Restaurant.objects.get(id=id)
    form = RestaurantForm(request.POST or None, instance=restaurant)
    if form.is_valid():
        form.save()
        return redirect("restaurants")
    contex = {
        'form': form
    }
    return render(request, "restaurant/form_update.html", contex)


@permission_required('restaurant.delete_restaurant')
def delete(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    restaurant.delete()
    return redirect("restaurants")
