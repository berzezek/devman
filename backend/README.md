## Документация к проекту Places
### Описание проекта
* Этот проект представляет собой веб-приложение, разработанное на базе Django, для управления информацией о местах (например, достопримечательностях, ресторанах и т. д.) и их изображениях.

### Модели данных
#### Модель Place представляет отдельное место и содержит следующие поля:

* title (CharField): Наименование места.
* description_short (CharField): Короткое описание места.
* description_long (TextField): Длинное описание места.
* latitude (FloatField): Широта места.
* longitude (FloatField): Долгота места.

#### Модель PlaceImage представляет изображение, связанное с определенным местом, и содержит следующие поля:

* place (ForeignKey): Связь с моделью Place.
* image (ImageField): Картинка места.
* image_number (PositiveSmallIntegerField): Позиция изображения в списке.

### Маршрутизаторы

* /admin/ - административная панель Django.
* /places/ - список всех мест.
* /places/<int:place_id>/ - информация о конкретном месте.

### Административная панель
#### Административная панель позволяет администраторам управлять местами и их изображениями. В административной панели реализовано следующее:

* Добавление, редактирование и удаление мест.
    
    поле `description_long` реализовано с помощью виджета `Textarea` + `tynymce` для удобного ввода текста.
* Добавление, редактирование и удаление изображений мест.

    поля `image_number` (позиция изображения в списке) и `image` (картинка места) реализованы с помощью `django-admin-sortable2` для удобной сортировки изображений.

### Deployment

* git clone <repository>
* echo SECRET_KEY=some_secret_key > .env
* echo DEBUG=True >> .env  (or False for production)
* python manage.py migrate
* python manage.py runserver

### DEMO
* [Demo site](https://booltazavr.pythonanywhere.com)