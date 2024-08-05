from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from api.views import CarViewSet

router = routers.DefaultRouter()
router.register('cars', CarViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Car API',
        default_version='v1',
        description='API для управления автомобилями',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='contact@carapi.local'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
)

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
