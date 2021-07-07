from django.contrib import admin
from django.urls import path
from .views import user_form
urlpatterns = [
        path('', user_form , name= 'user-form'),
]