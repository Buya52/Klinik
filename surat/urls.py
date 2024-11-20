# surat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_surat, name='list_surat'),
    path('add/', views.add_surat, name='add_surat'),
    path('edit/<int:surat_id>/', views.edit_surat, name='edit_surat'),
    path('delete/<int:surat_id>/', views.delete_surat, name='delete_surat'),
    path('surat/<int:surat_id>/preview/', views.preview_file, name='preview_file'),
]
