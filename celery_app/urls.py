from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.testing,name='testing'),
    path('transcription-api/', views.upload_and_transcribe, name='upload_and_transcribe'),
    path("transcription-result/<str:task_id>/", views.transcription_result),

]
