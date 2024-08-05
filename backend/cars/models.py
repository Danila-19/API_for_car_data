from django.db import models


class Car(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Бензин'),
        ('diesel', 'Дизель'),
        ('electric', 'Электричество'),
        ('hybrid', 'Гибрид'),
    ]

    TRANSMISSION_CHOICES = [
        ('manual', 'Механическая'),
        ('automatic', 'Автоматическая'),
        ('cvt', 'Вариатор'),
        ('robot', 'Робот'),
    ]

    brand = models.CharField(max_length=100, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель')
    year = models.PositiveIntegerField(verbose_name='Год выпуска')
    fuel_type = models.CharField(max_length=10,
                                 choices=FUEL_CHOICES,
                                 verbose_name='Тип топлива')
    transmission_type = models.CharField(max_length=10,
                                         choices=TRANSMISSION_CHOICES,
                                         verbose_name='Тип КПП')
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Цена')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
