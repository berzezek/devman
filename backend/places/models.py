from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    image_number = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f"{self.image_number} {self.place.title}"
