from django import forms
from .models import CalibrationData
from django.utils.translation import gettext as _


class CalibrationDataForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=200,
        label=_("email"),
        help_text=_("Enter your email for updates. (Optional)"),
        required=False)
    smartphone = forms.CharField(
        label=_("smartphone"),
        help_text=_("Manufacturer and name of your cell phone. (Optional)"),
        required=False)
    calibration_image = forms.ImageField(
        label=_("calibration image"),
        help_text=_("Image of an empty plate for calibration"),
        required=True)
    potato_image = forms.ImageField(
        label=_("potato image"),
        help_text=_("Image of a potato slice"),
        required=True)
    flour_image = forms.ImageField(
        label=_("flour image"),
        help_text=_("Image of some flour"),
        required=True)
    milk_image = forms.ImageField(
        label=_("milk image"),
        help_text=_("Image of some milk"),
        required=True)
    food_name = forms.CharField(
        label=_("food name"),
        help_text=_("Name of the food to analyze"),
        required=True)
    analyze_image = forms.ImageField(
        label=_("food image"),
        help_text=_("Food image to analyze"),
        required=True)
    comment = forms.CharField(
        label=_("comment"),
        help_text=_("Let us know how to improve our service! (Optional)"),
        required=False)

    class Meta:
        model = CalibrationData
        fields = ('email', 'smartphone',
                  'calibration_image', 'potato_image', 'flour_image', 'milk_image',
                  'food_name', 'analyze_image',
                  'comment')
