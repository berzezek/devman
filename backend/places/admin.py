from adminsortable2.admin import SortableTabularInline, SortableAdminMixin
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from tinymce.widgets import TinyMCE

from places.models import Place, PlaceImage


class PlaceImageTabularInline(SortableTabularInline):
    model = PlaceImage
    extra = 1
    fields = (
        "image",
        "get_current_image",
    )
    readonly_fields = ("get_current_image",)

    def get_current_image(self, instance):
        if instance.image:
            return format_html(
                '<img src="{}" style="max-height: 200px" />', instance.image.url
            )
        return "-"

    get_current_image.short_description = "Get preview"


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ("title", "description_short", "description_long", "lat", "lng")
    inlines = [PlaceImageTabularInline]
    search_fields = ["title"]

    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)
