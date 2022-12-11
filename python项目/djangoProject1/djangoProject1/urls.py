
from django.contrib import admin
from django.urls import path
from django.urls import path
from app01 import views
urlpatterns = [
    path('home/',views.home),

    path('add/',views.add),

    path('delete/', views.delete),

    path('update/', views.update),

    path('sort/', views.sort),

    path('login/', views.Login),

    path('Inquire/', views.Inquire),

    path('updatePassword/',views.updatePassword),

    path('enroll/',views.enroll)

]