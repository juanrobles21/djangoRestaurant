from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from restaurant.car import Carrito

def agregar_carrito(request,id):
    carrito=Carrito(request)


