from cars.models import Car
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from api.filters import CarFilter
from api.pagination import CarPagination
from api.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
    pagination_class = CarPagination
    permission_classes = [IsAuthenticated]
