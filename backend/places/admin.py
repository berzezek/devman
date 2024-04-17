from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableTabularInline, SortableAdminMixin


class PlaceImageTabularInline(SortableTabularInline):
    model = PlaceImage
    extra = 1
    fields = (
        "image",
        "current_image",
    )
    readonly_fields = ("current_image",)
    def current_image(self, instance):
        if instance.image:
            return mark_safe(
                '<img src="{}" style="max-height: 200px" />'.format(instance.image.url)
            )
        return "-"
    current_image.short_description = "Get preview"


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ("title", "description_short", "description_long", "latitude", "longitude")
    inlines = [PlaceImageTabularInline]
