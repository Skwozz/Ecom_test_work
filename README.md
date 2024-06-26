Т.З
Тестовое задание Back-end developer:
Необходимо реализовать Django приложение для учета
оборудование на складах.
Должны быть реализованный минимум 3 сущности:
- Stock (Для записи информации о складах для хранения)
- Category(Для хранения информации о категориях
оборудования)
- Equipment (Для хранения информации о единицах
оборудования)
Требования:
- Для каждой из модели должны быть реализованы CRUD
операции и подготовлены API эндпоинты для них.
Список операций:
1. Создание записей.
2. Получение конкретной записи.
3. Получение списка всех записей.
4. Удаление записи.
5. Изменение записи.
- Должны быть реализованы сериализаторы для каждой
модели.
- Данные должны храниться в любой базе данных по Вашему
усмотрению
- API должно быть реализовано с помощью Django REST
Framework
- Взаимосвязь между моделями должна быть выстроена
следующим образом:
1. Модель Equipment должна иметь связь по ключу с
моделями Category и Stock
(При реализации модели User, с ней также должна быть
настроена связь)
Будет существенным плюсом:
- Добавить сущность User (Для хранения информации о
пользователях (можно использовать дефолтную))
- Настроить permission для пользователей:
1. Администратор имеет доступ ко всем CRUD операциям
2. Авторизованный пользователь имеет доступ только к
чтению данных
- Реализовать логику авторизации и аутентификации с
использованием любой из библиотек
- Подключить базу данных PostgreSQL
- Докеризировать проект, чтобы он запускался через docker
compose up
- Настроить поиск и фильтры в панеле администратора django
- Написать документацию с использованием библиотеки drf-yasg
- Соблюдение PEP8
