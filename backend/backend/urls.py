"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from dj_rest_auth.registration.views import ConfirmEmailView, VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('users.urls')),
    path('', include('wallets.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('accounts/password/reset/confirm/<slug:uidb64>/<slug:token>/',
         PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'
    ),
]
