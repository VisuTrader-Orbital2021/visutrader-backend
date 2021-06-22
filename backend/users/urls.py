from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('accounts/users/<int:pk>/', views.UserDetailsView.as_view(), name='user-detail')
]