from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.safestring import mark_safe


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = (
        "image",
        "current_image",
        "image_number",
    )
    readonly_fields = ("current_image",)

    def current_image(self, instance):
        if instance.image:
            return mark_safe(
                '<img src="{}" style="max-height: 200px" />'.format(instance.image.url)
            )
        return "-"

    current_image.short_description = "Get preview"


class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title", "latitude", "longitude")
    inlines = [PlaceImageInline]


admin.site.register(Place, PlaceAdmin)
