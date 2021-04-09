from django.contrib import admin
from django.urls import path,include
from .  import views

urlpatterns = [
    path('',views.index,name='home'),
    path('contactus',views.contact,name='contact'),
    path('aboutus',views.about,name='about'),
]