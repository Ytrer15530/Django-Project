from rest_framework import serializers
from .models import Payments


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['currency', 'exchange_rete_to_usd']
