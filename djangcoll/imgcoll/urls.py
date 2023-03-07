from django.urls import path

from . import views

urlpatterns = [
    path('calibration/init', views.usercheck, name='usercheck'),
    path('', views.calibration_data_upload, name='upload'),
]