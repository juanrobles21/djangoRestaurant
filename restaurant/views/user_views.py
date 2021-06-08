from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from restaurant.forms import Registe_form
from django.contrib.auth import authenticate, login
def register(request):
    data={
        'form':Registe_form()
    }
    if request.method=='POST':
        formulario= Registe_form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])

            login(request, user)
            return redirect("WorldRestaurant")
            data
    return render(request,'users/register.html',data)


def loginView(request):
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(request, username=_username, password=_password)
        print(user)

        if user:
            login(request, user)
            return redirect("WorldRestaurant")
        else:
            return render(request, 'users/login.html', {'error': 'el usuario no se encuentra registrado'})

    return render(request, 'users/login.html')


@login_required
def logout_v(request):
    logout(request)
    return redirect("WorldRestaurant")
