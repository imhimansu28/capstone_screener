from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_company_details, name='index'),
]
