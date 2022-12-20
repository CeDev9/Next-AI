from django.urls import path
from . import views

urlpatterns = [
    path('generate_audio_pitch_factors', views.getFactor,name='FactorAudio'),
]