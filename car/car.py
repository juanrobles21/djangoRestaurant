
class Car:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        car = self.session.get("car")
        if not car:
            car = self.session["car"] = {}
        # else:
        self.car = car

    def add(self, dish):
        if (str(dish.id) not in self.car.keys()):
            self.car[dish.id] = {
                "id": dish.id,
                "name": dish.name,
                "price": dish.price,
                "amount": 1,
                "total":dish.price,
            }
        else:
            for key, value in self.car.items():
                if key == str(dish.id):
                    value['amount'] = value['amount'] + 1
                    value['total']=(int(value["price"]) * value["amount"])
                    break
        self.save_car()

    def save_car(self):
        self.session["car"] = self.car
        self.session.modified = True

    def delete(self, dish):
        dish.id = str(dish.id)
        if dish.id in self.car:
            del self.car[dish.id]
            self.save_car()

    def subtract_dish(self, dish):
        for key, value in self.car.items():
            if key == str(dish.id):
                value['amount'] = value['amount'] - 1
                value['total'] = (int(value["price"]) * value["amount"])
                if value['amount'] < 1:
                    self.delete(dish)
                break
        self.save_car()

    def clean_car(self):
        self.session['car'] = {}
        self.session.modified = True
