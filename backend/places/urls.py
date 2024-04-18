from django.urls import path

from places.views import index, place_detail_serializer

urlpatterns = [
    path("", index),
    path("places/<int:place_id>/", place_detail_serializer, name="place_detail"),
]
