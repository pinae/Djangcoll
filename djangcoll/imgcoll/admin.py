from django.contrib import admin
from .models import CalibrationData
from django.utils.html import mark_safe


class CalibrationDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'smartphone', 'food_name', 'analyze_image', 'comment')
    readonly_fields = ('calibration_image_preview', 'potato_image_preview', 'flour_image_preview',
                       'milk_image_preview', 'analyze_image_preview')

    def calibration_image_preview(self, obj):
        return mark_safe('<img src="{}" height="300" />'.format(obj.calibration_image.url))

    calibration_image_preview.short_description = 'Calibration'
    calibration_image_preview.allow_tags = True

    def potato_image_preview(self, obj):
        return mark_safe('<img src="{}" height="300" />'.format(obj.potato_image.url))

    potato_image_preview.short_description = 'Potato'
    potato_image_preview.allow_tags = True

    def flour_image_preview(self, obj):
        return mark_safe('<img src="{}" height="300" />'.format(obj.flour_image.url))

    flour_image_preview.short_description = 'Flour'
    flour_image_preview.allow_tags = True

    def milk_image_preview(self, obj):
        return mark_safe('<img src="{}" height="300" />'.format(obj.milk_image.url))

    milk_image_preview.short_description = 'Milk'
    milk_image_preview.allow_tags = True

    def analyze_image_preview(self, obj):
        return mark_safe('<img src="{}" height="300" />'.format(obj.analyze_image.url))

    analyze_image_preview.short_description = 'Analyze'
    analyze_image_preview.allow_tags = True


admin.site.register(CalibrationData, CalibrationDataAdmin)
