
from django.contrib import admin
from django.urls import path
from django.urls import path
from app01 import views
urlpatterns = [
    path('',views.my_view),

    path('view/',views.view),

    path('api/capture', views.capture_image, name='capture_image'),

]