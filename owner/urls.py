from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import Display, AddFormClass, DeleteItemClass, EditFormClass, DeleteView


urlpatterns = [
    path('', Display.homeDisplay, name="owner-home"),
    path('add-item', AddFormClass.get_name, name="add-item"),
    path('delete-item/<int:pk>/', DeleteView.as_view(), name='delete-item'),
    path('<int:item_id>/edit-item', EditFormClass.editHandler, name="edit-item"),
]

'''
# path('<int:pk>/delete-item', DeleteItemClass.deleteHandler, name="delete-item"),

'''