from django.db import models
from django.conf import settings


class CalibrationData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    smartphone = models.CharField(max_length=200)
    calibration_image = models.ImageField(upload_to='calibration_images')

    def __str__(self):
        return "<%s: %s>" % (self.user.username, self.smartphone)
