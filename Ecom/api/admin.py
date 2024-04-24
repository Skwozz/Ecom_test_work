from django.contrib import admin

from .models import User, Stock, Category, Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    """Класс для поиска и фильтрации оборудования в панели администратора"""

    list_display = ("name", "category", "stock", "username",) # Показываемые данные
    list_filter = ("name", "category", "stock", "username",) # Фильтрация данных
    search_fields = ("name__startswith",) # Реализация поиска

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    """Класс для поиска и фильтрации складов в панели администратора"""
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name__startswith",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для поиска и фильтрации категорий в панели администратора"""
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name__startswith",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для поиска и фильтрации пользователей в панели администратора"""
    list_display = ("username", "email", "is_superuser",)
    list_filter = ("email",)
    search_fields = ("username__startswith",)





















