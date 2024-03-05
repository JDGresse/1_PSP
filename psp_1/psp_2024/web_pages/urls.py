from django.urls import path
from . import views
from .views import SuccessView, ContactView

app_name = 'web_pages'

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("psychotherapy/", views.psychotherapy, name="psychotherapy"),
    path("adhd-support/", views.adhd, name="adhd"),
    path("what-to-expect/", views.what_to_expect, name="what-to-expect"),
    path("contact-psp/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
]
