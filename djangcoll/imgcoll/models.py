from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class CalibrationData(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    smartphone = models.CharField(
        max_length=512, verbose_name=_("smartphone"),
        help_text=_("manufacturer and name of your cell phone"))
    calibration_image = models.ImageField(
        upload_to='calibration_images',
        verbose_name=_("calibration image"),
        help_text=_("image of an empty plate for calibration"))
    potato_image = models.ImageField(
        upload_to='potato_images',
        help_text=_("image of a potato slice"))
    flour_image = models.ImageField(
        upload_to='flour_images',
        help_text=_("image of some flour"))
    milk_image = models.ImageField(
        upload_to='milk_images',
        help_text=_("image of some milk"))
    food_name = models.CharField(
        max_length=512,
        help_text=_("name of the food to analyze"))
    analyze_image = models.ImageField(
        upload_to='analyze_images',
        help_text=_("image to analyze"))
    comment = models.TextField(
        default="",
        verbose_name=_("comment"),
        help_text=_("Let us know how to improve our service!"))

    def __str__(self):
        return "<%s: %s>" % (self.user.username, self.smartphone)
