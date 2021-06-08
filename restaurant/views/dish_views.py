from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from restaurant.models import Dish
from restaurant.models import Restaurant
from restaurant.models import Comment
from restaurant.forms import DishForm
from django.db.models import Avg,Count


def listDish(request):
    restaurant = Restaurant.objects.all()
    dish = Dish.objects.all()
    comment = Comment.objects.all()
    comment_avg = comment.aggregate(Avg('qualification'))
    return render(request, 'dish\index.html',
                  {'dish': dish, 'restaurant': restaurant, 'comment': comment, 'comment_avg': comment_avg})


def search(request):
    search = request.POST.get('search', False)
    dish = Dish.objects.filter(name__startswith=search)
    return render(request, 'dish\search_dish.html', {'dish': dish})


@permission_required('restaurant.add_dish')
def create(request):
    form = DishForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("dish")
    contex = {
        'form': form
    }
    return render(request, "dish/form_save.html", contex)


@permission_required('restaurant.change_dish')
def update(request, id):
    dish = Dish.objects.get(id=id)
    form = DishForm(request.POST or None, instance=dish)
    if form.is_valid():
        form.save()
        return redirect("dish")
    contex = {
        'form': form
    }
    return render(request, "dish/form_update.html", contex)


@permission_required('restaurant.delete_dish')
def delete(request, id):
    dish = Dish.objects.get(pk=id)
    dish.delete()
    return redirect("dish")
