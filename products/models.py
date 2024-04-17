from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description =models.CharField(max_length=255, verbose_name='Описание')
    count = models.IntegerField(verbose_name='Количество')
    cost = models.FloatField(verbose_name='Цена', default=0.0)
