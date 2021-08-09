from django.urls import path
from . import views

urlpatterns = [
  path('ch', views.index)
]
