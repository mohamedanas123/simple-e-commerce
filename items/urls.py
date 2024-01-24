from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.detail,name='detail'),
    path('newitem/',views.new,name='newitem'),
    path('browse/',views.items.as_view(),name='browse')
]
