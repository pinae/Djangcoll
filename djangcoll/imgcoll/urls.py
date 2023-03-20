from django.urls import path

from . import views

urlpatterns = [
    path('calibration/init', views.usercheck, name='usercheck'),
    path('processing/ai/results', views.get_results, name='results'),
    path('impressum', views.impressum, name='impressum'),
    path('', views.calibration_data_upload, name='upload'),
]
