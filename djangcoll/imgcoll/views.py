from django.shortcuts import render
from django.http import HttpResponse
from .forms import CalibrationDataForm
from django.contrib.auth import get_user_model
User = get_user_model()
#from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hello, world. You're at the imgcoll index.")


def calibration_data_upload(request):
    if request.method == 'POST':

        form = CalibrationDataForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.data.get('email'))
            except User.DoesNotExist:
                user = User(username=form.data.get('email'), email=form.data.get('email'))
                print("Creating new user:", user)
                user.save()
            cal_data = form.save(commit=False)
            cal_data.user = user
            cal_data.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'imgcoll/upload_calibration.html', {'form': form, 'img_obj': img_obj})
    else:
        form = CalibrationDataForm()
    return render(request, 'imgcoll/upload_calibration.html', {'form': form})
