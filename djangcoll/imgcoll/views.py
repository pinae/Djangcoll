import json
from base64 import b64encode
from os import urandom
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import CalibrationDataForm
from .models import CalibrationData
import numpy as np
from skimage.io import imread
from skimage.util import img_as_float
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
            return render(request, 'imgcoll/upload_calibration.html', {
                'form': form,
                'cal_obj': cal_obj,
                'email': user.email
            })
    else:
        form = CalibrationDataForm()
    return render(request, 'imgcoll/upload_calibration.html', {
        'form': form
    })


def impressum(request):
    return render(request, 'imgcoll/impressum.html')


def get_results(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest(_("ERROR: Request body was not valid JSON."))
        if 'id' not in data:
            return HttpResponseBadRequest(_("ERROR: You have to send a processing ID."))
        cd = CalibrationData.objects.get(pk=data['id'])
        img = imread(cd.analyze_image.path)
        np_img = img_as_float(img)
        square_size = (min(np_img.shape[0], np_img.shape[0]) // 10) * 2
        middle_square = np_img[
            np_img.shape[0]//2-square_size//2:np_img.shape[0]//2+square_size//2,
            np_img.shape[1]//2-square_size//2:np_img.shape[1]//2+square_size//2, :]
        hist_data = {"full": {}, "middle": {}, "quotient": {}}
        flat_data = np.array([], dtype=np.float32)
        for ch_no, ch_name in enumerate(('red', 'green', 'blue')):
            fh = (np.histogram(np_img[:, :, ch_no], bins=16, range=(0, 1))[0]
                  / (np_img.shape[0] * np_img.shape[1]))
            flat_data = np.append(flat_data, fh)
            hist_data["full"][ch_name] = [x for x in fh]
            mh = (np.histogram(middle_square[:, :, ch_no], bins=16, range=(0, 1))[0]
                  / (middle_square.shape[0] * middle_square.shape[1]))
            flat_data = np.append(flat_data, mh)
            hist_data["middle"][ch_name] = [x for x in mh]
            hist_data["quotient"][ch_name] = [hist_data["middle"][ch_name][i] / hist_data["full"][ch_name][i]
                                              for i in range(len(hist_data["full"][ch_name]))]
            flat_data = np.append(flat_data, np.array(hist_data["quotient"][ch_name], dtype=np.float32))
        yellowness_of_the_center = np.average(hist_data["middle"]["red"][8:]) + np.average(hist_data["middle"]["green"][8:]) / (
                2 * np.average(hist_data["middle"]["blue"][8:]))
        return HttpResponse(json.dumps({
            "histogram": hist_data,
            "amylum": np.random.normal(yellowness_of_the_center * 0.75, 5.0),
            "lactose": (abs(np.random.normal(0.5, 1.5))
                        if np.random.random() > 0.1 else
                        abs(min(np.random.normal(5.0, 2.0), 1.0))),
            "insect_protein": (abs(np.random.normal(0.0, 0.2))
                               if np.random.random() > 0.01 else
                               abs(min(np.random.normal(90.0, 5.0), 1.0))),
            "raw_results": b64encode(urandom(4096)).decode("utf-8")
        }))
    return HttpResponseBadRequest(_("ERROR: Invalid request."))
