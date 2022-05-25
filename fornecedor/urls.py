from django.conf import settings
from django.urls import path

from app.settings import STATIC_ROOT
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('logged/', views.logged, name='logged')
]