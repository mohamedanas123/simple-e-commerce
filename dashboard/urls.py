from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>/',views.edit,name='edit'),
]
