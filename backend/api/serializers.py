from cars.models import Car
from django.contrib.auth import get_user_model
from rest_framework import serializers
from datetime import datetime

User = get_user_model()


class CarSerializer(serializers.ModelSerializer):

    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Car
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Цена должна быть положительным числом.')
        return value

    def validate_mileage(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'Пробег не может быть отрицательным.')
        return value

    def validate_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                'Год выпуска не может быть больше текущего года.')
        return value
