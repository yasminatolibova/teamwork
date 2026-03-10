from ..accounts.serializers import UserSerializer
from .models import PaymentType, Status, MobileCommunication, InternetPayment, CommunalPayment

from rest_framework import serializers

class PaymentTypeSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=PaymentType
        fields=['id', 'user', 'types']

class StatusSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Status
        fields=['id', 'user', 'status']

class MobileCommunicationSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=MobileCommunication
        fields=['id', 'user', 'operator', 'phone_number', 'amount', 'commission', 'type', 'status', 'operator_account_number',
                'created_at','updated_at', 'transaction_id','total_amount','account', 'current_balance', 'debt'  ]
        read_only_fields=['created_at']


class InternetPaymentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=InternetPayment
        fields=['id', 'user', 'provider', 'price', 'commission', 'type', 'account', 'status', 'provider_account_number',
                'created_at', 'updated_at', 'transaction_id', 'total_price',  'current_balance', 'debt' ]
        read_only_fields=['created_at']


class CommunalPaymentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=CommunalPayment
        fields=['id', 'user', 'provider', 'cost', 'commission', 'service_type', 'account', 'status', 'provider_account_number',
                'created_at', 'updated_at', 'transaction_id', 'total_cost', 'current_balance', 'debt' ]
        read_only_fields=['created_at']






    