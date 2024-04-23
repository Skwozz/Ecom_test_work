from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, StockViewSet, EquipmentViewSet, CategoryViewSet
from . import crud_for_stock, crud_for_categories,crud_for_equiepment ,views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'equipments', EquipmentViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.ApiOverview, name='home'),
    path('stock/create/', crud_for_stock.stockCreate),
    path('stock/update/<str:pk>/', crud_for_stock.stockUpdate),
    path('stock/delete/<str:pk>/', crud_for_stock.stockDelete),
    path('stock/', crud_for_stock.stockList),
    path('category/create/', crud_for_categories.categoryCreate),
    path('category/update/<str:pk>/', crud_for_categories.categoryUpdate),
    path('category/delete/<str:pk>/', crud_for_categories.categoryDelete),
    path('category/', crud_for_categories.categoryList),
    path('equipment/create/', crud_for_equiepment.equipmentCreate),
    path('equipment/update/<str:pk>/', crud_for_equiepment.equipmentUpdate),
    path('equipment/delete/<str:pk>/', crud_for_equiepment.equipmentDelete),
    path('equipment/', crud_for_equiepment.equipmentList),
    # path('create_stock/', views.StockViewSet.as_view(), name='add-stock'),
    # path('update_stock/<int:id>/', views.StockViewSet.as_view(), name='update-stock'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]