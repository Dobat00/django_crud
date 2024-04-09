from django.contrib import admin
from django.urls import path, include
from crud import views

urlpatterns = [
    path('clearall', views.clearall, name='clearall'),
    path('', views.index, name='index'),
    path('salvar', views.salvar, name='salvar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('editarPOST/<int:id>', views.editarPOST, name='editarPOST'),
    path('delete/<int:id>', views.delete, name='delete'),
]
