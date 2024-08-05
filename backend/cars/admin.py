from django.contrib import admin
from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand',
                    'model',
                    'year',
                    'fuel_type',
                    'transmission_type',
                    'mileage',
                    'price')
    list_filter = ('brand', 'fuel_type', 'transmission_type', 'year')
    search_fields = ('brand', 'model')
