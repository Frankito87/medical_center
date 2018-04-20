"""medical_center URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mc import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('create_appointment', views.create_appointment, name='create_appointment'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='logout'),
    path('register', views.register, name='register'),
    path('create_patient', views.create_patient, name='create_patient'),
    path('create_treatment', views.create_treatment, name='create_treatment'),
    path('appointment_list', views.appointment_list, name='appointment_list'),
    path('patient_list', views.patient_list, name='patient_list'),    
    path('treatment_list', views.treatment_list, name='treatment_list'),
    path('<str:pk>', views.patient_information, name='patient_information'),
    path('<str:pk>/update_patient', views.update_patient, name='update_patient'),
    path('<str:pk>/delete_patient', views.delete_patient, name='delete_patient'),
    path('<str:pk>/appointment_information', views.appointment_information, name='appointment_information'),
    path('<str:pk>/treatment_information', views.treatment_information, name='treatment_information'),
    path('<str:pk>/update_appointment', views.update_appointment, name='update_appointment'),
    path('<str:pk>/delete_appointment', views.delete_appointment, name='delete_appointment'),
    path('<str:pk>/delete_treatment', views.delete_treatment, name='delete_treatment'),
]
