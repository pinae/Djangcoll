from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from os.path import join
from uuid import uuid4


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return join(path, filename)
    return wrapper


class CalibrationData(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    smartphone = models.CharField(
        max_length=512, verbose_name=_("smartphone"),
        help_text=_("Manufacturer and name of your cell phone"))
    calibration_image = models.ImageField(
        upload_to=path_and_rename('calibration_images'),
        verbose_name=_("calibration image"),
        help_text=_("Image of an empty plate for calibration"))
    potato_image = models.ImageField(
        upload_to=path_and_rename('potato_images'),
        help_text=_("Image of a potato slice"))
    flour_image = models.ImageField(
        upload_to=path_and_rename('flour_images'),
        help_text=_("Image of some flour"))
    milk_image = models.ImageField(
        upload_to=path_and_rename('milk_images'),
        help_text=_("Image of some milk"))
    food_name = models.CharField(
        max_length=512,
        help_text=_("Name of the food to analyze"))
    analyze_image = models.ImageField(
        upload_to=path_and_rename('analyze_images'),
        help_text=_("Food image to analyze"))
    comment = models.TextField(
        default="",
        verbose_name=_("comment"),
        help_text=_("Let us know how to improve our service! (Optional)"))

    def __str__(self):
        return "<%s: %s>" % (self.user.username, self.smartphone)
