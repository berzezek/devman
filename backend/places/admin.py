from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.safestring import mark_safe
from django.utils.html import format_html


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1  # Количество пустых форм для добавления новых изображений
    fields = ("image", "image_number")  # Укажите поля, которые вы хотите отображать
    readonly_fields = (
        "current_image",
    )  # Если вы хотите показать текущее изображение, добавьте это в readonly_fields

    def current_image(self, instance):
        # Возвращает HTML для отображения текущего изображения; требуется, если вы добавили его в readonly_fields
        if instance.image:
            return mark_safe(
                '<img src="{}" width="150" height="150" />'.format(instance.image.url)
            )
        return "-"

    current_image.short_description = "Currently"  # Название колонки


class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title", "latitude", "longitude")  # Какие поля отображать в списке
    inlines = [PlaceImageInline]  # Добавляем inline для PlaceImage


admin.site.register(Place, PlaceAdmin)
