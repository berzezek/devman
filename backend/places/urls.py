from django.urls import path
from places.views import index

urlpatterns = [
    path("", index),
]
