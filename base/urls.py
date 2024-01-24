from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .forms import loginform
urlpatterns = [
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(authentication_form=loginform),name='login'),
    path('logout',views.Logout,name='logout'),
]