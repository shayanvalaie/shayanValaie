from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('contact/thankyou', views.thankyou, name="thankyou"),
    path('press/', views.press, name="press"),
    path('send_form/', views.send_form, name="send_form"),


]
