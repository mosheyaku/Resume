from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('download/<path:file_path>/', views.download_resume, name='download_resume'),

]