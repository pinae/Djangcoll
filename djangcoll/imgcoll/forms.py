from django import forms
from .models import CalibrationData
from django.utils.translation import gettext as _


class CalibrationDataForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, label=_("email"),
                             help_text=_("Enter your email for updates."),
                             required=True)

    class Meta:
        model = CalibrationData
        fields = ('email', 'smartphone',
                  'calibration_image', 'potato_image', 'flour_image', 'milk_image',
                  'food_name', 'analyze_image',
                  'comment')
