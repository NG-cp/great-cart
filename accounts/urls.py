from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('reset_password_validate/<uidb64>/<token>', views.reset_password_validate, name='reset_password_validate'),
]