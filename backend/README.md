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
* cd devman
* echo SECRET_KEY=some_secret_key > backend/.env
* echo DEBUG=True >> backend/.env  (or False for production)
* python -m venv venv (or python3 -m venv venv)
* source venv/bin/activate (or venv\Scripts\activate for Windows)
* pip install -r backend/requirements.txt
* python manage.py migrate
* python manage.py runserver

### DEMO
* [Demo site](https://booltazavr.pythonanywhere.com)
* [Admin panel](https://booltazavr.pythonanywhere.com/admin) (login: root, password: pass)

### LOAD_PLACES script
* python manage.py load_places <json_file> - загрузка мест из json-файла в базу данных

* Пример json-файла:

```sh
{
    "title": "Экскурсионная компания «Легенды Москвы»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a55cbc706d764c1764dfccf832d50541.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/65153b5c595345713f812d1329457b54.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0a79676b3d5e3b394717b4bf2e610a57.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e27f507cb72e76b604adbe5e7b5f315.jpg"
    ],
    "description_short": "Неважно, живёте ли вы в Москве всю жизнь или впервые оказались в столице, составить ёмкий, познавательный и впечатляющий маршрут по городу — творческая и непростая задача. И её с удовольствием берёт на себя экскурсионная компания «Легенды Москвы»!",
    "description_long": "<p>Экскурсия от компании «Легенды Москвы» — простой, удобный и приятный способ познакомиться с городом или освежить свои чувства к нему. Что выберете вы — классическую или необычную экскурсию, пешую прогулку или путешествие по городу на автобусе? Любые варианты можно скомбинировать в уникальный маршрут и создать собственную индивидуальную экскурсионную программу.</p><p>Компания «Легенды Москвы» сотрудничает с аккредитованными экскурсоводами и тщательно следит за качеством экскурсий и сервиса. Автобусные экскурсии проводятся на комфортабельном современном транспорте. Для вашего удобства вы можете заранее забронировать конкретное место в автобусе — это делает посадку организованной и понятной.</p><p>По любым вопросам вы можете круглосуточно обратиться по телефонам горячей линии.</p><p>Подробности узнавайте <a class=\"external-link\" href=\"https://moscowlegends.ru \" target=\"_blank\">на сайте</a>. За обновлениями удобно следить <a class=\"external-link\" href=\"https://vk.com/legends_of_moscow \" target=\"_blank\">«ВКонтакте»</a>, <a class=\"external-link\" href=\"https://www.facebook.com/legendsofmoscow?ref=bookmarks \" target=\"_blank\">в Facebook</a>.</p>",
    "coordinates": {
        "lng": "37.64912239999976",
        "lat": "55.77754550000014"
    }
}
```