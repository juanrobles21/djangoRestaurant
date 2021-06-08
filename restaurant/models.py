from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class RestaurantType(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'restaurant_type'


class Restaurant(models.Model):
    restauran_type_id = models.ForeignKey(RestaurantType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    direction = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'restaurant'


QUALIFICATION_CHOICES = {
    (1, '1-Pésiomo'),
    (2, '2-Malo'),
    (3, '3-Regular'),
    (4, '4-Muy bueno'),
    (5, '5-Excelente'),
}


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    qualification = models.PositiveSmallIntegerField(choices=QUALIFICATION_CHOICES)
    title_opinion = models.CharField(max_length=100)
    opinion = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'comment'


class Dish(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dish'


'''
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return {self.user.username}

    class Meta:
        db_table = 'client'


class Order(models.Model):
    date = models.DateField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def order_id(self):
        return "Order" + str(self.id)

    def get_cost_total(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        db_table = 'order'


class Detail_order(models.Model):
    order_id = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, related_name='item_order', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.amount
'''
