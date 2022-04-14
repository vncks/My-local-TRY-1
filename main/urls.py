from django.urls import path
from . import views


urlpatterns = [
    path('', views.page, name='home'),
    path('notes', views.python, name='notes'),
    path('add', views.add, name='add')
]