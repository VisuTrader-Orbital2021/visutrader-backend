from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.serializers import UserSerializer
from wallets.models import Wallet, Transaction, Position


class WalletSerializer(serializers.HyperlinkedModelSerializer):    
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='users:user-detail', read_only=True)
    history = serializers.HyperlinkedRelatedField(many=True, view_name='transaction-detail', read_only=True)

    class Meta:
        model = Wallet
        fields = ['id', 'owner', 'balance', 'history']

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount', 'quantity', 'market', 'from_wallet', 'created_at']
    
    def validate(self, data):
        if data['transaction_type'] == 'buy':
            if data['from_wallet'].balance - data['amount'] < 0:
                raise serializers.ValidationError('Wallet cannot have negative balance after transaction.')
        
        if data['transaction_type'] == 'sell':
            position_data = data['from_wallet'].owner.position.data
            position_quantity = position_data.get(data['market'], 0)

            if position_quantity < data['quantity']:
                raise serializers.ValidationError('You cannot sell stock(s) more than what you have.')

        return data

class WalletHistorySerializer(TransactionSerializer):
    class Meta:
        model = Transaction
        fields = ['url', 'amount', 'market', 'created_at']

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='users:user-detail', read_only=True)

    class Meta:
        model = Position
        fields = ['owner', 'data']