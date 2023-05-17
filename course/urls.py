from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index),
    path('course/<int:pk>/', views.detail),
    path('course/search/', views.search),
]

urlpatterns += [
    path('about/', views.about),
    path('services/', views.services),
    path('contact/', views.contact),
    path('branches/', views.branches),
    path('admission/', views.admission),
]