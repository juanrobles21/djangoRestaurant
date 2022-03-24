from decimal import Decimal
from django.conf import settings
from restaurant.models import Dish


class Carrito(object):
    # inicio el carro
    def __init__(self, request):
        carrito = self.session.get(settings.CAR_SESSION_ID)
        if not carrito:
            # guardar un carrito vacio en la sesion
            carrito = self.session[settings.CAR_SESSION_ID] = {}
        self.carrito = carrito

    #'add' y 'save':Añadir un producto al carrito o actualizar su cantidad
    def agregar(self,producto,candidad=1, override_cantidad=False):
        dish_id=str(Dish.id)
        if dish_id not in self.carrito:
            self.carrito[dish_id]={'cantidad':0,
                                   'precio':str(Dish.price)}
        if override_cantidad:
            self.carrito[dish_id]['cantidad']=candidad
        else:
            self.carrito[dish_id]['cantidad']+=candidad
        self.save()
    #marca la sesion como modificada para que Django la guarde
    def save(self):
        self.session.modified=True

    def remover(self,producto):
        dish_id=str(Dish.id)
        if dish_id in self.carrito:
            del self.carrito[dish_id]
            self.save()
    #Itera entre los elementod en 'carrito' y obtiene los productos
    #desde la base de datos

    def __iter__(self):
        ids_producto=self.carrito.keys()
        productos=Dish.objects.filter(id=ids_producto)
        carrito=self.carrito.copy()
        for producto in productos:
            carrito[str(Dish.id)]['producto']=producto
        for item in carrito.values():
            item['precio']=Decimal(item['precio'])
            item['precio_tota']= item['precio'] *item['cantidad']
            yield item
    #Cuenta los item en el carrito
    def __len__(self):
        return sum(item['cantidad'] for item in self.carrito.values())

    #trae el precio total
    def get_precio_total(self):
        return sum(Decimal(item['precio'])*item['cantidad']for item in self.carrito.values())
    #Eliminar el carrito de la sesion actual
    def clear(self):
        del self.session[settings.CAR_SESSION_ID]
        self.save()

def carrito(request):
    return {'carrito':Carrito(request)}



