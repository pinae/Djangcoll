# Generated by Django 4.1.7 on 2023-03-06 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CalibrationData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "smartphone",
                    models.CharField(
                        help_text="Hersteller und Modellbezeichnung des Smartphones",
                        max_length=512,
                        verbose_name="Smartphone",
                    ),
                ),
                (
                    "calibration_image",
                    models.ImageField(
                        help_text="Kalibrierungsbild von einem leeren Teller",
                        upload_to="calibration_images",
                        verbose_name="Kalibrierungsbild",
                    ),
                ),
                (
                    "potato_image",
                    models.ImageField(
                        help_text="Foto einer Kartoffelscheibe",
                        upload_to="potato_images",
                    ),
                ),
                (
                    "flour_image",
                    models.ImageField(
                        help_text="Foto von etwas Mehl", upload_to="flour_images"
                    ),
                ),
                (
                    "milk_image",
                    models.ImageField(
                        help_text="Foto einer Milchpfütze", upload_to="milk_images"
                    ),
                ),
                (
                    "food_name",
                    models.CharField(
                        help_text="Bezeichnung des zu analysierenden Nahrungsmittels",
                        max_length=512,
                    ),
                ),
                (
                    "analyze_image",
                    models.ImageField(
                        help_text="Bild des zu analysierenden Nahrungsmittels",
                        upload_to="analyze_images",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        default="",
                        help_text="Wie können wir die Software verbessern?",
                        verbose_name="Kommentar",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
