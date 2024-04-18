from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255)
    description_short = models.CharField(
        verbose_name="Описание короткое", max_length=255, blank=True, null=True
    )
    description_long = models.TextField(verbose_name="Описание длинное", blank=True, null=True)
    latitude = models.FloatField(verbose_name="Широта", default=0.0)
    longitude = models.FloatField(verbose_name="Долгота", default=0.0)

    class Meta:
        ordering = ["pk"]
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место", related_name="images")
    image = models.ImageField(verbose_name="Картинка", upload_to="images/")
    image_number = models.PositiveSmallIntegerField(
        verbose_name="Позиция", blank=True, null=True, default=0
    )

    class Meta:
        ordering = ["image_number"]
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"{self.image_number} {self.place.title}"
