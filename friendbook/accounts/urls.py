from django.urls import path
from . import views
urlpatterns = [

    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('userprofile/', views.user_profile, name='userprofile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('user_changepassword/', views.user_changepassword, name='user_changepassword'),
    path('user_resetpassword/', views.user_resetpassword, name='user_resetpassword'),
    path('user_logout/', views.user_logout, name='user_logout'),


]