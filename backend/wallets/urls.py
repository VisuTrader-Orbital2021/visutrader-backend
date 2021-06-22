from django.urls import path
from wallets import views

urlpatterns = [
    path('wallets/', views.WalletList.as_view(), name='wallet-list'),
    path('wallets/<int:pk>/', views.WalletDetail.as_view(), name='wallet-detail'),
    path('wallets/<int:pk>/history/', views.WalletHistory.as_view(), name='wallet-history'),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transaction-detail'),
]