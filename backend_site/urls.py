"""
URL configuration for backend_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from accounts.views import verify_email, password_reset_confirm, ResendEmailVerificationView
# from accounts.views import GoogleLogin

from dj_rest_auth.registration.views import  VerifyEmailView  # config

# from dj_rest_auth.views import PasswordResetConfirmView # config

urlpatterns = [
    path("admin/", admin.site.urls),

# dj-rest-auth

    path('accounts/', include('dj_rest_auth.urls')),

# Registration

    path('accounts/registration/', include('dj_rest_auth.registration.urls')),

    path("accounts/registration/verify-email/", VerifyEmailView.as_view(), name="account_email_verification_sent"),

    path('accounts/registration/resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),

    path('accounts/registration/verify-email/<str:key>', verify_email, name="account_confirm_email"),


# Password

    path('accounts/password/reset/confirm/<uid>/<str:token>', password_reset_confirm, name="password_reset_confirm"),

    # path("accounts/password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

# Social Login

    # path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
]
