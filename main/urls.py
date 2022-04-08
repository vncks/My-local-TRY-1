from django.urls import path
from . import views


urlpatterns = [
    path('', views.page, name='home'),
    path('langs', views.python, name='langs'),
    path('add', views.add, name='add')
]