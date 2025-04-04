from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('student', views.student, name= 'student'),
    path('faculty', views.faculty, name = 'faculty'),
    path('guest', views.guest, name= 'guest'),
]