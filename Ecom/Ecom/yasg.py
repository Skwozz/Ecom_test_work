from rest_framework import permissions
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


"""Документация с использованием библиотеки drf-yasg"""

schema_view = get_schema_view(
    openapi.Info(

        title="Django API for warhouse",
        default_version='v1',
        description="Test description",
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swager(?P<format>\.json|\.yaml)',schema_view.with_ui(cache_timeout=0),name='shema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]