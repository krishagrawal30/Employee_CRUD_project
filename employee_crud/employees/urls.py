from django.urls import path
from . import views
urlpatterns = [
    path('', views.emp_list, name = 'emp_list'),
    path('add/', views.add_emp, name = 'add_emp'),
    path('delete/<int:id>/', views.delete_emp, name = 'delete_emp' ),
    path('edit/<int:id>/', views.edit_emp, name = 'edit_emp'),
]