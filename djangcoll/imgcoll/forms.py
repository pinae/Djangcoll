from django import forms
from .models import CalibrationData
from django.utils.translation import gettext as _


class CalibrationDataForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, label=_("email"),
                             help_text=_("Enter your email for updates."),
                             required=False)
    smartphone = forms.CharField(label=_("smartphone"),
                                 help_text=_("manufacturer and name of your cell phone"),
                                 required=False)
    food_name = forms.CharField(label=_("food_name"),
                                help_text=_("name of the food to analyze"),
                                required=True)
    comment = forms.CharField(label=_("comment"),
                              help_text=_("Let us know how to improve our service!"),
                              required=False)

    class Meta:
        model = CalibrationData
        fields = ('email', 'smartphone',
                  'calibration_image', 'potato_image', 'flour_image', 'milk_image',
                  'food_name', 'analyze_image',
                  'comment')
