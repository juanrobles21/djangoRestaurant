
from .car import Car
def impot_total_car(request):
    car=Car(request)
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["car"].items():
            total = total + (int(value["price"]) * value["amount"])
    return {"importe_total_car":total}
