
from django.shortcuts import render, redirect, get_object_or_404
from car.car import Car
from restaurant.models import Dish
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.conf import settings


@login_required()
def list(request):
    return render(request, "car/index.html")


@login_required()
def add_dish(request, dish_id):
    car = Car(request)
    dish = get_object_or_404(Dish, id=dish_id)
    car.add(dish=dish)
    return redirect("car")


def delete_dish(request, dish_id):
    car = Car(request)
    dish = Dish.objects.get(id=dish_id)
    car.delete(dish=dish)
    return redirect("car")


def substract_dish(request, dish_id):
    car = Car(request)
    dish = Dish.objects.get(id=dish_id)
    car.subtract_dish(dish=dish)
    return redirect("car")


def clear_car(request):
    car = Car(request)
    car.clean_car()
    return render(request, "car/form_email.html")


def Confirmarcorreo(request):
    return render(request, "car/correo.html")


def send_email(mail,name,lastname,address):
    context = {'mail': mail,'name':name,'lastname':lastname,'address':address}
    template = get_template(('car/informacion.html'))
    content = template.render(context)
    email = EmailMultiAlternatives(
        'Compra realizada con exito en WorldRestaurant',
        'WorldRestaurants',
        settings.EMAIL_HOST_USER,
        [mail],
    )
    email.attach_alternative(content, 'text/html')
    email.send()


def correo(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        send_email(mail,name,lastname,address)
        "return render(request, 'car/form_email.html')"
    return redirect("WorldRestaurant")


