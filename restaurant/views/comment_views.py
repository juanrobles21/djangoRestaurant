from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from restaurant.models import Comment, Restaurant
from django.contrib.auth.models import User
from restaurant.forms import CommentForm


@login_required()
def Comment(request, id):
    restaurant = Restaurant.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.restaurant_id = restaurant
            comment.save()
            return redirect("restaurants")
    else:
        form = CommentForm()

        contex = {
            'form': form
        }
        return render(request, "comment/create_comment.html", contex)


'''
@login_required()
def Comment(request):
    form=CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("dish")
    contex={
        'form':form
    }
    return render(request,"comment/create_comment.html",contex)
'''
