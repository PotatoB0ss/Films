from django.urls import path
from .views import *


urlpatterns = [
path('email_success/', email_success,
name='email_success'),
    path('', base, name='base'),
    path('genre/<slug:genr>/', genr, name='genrd'),
    path('film/<int:filmm>/', film_watch, name="film_watch"),
]

