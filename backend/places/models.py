from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255)
    description_short = models.CharField(
        verbose_name="Описание короткое", max_length=255
    )
    description_long = models.TextField(verbose_name="Описание длинное")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["pk"]
        verbose_name = "Место"
        verbose_name_plural = "Места"


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Картинка", upload_to="images/")
    image_number = models.PositiveSmallIntegerField(
        verbose_name="Позиция", blank=True, null=True, default=0
    )

    def __str__(self):
        return f"{self.image_number} {self.place.title}"

    class Meta:
        ordering = ["image_number"]
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
