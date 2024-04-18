import json
import os
import requests

from django.core.files import File
from django.core.management.base import BaseCommand
from django.conf import settings

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Импортировать данные о местах из JSON-файла в базу данных"

    def add_arguments(self, parser):
        parser.add_argument("json_file_path", type=str, help="Путь к JSON-файлу")

    def handle(self, *args, **kwargs):
        json_file_path = kwargs["json_file_path"]

        # Чтение данных из JSON-файла
        with open(json_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Создание объекта Place
        place = Place.objects.create(
            title=data["title"],
            description_short=data["description_short"],
            description_long=data["description_long"],
            lat=float(data["coordinates"]["lat"]),
            lng=float(data["coordinates"]["lng"]),
        )

        # Создание объектов PlaceImage и сохранение изображений
        for idx, img_url in enumerate(data["imgs"], start=1):
            # Создание объекта PlaceImage
            place_image = PlaceImage(place=place, image_number=idx)

            # Загрузка изображения из URL
            img_name = img_url.split("/")[-1]
            img_path = f"{settings.MEDIA_ROOT}/images/{img_name}"
            img_content = requests.get(img_url).content
            with open(img_path, "wb") as img_file:
                img_file.write(img_content)

            # Сохранение изображения в объекте PlaceImage
            place_image.image.save(img_name, File(open(img_path, "rb")))
            place_image.save()

            # Опционально: удаление временного файла изображения
            os.remove(img_path)

        self.stdout.write(
            self.style.SUCCESS("Данные успешно импортированы в базу данных")
        )
