from django.urls import path
from . import views

urlpatterns = [
    path('', views.atm_list, name='atm_list'),
    path('atm/<int:atm_id>/', views.atm_detail, name='atm_detail'),
]
