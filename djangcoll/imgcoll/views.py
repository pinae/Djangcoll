import json
from base64 import b64encode
from os import urandom
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import CalibrationDataForm
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
User = get_user_model()


def usercheck(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest(_("ERROR: Request body was not valid JSON."))
        if 'email' not in data:
            return HttpResponseBadRequest(_("ERROR: You have to send a email address."))
        try:
            user = User.objects.get(email=data['email'])
            return HttpResponse(json.dumps({
                "user": user.username,
                "calibration_data": b64encode(urandom(1024)).decode("utf-8")
            }))
        except User.DoesNotExist:
            return HttpResponse(json.dumps({
                "user": None,
                "calibration_data": b64encode(urandom(1024)).decode("utf-8")
            }))
    return HttpResponseBadRequest(_("ERROR: Invalid request."))


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
            cal_obj = form.instance
            return render(request, 'imgcoll/upload_calibration.html', {'form': form, 'cal_obj': cal_obj})
    else:
        form = CalibrationDataForm()
    return render(request, 'imgcoll/upload_calibration.html', {'form': form})
