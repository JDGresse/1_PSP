from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('individuals/', views.individuals, name='individuals'),
    path('couples/', views.couples, name='couples'),
    path('what-to-expect/', views.what_to_expect, name='what-to-expect'),
    path('contact-helderberg-theraphy/', views.contact, name='contact'),
]