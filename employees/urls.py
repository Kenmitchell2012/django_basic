from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
]