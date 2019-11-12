from django.urls import path
from hello_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello_app/<name>",views.hello_there,name="hello_there"),
    path("hello_app/about/", views.about, name="about"),
    path("hello_app/contact/", views.contact, name="contact"),
]