# Generated by Django 3.2.3 on 2021-06-02 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'restaurant_type',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('direction', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('restauran_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restauranttype')),
            ],
            options={
                'db_table': 'restaurant',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
            options={
                'db_table': 'dish',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.PositiveSmallIntegerField(choices=[(4, '4-Muy bueno'), (5, '5-Excelente'), (1, '1-Pésiomo'), (2, '2-Malo'), (3, '3-Regular')])),
                ('title_opinion', models.CharField(max_length=100)),
                ('opinion', models.CharField(max_length=1000)),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]