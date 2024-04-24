from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, StockViewSet, EquipmentViewSet, CategoryViewSet
from . import crud_for_stock, crud_for_categories,crud_for_equiepment, crud_for_user, views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'equipments', EquipmentViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),#работа с api через встроенный функционал rest-framework Api Root

    path('', views.ApiOverview, name='home'),#

    # endpoint для CRUD operations с сущностью user
    path('user/create/', crud_for_user.userCreate),
    path('user/update/<str:pk>/', crud_for_user.userUpdate),
    path('delete/user/<str:pk>/', crud_for_user.userDelete),
    path('user/', crud_for_user.userList),

    # endpoint для CRUD operations с сущностью stock
    path('stock/create/', crud_for_stock.stockCreate),
    path('stock/update/<str:pk>/', crud_for_stock.stockUpdate),
    path('delete/stock/<str:pk>/', crud_for_stock.stockDelete),
    path('stock/', crud_for_stock.stockList),

    # endpoint для CRUD operations с сущностью category
    path('category/create/', crud_for_categories.categoryCreate),
    path('category/update/<str:pk>/', crud_for_categories.categoryUpdate),
    path('delete/category/<str:pk>/', crud_for_categories.categoryDelete),
    path('category/', crud_for_categories.categoryList),

    # endpoint для CRUD operations с сущностью equipment
    path('equipment/create/', crud_for_equiepment.equipmentCreate),
    path('equipment/update/<str:pk>/', crud_for_equiepment.equipmentUpdate),
    path('delete/equipment/<str:pk>/', crud_for_equiepment.equipmentDelete),
    path('equipment/', crud_for_equiepment.equipmentList),

    # аутентификация пользователя
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]