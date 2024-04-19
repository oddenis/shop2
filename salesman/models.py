from django.db import models

# Create your models here.

class Dolgnost(models.Model):
    dolgnost = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return self.dolgnost

class Salesman(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', null=True)
    familia = models.CharField(max_length=100, verbose_name='Фамилия')
    tel = models.CharField(max_length=11, verbose_name='Телефон')
    email = models.CharField(max_length=100, verbose_name='Емеил')
    date_to_work = models.DateField(verbose_name='Дата приема на работу')
    job_title = models.ForeignKey(Dolgnost, on_delete=models.CASCADE, verbose_name='Должность')

    def __str__(self):
        return self.familia