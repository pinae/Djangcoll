from django import forms
from .models import CalibrationData


class CalibrationDataForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, label="email", required=True)

    class Meta:
        model = CalibrationData
        fields = ('email', 'smartphone', 'calibration_image')
