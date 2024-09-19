from .views import formAPI, about
from django.urls import path

urlpatterns = [
    path('', formAPI, name='formAPI'),
    path('about/', about, name='about'),
]
