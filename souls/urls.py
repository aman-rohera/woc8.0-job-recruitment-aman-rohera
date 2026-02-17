from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # --- CORE ---
    path('', views.graveyard_welcome, name='home'),
    path('signup/', views.register, name='signup'),
    path('ajax/validate_user/', views.check_username_email, name='validate_user'),
    
    # --- AUTHENTICATION ---
    # 1. Login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # 2. Logout (This is the one missing!)
    # We use 'next_page' to redirect them to login screen after leaving
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # --- PROFILE COMPLETION (Google Sign-In) ---
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    
    # --- PROFILE DASHBOARD ---
    path('crypt/', views.soul_dashboard, name='dashboard'),
    path('crypt/edit/', views.soul_edit, name='soul_edit'),
    path('banish/', views.banish_soul_to_void, name='banish_soul'),
    path('crypt/delete-resume/', views.delete_resume, name='delete_resume'),

    # --- PASSWORD RESET FLOW (Gmail/Brevo) ---
    path('password-reset/', auth_views.PasswordResetView.as_view(
          template_name='registration/password_reset.html',email_template_name='registration/password_reset_email.html'), name='password_reset'),

    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
         name='password_reset_confirm'),

    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)