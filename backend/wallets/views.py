from django.urls import reverse
from wallets.models import Wallet, Transaction
from wallets.serializers import WalletSerializer, WalletHistorySerializer, TransactionSerializer
from rest_framework import generics, status

# Create your views here.
class WalletList(generics.ListCreateAPIView):
    '''
    get:
    Get list of crated wallets.

    post:
    Create a new wallet.
    '''
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletDetail(generics.RetrieveUpdateAPIView):
    '''
    retrieve:
    Get details of a wallet.

    update:
    Update details of the wallet.
    '''
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletHistory(generics.ListCreateAPIView):
    '''
    get:
    Get a list of history transaction of the wallet.

    post:
    Create a new transaction for the wallet.
    '''
    def get_queryset(self):
        # TODO: Try to find a way to cache the wallet object
        return Transaction.objects.filter(from_wallet=Wallet.objects.get(pk=self.kwargs['pk']))
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TransactionSerializer
        return WalletHistorySerializer

    def post(self, request, pk, *args, **kwargs):
        request.data['from_wallet'] = reverse('wallet-detail', args=[pk])
        return self.create(request, *args, **kwargs)

class TransactionDetail(generics.RetrieveAPIView):
    '''
    retrieve:
    Get details of a transaction
    '''
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
