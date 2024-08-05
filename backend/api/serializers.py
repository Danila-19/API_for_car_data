from cars.models import Car
from django.contrib.auth import get_user_model
from rest_framework import serializers

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
