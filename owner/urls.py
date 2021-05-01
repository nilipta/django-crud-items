from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import Display, AddFormClass


urlpatterns = [
    path('', Display.homeDisplay),
    path('add-item', AddFormClass.get_name),
]