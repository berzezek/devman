from django.urls import path
from afisha.views import index

urlpatterns = [
    path("", index),
]
