from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('test', views.fileUpload, name='test')
]