import django_filters
from cars.models import Car


class CarFilter(django_filters.FilterSet):
    mileage_min = django_filters.NumberFilter(field_name='mileage',
                                              lookup_expr='gte')
    mileage_max = django_filters.NumberFilter(field_name='mileage',
                                              lookup_expr='lte')
    price_min = django_filters.NumberFilter(field_name='price',
                                            lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price',
                                            lookup_expr='lte')

    class Meta:
        model = Car
        fields = {
            'brand': ['exact', 'icontains'],
            'model': ['exact', 'icontains'],
            'year': ['exact', 'gte', 'lte'],
            'fuel_type': ['exact'],
            'transmission_type': ['exact'],
        }
