from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Driver(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='first name')
    last_name = models.CharField(max_length=50, verbose_name='first name')
    created_at = models.DateField(verbose_name='Date create', auto_now_add=True)
    update_at = models.DateField(verbose_name='Date update', auto_now=True)

    def __str__(self):
        return self.first_name


class Vehicle(models.Model):
    driver_id = models.ForeignKey('Driver', on_delete=models.SET_NULL, blank=True, null=True)
    make = models.CharField(max_length=50, verbose_name='make')
    model = models.CharField(max_length=50, verbose_name='model')
    plate_number = models.CharField(max_length=50, verbose_name='plate_number', unique=True,
                                    validators=[RegexValidator(regex=r"^[A-Z]{2} \d{4} [A-Z]{2}$")])
    created_at = models.DateField(verbose_name='Date create', auto_now_add=True)
    update_at = models.DateField(verbose_name='Date update', auto_now=True)

