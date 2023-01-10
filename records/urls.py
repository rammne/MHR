from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('patient-form/', views.patient_form, name='patient_form'),
    path('patients-list/', views.patients_list, name='patients_list'),
    path('patient-details/<int:pk>', views.patient_details, name='patient_details'),
    path ('update/<int:pk>', views.update_patient_details, name='update_detail'),
    path('delete/<int:pk>', views.delete_patient, name='delete_patient'),
    path('', views.home_page, name='home')
]
