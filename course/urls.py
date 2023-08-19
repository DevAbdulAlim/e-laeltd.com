from django.urls import path 
from .views import index, detail, categories, about, services, contact, branches, AdmissionView

app_name = 'course'
urlpatterns = [
    path('', index),
    path('course/<int:pk>/', detail),
    path('course/categories/', categories),
]

urlpatterns += [
    path('about/', about),
    path('services/', services),
    path('contact/', contact),
    path('branches/', branches),
    path('admission/', AdmissionView.as_view(), name='admission'),
]