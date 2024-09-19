from .views import formAPI
from django.urls import path

urlpatterns = [
    path('', formAPI, name='formAPI'),
]
